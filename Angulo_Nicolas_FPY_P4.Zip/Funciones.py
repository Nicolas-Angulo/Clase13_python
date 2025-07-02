productos=[]

def BuscarProducto(codigo):
    for i in range(len(productos)):
        if productos[i]["codigo"]==codigo:
            return i
        else:
            print("Codigo no encontrado")
    return -1

def RegistrarProductos(codigo, nombre, stock, precio):
    #a) El código no debe estar registrado previamente.
    if BuscarProducto(codigo) == -1:
        #b) El nombre debe tener al menos 3 caracteres alfabéticos
        if len(nombre)>=3:
            #c) El stock debe ser un número entero mayor o igual a 0.
            if int(stock)>=0:
                #d) El precio debe ser un número mayor a 0.
                if int(precio)>0:
                    datos = {
                        "codigo" : codigo,
                        "nombre" : nombre,
                        "stock"  : stock,
                        "precio" : precio 
                    }
                    productos.append(datos)
                else:
                    print("El precio debe ser mayor a 0")
            else:
                print("El stock debe ser numero mayor o igual a 0")
        else:
            print("El nombre debe tener al menos 3 caracteres alfanumericos")
    else:
        print("Producto existente ")
    return False

def ListarProducto():
    if len(productos)>0:
        for i in range(len(productos)):
            if productos[i]["codigo"]>0:
                print(f"{i+1} Codigo = {productos[i]["codigo"]} Nombre = {productos[i]["nombre"]} Stock = {productos[i]["stock"]} Precio = {productos[i]["precio"]}")
            else:
                print("No hay productos disponibles en stock")

def EliminarProducto(productos, codigo):
    for productos in productos:
        if productos["codigo"] == codigo:
            productos.remove(productos)
            print("Producto eliminado")
            return
    else:
        print("Producto no encontrado")

        