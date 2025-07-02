from Funciones import *

while True:
        #try:
            print("""
                ------- Menu principal -------
                1) Registrar producto 
                2) Listar producto con stock
                3) Eliminar producto por codigo 
                4) Salir 
                """)
            Seleccion = int(input("Ingrese una opcion : "))

            match Seleccion:
                case 1:
                    codigo = int(input("Ingrese codigo : "))
                    nombre = input("Ingrese nombre producto : ")
                    stock = int(input("Ingrese Stock : "))
                    precio = int(input("Ingrese precio : "))
                    RegistrarProductos(codigo, nombre, stock, precio)
                case 2:
                    ListarProducto()
                case 3:
                    codigo = input("Ingrese codigo del producto a eliminar : ")
                    EliminarProducto(productos, codigo)
                case 4:
                    break
        #except:
             #print("")
    