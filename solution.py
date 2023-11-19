# Import math
import math

# method untuk generator hasil dari f(x) = sin(x) - x
def f(x):
  return math.sin(x) - x;

# method untuk generator hasil dari f'(x) = cos(x) - 1
def derivativeF(x):
  return math.cos(x) - 1;

# Method untuk menghitung iterasi dengan methode newton raphson
def newtonRaphson(x0, iterasi):
  # Membuat index perhitungan
  n = 0
  # Melakukan iterasi hingga unequal
  while n != iterasi:
    # deklarasi rumus newton Raphson
    x1 = x0 - f(x0)/derivativeF(x0)
    #membuat bilangan desimal menjadi 4 digit belakang
    x1 = round(x1, 4)
    # update nilai x0 dari hasil x1
    x0 = x1
    # Melakukan increment
    n += 1
    # console hasil perhitungan
    print(
        f"Iteration {n}: x = {x1}, f(x) = {f(x1)}, f'(x) = {derivativeF(x0)} ."
        )
  # Menngembalikan nilai akhir dari iterasi
  return x1

# Deklarasi nilai awal
x0 = 1
# Deklarasi nilai batas iterasi
iterasi = 4
# invoke methode dengan memberikan variabel karena butuh hasil akhir iterasi
result = newtonRaphson(x0, iterasi)
# Console.log()
print(f"hasil iterasi sebanyak {iterasi} dari perhitungan f(x) = sin(x) - x = {result}")
