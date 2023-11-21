#Crea un script que genere la secuencia de Fibonacci y retorna el número que está en una posición dada
def fibonacci(posicion):
    if posicion <= 0:
        return []
    elif posicion == 1:
        return [0]
    elif posicion == 2:
        return [0, 1]
    else:
        secuencia = [0, 1]
        while len(secuencia) < posicion:
            #Suma el último y el penúltimo numero de la secuencia para obtener el siguiente número
            next_num = secuencia[-1] + secuencia[-2]
            secuencia.append(next_num)
        return secuencia
