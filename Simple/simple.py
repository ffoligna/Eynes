# Hacer una función que genere una lista de diccionarios que contengan
# id y edad, donde edad sea un número aleatorio entre 1 y 100
# y la longitud de la lista sea de 10 elementos. retornar la lista.
# Hacer otra función que reciba lo generado en la primer función
# y ordenarlo de mayor a menor. 
# Printear el id de la persona más joven y más vieja.
# Devolver la lista ordenada.

from random import randint

def lista_diccionarios():
    nombres = [
        "Isidora",
        "Juan",
        "Ana",
        "Federico",
        "José",
        "Julia",
        "Felipe",
        "Soledad",
        "Tania",
        "Pablo"]
    lista = [] 
    for i in range(10):
        lista.append({"Id" : nombres[i] , "Edad" : randint(1, 100)})
    return lista

def ordenar_lista():
    lista = lista_diccionarios()
    mayor_a_menor = sorted(lista, key=lambda a:a["Edad"], reverse=True)
    orden_alfabetico = sorted(lista, key=lambda a:a["Id"])
    menor = mayor_a_menor[9]
    mayor = mayor_a_menor[0]
    
    print(f"""
La persona más joven es: {menor["Id"]}
La persona más vieja es: {mayor["Id"]}

La lista ordenada alfabeticamente:

{orden_alfabetico}
""")

ordenar_lista()
