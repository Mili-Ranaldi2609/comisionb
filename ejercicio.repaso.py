#En este ejercicio creamos una lista de compra, 
#donde luego el usuario con esa misma lista ira a comprar al supermercado, 
#que segun las opciones que marque se haran ciertas acciones
#Se declaran las variables

product_list=[]
total_price=0
product_price=0
dsicount=0.10
w=True
position=0

print("Vamos a pedirle que ingrese los productos de su compra")
while w==True:
    #Aca se van a ir guardando los productos en la lista de compras
    option=input("Para agregar un producto ingrese: (a), para terminar la lista ingrese (b): ").lower()
    if option=="a":
        product=input("Producto: ")
        product_list.append(product)
    elif option=="b":
        print("Lista terminada")
        w=False
        break
    elif ((option!="a")or(option!="b") ):
        print("La opcion ingresada es incorrecta. Vuelva a intentar")
    
#Una vez en el supermercado la persona ira viendo los elementos de la lista y verificara si los consiguio o no.
#Verificara el precio de cada elemento.
for i in product_list:
    
    find_product=int(input(f"¿Conseguiste el producto, {i}  en el supermercado?(1)SI---(2)NO: "))
    if(find_product!=1 and find_product!=2):
        while (find_product!=1 or find_product!=2):
            find_product=input("la opcion ingresada no es valida, ingrese la opcion nevamente: ")
    elif find_product==1:
        product_price=float(input("Ingresar el precio del producto y si estaba con descuento el precio con descuento: "))
        total_price+=product_price 
    elif find_product==2:
        #Si no encontro el producto lo puede cambiar por otro que no puso en la lista o puede no cambiarlo
        replace_product=int(input("¿Desea reemplazar el producto?(1)SI---(2)NO: "))
        if replace_product==1:
            product_list[position]=(input("Ingrese el nuevo producto: "))
            product_price=float(input("¿Cual seria el precio?: "))
            total_price+=product_price
        elif replace_product==2:
            continue
    else:
        print("Ha ingresado mal el precio del producto")
    position+=1   
#Si el usuario pago en efectivo se le aplica un 10% de descuento sino paga lo mismo del total
pay=int(input("Seleccione el metodo de pago--(1)Efectivo--(2)Tarjeta: "))
if (pay!=1 and pay!=2):
    while (pay!=2 or pay!=1):
        pay=input("La opcion ingresada no es valida. Seleccione el metodo de pago--(1)Efectivo--(2)Tarjeta: ")
elif pay==1:
    total_price-=(total_price*0.10)
elif pay==2:
    total_price==total_price
print("El total a pagar es: ", total_price)