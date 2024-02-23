import json
import csv
import leerdocs

   
#falta identificar el valor del pedido total
def crearpedido():
    listaMenu=leerdocs.CargarDatoscsv("datosmenu.csv")
    ListaPedidos=leerdocs.CargarDatosjson("pedidos.json")
    Entradas=[]
    platosFuertes=[]
    bebidas=[]
    print("----------------------------------------")
    print("----------Lista de Platos Menu ---------")
    print("----------------------------------------") 
    print("seleccione cero(0) para dejar de ordenar")
    print("----------------------------------------")
    for index,plato in enumerate(listaMenu):
        tipo=plato[0]
        nombre=plato[1]
        precio=plato[2]
        estado="Creado"
        pago="No Pago"
        Precio="0"

        print(f"{index+1}-{tipo} - {nombre} - ${precio}")
    try:
        idcliente=input("\nPor favor ingresa el documento del cliente:   ")
        print("\nPor favor escribe el numero del plato que deseas ordenar\n")
        while True:
            opcion=int(input("Opcion:  "))
            if opcion>=0 and opcion<=12:
                if opcion==0:
                    print("...Saliendo...")
                    break
                elif opcion>=1 and opcion<=4:
                    Entradas.append(listaMenu[opcion-1][1])
                elif opcion>=5 and opcion<=8:
                    platosFuertes.append(listaMenu[opcion-1][1])
                elif opcion>=9:
                    bebidas.append(listaMenu[opcion-1][1])
            else:
                print("la opción indicada es incorrecta")

        Pedido={'idcliente':idcliente,
                'entradas':Entradas,   
                'PlatosFuertes':platosFuertes,
                'Bebidas':bebidas,
                'Estado':estado,
                'Pago':pago}
        EntradasPedidas=Pedido['entradas']
        platosFuertesPedidos=Pedido['PlatosFuertes']
        bebidasPedidas=Pedido['Bebidas']
        leerdocs.limpiarTerminal()
        print("\n------------------")
        print("Entradas Ordenadas")
        print("------------------")
        for x in EntradasPedidas:
            print(x)
        print("\n-------------------------")    
        print("Platos Fuertes Ordenadados")
        print("--------------------------")
        for x in platosFuertesPedidos:
            print(x)
        print("\n------------------")
        print("Bebidas Ordenadas")
        print("------------------")
        for x in bebidasPedidas:
            print(x)

        ListaPedidos.append(Pedido)
        leerdocs.guardarcambiosjson(ListaPedidos,"pedidos.json")    
    except Exception:
        print("escribe una opción valida")


#no guarda aún ni se ponene los datos en la variable solicitada, revisar
def modificarpedido():
    listaMenu=leerdocs.CargarDatoscsv("datosmenu.csv")
    ListaPedidos=leerdocs.CargarDatosjson("pedidos.json")
    print("---------------------------------------------")
    print("----Los pedidos que puedes modificar son-----")
    print("---------------------------------------------") 
    for index,pedido in enumerate(ListaPedidos):
        nombrecliente=pedido['idcliente']
        if pedido['Estado'] == "Creado" :
            print(f"{index+1}-{nombrecliente}")
    
    try:
        opcion=int(input("¿Que pedido deseas modificar?:   "))
        while True:
            if opcion>0 and opcion<=len(ListaPedidos):
                print("¿Qué deseas hacer? Elige tu opcion")
                print("1) Si deseas agregar algun producto")
                print("2) Si deseas eliminar algun producto")
                print("0) Si deseas salir")
                opcion2=int(input("Opción:   "))
                if opcion2>=0 and opcion2<=2:
                    if opcion2==0:
                        print("....Saliendo....")
                        break
                    elif opcion2==1:
                        pedidoSeleccionado=ListaPedidos[opcion-1]
                        print("----------------------------------------")
                        print("----------Lista de Platos Menu ---------")
                        print("----------------------------------------") 
                        print("seleccione cero(0) para dejar de ordenar")
                        print("----------------------------------------")
                        for index,plato in enumerate(listaMenu):
                            tipo=plato[0]
                            nombre=plato[1]
                            precio=plato[2]
                            print(f"{index+1}-{tipo} - {nombre} - ${precio}")
                        
                        print("\nPor favor escribe el numero del plato que deseas ordenar\n")
                        Entradaspedidas=list(pedidoSeleccionado['entradas'])
                        platosFuertespedidos=list(pedidoSeleccionado['PlatosFuertes'])
                        bebidaspedidas=list(pedidoSeleccionado['Bebidas'])
                        while True:
                            opcion3=int(input("Opcion:  "))
                            if opcion3>=0 and opcion3<=12:
                                if opcion3==0:
                                    print("...Saliendo...")
                                    break
                                elif opcion3>0 and opcion3<5:
                                    Entradaspedidas.append(listaMenu[opcion3-1][1])
                                elif opcion3>=5 and opcion3<=8:
                                    platosFuertespedidos.append(listaMenu[opcion3-1][1])
                                elif opcion3>=9:
                                    bebidaspedidas.append(listaMenu[opcion3-1][1])            
                            else:
                                print("la opción indicada es incorrecta")

                        leerdocs.limpiarTerminal()

                        print("\n------------------")
                        print("Entradas Ordenadas")
                        print("------------------")
                        for x in Entradaspedidas:
                            print(x)
                        print("\n-------------------------")    
                        print("Platos Fuertes Ordenadados")
                        print("--------------------------")
                        for x in platosFuertespedidos:
                            print(x)
                        print("\n------------------")
                        print("Bebidas Ordenadas")
                        print("------------------")
                        for x in bebidaspedidas:
                            print(x)
                        
                        pedidoSeleccionado['entradas']=Entradaspedidas
                        pedidoSeleccionado['PlatosFuertes']=platosFuertespedidos
                        pedidoSeleccionado['Bebidas']=bebidaspedidas
                        leerdocs.guardarcambiosjson(ListaPedidos,"pedidos.json")
                        break    
                    elif opcion2==2:
                       print("¿Que deseas eliminar?")
                       print("1.) ¿Una entrada?")
                       print("2.) ¿Un Plato Fuerte?")
                       print("3.) ¿Una bebida?") 
                       print("0.) Deseas Salir?")
                       try:
                           opcion4=int(input("Opcion:  "))
                        except ValueError:
                           print("Selecciona un valor numerico")
                        
                        if opcion4<0 and opcion4>3:
                           
                else:
                    print("la opción no se encuentra dentro de las opciones dadas")            
            else:
                print("selecciona una opción valida")
    except ValueError:
        print("No escribiste una opción numerica.")                           
modificarpedido()

def cambiarapreparacion():
    ListaPedidos=leerdocs.CargarDatosjson("pedidos.json")
    print("---------------------------------------------")
    print("----Los pedidos que puedes modificar son-----")
    print("---------------------------------------------") 
    for index,pedido in enumerate(ListaPedidos):
        nombrecliente=pedido['idcliente']
        if pedido['Estado'] == "Creado" :
            print(f"{index+1}-{nombrecliente}")
        
    try:
        opcion=int(input("Por favor inserta el numero de pedido que se encuentra en preparación:    "))
        while True:
            if opcion<0 or opcion>=len(ListaPedidos):
                ListaPedidos[opcion-1]['Estado']="En preparacion"
                leerdocs.guardarcambiosjson(ListaPedidos,"pedidos.json")  
                break
            else:
                print("la opción no hace parte de los datos")  
    except ValueError:
        print("Ingrese una opcion numerica")                   

#Para pagar un pedido, 
# guardar los datos del pago en un archivo csv 
#un archivo con la fehca de pago, valor total e identificador del cliente
def pagarpedido():
    ListaPedidos=leerdocs.CargarDatosjson("pedidos.json")
    print("---------------------------------------------")
    print("----Los pedidos que puedes modificar son-----")
    print("---------------------------------------------") 
    for index,pedido in enumerate(ListaPedidos):
        nombrecliente=pedido['idcliente']
        if pedido['Estado'] == "Creado" or pedido['Estado']=="En preparacion":
            print(f"{index+1}-{nombrecliente}")
        
    try:
        opcion=int(input("Por favor inserta el numero de pedido que deseas pagar:    "))
        fechadepago=input("Por favor escribe la fecha en la que fue pagado el pedido")

        while True:
            if opcion<0 or opcion>=len(ListaPedidos):
                ListaPedidos[opcion-1]['Pago']="Pagado"
                leerdocs.guardarcambiosjson(ListaPedidos,"pedidos.json")  
                break
            else:
                print("la opción no hace parte de los datos")  
    except ValueError:
        print("Ingrese una opcion numerica")    

#Para servir un pedido ok
def servirpedido():
    ListaPedidos=leerdocs.CargarDatosjson("pedidos.json")
    print("---------------------------------------------")
    print("----Los pedidos listos para servir son-------")
    print("---------------------------------------------") 
    for index,pedido in enumerate(ListaPedidos):
        nombrecliente=pedido['idcliente']
        if pedido['Estado'] == "Creado" or pedido['Estado']=="En preparacion":
            if pedido['Pago']=="Pagado":
                print(f"{index+1}-{nombrecliente}")
        
    try:
        opcion=int(input("Por favor inserta el numero de pedido que deseas servir:    "))
        while True:
            if opcion<0 or opcion>=len(ListaPedidos):
                ListaPedidos[opcion-1]['Estado']="Servido"
                leerdocs.guardarcambiosjson(ListaPedidos,"pedidos.json")  
                break
            else:
                print("la opción no hace parte de los datos")  
    except ValueError:
        print("Ingrese una opcion numerica")                   
 
#Para cancelar un pedido ok
def cancelarpedido():
    ListaPedidos=leerdocs.CargarDatosjson("pedidos.json")
    print("---------------------------------------------")
    print("----Los pedidos que puedes cancelar son------")
    print("---------------------------------------------") 
    for index,pedido in enumerate(ListaPedidos):
        nombrecliente=pedido['idcliente']
        if pedido['Estado'] == "Creado":
            if pedido['Pago']=="No pago":
                print(f"{index+1}-{nombrecliente}")
        
    try:
        opcion=int(input("Por favor inserta el numero de pedido que deseas cancelar:    "))
        while True:
            if opcion<0 or opcion>=len(ListaPedidos):
                ListaPedidos[opcion-1]['Estado']="Cancelado"
                leerdocs.guardarcambiosjson(ListaPedidos,"pedidos.json")  
                break
            else:
                print("la opción no hace parte de los datos")  
    except ValueError:
        print("Ingrese una opcion numerica")