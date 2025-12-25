# Cattolica Manifesti

🇺🇸: This project automates the integration of descriptive metadata and technical paradata extracted from XMP files for the management of a digital poster archive on WordPress via the Tainacan plugin.

🇮🇹: Questo progetto automatizza l'integrazione di metadati descrittivi e paradati tecnici estratti da file  XMP per la gestione di un archivio digitale di manifesti su WordPress tramite il plugin Tainacan.


## 🇺🇸 English version

### Overview
This system processes a collection of approximately 800 digitized posters. It combines descriptive metadata (from a central CSV) with technical acquisition and post-production details saved in XMP format.

### Key features
* ***XMP extraction***: Systematically handles both XMP files structured with XML child nodes and those using attributes within the root node.
* ***History merging***: Unifies file history (`xmpMM:History`) by removing duplicates between import (`_imp`) and processing (`_proc`) files.
* ***Recursive parsing***: Extracts complex structures such as tone curves and correction masks into JSON format.
* ***Tainacan ready***: Automatically formats column headers using a specific syntax (e.g., `Title|text|status_public`) for the WordPress Tainacan CSV importer.

### Project structure
* `main.py`: Pipeline orchestrator.
* `config.py`: Centralised configuration for namespaces, XPaths, and labels.
* `src/process.py`: Specialised XMP extraction engine.
* `src/tainacan_prep.py`: Formatting logic for Tainacan integration.

### Usage
This project relies on [uv](https://github.com/astral-sh/uv) for fast and reliable dependency management.

1. **Installing uv**: If you haven't installed it yet, run:

```bash
curl -LsSf https://astral-sh.uv/install.sh | sh
```

2. **Project synchronization**: Create the virtual environment and install dependencies with a single command:

```bash
uv sync
```

3. **Configuration**: Verify directory paths and the metadata CSV file in `config.py`.

4. **Execution**: Run the processing pipeline using `uv`:

```bash
uv run main.py
```

5. **Output**: The script will generate a CSV dataset containing complete integrated data and another CSV dataset formatted for Tainacan import.


## 🇮🇹 Versione italiana

### Panoramica
Il sistema processa una collezione di circa 800 manifesti digitalizzati. Combina i dati descrittivi (provenienti da un CSV centrale) con i dettagli tecnici di acquisizione e post-produzione salvati in formato XMP.

### Caratteristiche principali
* ***Estrazione XMP***: Gestisce sistematicamente sia i file XMP strutturati con nodi XML figli sia quelli che utilizzano attributi nel nodo root.
* ***Merge della cronologia***: Unifica la storia dei file `(xmpMM:History`) eliminando i duplicati tra i file di importazione (`_imp`) e processamento (`_proc`).
* ***Parsing ricorsivo***: Estrae strutture complesse come curve di tono e maschere di correzione in formato JSON.
* ***Preparazione per Tainacan***: Formatta automaticamente le intestazioni delle colonne con una sintassi specifica (es. `Identificativo|text|status_private`) per l'importatore CSV di Tainacan.

### Struttura del progetto
* `main.py`: Orchestratore del processo.
* `config.py`: Configurazione centralizzata per namespace, XPath, e etichette.
* `src/process.py`: Engine di estrazione di metadati e paradati da file XMP e CSV.
* `src/tainacan_prep.py`: Logica di formattazione per l'integrazione con Tainacan.

### Uso
Questo progetto utilizza [uv](https://github.com/astral-sh/uv) per una gestione rapida e affidabile delle dipendenze.

1. **Installazione di uv**: Se non lo hai già, installalo con:

```bash
curl -LsSf https://astral-sh.uv/install.sh | sh
```

2. **Sincronizzazione progetto**: Crea l'ambiente virtuale e installa le dipendenze con:

```bash
uv sync
```

3. **Configurazione**: Verifica i percorsi delle directory e del file CSV in `config.py`.

4. **Esecuzione**: Avvia la pipeline di elaborazione tramite `uv`:

```bash
uv run main.py
```

5. **Risultato**: Il comando genererà un dataset CSV contenente i dati completi e un altro dataset CSV formattato per l'importazione automatica in Tainacan.
