numeros_repetidos=1,2,2,3,4,5,6,7,8,9,10,2,2,2,2
numero_usuario=int(input("ingrese un numero: "))

for i in range(len(numeros_repetidos)):
  if numero_usuario == i:
    print(numeros_repetidos.count(numero_usuario))
if numero_usuario not in numeros_repetidos:
  print("el numero no se encuentra")
