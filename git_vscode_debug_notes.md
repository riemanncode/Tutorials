# ✅ Riepilogo Giornaliero — Git, VS Code, PYTHONPATH, Import personalizzati

## 🔧 Sezione 1 — Gestione Git

### COMANDI BASE UTILI
```bash
git log --oneline --graph --decorate --all    # per vedere il percorso grafico del developement
git log --oneline
git fetch     # per aggiornare i branch fatti nella IDE (se non li legge)
```

### PER DOWNLOADARE PERFETTAMENTE E SINCRONIZZARE IL MIO PROGETTO CON IL BRANCH DI SCELTO
```bash
git fetch origin
git checkout _dev
git reset --hard origin/_dev
git clean -fdx
```

### CHERRY PICKING
```bash
git branch
git checkout nome_del_branch
git cherry-pick 123456abc

echo per tornare indietro e cancellare cherry pick dal branch (locale)
git reset --hard HEAD~1

echo per pusharlo su github in remoto
git push

echo comando per cancellare il push che è stato fatto in remoto
git push origin HEAD~1:_dev --force

echo comando per ri-allineare il locale con quello che c'è in remoto
git fethc origin
git reset --hard origin/dev
```


### ▶️ CASO 1: Parti da una cartella locale (progetto già esistente)

```bash
git init
git remote add origin https://github.com/tuo_username/NOME_REPO.git
git remote -v
git remote show origin
git add .
git commit -m "Primo commit"
git push -u origin master
```

### ▶️ CASO 2: Parti da GitHub e vuoi clonare il progetto
```bash
rmdir /s /q .git
cd c:\path\del\tuo\progetto
git clone https://github.com/tuo_username/NOME_REPO.git
cd NOME_REPO
python -m venv _venv 
cd _venv\Scripts\
activate
pip install -r requirements.txt
code .
```
Dopo il clone:
```bash
git add .
git commit -m "Modifiche"
git push
```

### Creazione nuovo branch su GitHub
```bash
git branch nome_del_branch
git branch
git checkout nome_del_branch
git push -u origin nome_del_branch
git branch -r
```

### 📂 Ignorare file inutili

File `.gitignore` ideale:

```
# Ambenti virtuali
venv/
_bot_11_2/
env/

# Cache Python
__pycache__/
*.pyc
*.pyo

# IDE
.idea/
.vscode/

# File vari
*.log
*.dill
autosaves/
```

### 🔍 Controllo dei file prima del commit

```bash
git status                  # Vedi cosa è pronto
git diff                    # Differenze non aggiunte
git diff --cached           # Differenze già aggiunte (staged)
git diff --name-only --cached  # Solo nomi file staged
```

---

## 🧠 Sezione 2 — VS Code vs PyCharm + problemi comuni

### 🧩 Differenze chiave:

| Aspetto        | VS Code                  | PyCharm                   |
|----------------|--------------------------|---------------------------|
| Git integrato  | Leggero ma meno smart    | Più robusto e visivo      |
| PYTHONPATH     | Non gestito da default   | Spesso configurato per progetto |
| Console        | Più simile a quella reale| Usa cwd = root del progetto |

### 💥 Problema: importazione di vecchi moduli

Sintomo: un modulo importato (`colored`) stampa da un file **vecchio** che non esiste più o appartiene a un altro progetto (`BOT_6`).

---

## 🚨 Soluzione — individuazione e fix

### ✅ Scoprire da dove viene il modulo:

```python
from UFZ.utili_funzioni.colored2gpt.colored2gpt01 import colored
import sys

print(colored("Testo colorato", "black", "on_red", ["bold", "underline"]))
print("\n--- DEBUG ORIGINE FUNZIONE 'colored' ---")

# Stampa il nome del modulo da cui la funzione è importata
print("Modulo dichiarato:", colored.__module__)

# Cerca nel sys.modules il modulo da cui è stata importata
modulo_origine = sys.modules.get(colored.__module__)

# Stampa il file fisico se esiste
if modulo_origine:
    print("File effettivo del modulo:", getattr(modulo_origine, '__file__', '❌ Modulo non trovato su disco'))
else:
    print("❌ Modulo non presente in sys.modules")

print("--- FINE DEBUG ---\n")
```

### ✅ Eliminare interferenze di `PYTHONPATH`

#### 1. Da terminale (temporaneo)

```bash
set PYTHONPATH=
```

#### 2. Da codice Python (per sicurezza)

```python
import os
os.environ.pop("PYTHONPATH", None)
```

#### 3. DEFINITIVO: rimuovi `PYTHONPATH` dalle Variabili d’Ambiente di Windows

---

## 📦 Altri strumenti diagnostici utili

```python
import sys
print("sys.path:")
print("\n".join(sys.path))
```

```bash
# Trova tutte le copie del modulo
dir /s /b Colored.py
```

```bash
# Elimina __pycache__ in tutta la repo
for /r %i in (__pycache__) do @rd /s /q "%i"
```

---

## ✅ Conclusione

- Gestisci sempre `.gitignore` prima dei commit
- Controlla `PYTHONPATH` quando vedi import strani
- Preferisci ambienti `venv` isolati per ogni progetto
- Usa `colored.__module__` + `sys.modules` per sapere esattamente da dove viene qualsiasi funzione o modulo

---

📅 Ultima modifica: 7 Maggio 2025
