# 🧪 Diagnostica della Struttura del Virtual Environment — `analyze_venv_integrity.py`

## 🎯 Obiettivo dello script

Questo script è stato creato per **ispezionare in dettaglio la struttura interna di un virtual environment Python**, con particolare attenzione al file `pyvenv.cfg`, all’origine della standard library utilizzata e alla portabilità dell’ambiente.

---

## 🧠 Perché è stato necessario

Durante una serie di test avanzati sul funzionamento del mio venv `_bot11_dev`, ho scoperto che:

- Alcuni moduli come `__future__` e `ctypes` risultavano **non disponibili** quando ripulivo `sys.path`.
- Altri moduli sembravano funzionare solo se il venv **continuava a puntare** a directory del Python installato globalmente.
- Avevo il dubbio che il mio ambiente virtuale non fosse realmente **isolato**, ma **accoppiato a una installazione legacy** di Python (`C:\Python39`).
- Inoltre, sospettavo che il venv stesse caricando moduli dalla stdlib di sistema anche quando non avrebbe dovuto.

Da qui la necessità di creare **uno script di diagnostica strutturata**, capace di:

- Leggere `pyvenv.cfg`
- Mostrare da dove viene presa la stdlib
- Confrontare `sys.prefix` e `sys.executable`
- Verificare se l’ambiente può dirsi "portabile"

---

## 🔎 Cosa fa lo script

1. Mostra:

   - il `python.exe` attivo
   - il valore di `sys.prefix`
   - il path del file `pyvenv.cfg`
   - il valore della variabile d'ambiente `VIRTUAL_ENV`
   - il sistema operativo in uso

2. Legge il file `pyvenv.cfg` e cerca la riga `home = ...`  
   Questo campo è fondamentale: **definisce dove il venv va a cercare la standard library** (`Lib`, `DLLs`, moduli integrati, ecc.)

3. Verifica:
   - Se quella directory esiste
   - Se `home` corrisponde al percorso dell'interprete attivo
   - Se il venv è effettivamente "consistente" oppure **accoppiato a un Python esterno**

---

## 🧾 Esempio di output significativo

```
🔍 VENV Diagnostic Report
🐍 Python executable: D:\...\_bot11_dev\Scripts\python.exe
📂 sys.prefix: D:\...\_bot11_dev
💾 VIRTUAL_ENV env var: D:\...\_bot11_dev
🖥️ OS: Windows 10 (64bit)

📄 Found pyvenv.cfg at: D:\...\_bot11_dev\pyvenv.cfg
   home = C:\Python\Python39
   include-system-site-packages = false
   version = 3.9.9

🔗 Standard library likely comes from: C:\Python\Python39\Lib
✅ stdlib found at: C:\Python\Python39\Lib

⚠️ venv uses stdlib from C:\Python\Python39, but Python executable is in another location.
   This indicates a non-portable or system-coupled virtual environment.

📌 Summary:
✅ Venv structure appears intact, but check 'home' path for coupling with global Python.
```

---

## ✅ Conclusioni

Questo tipo di diagnostica è stato **cruciale** per confermare che il mio venv `_bot11_dev`:

- Non era realmente autonomo
- Dipendeva ancora da una installazione globale (`C:\Python39`)
- Poteva causare **comportamenti ambigui** durante test, debugging o distribuzione

> Lo script è ora parte del mio toolset di diagnostica Python per garantire ambienti riproducibili, isolati e trasparenti.
