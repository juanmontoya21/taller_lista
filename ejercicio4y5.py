usuarios={}
centinela = ""

while centinela != "si":
  nombre_usuario=input("ingrese su nombre: ")
  if nombre_usuario not in usuarios:
    telefono=input("ingrese su numero telefonico: ")
    usuarios[nombre_usuario]=telefono
  else:
    print("el nombre esta repetido")
  centinela = input("desea salir si o no?: ")

print(usuarios)

clave_usuario=input("ingrese su clave: ")
for clave in usuarios.keys():
  if clave_usuario == clave:
    print(usuarios[clave_usuario])