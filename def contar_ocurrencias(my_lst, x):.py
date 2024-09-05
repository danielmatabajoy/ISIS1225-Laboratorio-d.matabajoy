def buscar_mas_repetido(my_lst):
    """
    Buscar el numero que se repite mas veces en la lista my_lst
    param my_lst: list con los numeros
    type my_lst: dict (representa una list)
    Return: numero que se repite más veces en la lista my_lst
    """
    numero=0
    contador=0
    for i in my_lst:
        if i > numero:
            contador+=1
        return numero
    return contador

lista= [20, 14, 6, 28, 10, 14, 62, 10, 14]
print(buscar_mas_repetido(lista))

