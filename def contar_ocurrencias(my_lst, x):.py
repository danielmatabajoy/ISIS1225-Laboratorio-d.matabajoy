def contar_ocurrencias(my_lst, x):
    """
    Contar el numero de ocurrencias de x al interior de my_lst
    param my_lst: array list con los numeros
    type my_lst: dict (representa un array list)
    param x: elemento a contar ocurrencias en la lista
    Return: numero de ocurrencias de x en my_lst
    """
    contador=0
    for i in my_lst:
        if  i == x :
         contador+=1 
    return contador

lista= [20, 14, 6, 28, 10, 14, 62, 10, 14]

x=int(input("ingrese un vslor:" ))
print(contar_ocurrencias(lista,x))