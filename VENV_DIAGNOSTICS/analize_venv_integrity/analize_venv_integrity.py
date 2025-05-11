import os
import sys
from pathlib import Path
import platform

venv_root = os.environ.get('VIRTUAL_ENV')
python_exe = sys.executable
venv_cfg = Path(venv_root or ".") / "pyvenv.cfg"
system_prefix = sys.prefix
real_prefix = getattr(sys, 'real_prefix', None)

print(f"🔍 VENV Diagnostic Report")
print(f"🐍 Python executable: {python_exe}")
print(f"📂 sys.prefix: {system_prefix}")
print(f"💾 VIRTUAL_ENV env var: {venv_root}")
print(f"🖥️ OS: {platform.system()} {platform.release()} ({platform.architecture()[0]})\n")

if venv_cfg.exists():
    print(f"📄 Found pyvenv.cfg at: {venv_cfg}")
    with open(venv_cfg, "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            print(f"   {line.strip()}")
    print()

    home_path = None
    for line in lines:
        if line.lower().startswith("home"):
            home_path = line.split("=", 1)[-1].strip()
            break

    if home_path:
        print(f"🔗 Standard library likely comes from: {home_path}\\Lib")
        stdlib_path = Path(home_path) / "Lib"
        if stdlib_path.exists():
            print(f"✅ stdlib found at: {stdlib_path}")
        else:
            print(f"❌ stdlib path NOT found: {stdlib_path}")
        
        # Check if stdlib and executable mismatch
        if home_path.lower() not in python_exe.lower():
            print(f"\n⚠️ venv uses stdlib from {home_path}, but Python executable is in another location.")
            print(f"   This indicates a non-portable or system-coupled virtual environment.")
        else:
            print(f"\n✅ venv and stdlib are consistent.")
    else:
        print("❌ Could not determine stdlib 'home' path from pyvenv.cfg")
else:
    print("❌ pyvenv.cfg not found in the current VENV — are you sure it's active?")

print("\n📌 Summary:")
if not venv_root:
    print("❌ No virtual environment is currently active.")
elif not venv_cfg.exists():
    print("⚠️ pyvenv.cfg missing — venv may be broken or incomplete.")
else:
    print("✅ Venv structure appears intact, but check 'home' path for coupling with global Python.")
