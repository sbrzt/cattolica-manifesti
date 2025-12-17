# process.py

import json
import re
from lxml import etree

NS_MAP = {
    'x': 'adobe:ns:meta/',
    'aux': 'http://ns.adobe.com/exif/1.0/aux/',
    'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
    'xmp': 'http://ns.adobe.com/xap/1.0/',
    'xmpMM': 'http://ns.adobe.com/xap/1.0/mm/',
    'dc': 'http://purl.org/dc/elements/1.1/',
    'crs': 'http://ns.adobe.com/camera-raw-settings/1.0/',
    'exif': 'http://ns.adobe.com/exif/1.0/',
    'photoshop': 'http://ns.adobe.com/photoshop/1.0/',
    'stEvt': 'http://ns.adobe.com/xap/1.0/sType/ResourceEvent#',
    'tiff': 'http://ns.adobe.com/tiff/1.0/'
}

def extract_xmp_data(imp_file_path, proc_file_path):
    with open(imp_file_path, 'rb') as f:
        imp_tree = etree.parse(f)
    with open(proc_file_path, 'rb') as f:
        proc_tree = etree.parse(f)
    imp_root = imp_tree.xpath('//rdf:Description', namespaces=NS_MAP)[0]
    proc_root = proc_tree.xpath('//rdf:Description', namespaces=NS_MAP)[0]
    imp_history = _extract_history(imp_root)
    proc_history = _extract_history(proc_root)
    seen_ids = set()
    history = []
    for event in imp_history + proc_history:
        event_key = (event['instance_id'], event['when'])
        if event_key not in seen_ids:
            history.append(event)
            seen_ids.add(event_key)
    data = {
        'document_id': proc_root.xpath('xmpMM:DocumentID/text()', namespaces=NS_MAP)[0],
        'original_document_id': proc_root.xpath('xmpMM:OriginalDocumentID/text()', namespaces=NS_MAP)[0],
        'instance_id': proc_root.xpath('xmpMM:InstanceID/text()', namespaces=NS_MAP)[0],
        'acquisition_date': proc_root.xpath('exif:DateTimeOriginal/text()', namespaces=NS_MAP)[0],
        'create_date': proc_root.xpath('xmp:CreateDate/text()', namespaces=NS_MAP)[0],
        'hardware': proc_root.xpath('tiff:Model/text()', namespaces=NS_MAP)[0],
        'serial_number': proc_root.xpath('aux:SerialNumber/text()', namespaces=NS_MAP)[0],
        'dpi': proc_root.xpath('tiff:XResolution/text()', namespaces=NS_MAP)[0],
        'width': proc_root.xpath('exif:PixelXDimension/text()', namespaces=NS_MAP)[0],
        'height': proc_root.xpath('exif:PixelYDimension/text()', namespaces=NS_MAP)[0],
        'format': proc_root.xpath('dc:format/text()', namespaces=NS_MAP)[0],
        'parameters': _extract_parameters(proc_root),
        'history': json.dumps(history)
    }
    return data


def _extract_history(tree):
    history_list = []
    items = tree.xpath('xmpMM:History/rdf:Seq/rdf:li', namespaces=NS_MAP)
    for item in items:
        event = {
            'action': item.xpath('stEvt:action/text()', namespaces=NS_MAP),
            'instance_id': item.xpath('stEvt:instanceID/text()', namespaces=NS_MAP),
            'when': item.xpath('stEvt:when/text()', namespaces=NS_MAP),
            'software': item.xpath('stEvt:softwareAgent/text()', namespaces=NS_MAP),
            'parameters': item.xpath('stEvt:parameters/text()', namespaces=NS_MAP)
        }
        event = {key: value[0] if value else None for key, value in event.items()}
        history_list.append(event)
    return history_list


def _extract_parameters(tree):
    param = [
        'camera-raw-settings',
        'exif',
        'aux',
        'photoshop'
    ]
    parameters = {}
    for child in tree.getchildren():
        tag = child.tag
        if any(ns in tag for ns in param):
            tag_name = _to_snake_case(tag.split('}')[-1])           
            parameters[tag_name] = _extract_node_content(child)
    return json.dumps(parameters)


def _to_snake_case(text):
    strng = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
    strng = re.sub('([a-z0-9])([A-Z])', r'\1_\2', strng).lower()
    return strng


def _extract_node_content(node):
    if len(node.getchildren()) > 0:
        seq = node.xpath('./rdf:Seq/rdf:li/text() | ./rdf:Alt/rdf:li/text()', namespaces=NS_MAP)
        if seq:
            return seq if len(seq) > 1 else seq[0]
        res = {}
        for child in node.getchildren():
            if 'rdf' not in child.tag:
                child_name = _to_snake_case(child.tag.split('}')[-1])
                res[child_name] = _extract_node_content(child)
        return res if res else None
    return node.text.strip() if node.text else None
