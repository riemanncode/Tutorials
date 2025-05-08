# ✅ Guida Git & GitHub per sviluppo con branch `_dev` e `main`

Questa guida raccoglie tutto ciò che serve sapere per gestire un progetto Git/GitHub strutturato con branch di sviluppo e produzione.

---

## 🚀 STRUTTURA CONSIGLIATA

- `main` (o `master`) → branch stabile, ufficiale
- `_dev` → branch di sviluppo, test, sperimentazioni

---

## 🛠️ Creazione repository da GitHub (CASO 2)

```bash
cd D:\percorso\dove\vuoi
git clone https://github.com/tuo_username/NOME_REPO.git
cd NOME_REPO
python -m venv _venv
_venv\Scripts\activate
pip install -r requirements.txt
code .
```

---

## 🧹 File `.gitignore` consigliato

```gitignore
# Ambienti virtuali
venv/
_venv/
env/
_bot_11_2/

# Cache Python
__pycache__/
*.pyc
*.pyo

# IDE/editor
.vscode/
.idea/

# File temporanei
*.log
*.dill
autosaves/
```

---

## 🧱 Inizializzazione Git da progetto locale (CASO 1)

```bash
git init
git remote add origin https://github.com/tuo_username/NOME_REPO.git
git add .
git commit -m "Primo commit"
git push -u origin master
```

---

## 🌿 Branch: creare e gestire `_dev`

### Creare senza spostarsi:

```bash
git branch _dev
```

### Creare e spostarsi:

```bash
git checkout -b _dev
```

### Verificare i branch:

```bash
git branch        # locali
git branch -r     # remoti
```

### Pusha `_dev` su GitHub:

```bash
git push -u origin _dev
```

---

## 🔀 Unire `_dev` dentro `main`

### Metodo diretto:

```bash
git checkout main
git pull origin main
git merge _dev
git push origin main
```

### Metodo controllato (dry-run):

```bash
git checkout main
git merge --no-commit --no-ff _dev
# Se tutto ok:
git commit
git push origin main
# Se vuoi annullare:
git merge --abort
```

---

## 🔁 Rebase (linea di sviluppo pulita)

```bash
git checkout _dev
git rebase main
git checkout main
git merge _dev
```

---

## ✅ Controlli utili

### Visualizza stato prima del commit:

```bash
git status
```

### Controlla i file staged:

```bash
git diff --cached
git diff --name-only --cached
```

### Verifica remote attivo:

```bash
git remote -v
```

---

## 🧠 Concetti chiave

| Term | Significato |
|------|-------------|
| `origin` | Nome predefinito del repository remoto su GitHub |
| `HEAD -> main` | Indica il branch attualmente attivo |
| `origin/HEAD -> origin/main` | Il branch predefinito del repo su GitHub |
| `-u` (in push) | Collega il branch locale al corrispondente remoto |

---

## 📌 Best Practices

- Lavora sempre su `_dev`, non direttamente su `main`
- Usa `pull request` se vuoi revisione o tracciamento
- Pulisci spesso con `.gitignore` e `git rm --cached ...`
- Riusa i comandi `git status` e `git branch` ogni giorno

---

📅 Ultima modifica: 7 Maggio 2025