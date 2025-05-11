import os
import sys
import importlib


# ho fatto questo file perché in colored2gpt01.py si verificava un print statement print("colored()") che in realtà non era
# presente nell ultima versione di colored2gpt01.py ma in una versione precedente, quindi ho capito 
# che la funzione non veniva chiamata dal nuovo progetto BOT11 dentro UFZ ma da un vecchio progetto
# che aveva questa vecchia versione di colored2gpt01.py --> BOT6. Ho quindi cominciato ad indagare


from UFZ.utili_funzioni.colored2gpt.colored2gpt01 import colored

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




print("rimuoviamo tutti i venv e anche il python di sistema che si trova in C:\\ e rifacciamo la diagnostica")
venv_root = os.environ.get('VIRTUAL_ENV', '')
# Mantieni solo i path che stanno dentro il tuo venv attivo o nella directory corrente
sys.path = [p for p in sys.path if venv_root in p or p.startswith(os.getcwd())]
print("sys.path pulito:")
for p in sys.path:
    print(" -", p)


# Cancella il modulo dalla cache per forzare la nuova importazione
module_name = colored.__module__
if module_name in sys.modules:
    print(f"🔁 Rimozione da cache: {module_name}")
    del sys.modules[module_name]
from UFZ.utili_funzioni.colored2gpt.colored2gpt01 import colored

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








# OUTPUT:
# (_bot11_dev) D:\ASUS2(R)\Science\CODING\Python\VS_CODE\BOT11_2>"D:/ASUS2(R)/Science/CODING/Python/VS_CODE/BOT11_2/_bot11_dev/Scripts/python.exe" "d:/ASUS2(R)/Science/CODING/Python/VS_CODE/BOT11_2/__misc/VENV_DIAGNOSTICS/check_errore_venv_bot6_bot11_colored.py"
# colored()
# Testo colorato

# --- DEBUG ORIGINE FUNZIONE 'colored' ---
# Modulo dichiarato: UFZ.utili_funzioni.colored2gpt.colored2gpt01
# File effettivo del modulo: D:\ASUS2(R)\Science\CODING\Python\PycharmProjects\BOT_6\UFZ\utili_funzioni\colored2gpt\colored2gpt01.py
# --- FINE DEBUG ---

# rimuoviamo tutti i venv e anche il python di sistema che si trova in C:\ e rifacciamo la diagnostica
# sys.path pulito:
#  - D:\ASUS2(R)\Science\CODING\Python\VS_CODE\BOT11_2
#  - D:\ASUS2(R)\Science\CODING\Python\VS_CODE\BOT11_2\_bot11_dev
#  - D:\ASUS2(R)\Science\CODING\Python\VS_CODE\BOT11_2\_bot11_dev\lib\site-packages
#  - D:\ASUS2(R)\Science\CODING\Python\VS_CODE\BOT11_2\_bot11_dev\lib\site-packages\win32
#  - D:\ASUS2(R)\Science\CODING\Python\VS_CODE\BOT11_2\_bot11_dev\lib\site-packages\win32\lib
#  - D:\ASUS2(R)\Science\CODING\Python\VS_CODE\BOT11_2\_bot11_dev\lib\site-packages\Pythonwin
# 🔁 Rimozione da cache: UFZ.utili_funzioni.colored2gpt.colored2gpt01
# Testo colorato

# --- DEBUG ORIGINE FUNZIONE 'colored' ---
# Modulo dichiarato: UFZ.utili_funzioni.colored2gpt.colored2gpt01
# File effettivo del modulo: D:\ASUS2(R)\Science\CODING\Python\VS_CODE\BOT11_2\UFZ\utili_funzioni\colored2gpt\colored2gpt01.py
# --- FINE DEBUG ---


# (_bot11_dev) D:\ASUS2(R)\Science\CODING\Python\VS_CODE\BOT11_2>