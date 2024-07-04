contador_20lts= 0
contador_10lts= 0
contador_6lts= 0
opc = 0
lista= ['Concepcion','Chiguayante','Talcahuano','Hualpen','San pedro']
def menu_app():

    print("1.Registrar pedido")
    print("2.Listar todos los pedidos")
    print("3.Imprimir hoja de ruta")
    print("4.Buscar un pedido por ID")
    print("5.Salir del programa")


menu_app()



def registro_pedido():
        nombre=input("Ingrese el nombre del cliente: ")
        apellido=input("Ingrese el apellido del cliente: ")
        comuna=input("Ingrese la comuna del cliente: ")
        contador_6lts=input("Ingrese cantidad bidones de 6 litros a pedir: ")
        contador_10lts=input("Ingrese cantidad bidones de 10 litros a pedir: ")
        contador_20lts=input("Ingrese cantidad de bidones de 20 litros a pedir: ")
       
        print(f'cliente:', nombre, apellido,"-",'direccion: ',comuna,"-",'disp 6lts:',"-" ,contador_6lts,"dis.10lts",contador_10lts,"-", "disp.20lts",contador_20lts)
        print("la cantidad de bidones de 20 litros son: ",contador_20lts)
        print("La cantidad de bidones de 10 litros son: ", contador_10lts)
        print("La cantidad de bidones de 6 litros son: ", contador_6lts)
registro_pedido()
def hoja_ruta():
      print("1.Concepcion")
      print("2.Chiguayante")
      print("3.Talcahuano")
      print("4.Hualpen")
      print("5. San Pedro")
hoja_ruta()
while True:
    if opc in menu_app == "1":
         print(registro_pedido)
    if opc in menu_app == "2":
        continue
    if opc in menu_app == "3":
          print(hoja_ruta)
    if opc in menu_app == "4":
          continue

    
    if opc in menu_app == "5":
            break

      
