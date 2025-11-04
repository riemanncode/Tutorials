# Avvio Ollama con GPU (Windows, NVIDIA)

## Prerequisiti
1) scaricare ultimi driver nvdia per la propria gpu  
2) scaricare e settare CUDA compatibile con il proprio computer  
3.1) aggiungere il path di ollama.exe nel pannello di controllo nvidia: gestiscileimpostazioni3d/impostazioniprogramma/aggiungi/path_ollama/ollama.exe  
3.2) aggiungi alle impostazioni di grafiche di windows ollama: sistema/schermo/grafica/aggiungiappdesktop/path_ollama/ollama.exe  
4) scaricare ollama dal suo sito principale. normalmente runnerà usando soltanto la cpu con i comandi 'ollama run gemma3:1b' (gemma3:1b è il modello google da 1B params). 
i comandi per runnare l'llm locale con anche la gpu sono i seguenti:

---

## Avvia server con GPU
```powershell
# Chiudi eventuali processi Ollama
Get-Process ollama -ErrorAction SilentlyContinue | Stop-Process -Force

# Percorsi librerie Ollama
$oll = "$Env:LOCALAPPDATA\Programs\Ollama\lib\ollama"

# Lascia vuoto OLLAMA_LLM_LIBRARY (autodetect)
Remove-Item Env:OLLAMA_LLM_LIBRARY -ErrorAction SilentlyContinue

# Espone le DLL CUDA v12 incluse con Ollama
$env:OLLAMA_LIBRARY_PATH = "$oll;$oll\cuda_v12"
$env:PATH = "$oll;$oll\cuda_v12;$env:PATH"

# Forza uso della GPU 0
$env:CUDA_VISIBLE_DEVICES = "0"

# Avvia il server
& "$Env:LOCALAPPDATA\Programs\Ollama\ollama.exe" serve
```
---
