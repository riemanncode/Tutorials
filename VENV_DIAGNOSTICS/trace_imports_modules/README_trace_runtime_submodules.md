# 🧪 Tracciamento Runtime dei Sottomoduli — `trace_runtime_submodules_to_txt.py`

## 🎯 Obiettivo dello script

Questo script è stato progettato per **ispezionare a runtime tutti i sottocomponenti realmente caricati** da un modulo Python specificato (es. `pandas`, `__future__`, ecc.) e verificare **da dove vengono effettivamente importati** nel filesystem.

---

## 🧠 Contesto dell'indagine

Durante i test diagnostici avanzati sull’ambiente virtuale `_bot11_dev`, è emerso un dubbio cruciale:

> I moduli esterni sembrano corretti, ma... **da dove vengono effettivamente importati i sottopacchetti che li compongono?**

In particolare:
- Si sospettava che alcuni moduli venissero caricati da **ambienti vecchi (es. `BOT_6`)** o **dalla Python standard installata in `C:\Python39`**
- Si voleva verificare che tutte le importazioni effettive **rientrassero nel venv attivo**
- Quando si rimuovevano i path ambientali (come `C:\Python39`), `__future__` e altri **non venivano più trovati**

---

## 🧪 Cosa fa lo script

1. Permette di specificare un modulo target (`TARGET_MODULE = 'pandas'` oppure `'__future__'`)
2. Importa dinamicamente il modulo principale
3. Se il modulo ha `__path__`, esplora i suoi sottopacchetti tramite `pkgutil.walk_packages`
4. Per ciascun sottomodulo:
   - Lo importa dinamicamente
   - Registra il percorso fisico da cui è stato caricato
   - Evidenzia se:
     - 🟥 È **fuori dal venv**
     - ⚠️ È **sospetto** (es. viene da `BOT_6`, `AppData`, `pycharmprojects`)
     - 🧩 È un modulo binario (`.pyd`, `.so`, `.dll`)
5. Salva l’intera traccia in un file `.txt` con timestamp

---

## 🧾 Esempio di uso diagnostico

Tracciando `__future__` senza rimuovere i vecchi `sys.path`:

```
📦 Root module path: C:\Python39\Lib\__future__.py
```

Dopo la rimozione dei path di sistema:

```
❌ Cannot import __future__: No module named '__future__'
```

💡 Questo conferma che:
> Il modulo `__future__` **non è realmente integrato nel venv**, ma viene servito dalla **standard library del Python globale** configurata in `pyvenv.cfg`

---

## ✅ Perché è utile

- Ti mostra la **verità runtime** su ogni modulo importato
- Rende evidente se stai caricando codice da **percorsi obsoleti**
- È ideale per audit, debugging, sicurezza e deployment in ambienti controllati

---

## 🔐 Consigli pratici

- Non fidarti solo dell'import logico o delle dipendenze in `requirements.txt`
- Verifica sempre **da dove viene davvero importato un modulo o sottomodulo**
- Usa questo strumento per isolare le dipendenze effettive prima di fare refactor o packaging

---

## 📌 Conclusione

> `trace_runtime_submodules_to_txt.py` è uno strumento potente per chi vuole avere **il controllo assoluto su cosa sta girando nel proprio ambiente Python**, utile in ogni contesto di refactoring, analisi della portabilità o audit di sicurezza.