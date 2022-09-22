# Gestione dei cookies #

Queste istruzioni sono relative alla macchina "desktop" del laboratorio virtuale.

Per svolgere l'attività di laboratorio digitare, in una console della macchina virtuale, il comando:

```
$ make run
```

Dal computer host, quello reale, aprite il browser e digitate la url:

```
http://192.168.5.2:5000
```
(o sostituite 192.168.5.2 con l'IP della macchina virtuale *desktop*).

Dopo aver digitato un nome corretto visitate la url:
```
http://192.168.5.2:5000/id
```
e verificate che venga visualizzato l'ultimo utente dichiarato nel login

## Esercizio ##

Fate in modo che la route "id" sia visualizzata solo se l'utente è stato riconosciuto.
