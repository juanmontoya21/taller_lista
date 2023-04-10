usuarios={}

centinela = ""


while centinela != "si":
  nombre_ususario=input("ingrese su nombre: ")
  telefono=input("ingrese su numero telefonico: ")
  usuarios[nombre_ususario]=telefono
  centinela = input("desea salir si o no?: ")

print(usuarios.keys())
print(nombre_ususario)

nombre_ususario=input("ingrese su la clave: ")
if nombre_ususario  == usuarios.keys():
  print(usuarios[telefono])
else:
  print("la clave es incorrecta")




