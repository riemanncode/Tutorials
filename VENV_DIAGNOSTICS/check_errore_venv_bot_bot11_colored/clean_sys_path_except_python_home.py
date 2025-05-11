import sys
import os
from pathlib import Path

def clean_sys_path_except_python_home(include_cwd=True):
    # Determina la Python home da pyvenv.cfg o sys.base_prefix
    python_home = Path(sys.base_prefix).resolve()
    cwd = Path(os.getcwd()).resolve()

    # Costruisci nuovo sys.path filtrato
    new_path = []
    for p in sys.path:
        try:
            full_path = Path(p).resolve()
            if python_home in full_path.parents or full_path == python_home:
                new_path.append(p)
            elif include_cwd and cwd in full_path.parents:
                new_path.append(p)
        except Exception:
            continue

    sys.path = new_path
    print("🧹 sys.path pulito:")
    for p in sys.path:
        print(" -", p)


if __name__ == "__main__":
    # Esegui la funzione per pulire sys.path
    clean_sys_path_except_python_home()
    print("\n✅ Pulizia completata.")