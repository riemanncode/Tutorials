import sys
from pathlib import Path
import os


print(">>> sys.path attivi:\n")
for i, p in enumerate(sys.path):
    label = " (esiste)" if Path(p).exists() else " (NON esiste)"
    print(f"{i:02d}: {p}{label}")

print("")
print("sys.executable",sys.executable)
print("")



## rimozione delle variabili di ambiente
print(">>> rimozione delle variabili di ambiente <<<")
print(">>> rimozione delle variabili di ambiente <<<")

venv_root = os.environ.get('VIRTUAL_ENV', '')
# Mantieni solo i path che stanno dentro il tuo venv attivo o nella directory corrente
sys.path = [p for p in sys.path if venv_root in p or p.startswith(os.getcwd())]
print("sys.path pulito:")
for p in sys.path:
    print(" -", p)


print(">>> sys.path attivi:\n")
for i, p in enumerate(sys.path):
    label = " (esiste)" if Path(p).exists() else " (NON esiste)"
    print(f"{i:02d}: {p}{label}")

print("")
print("sys.executable",sys.executable)
print("")