from pathlib import Path
from llama_index import download_loader

CJKPDFReader = download_loader("CJKPDFReader")

loader = CJKPDFReader()

documents = loader.load_data(file=Path('문서002.pdf'))

print(documents)