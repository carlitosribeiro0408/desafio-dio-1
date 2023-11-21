#Desafio de Código DIO
#Calculador de Nivel de Heroi
#
#Uso: py scripy.py HEROI XP
#
import sys


nomeHeroi = sys.argv[1]
xp = int(sys.argv[2])




def ranque(num):
    switch = {
    1:'Ferro',
    2:'Bronze',
    3:'Prata',
    4:'Ouro',
    5:'Platina',
    6:'Ascendente',
    7:'Imortal',
    8:'Radiante'
    }
    print("está no nivel de", switch.get(num))

def callHero():
    print("O heroi", nomeHeroi, end=' ')

if xp <= 1000:
    callHero()
    ranque(1)
elif xp > 10^3 and xp <= 2000:
    callHero()
    ranque(2)
elif xp > 2*10**3 and xp <= 5*10**3:
    callHero()
    ranque(3)
elif xp > 5*10**3 and xp <= 7*10**3:
    callHero()
    ranque(4)
elif xp > 7*10**3 and xp <= 8*10**3:
    callHero()
    ranque(5)
elif xp > 8*10**3 and xp <= 9*10**3:
    callHero()
    ranque(6)
elif xp > 9*10**3 and xp <= 10**4:
    callHero()
    ranque(7)
elif xp >= 10**4:
    callHero()
    ranque(8)
