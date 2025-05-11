import os
import sys

venv_root = os.environ.get('VIRTUAL_ENV', '')
# Mantieni solo i path che stanno dentro il tuo venv attivo o nella directory corrente
sys.path = [p for p in sys.path if venv_root in p or p.startswith(os.getcwd())]
print("sys.path pulito:")
for p in sys.path:
    print(" -", p)

try:
    import pandas as pd

    print("Pandas:", pd.__version__)
except ImportError as e:
    print("❌ Errore di importazione:", e)
    # sys.exit(1)


try:
    import numpy as np

    print("Numpy:", np.__version__)
except ImportError as e:
    print("❌ Errore di importazione:", e)
    # sys.exit(1)