# 🔍 Deep Scan dei Moduli da `requirements.txt` — `deep_trace_imports_requirements.py`

## 🎯 Obiettivo dello script

Questo script esegue una **scansione approfondita** di tutti i moduli elencati in `requirements.txt`, verificando non solo l'importazione principale ma anche:

- Il **percorso fisico di ogni modulo**
- L'**origine dei sottomoduli**, soprattutto se compilati (`.pyd`, `.dll`, `.so`)
- La **presenza di tracce sospette** riconducibili ad ambienti virtuali precedenti (es. `BOT_6`, `pycharmprojects`, ecc.)

---

## 🧠 Perché è stato scritto

Dopo aver rilevato che molti moduli funzionavano correttamente solo con vecchi ambienti virtuali ancora caricati nel `sys.path`, si è presentata la necessità di:

- Capire se anche i **moduli "attivi" nel venv** stavano in realtà **caricando componenti binarie da ambienti obsoleti**
- Tracciare l’origine **a runtime** di ciascun modulo e dei suoi sottocomponenti compilati
- Identificare con certezza se un modulo è effettivamente servito dal venv attuale

---

## 🧪 Cosa fa lo script

1. Pulisce `sys.path`, mantenendo solo:
   - I path contenenti il venv attivo
   - Il progetto corrente

2. Carica tutti i moduli elencati in `requirements.txt` (compatibile con `==`, `>=`, `<=`, ecc.)

3. Per ogni modulo:
   - Effettua un `importlib.import_module()`
   - Mostra il percorso da cui viene importato (`__file__`)
   - Evidenzia ⚠️ se il modulo proviene da una directory sospetta (es. `BOT_6`, `pycharmprojects`)

4. Se il modulo ha attributo `__path__`, esegue `pkgutil.walk_packages()` per analizzare tutti i sottomoduli:
   - Tenta l'importazione di ciascuno
   - Registra ogni percorso `.pyd`, `.dll`, `.so`
   - Evidenzia ⚠️ se anche questi puntano a posizioni non desiderate

---

## 🧾 Esempio di output

```
📦 Current VENV: D:\...\_bot11_dev

🔍 numpy loaded from: D:\Python39\Lib\site-packages\numpy\__init__.py
    ⚠️  Suspicious path: likely from old venv or shared cache
    📂 Scanning submodules for binary extensions...
       • numpy.core._multiarray_umath → D:\Python39\Lib\site-packages\numpy\core\_multiarray_umath.cp39-win_amd64.pyd
         ⚠️  Linked to suspicious location (BOT_6?)
```

---

## ✅ Risultati attesi

- 🛑 Ti avvisa se stai **usando ancora librerie binarie compilate in ambienti precedenti**
- 🔍 Ti permette di decidere quali moduli vanno **reinstallati** nel venv attuale
- 🛡️ Ti protegge da bug silenziosi o comportamenti anomali dovuti a cache di PyCharm, shared folders, o copie residue

---

## 🔐 Buone pratiche consigliate

- Reinstalla i moduli sospetti con:
  ```bash
  pip uninstall -y <modulo> && pip install --no-cache-dir <modulo>
  ```

- Usa ambienti creati con `--copies` per portabilità:
  ```bash
  python -m venv --copies _bot11_dev
  ```

- Evita di usare moduli condivisi tra ambienti diversi (specialmente compilati)

---

## 📌 Conclusione

> Questo è il **livello massimo di controllo** possibile su ciò che viene effettivamente eseguito nel tuo ambiente Python.  
> Perfetto per validazione pre-deploy, refactor di ambienti legacy, e audit di sicurezza nei progetti complessi.