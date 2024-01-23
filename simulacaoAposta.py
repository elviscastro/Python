import random

numero = random.randint(1, 25)
# numero_de_palpites = 0
for i in range(5):
  # while numero_de_palpites < 5:
  print('Adivinhe um número entre 1 e 25:')
  palpite = input()
  palpite = int(palpite)
