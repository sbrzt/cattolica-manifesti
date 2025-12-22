# main.py

import pandas as pd
import os
from config import (
    PROCESS_DIR_PATH,
    METADATA_FILE_PATH,
    FILE_FORMAT,
    FILE_IMPORT_CODE,
    FILE_PROCESSING_CODE,
    MERGING_KEY,
    OUTPUT_FILE_PATH
)
from src.tainacan_prep import data_prep
from src.process import extract_metadata, extract_paradata


def main():
    df_metadata = extract_metadata(METADATA_FILE_PATH)
    paradata_list = []
    for subdir, dirs, files in os.walk(PROCESS_DIR_PATH):
        imp_file_path = None
        proc_file_path = None
        for file in files:
            if file.endswith(FILE_FORMAT):
                full_path = os.path.join(subdir, file)
                if FILE_IMPORT_CODE in file:
                    imp_file_path = full_path
                elif FILE_PROCESSING_CODE in file:
                    proc_file_path = full_path
        if imp_file_path and proc_file_path:
            try:
                paradata = extract_paradata(imp_file_path, proc_file_path)
                paradata_list.append(paradata)
            except Exception as e:
                print(f"error {subdir}: {e}")
    df_paradata = pd.DataFrame(paradata_list)
    df = df_metadata.merge(df_paradata, how="inner", on=MERGING_KEY)
    df = data_prep(df)
    df.to_csv(OUTPUT_FILE_PATH, index=False)



if __name__ == "__main__":
    main()
