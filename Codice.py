import redis 
from random import *


r = redis.StrictRedis(host='93.145.175.242', password='1357642rVi0', port=6379, db=0)

r.keys()

#profilo_utente={}
#def_registrazione():
  #profilo_utente=[]
  #r.sadd('Utente1',str(input('inserisci nome utente:\n '))))

  #profilo_utente.append (str(input('inserisci nome utente: ')))
  #profilo_utente.append (str(input('inserisci password: ')))
  #print(profilo_utente)
  #r.sadd('Utente1',profilo_utente)

#registrazione()
def Combinazioni_lettere():
  for i in range(1,10): #grandezza griglia
    
