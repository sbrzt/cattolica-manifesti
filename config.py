# config.py

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
PARAMS_NS_MAP = {
    'crs': 'camera-raw-settings',
    'exif': 'exif',
    'aux': 'aux',
    'photoshop': 'photoshop',
    'tiff': 'tiff'
}

ROOT = '//rdf:Description'
EVENT_KEY = 'instance_id'
EVENT_DATE = 'when'
PROCESS_DIR_PATH = "data/process"
METADATA_FILE_PATH = "data/object/balan_objects.csv"
FILE_FORMAT = ".xmp"
FILE_IMPORT_CODE = "_imp"
FILE_PROCESSING_CODE = "_proc"
MERGING_KEY = "id"
OUTPUT_FILE_PATH = "tabella_balan.csv"