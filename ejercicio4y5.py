usuarios={}

centinela = ""


while centinela != "si":
  nombre_usuario=input("ingrese su nombre: ")
  telefono=input("ingrese su numero telefonico: ")
  usuarios[nombre_usuario]=telefono
  centinela = input("desea salir si o no?: ")

print(usuarios)

clave_usuario=input("ingrese su la clave: ")

if clave_usuario == usuarios.keys():
  print(usuarios[nombre_usuario], "hola")
else:
  print("la clave es incorrecta")




