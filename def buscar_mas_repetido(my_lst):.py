
def buscar_mas_repetido(my_lst):
    """
    Buscar el número que se repite más veces en la lista enlazada o lista simple my_lst.
    
    param my_lst: Lista de números o Nodo inicial de la lista enlazada simple
    type my_lst: list
    return: número que se repite más veces en la lista my_lst
    """
    
    ocurrencias = {}
    
    
    for num in my_lst:
        if num in ocurrencias:
            ocurrencias[num] += 1
        else:
            ocurrencias[num] = 1
    
    
    max_valor = None
    max_ocurrencias = 0
    for num, count in ocurrencias.items():
        if count > max_ocurrencias:
            max_ocurrencias = count
            max_valor = num
    
    return max_valor

lista = [20, 14, 6, 28, 10, 14, 62, 10, 14]

print(buscar_mas_repetido(lista)) 
