# Função que calcula o enésimo número de Fibonacci
def Fibonacci(n):
  if n < 0:
    print("Entrada inválida")
# O primeiro número de Fibonacci é 0
  elif n == 1:
    return 0


# O segundo número de Fibonacci é 1
  elif n == 2:
    return 1
  else:
    return Fibonacci(n - 1) + Fibonacci(n - 2)

if __name__ == "__main__":
  print(Fibonacci(9))
