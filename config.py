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

DOCUMENT_ID_PATH = 'xmpMM:DocumentID/text()'
ORIGINAL_DOCUMENT_ID_PATH = 'xmpMM:OriginalDocumentID/text()'
INSTANCE_ID_PATH = 'xmpMM:InstanceID/text()'
CREATION_DATE_PATH = 'xmp:CreateDate/text()'
MODIFY_DATE_PATH = 'xmp:ModifyDate/text()'
METADATA_DATE_PATH = 'xmp:MetadataDate/text()'
TOOL_PATH = 'xmp:CreatorTool/text()'
MANUFACTURER_PATH = 'tiff:Make/text()'
DEVICE_PATH = 'tiff:Model/text()'
IMG_RES_WIDTH_PATH = 'tiff:XResolution/text()'
IMG_RES_HEIGHT_PATH = 'tiff:YResolution/text()'
IMG_RES_UNIT_PATH = 'tiff:ResolutionUnit/text()'
IMG_WIDTH_PATH = 'exif:PixelXDimension/text()'
IMG_HEIGHT_PATH = 'exif:PixelYDimension/text()'
FORMAT_PATH = 'dc:format/text()'
EXPOSURE_TIME_PATH = 'exif:ExposureTime/text()'
APERTURE_PATH = 'exif:FNumber/text()'
ISO_PATH_PATH = 'exif:ISOSpeedRatings/rdf:Seq/rdf:li/text()'
FOCAL_LENGTH_PATH = 'exif:FocalLength/text()'
LICENSE_PATH = 'https://creativecommons.org/licenses/by-nc-sa/4.0/'
HISTORY_ITEMS_PATH = 'xmpMM:History/rdf:Seq/rdf:li'
HISTORY_ACTION_PATH = 'stEvt:action/text()'
HISTORY_INSTANCE_ID_PATH = 'stEvt:instanceID/text()'
HISTORY_WHEN_PATH = 'stEvt:when/text()'
HISTORY_SOFTWARE_PATH = 'stEvt:softwareAgent/text()'
HISTORY_PARAMETERS_PATH = 'stEvt:parameters/text()'
SEQUENCE_NODE_PATH = './rdf:Seq/rdf:li/text() | ./rdf:Alt/rdf:li/text()'
PROCESS_DIR_PATH = "data/process"
METADATA_FILE_PATH = "data/object/balan_objects.csv"
FILE_FORMAT = ".xmp"
FILE_IMPORT_CODE = "_imp"
FILE_PROCESSING_CODE = "_proc"
MERGING_KEY = "id"
OUTPUT_FILE_PATH = "tabella_balan.csv"