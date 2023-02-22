import os
from pathlib import Path

ROOT_DIR = PROGRAM_DIR = Path(__file__).resolve().parent.parent
CONFIG_file_path = os.path.join(ROOT_DIR,"config.ini")
SOURCES_DIR = os.path.join(ROOT_DIR, "sources")
OUTPUT_DIR = os.path.join(ROOT_DIR, "outputs")

