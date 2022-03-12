#Definicion de la funcion que suma 2 numeros enteros
def Suma2Enteros (x,y):
  z = x + y 
  return z

# Estructura del menú y las entradas al programa
while True:
  print ("¿Quieres jugar a sumar dos números?")  
  print ("1 Si")
  print ("2 No")
  opcion = int(input("Introduce la opcion==>"))

  if opcion == 1: 
    x = int(input("Escribe el valor del primer número entero==>"))
    y = int(input("Escribe el valor del segundo número entero==>"))
    z = Suma2Enteros(x,y)
    print (x, " + ", y, " = ", z)

  elif opcion == 2:
    print ("Bye")
    break
  else:
    print("Opción incorrecta")
  
