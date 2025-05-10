# Python Virtual Environment Diagnostic Toolkit

Questa guida documenta **tutti i comandi, script e tecniche diagnostiche** utilizzate per analizzare in profondità l'integrità e le dipendenze del virtual environment `_bot11_dev`.

---

## ✅ Obiettivi della Diagnosi

- Verificare da dove vengono realmente caricati i moduli (es. `pandas`, `numpy`)
- Identificare dipendenze nascoste da ambienti precedenti (`BOT_6`) o da Python di sistema
- Capire la struttura interna dei virtual environment e la relazione con la `stdlib`

---

## 1. Verifica dell'interprete Python attivo

### Comando terminale
```bash
where python    # in CMD
Get-Command python  # in PowerShell
```

### In Python
```python
import sys
print(sys.executable)
```

---

## 2. Verifica dei percorsi da cui Python importa i moduli (`sys.path`)

### Script base
```python
import sys
for p in sys.path:
    print(p)
```

### Variante per visualizzare solo percorsi esistenti
```python
from pathlib import Path
for p in sys.path:
    print(f"{p} - {'EXISTS' if Path(p).exists() else 'NOT FOUND'}")
```

---

## 3. Diagnostica modulo `__future__`

### Script `trace_future_import.py`
```python
import importlib
import sys
import os

print(f"Python Executable: {sys.executable}")
print(f"VIRTUAL_ENV: {os.environ.get('VIRTUAL_ENV')}")

import __future__
print(f"__future__.__file__ = {getattr(__future__, '__file__', 'built-in')}")
```

---

## 4. Analisi `pyvenv.cfg` del venv

### Script `analyze_venv_integrity.py`
```python
from pathlib import Path
import sys, os

venv_root = os.environ.get("VIRTUAL_ENV")
venv_cfg = Path(venv_root or ".") / "pyvenv.cfg"

if venv_cfg.exists():
    with open(venv_cfg, "r", encoding="utf-8") as f:
        print(f.read())
```

---

## 5. Tracciamento dei sottomoduli runtime

### Script `trace_runtime_submodules.py`
```python
import importlib
import pkgutil
from pathlib import Path
import os

TARGET_MODULE = 'pandas'
venv_root = os.environ.get("VIRTUAL_ENV", "")

module = importlib.import_module(TARGET_MODULE)
for finder, name, ispkg in pkgutil.walk_packages(module.__path__, module.__name__ + "."):
    submod = importlib.import_module(name)
    subfile = getattr(submod, '__file__', '')
    print(f"{name} → {subfile} {'OUTSIDE VENV' if venv_root not in str(subfile) else ''}")
```

---

## 6. Pulizia selettiva di `sys.path`

### Mini funzione `clean_sys_path_except_python_home`
```python
import sys
import os
from pathlib import Path

def clean_sys_path_except_python_home(include_cwd=True):
    python_home = Path(sys.base_prefix).resolve()
    cwd = Path(os.getcwd()).resolve()
    sys.path = [
        p for p in sys.path
        if (python_home in Path(p).resolve().parents or Path(p).resolve() == python_home) or
           (include_cwd and cwd in Path(p).resolve().parents)
    ]
```

---

## 7. Verifica completa delle importazioni da `requirements.txt`

### Script `check_imports_requirements.py`
```python
import importlib
import os
from pathlib import Path

venv_root = os.environ.get("VIRTUAL_ENV", "")
with open("requirements.txt", "r") as f:
    modules = [line.strip().split("==")[0] for line in f if line.strip() and not line.startswith("#")]

for mod_name in modules:
    try:
        mod = __import__(mod_name)
        path = getattr(mod, '__file__', '<built-in>')
        print(f"{mod_name} → {path} {'OUTSIDE VENV' if venv_root not in path else ''}")
    except Exception as e:
        print(f"{mod_name} → IMPORT ERROR: {e}")
```

---

## 📌 Note Finali

- La `stdlib` (inclusi moduli come `__future__`, `abc`, `typing`) **non viene copiata dentro i venv**
- Il file `pyvenv.cfg` determina da dove viene caricata
- Per venv completamente isolati si può usare `--copies` oppure ambienti portabili

---

## ✅ Consiglio finale

Per garantire un ambiente pulito, considera l’uso di:

```bash
python -m venv nome_env --copies
```

oppure l’uso di ambienti containerizzati (es. Docker) se l’obiettivo è la massima portabilità e isolamento.