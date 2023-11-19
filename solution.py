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
  # Initialize the error
  error = 1
  # Initialize the iteration counter
  n = 0
  # Loop until the error is less than the tolerance
  while n != iterasi:
    # rumus newton Raphson
    x1 = x0 - f(x0)/derivativeF(x0)
    #membuat bilangan desimal menjadi 4 digit belakang
    x1 = round(x1, 4)
    # Update the previous approximation
    x0 = x1
    # Increment the iteration counter
    n += 1
    # Print the iteration details
    print(
        f"Iteration {n}: x = {x1}, f(x) = {f(x1)}, f'(x) = {derivativeF(x0)} ."
        )
  # Return the final approximationr
  return x1

# Deklarasi nilai awal
print("Masukan nilai awal dari x : ");
x0 = int(input());
# Deklarasi nilai batas iterasi
print("Masukan max jumlah iterasi : ");
iterasi = int(input());
# Call the Newton Raphson method
result = newtonRaphson(x0, iterasi)
# Print the final result
print(f"hasil iterasi sebanyak {iterasi} dari perhitungan f(x) = sin(x) - x = {result}")