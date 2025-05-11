# 🧼 Diagnosi e rimozione dei path ambientali da `sys.path`

Questo script ha lo scopo di:

- Stampare tutti i percorsi attivi nel `sys.path`
- Evidenziare se esistono o meno sul filesystem
- Rimuovere dinamicamente dal `sys.path` tutti i path **non appartenenti al venv attivo o alla cartella di lavoro corrente**

---

## 📦 OUTPUT ATTESO

```python
(_bot11_dev) D:\ASUS2(R)\Science\CODING\Python\VS_CODE\BOT11_2>"D:/ASUS2(R)/Science/CODING/Python/VS_CODE/BOT11_2/_bot11_dev/Scripts/python.exe" "d:/ASUS2(R)/Science/CODING/Python/VS_CODE/BOT11_2/__misc/check_errore_venv_bot_6_2.py"
>>> sys.path attivi:

00: d:\ASUS2(R)\Science\CODING\Python\VS_CODE\BOT11_2\__misc (esiste)
01: D:\ASUS2(R)\Science\CODING\Python\PycharmProjects\BOT_6 (esiste)
02: D:\ASUS2(R)\Science\CODING\Python\PycharmProjects\BOT_6\_bot_6_ (esiste)
03: D:\ASUS2(R)\Science\CODING\Python\PycharmProjects\BOT_6\_bot_6_\Scripts (esiste)
04: D:\ASUS2(R)\Science\CODING\Python\VS_CODE\BOT11_2 (esiste)
05: C:\Python\Python39\python39.zip (NON esiste)
06: C:\Python\Python39\DLLs (esiste)
07: C:\Python\Python39\lib (esiste)
08: C:\Python\Python39 (esiste)
09: D:\ASUS2(R)\Science\CODING\Python\VS_CODE\BOT11_2\_bot11_dev (esiste)
10: D:\ASUS2(R)\Science\CODING\Python\VS_CODE\BOT11_2\_bot11_dev\lib\site-packages (esiste)
11: D:\ASUS2(R)\Science\CODING\Python\VS_CODE\BOT11_2\_bot11_dev\lib\site-packages\win32 (esiste)    
12: D:\ASUS2(R)\Science\CODING\Python\VS_CODE\BOT11_2\_bot11_dev\lib\site-packages\win32\lib (esiste)
13: D:\ASUS2(R)\Science\CODING\Python\VS_CODE\BOT11_2\_bot11_dev\lib\site-packages\Pythonwin (esiste)

sys.executable D:\ASUS2(R)\Science\CODING\Python\VS_CODE\BOT11_2\_bot11_dev\Scripts\python.exe

>>> rimozione delle variabili di ambiente <<<
>>> rimozione delle variabili di ambiente <<<
sys.path pulito:
 - D:\ASUS2(R)\Science\CODING\Python\VS_CODE\BOT11_2
 - D:\ASUS2(R)\Science\CODING\Python\VS_CODE\BOT11_2\_bot11_dev
 - D:\ASUS2(R)\Science\CODING\Python\VS_CODE\BOT11_2\_bot11_dev\lib\site-packages
 - D:\ASUS2(R)\Science\CODING\Python\VS_CODE\BOT11_2\_bot11_dev\lib\site-packages\win32
 - D:\ASUS2(R)\Science\CODING\Python\VS_CODE\BOT11_2\_bot11_dev\lib\site-packages\win32\lib
 - D:\ASUS2(R)\Science\CODING\Python\VS_CODE\BOT11_2\_bot11_dev\lib\site-packages\Pythonwin
>>> sys.path attivi:

00: D:\ASUS2(R)\Science\CODING\Python\VS_CODE\BOT11_2 (esiste)
01: D:\ASUS2(R)\Science\CODING\Python\VS_CODE\BOT11_2\_bot11_dev (esiste)
02: D:\ASUS2(R)\Science\CODING\Python\VS_CODE\BOT11_2\_bot11_dev\lib\site-packages (esiste)
03: D:\ASUS2(R)\Science\CODING\Python\VS_CODE\BOT11_2\_bot11_dev\lib\site-packages\win32 (esiste)
04: D:\ASUS2(R)\Science\CODING\Python\VS_CODE\BOT11_2\_bot11_dev\lib\site-packages\win32\lib (esiste)
05: D:\ASUS2(R)\Science\CODING\Python\VS_CODE\BOT11_2\_bot11_dev\lib\site-packages\Pythonwin (esiste)

sys.executable D:\ASUS2(R)\Science\CODING\Python\VS_CODE\BOT11_2\_bot11_dev\Scripts\python.exe

