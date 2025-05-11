# 🧪 Test import moduli dopo pulizia `sys.path`

## 🎯 Obiettivo del test

Questo script nasce dalla necessità di verificare che i moduli esterni `pandas` e `numpy` vengano importati **esclusivamente** dal virtual environment attivo (`_bot11_dev`), escludendo qualsiasi interferenza da ambienti precedenti come `BOT_6`.

Per assicurarsi di ciò, è stata fatta una **pulizia esplicita di `sys.path`**, conservando soltanto:

- Le directory appartenenti al venv attivo
- La directory corrente del progetto

## Verificare se l’ambiente virtuale attivo (`_bot11_dev`) è realmente autonomo e autosufficiente nel fornire accesso ai moduli della standard library (`stdlib`), tra cui `__future__` e `ctypes`.

## 🧠 Motivazione

Durante l’indagine è emerso che, anche con il venv attivo, alcuni moduli venivano comunque caricati da ambienti legacy.  
Per ottenere **una diagnostica reale e "sterile"**, si è deciso di eliminare dal `sys.path` tutto ciò che non appartiene al contesto corrente.

Durante un'indagine più ampia sull'isolamento del virtual environment, ho notato che moduli come `pandas` e `numpy` funzionavano solo **se non veniva ripulito `sys.path`**.  
Quando `sys.path` veniva limitato **esclusivamente al venv**, improvvisamente moduli come `__future__` e `ctypes` risultavano **non importabili**.

---

## 🧪 OUTPUT ATTESO

```python
(_bot11_dev) D:\ASUS2(R)\Science\CODING\Python\VS_CODE\BOT11_2>"D:/ASUS2(R)/Science/CODING/Python/VS_CODE/BOT11_2/_bot11_dev/Scripts/python.exe" "d:/ASUS2(R)/Science/CODING/Python/VS_CODE/BOT11_2/__misc/test_if_modules_are_in_venv.py"
sys.path pulito:
 - D:\ASUS2(R)\Science\CODING\Python\VS_CODE\BOT11_2
 - D:\ASUS2(R)\Science\CODING\Python\VS_CODE\BOT11_2\_bot11_dev
 - D:\ASUS2(R)\Science\CODING\Python\VS_CODE\BOT11_2\_bot11_dev\lib\site-packages
 - D:\ASUS2(R)\Science\CODING\Python\VS_CODE\BOT11_2\_bot11_dev\lib\site-packages\win32
 - D:\ASUS2(R)\Science\CODING\Python\VS_CODE\BOT11_2\_bot11_dev\lib\site-packages\win32\lib
 - D:\ASUS2(R)\Science\CODING\Python\VS_CODE\BOT11_2\_bot11_dev\lib\site-packages\Pythonwin
❌ Errore di importazione: No module named '__future__'
❌ Errore di importazione: No module named 'ctypes'

(_bot11_dev) D:\ASUS2(R)\Science\CODING\Python\VS_CODE\BOT11_2>
```
