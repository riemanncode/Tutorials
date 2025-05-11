import os
import sys
import importlib
import pkgutil
from pathlib import Path


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


# Custom: set your old venv path to flag it
SUSPICIOUS_KEYWORDS = ["BOT_6", "_bot_6_", "pycharmprojects"]

# Get venv root
venv_root = os.environ.get("VIRTUAL_ENV", "")
print(f"\n📦 Current VENV: {venv_root or 'None'}\n")

# Load requirements.txt
req_file = Path("requirements.txt")
if not req_file.exists():
    print("❌ requirements.txt not found.")
    sys.exit(1)

with open(req_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

modules = []
for line in lines:
    line = line.strip()
    if line and not line.startswith("#"):
        modules.append(line.split("==")[0].split(">=")[0].split("<=")[0].strip())

def analyze_module(name):
    try:
        mod = importlib.import_module(name)
        mod_path = Path(getattr(mod, '__file__', 'N/A')).resolve()
        print(f"\n🔍 {name} loaded from: {mod_path}")

        if any(k.lower() in str(mod_path).lower() for k in SUSPICIOUS_KEYWORDS):
            print(f"    ⚠️  Suspicious path: likely from old venv or shared cache")

        if hasattr(mod, '__path__'):
            print("    📂 Scanning submodules for binary extensions...")
            for finder, subname, ispkg in pkgutil.walk_packages(mod.__path__, mod.__name__ + "."):
                try:
                    submod = importlib.import_module(subname)
                    submod_file = getattr(submod, '__file__', '')
                    if submod_file and any(ext in submod_file for ext in ['.pyd', '.dll', '.so']):
                        sub_path = Path(submod_file).resolve()
                        print(f"       • {subname} → {sub_path}")
                        if any(k.lower() in str(sub_path).lower() for k in SUSPICIOUS_KEYWORDS):
                            print(f"         ⚠️  Linked to suspicious location (BOT_6?)")
                except Exception:
                    continue

    except Exception as e:
        print(f"\n❌ Failed to import {name}: {e}")

# Main loop
for module in modules:
    analyze_module(module)

print("\n✅ Scan complete.")