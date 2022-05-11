import redis
import random 
r = redis.StrictRedis(host='10.255.237.221', port=6379, password='1357642rVi0', db=0)
r.keys()

profilo_utente={}
def registrazione():
    profilo_utente = []
    r.sadd('profilo1',str(input("Inserisci il tuo nome utente:\n ")))
    #profilo_utente.append(str(input("Inserisci il tuo nome utente")))
    #profilo_utente.append(str(input("Inserisci la tua password")))
    #print(profilo_utente)
    
    #r.sadd('profilo1',profilo_utente)

registrazione()