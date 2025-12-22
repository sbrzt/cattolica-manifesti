# tainacan_prep.py

import pandas as pd


def data_prep(data):
    #data["id"] = f"{data['index']}_{data['assigned_id']}"
    data2 = data.drop(columns=["index"])
    data["special_document"] = "file:manifesti/" + data["id"] + ".jpg"
    data["special_attachments"] = f"metadata/{data['id']}_imp.xmp; metadata/{data['id']}_proc.xmp"
    df = data.rename(columns={
        'id': 'Identificativo|collection_key_yes|status_private',
        'title': 'Titolo|status_public',
        'type': 'Tipologia|status_public',
        'related_to': 'Lavori correlati|relationship',
        'work_dimension_height': 'Altezza|numeric|status_public',
        'work_dimension_width': 'Larghezza|numeric|status_public',
        'dimension_unit': 'Unità di misura|status_public',
        'date': 'Data di creazione|date|status_public',
        'subject': 'Soggetto|status_public',
        'commissioner': 'Committente|status_public',
        'photographer': 'Fotografo|status_public',
        'graphic_designer': 'Designer|status_public',
        'copywriter': 'Copy|status_public',
        'inventory_number': 'Numero di inventario|text|status_public',
        'text_contents': 'Contenuti|status_public',
        'notes': 'Note|status_public',
        'image_making_technique': 'Tecnica|status_public',
        'acquisition_resp': "Responsabile dell'acquisizione|status_public",
        'processing_resp': "Responsabile del processamento|status_public",
        'document_id': 'Identificativo della foto|status_private',
        'original_document_id': "Identificativo dell'originale|status_private",
        'instance_id': "Identificativo dell'esemplare|status_private",
        'creation_date': 'Data di acquisizione|date|status_public',
        'modify_date': 'Data di ultima modifica|date|status_private',
        'metadata_date': 'Data di ultima metadatazione|date|status_private',
        'tool': 'Software di processamento|status_public',
        'manufacturer': 'Creatore dello strumento di acqusizione|status_public',
        'device': 'Strumento di acquisizione|status_public',
        'img_resolution_width': 'Risoluzione (larghezza)|status_public',
        'img_resolution_height': 'Risoluzione (altezza)|status_public',
        'img_resolution_unit': 'Unità di risoluzione|status_public',
        'img_width': "Larghezza dell'immagine|numeric|status_public",
        'img_height': "Altezza dell'immagine|numeric|status_public",
        'format': 'Formato|status_public',
        'exposure_time': 'Tempo di esposizione|status_public',
        'aperture': 'Apertura|status_public',
        'iso': 'ISO|status_public',
        'focal_length': 'Fuoco|status_public',
        'license': 'Licenza|status_public',
        'parameters': 'Parametri|status_private',
        'history': 'Cronologia|status_private'
    })

    return df