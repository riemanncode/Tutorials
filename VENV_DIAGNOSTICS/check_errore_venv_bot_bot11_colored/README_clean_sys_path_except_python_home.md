# 🧼 Pulizia selettiva di `sys.path` — `clean_sys_path_except_python_home.py`

## 🎯 Obiettivo dello script

Questo script ha lo scopo di **ripulire `sys.path` da percorsi estranei**, mantenendo soltanto quelli **essenziali per il corretto funzionamento del Python corrente**, ovvero:
- La **standard library** del Python associato all’ambiente virtuale o interprete attivo
- (Opzionalmente) La directory di lavoro corrente (`cwd`)

---

## 🧠 Perché è stato scritto

Durante l’indagine su ambienti virtuali corrotti o ibridi, ho osservato che Python manteneva in `sys.path`:
- Vecchie cartelle (`BOT_6`, progetti PyCharm, cartelle temporanee)
- Percorsi legati alla Python globale (`C:\Python39\...`)
- Riferimenti ambigui tra più ambienti virtuali

> Questo portava a situazioni dove moduli venivano caricati da ambienti errati, causando bug silenziosi, incompatibilità e comportamenti non riproducibili.

---

## 🧪 Cosa fa lo script

- Analizza tutti i path presenti in `sys.path`
- Determina qual è la root Python (tramite `sys.base_prefix`)
- Tiene solo:
  - Percorsi che appartengono alla **Python Home**
  - (Se attivo) la **directory corrente** e sue sottocartelle
- Aggiorna `sys.path` con i percorsi filtrati
- Stampa il nuovo elenco “pulito”

---

## 🧾 Esempio di output

```
🧹 sys.path pulito:
 - D:\Python39\Lib
 - D:\Progetto\BOT11_2
 - D:\Progetto\BOT11_2\moduli
✅ Pulizia completata.
```

---

## ✅ Quando usarlo

- Prima di import diagnostici o test isolati
- In script automatici per verificare la coerenza degli import
- Quando si vuole evitare qualunque interferenza da ambienti esterni

---

## ⚠️ Attenzione

> Questo script **non include i path al venv attivo** (`site-packages`) se questi non coincidono con la Python Home.  
> È adatto per contesti in cui si vuole **simulare un ambiente minimale** oppure isolare la standard library.

---

## 📌 Conclusione

> `clean_sys_path_except_python_home.py` è uno strumento semplice ma potente per garantire che Python utilizzi solo le risorse fondamentali, rendendo il comportamento del tuo script più prevedibile e pulito.