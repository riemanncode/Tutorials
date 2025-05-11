import importlib
import sys
import os

venv_root = os.environ.get('VIRTUAL_ENV', '')
print(f"🔍 Active VENV: {venv_root or 'None'}")
print(f"🐍 Python Executable: {sys.executable}\n")

print("📦 Importing __future__...")
try:
    import __future__
    future_path = getattr(__future__, '__file__', None)
    if future_path:
        print(f"✅ __future__.__file__ = {future_path}")
    else:
        print("✅ __future__ is a built-in module (no __file__)")
except Exception as e:
    print(f"❌ Import failed: {e}")