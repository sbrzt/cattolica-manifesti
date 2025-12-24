# process.py

import json
import re
import pandas as pd
from config import(
    NS_MAP,
    ROOT,
    EVENT_KEY,
    EVENT_DATE,
    PARAMS_NS_MAP,
    DOCUMENT_ID_PATH,
    ORIGINAL_DOCUMENT_ID_PATH,
    INSTANCE_ID_PATH,
    CREATION_DATE_PATH,
    MODIFY_DATE_PATH,
    METADATA_DATE_PATH,
    TOOL_PATH,
    MANUFACTURER_PATH,
    DEVICE_PATH,
    IMG_RES_WIDTH_PATH,
    IMG_RES_HEIGHT_PATH,
    IMG_RES_UNIT_PATH,
    IMG_WIDTH_PATH,
    IMG_HEIGHT_PATH,
    FORMAT_PATH,
    EXPOSURE_TIME_PATH,
    APERTURE_PATH,
    ISO_PATH_PATH,
    LICENSE_PATH,
    FOCAL_LENGTH_PATH,
    HISTORY_ITEMS_PATH,
    HISTORY_ACTION_PATH,
    HISTORY_INSTANCE_ID_PATH,
    HISTORY_WHEN_PATH,
    HISTORY_SOFTWARE_PATH,
    HISTORY_PARAMETERS_PATH,
    SEQUENCE_NODE_PATH,
    LABELS
)
from lxml import etree
from pathlib import Path


def extract_metadata(file_path):
    df = pd.read_csv(file_path)
    df["id"] = df.ind.astype(str).str.cat(df.assigned_id, sep="_")
    df2 = df.drop(columns=["ind", "assigned_id"])
    return df2


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
        LABELS[0][0]: Path(proc_file_path).parts[-2],
        LABELS[19][0]: _get_val(proc_root, DOCUMENT_ID_PATH)[0],
        LABELS[20][0]: _get_val(proc_root, ORIGINAL_DOCUMENT_ID_PATH)[0],
        LABELS[21][0]: _get_val(proc_root, INSTANCE_ID_PATH)[0],
        LABELS[22][0]: _get_val(proc_root, CREATION_DATE_PATH)[0],
        LABELS[23][0]: _get_val(proc_root, MODIFY_DATE_PATH)[0],
        LABELS[24][0]: _get_val(proc_root, METADATA_DATE_PATH)[0],
        LABELS[25][0]: _get_val(proc_root, TOOL_PATH)[0],
        LABELS[26][0]: _get_val(proc_root, MANUFACTURER_PATH)[0],
        LABELS[27][0]: _get_val(proc_root, DEVICE_PATH)[0],
        LABELS[28][0]: _get_val(proc_root, IMG_RES_WIDTH_PATH)[0],
        LABELS[29][0]: _get_val(proc_root, IMG_RES_HEIGHT_PATH)[0],
        LABELS[30][0]: _get_val(proc_root, IMG_RES_UNIT_PATH)[0],
        LABELS[31][0]: _get_val(proc_root, IMG_WIDTH_PATH)[0],
        LABELS[32][0]: _get_val(proc_root, IMG_HEIGHT_PATH)[0],
        LABELS[33][0]: _get_val(proc_root, FORMAT_PATH)[0],
        LABELS[34][0]: _get_val(proc_root, EXPOSURE_TIME_PATH)[0],
        LABELS[35][0]: _get_val(proc_root, APERTURE_PATH)[0],
        LABELS[36][0]: proc_root.xpath(ISO_PATH_PATH, namespaces=NS_MAP)[0],
        LABELS[37][0]: _get_val(proc_root, FOCAL_LENGTH_PATH)[0],
        LABELS[38][0]: LICENSE_PATH,
        LABELS[39][0]: _extract_parameters(proc_root),
        LABELS[40][0]: json.dumps(history)
    }
    return data


def _extract_history(tree):
    history_list = []
    items = tree.xpath(HISTORY_ITEMS_PATH, namespaces=NS_MAP)
    for item in items:
        event = {
            'action': item.xpath(HISTORY_ACTION_PATH, namespaces=NS_MAP),
            'instance_id': item.xpath(HISTORY_ITEMS_PATH, namespaces=NS_MAP),
            'when': item.xpath(HISTORY_WHEN_PATH, namespaces=NS_MAP),
            'software': item.xpath(HISTORY_SOFTWARE_PATH, namespaces=NS_MAP),
            'parameters': item.xpath(HISTORY_PARAMETERS_PATH, namespaces=NS_MAP)
        }
        event = {key: value[0] if value else None for key, value in event.items()}
        history_list.append(event)
    return history_list


def _extract_parameters(tree):
    param = PARAMS_NS_MAP.values()
    parameters = {}
    for attr_name, attr_value in tree.attrib.items():
        if any(ns_uri in attr_name for ns_uri in NS_MAP.values()):
            tag_name_raw = attr_name.split('}')[-1]
            for prefix in PARAMS_NS_MAP.keys():
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
        seq = node.xpath(SEQUENCE_NODE_PATH, namespaces=NS_MAP)
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