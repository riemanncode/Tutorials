# 📦 Verifica degli Import da `requirements.txt` — `trace_imports_modules.py`

## 🎯 Obiettivo dello script

Questo script serve per **verificare concretamente** che tutti i moduli elencati in `requirements.txt` siano:
- **Installati correttamente**
- **Importabili**
- **Localizzati nel virtual environment attivo** (`_bot11_dev`)

---

## 🧠 Perché è stato creato

Durante l'indagine sul malfunzionamento degli import in `_bot11_dev`, era emersa una situazione ambigua:
- Alcuni moduli sembravano funzionare solo se il `sys.path` non veniva ripulito
- C'era il dubbio che alcuni moduli installati **venissero in realtà caricati da ambienti precedenti** (es. `BOT_6`) o da Python globale
- Era necessario un controllo realistico che simulasse effettivamente l'import e mostrasse **la provenienza reale dei moduli**

---

## 🧪 Cosa fa lo script

1. **Pulisce `sys.path`**, mantenendo solo:
   - I path del venv attivo
   - La directory corrente del progetto

2. Legge riga per riga il file `requirements.txt`  
   (compatibile con versioni tipo `modulo==1.2.3`, `modulo>=1.0`, ecc.)

3. Per ogni modulo:
   - Tenta l'import reale
   - Identifica il file sorgente (`__file__`) da cui è stato importato
   - Verifica se quel file si trova **dentro il venv o no**
   - Evidenzia i moduli “esterni” o problematici

4. Elenca alla fine tutti i moduli:
   - ❌ Che non si riescono a importare
   - 🟥 Che sono stati caricati da fuori dal venv

---

## 🧾 Output tipico

```
📦 Verifica reale degli import da requirements.txt
🔒 Virtual Env attivo: D:\...\_bot11_dev

 - pandas               → D:\...\_bot11_dev\lib\site-packages\pandas\__init__.py 🟩 interno
 - numpy                → D:\...\Python39\Lib\site-packages\numpy\__init__.py 🟥 ESTERNO
 - matplotlib           → ❌ Import error: No module named 'matplotlib'

⚠️ Moduli problematici (fuori dal venv o con errori di import):
 - numpy → D:\...\Python39\Lib\site-packages\numpy\__init__.py
 - matplotlib → IMPORT FAILED
```

---

## ✅ Vantaggi

- 🔍 **Controllo realistico**: simula esattamente cosa succede quando Python importa i moduli
- 🚨 **Individua rischi invisibili**: scopre moduli caricati da ambienti sbagliati
- 🛡️ **Utile in produzione**: assicura che il deployment sia chiuso e autonomo

---

## 🔐 Suggerimenti

- Usa questo script prima di fare deploy su server o condivisione del progetto
- Se un modulo risulta “ESTERNO”, reinstalla forzatamente nel venv con:
  ```bash
  pip install --force-reinstall <modulo>
  ```
- Mantieni sempre aggiornato `requirements.txt` con:
  ```bash
  pip freeze > requirements.txt
  ```

---

## 📌 Conclusione

> Questo script è la garanzia che **tutti i moduli del tuo progetto siano realmente installati e serviti dal venv corretto**, proteggendoti da dipendenze invisibili, ambienti corrotti o import legacy da progetti passati.