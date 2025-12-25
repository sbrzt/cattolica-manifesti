# config.py

"""
Configuration file for XMP metadata extraction and Tainacan preparation.

This module centralises all constants, XML namespaces, XPath expressions, 
and metadata labels required to process descriptive metadata and paradata 
and prepare them for Tainacan's automatic import.
"""


# XML Namespace Mapping for lxml XPath evaluations
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

# Namespaces to be included in the technical parameters dump
PARAMS_NS_MAP = {
    'crs': 'camera-raw-settings',
    'exif': 'exif',
    'aux': 'aux',
    'photoshop': 'photoshop',
    'tiff': 'tiff'
}

# XPath expressions for single technical fields
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

# XPath expressions for history
HISTORY_ITEMS_PATH = 'xmpMM:History/rdf:Seq/rdf:li'
HISTORY_ACTION_PATH = 'stEvt:action/text()'
HISTORY_INSTANCE_ID_PATH = 'stEvt:instanceID/text()'
HISTORY_WHEN_PATH = 'stEvt:when/text()'
HISTORY_SOFTWARE_PATH = 'stEvt:softwareAgent/text()'
HISTORY_PARAMETERS_PATH = 'stEvt:parameters/text()'

# Recursive parsing constant for structured nodes
SEQUENCE_NODE_PATH = './rdf:Seq/rdf:li/text() | ./rdf:Alt/rdf:li/text()'

# File system and processing configuration
ROOT = '//rdf:Description'
PROCESS_DIR_PATH = "data/process"
METADATA_FILE_PATH = "data/object/balan_objects.csv"
FILE_FORMAT = ".xmp"
FILE_IMPORT_CODE = "_imp"
FILE_PROCESSING_CODE = "_proc"
MERGING_KEY = "id"

# Event parameters
EVENT_KEY = 'instance_id'
EVENT_DATE = 'when'

# Output configuration
OUTPUT_FILE_PATH = "dataset_balan.csv"
OUTPUT_DB_FILE_PATH = "db_balan.csv"

# Tainacan CSV import syntax constants
LABEL_SEPARATOR = "|"
DB_KEY_PARAMETER = 'collection_key_yes'
STATUS_PRIVATE_PARAMETER = 'status_private'
STATUS_PUBLIC_PARAMETER = 'status_public'
RELATIONSHIP_PARAMETER = 'relationship'
NUMERIC_PARAMETER = 'numeric'
DATE_PARAMETER = 'date'
TEXT_PARAMETER = 'text'
LABELS = {
    0: {
        0: "id",
        1: "Identificativo"
        },
    1: {
        0: "title", 
        1: "Titolo"
        },
    2: {
        0: "type",
        1: "Tipologia"
        },
    3: {
        0: "date",
        1: "Data di creazione"
        },
    4: {
        0: "technique",
        1: "Tecnica"
        },
    5: {
        0: "work_dimension_height",
        1: "Altezza (cm)"
        },
    6: {
        0: "work_dimension_width",
        1: "Larghezza (cm)"
        },
    7: {
        0: "dimension_unit",
        1: "Unità di misura"
        },
    8: {
        0: "subject",
        1: "Soggetto"
        },
    9: {
        0: "contents",
        1: "Contenuti"
        },
    10: {
        0: "notes",
        1: "Note"
        },
    11: {
        0: "commissioner",
        1: "Committente"
        },
    12: {
        0: "photographer",
        1: "Fotografo"
        },
    13: {
        0: "graphic_designer",
        1: "Designer"
        },
    14: {
        0: "copywriter",
        1: "Copy"
        },
    15: {
        0: "related_to", 
        1: "Lavori correlati"
        },
    16: {
        0: "inventory_number",
        1: "Numero di inventario"
        },
    17: {
        0: "acquisition_resp",
        1: "Responsabile dell'acquisizione"
        },
    18: {
        0: "processing_resp",
        1: "Responsabile del processamento"
        },
    19: {
        0: "document_id",
        1: "Identificativo della foto"
        },
    20: {
        0: "original_document_id",
        1: "Identificativo dell'originale"
        },
    21: {
        0: "instance_id",
        1: "Identificativo dell'esemplare"
        },
    22: {
        0: "creation_date",
        1: "Data di acquisizione"
        },
    23: {
        0: "modify_date",
        1: "Data di ultima modifica"
        },
    24: {
        0: "metadata_date",
        1: "Data di ultima metadatazione"
        },
    25: {
        0: "tool",
        1: "Software di processamento"
        },
    26: {
        0: "manufacturer",
        1: "Creatore dello strumento di acquisizione"
        },
    27: {
        0: "device",
        1: "Strumento di acquisizione"
        },
    28: {
        0: "img_resolution_width",
        1: "Risoluzione (larghezza)"
        },
    29: {
        0: "img_resolution_height",
        1: "Risoluzione (altezza)"
        },
    30: {
        0: "img_resolution_unit",
        1: "Unità di risoluzione"
        },
    31: {
        0: "img_width",
        1: "Larghezza dell'immagine (pixel)"
        },
    32: {
        0: "img_height",
        1: "Altezza dell'immagine (pixel)"
        },
    33: {
        0: "format",
        1: "Formato"
        },
    34: {
        0: "exposure_time",
        1: "Tempo di esposizione"
        },
    35: {
        0: "aperture",
        1: "Apertura"
        },
    36: {
        0: "iso",
        1: "ISO"
        },
    37: {
        0: "focal_length",
        1: "Fuoco"
        },
    38: {
        0: "license",
        1: "Licenza"
        },
    39: {
        0: "parameters",
        1: "Parametri"
        },
    40: {
        0: "history",
        1: "Cronologia"
        }
}