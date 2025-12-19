# process.py

import json
import re
import pandas as pd
from config import(
    NS_MAP,
    ROOT,
    EVENT_KEY,
    EVENT_DATE,
    PARAMS_NS_MAP
)
from lxml import etree
from pathlib import Path


def extract_metadata(file_path):
    df = pd.read_csv(file_path)
    return df


def extract_paradata(imp_file_path, proc_file_path):
    with open(imp_file_path, 'rb') as f:
        imp_tree = etree.parse(f)
    with open(proc_file_path, 'rb') as f:
        proc_tree = etree.parse(f)
    imp_root = imp_tree.xpath(ROOT, namespaces=NS_MAP)[0]
    proc_root = proc_tree.xpath(ROOT, namespaces=NS_MAP)[0]
    imp_history = _extract_history(imp_root)
    proc_history = _extract_history(proc_root)
    seen_ids = set()
    history = []
    for event in imp_history + proc_history:
        event_key = (event[EVENT_KEY], event[EVENT_DATE])
        if event_key not in seen_ids:
            history.append(event)
            seen_ids.add(event_key)
    data = {
        'id': Path(proc_file_path).parts[-2],
        'document_id': _get_val(proc_root, 'xmpMM:DocumentID/text()')[0],
        'original_document_id': _get_val(proc_root, 'xmpMM:OriginalDocumentID/text()')[0],
        'instance_id': _get_val(proc_root, 'xmpMM:InstanceID/text()')[0],
        'creation_date': _get_val(proc_root, 'xmp:CreateDate/text()')[0],
        'modify_date': _get_val(proc_root, 'xmp:ModifyDate/text()')[0],
        'metadata_date': _get_val(proc_root, 'xmp:MetadataDate/text()')[0],
        'tool': _get_val(proc_root, 'xmp:CreatorTool/text()')[0],
        'manufacturer': _get_val(proc_root, 'tiff:Make/text()')[0],
        'device': _get_val(proc_root, 'tiff:Model/text()')[0],
        'img_resolution_width': _get_val(proc_root, 'tiff:XResolution/text()')[0],
        'img_resolution_height': _get_val(proc_root, 'tiff:YResolution/text()')[0],
        'img_resolution_unit': _get_val(proc_root, 'tiff:ResolutionUnit/text()')[0],
        'img_width': _get_val(proc_root, 'exif:PixelXDimension/text()')[0],
        'img_height': _get_val(proc_root, 'exif:PixelYDimension/text()')[0],
        'format': _get_val(proc_root, 'dc:format/text()')[0],
        'exposure_time': _get_val(proc_root, 'exif:ExposureTime/text()')[0],
        'aperture': _get_val(proc_root, 'exif:FNumber/text()')[0],
        'iso': proc_root.xpath('exif:ISOSpeedRatings/rdf:Seq/rdf:li/text()', namespaces=NS_MAP)[0],
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
    parameters = {}
    for attr_name, attr_value in tree.attrib.items():
        if any(ns_uri in attr_name for ns_uri in NS_MAP.values()):
            tag_name_raw = attr_name.split('}')[-1]
            for prefix in ['crs', 'exif', 'aux', 'photoshop', 'tiff']:
                if NS_MAP[prefix] in attr_name:
                    tag_name = _to_snake_case(tag_name_raw)
                    parameters[tag_name] = attr_value
    for child in tree.getchildren():
        tag = child.tag
        if any(ns in tag for ns in param):
            tag_name = _to_snake_case(tag.split('}')[-1])           
            content = _extract_node_content(child)
            if content:
                parameters[tag_name] = content
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


def _get_val(node, query):
    prefix, tag = query.split(':')
    tag = tag.replace('/text()', '')
    for attr_key, attr_value in node.attrib.items():
        if attr_key.endswith(tag):
            return [attr_value]
    res = node.xpath(f'./{prefix}:{tag}/text()', namespaces=NS_MAP)
    return res if res else [None]