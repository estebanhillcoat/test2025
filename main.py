productos = []


with open("base.txt", "r") as base:
    productos = base.read().splitlines()

def actualizar_base():
    with open("base.txt", "w") as base:
        for producto in productos:
            base.write(producto + "\n")


while True:
    print("ingrese la opcion deseada:")

    print("1. Agregar producto")
    print("2. Ver productos")
    print("3. Salir")
    print("4. Eliminar producto")
    print("5. Buscar producto")

    opcion = input("Opción: ")

    match opcion:
        case "1":
            producto = (input("Ingrese el nombre del producto: ")).strip()
            productos.append(producto)
            print(f"Producto '{producto}' agregado.")
            actualizar_base()
        
        case "2":
            print("Productos:", productos)

        case "5":
            break

        case "4":
            producto = input("Ingrese el nombre del producto a eliminar: ")
            if producto in productos:
                productos.remove(producto)
                print(f"Producto '{producto}' eliminado.")
                actualizar_base()
            else:
                print(f"Producto '{producto}' no encontrado.")
        case "3":
            producto = input("Ingrese el nombre del producto a buscar: ")
            if producto in productos:
                print(f"Producto '{producto}' encontrado.")
            else:
                print(f"Producto '{producto}' no encontrado.")  



