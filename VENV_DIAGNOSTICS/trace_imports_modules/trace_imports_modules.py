import sys
import os
from pathlib import Path

venv_root = os.environ.get('VIRTUAL_ENV', '')
# Mantieni solo i path che stanno dentro il tuo venv attivo o nella directory corrente
# queste riga qua sotto è da includere/escludere per fare degli esperimenti sul codice
sys.path = [p for p in sys.path if venv_root in p or p.startswith(os.getcwd())]
print("sys.path pulito:")
for p in sys.path:
    print(" -", p)


req_file = Path("requirements.txt")

if not req_file.exists():
    print("❌ requirements.txt non trovato.")
    sys.exit(1)

print(f"\n📦 Verifica reale degli import da requirements.txt")
print(f"🔒 Virtual Env attivo: {venv_root or 'Nessuno'}\n")

external_modules = []

with open(req_file, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith("#"):
            continue

        mod_name = line.split("==")[0].split(">=")[0].split("<=")[0].strip()

        try:
            module = __import__(mod_name)
            origin = getattr(module, '__file__', '<built-in or frozen>')
            is_external = venv_root not in origin if venv_root else True
            tag = "🟥 ESTERNO" if is_external else "🟩 interno"
            print(f" - {mod_name:<20} → {origin} {tag}")
            if is_external:
                external_modules.append((mod_name, origin))
        except Exception as e:
            print(f" - {mod_name:<20} → ❌ Import error: {e}")
            external_modules.append((mod_name, "IMPORT FAILED"))

if external_modules:
    print("\n⚠️ Moduli problematici (fuori dal venv o con errori di import):")
    for name, path in external_modules:
        print(f" - {name} → {path}")
else:
    print("\n✅ Tutti i moduli sono stati importati correttamente dal venv attivo.")
