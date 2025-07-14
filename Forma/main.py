from os import system
system("CLS")

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1], 
              'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7], 
              'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0], 
                 } 



productos = {'8475HD':
              ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],                       
              '2175HD': ['Acer', 14, '4GB', 'SSD', '512GB', 'Intel Core i7', 'Nvidia GTX1050'], 
              'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i5', 'Nvidia RTX2080Ti'], 
                'fgdxFHD': ['HP', 15.6, '12GB', 'DD', '1T', 'Intel Core i5', 'integrada'], 
                'GF75HD': ['Asus', 15.6, '12GB', 'DD', '1T', 'Intel Core i3', 'Nvidia GTX1050'],                      
                '123FHD': ['Acer', 14, '6GB', 'DD', '1T', 'AMD Ryzen 7', 'integrada'], 
                '342FHD': ['Acer', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 5', 'Nvidia GTX1050'], 
                'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 5', 'Nvidia GTX1050'],
                           }



def stock_Marca(marca):
        try:
            total = 0
            for modelo in productos.items():
                if productos[productos][0].lower() == marca.lower():
                    total += stock([modelo][1])
                print(f"El stock es: {total}")
        except TypeError:
            print("Debe de escribir con variables")
        else:
            print("Debe ser con caracter ")

def Busquede_precio(minimo, maximo):
    
    encontrados = []

    for modelo in stock.items():
        precio = stock[modelo][0]
        if minimo <= precio <= maximo:
            encontrados.append(modelo)
    if len(encontrados) == 0:
        print("Los notebooks entre los precios consultados son: ", encontrados)
    else:
        print("No ahi notebooks en este rango de precio")


def	Listado_productos():
    if not productos:
        for modelo in productos:
            marca = productos[modelo][1]
            procesador = productos[modelo][1]
            print(marca, "-", modelo , "-", procesador)

    


def menu():
    while True:
        print("---Pybooks---")
        print("1.Stock Marca")
        print("2.Busqueda por Precio")
        print("3.Listado de stock")
        print("4.Salir")
        opc = int(input("Ingrese una opc:  "))


        if opc == 1:
            marca = input("Ingresa una consulta: ")
            stock_Marca(marca)
        elif opc == 2:
            try:
                minimo= int(input("Ingrese un valor minimo: "))
                maximo= int(input("Ingresa un valor maximo: "))
            except:
                print("Debe de ingresar numeros enteros")
            Busquede_precio(minimo, maximo)
        elif opc == 3:
            Listado_productos()
        elif opc == 4:
            break

menu()



