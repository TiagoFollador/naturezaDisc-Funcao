import math
keepAsking = True
x = 0

def f():
  global x
  x = x**2 + 7
  return x

def g():
  global x
  x = x * 7
  return x

x = int(input(f"sabendo que a funcao f(x) = X^2 + 7 e a g(x) = 7X, escolha um valor pra X:\n>>>"))

Operator = int(input("indique qual operacao voce deseja fazer: \n[1] f(x) [2] g(x) \n[3] (g ° f)(x) [4] (g ° g)(x) \n[5] (f ° f)(x) [6] (f ° g)(x) \n>>>"))

if Operator == 1:
  f()
  print(x)
elif Operator == 2:
  g()
  print(x)
elif Operator == 3:
  g()
  f()
  print(x)
elif Operator == 4:
  g()
  g()
  print(x)
elif Operator == 5:
  f()
  f()
  print(x)
elif Operator == 6:
  f()
  g()
  print(x)