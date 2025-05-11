import importlib
import sys
import os
import pkgutil
from pathlib import Path
from datetime import datetime

##########################################################################
##########################################################################
## RIMUOVIAMO I VENVS VECCHI E RIFACCIAMO IL TEST (BOT_6)(PYTHON.EXE)(ECC..)
# venv_root = os.environ.get('VIRTUAL_ENV', '')
# # Mantieni solo i path che stanno dentro il tuo venv attivo o nella directory corrente
# sys.path = [p for p in sys.path if venv_root in p or p.startswith(os.getcwd())]
# print("sys.path pulito:")
# for p in sys.path:
#     print(" -", p)
##########################################################################
##########################################################################


# 🔧 Cambia qui il modulo target da ispezionare
# finalmente senza rimuovere i venv vecchi abbiamo trovato la provenienza di __future__ ---> PYTHON STANDARD!!! IN C:\\
# se rimuoviamo tutti le variabili di ambiente (PYTHON STANDARD!!! IN C:\\), __future__ non viene più trovato!!
TARGET_MODULE = '__future__'
# TARGET_MODULE = 'pandas'


SUSPICIOUS = ['BOT_6', 'pycharmprojects', 'AppData\\Roaming\\Python']
venv_root = os.environ.get('VIRTUAL_ENV', '')
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
output_file = Path(f"import_trace_{TARGET_MODULE}_{timestamp}.txt")

lines = []

def is_suspicious(path: str):
    return any(s.lower() in path.lower() for s in SUSPICIOUS)

def log(line: str):
    print(line)
    lines.append(line)

log(f"🔍 Tracking real submodule imports for: {TARGET_MODULE}")
log(f"🔒 VENV: {venv_root or 'None'}\n")

try:
    module = importlib.import_module(TARGET_MODULE)
    base_path = Path(getattr(module, '__file__', 'N/A')).resolve()
    log(f"📦 Root module path: {base_path}")

    if hasattr(module, '__path__'):
        log("\n📂 Submodules loaded:")
        for finder, name, ispkg in pkgutil.walk_packages(module.__path__, module.__name__ + "."):
            try:
                submod = importlib.import_module(name)
                subfile = getattr(submod, '__file__', '')
                if subfile:
                    subfile_res = Path(subfile).resolve()
                    flag = ''
                    if not str(subfile_res).startswith(venv_root):
                        flag += '🟥 OUTSIDE venv'
                    if is_suspicious(str(subfile_res)):
                        flag += ' ⚠️ SUSPICIOUS'
                    if subfile_res.suffix in ['.pyd', '.dll', '.so']:
                        flag += ' 🧩 binary'
                    log(f" - {name:<40} → {subfile_res} {flag}")
            except Exception as e:
                log(f" - {name:<40} → ❌ {type(e).__name__}: {e}")
    else:
        log(f"ℹ️ Module {TARGET_MODULE} has no __path__, cannot walk submodules.")

except Exception as e:
    log(f"❌ Cannot import {TARGET_MODULE}: {e}")

# 📄 Salvataggio su file
with open(output_file, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

log(f"\n✅ Output saved to {output_file.absolute()}")
