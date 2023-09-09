num = int(input("Enter a number: "))
fact = 1

for a in range (num, 1, -1):
  fact *= a

print("Factorial is ",fact)