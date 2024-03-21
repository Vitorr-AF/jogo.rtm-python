import random
import time

def ppt(tempo, limit):
    if tempo < limit:
        return 10 - tempo

def game(limit):
    pontos = 0
    while True:
        rng = random.randint(1, 9)
        ini = time.time()
        clique = int(input(rng))
        tempo = time.time() - ini
        if tempo > limit or clique != rng :
           print(f' {pontos :.2f} pontos')
           break
        else:
            pontos += ppt(tempo, limit)

while True:
    limit = int(input("Escolha o limite de tempo: "))
    if limit > 0:
        game(limit)