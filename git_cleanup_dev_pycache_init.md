# 🔁 Pulizia del progetto Git (branch `_dev`)

Obiettivo: **rimuovere file compilati Python** (`*.pyc`, `__pycache__/`) dal repository Git **nel branch `_dev`**, e opzionalmente anche i file `__init__.py` se non servono.

---

## ✅ 1. Vai nella root del progetto Git

```bash
cd D:\ASUS2(R)\Science\CODING\Python\VS_CODE\BOT11_2
```

Assicurati che in questa directory sia presente la cartella `.git`.

---

## ✅ 2. Passa al branch `_dev`

```bash
git checkout _dev
```

Ora stai lavorando **solo su `_dev`**.

---

## ✅ 3. Rimuovi dall’indice Git tutti i file `.pyc` (senza cancellarli dal disco)

```bash
git rm -r --cached --ignore-unmatch *.pyc
```

Questo dice a Git:  
> "Smetti di tracciare ogni `.pyc`, ma non cancellarli."

---

## ✅ 4. Rimuovi anche tutte le cartelle `__pycache__` tracciate

```bash
git rm -r --cached --ignore-unmatch __pycache__/
```

💡 Questo vale **anche nei sottopercorsi**.

---

## ✅ 5. Verifica cosa stai per committare

```bash
git status
```

Vedrai i `.pyc` e `__pycache__` elencati sotto "Changes to be committed (deleted)".

---

## ✅ 6. Commit della pulizia

```bash
git commit -m "Pulizia: rimossi file compilati Python (.pyc) e cache"
```

---

## ✅ 7. Pusha le modifiche su GitHub

```bash
git push origin _dev
```

Ora anche **GitHub sarà pulito**.

---

## 🧹 (Facoltativo) Rimozione dei file `__init__.py` se non più necessari

### ✅ Cerca tutti gli `__init__.py` nel progetto:

```bash
dir /s /b __init__.py
```

### ✅ Rimuovili manualmente se **non sono usati per import tra cartelle**.

⚠️ **NON cancellare `__init__.py` da pacchetti che vengono importati come moduli.**  
Tienili solo se **non stai usando import cross-folder**.

---

📅 Ultima modifica: 7 Maggio 2025