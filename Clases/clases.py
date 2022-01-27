# Escribir una clase en python llamada círculo que contenga un radio,
# con un método que devuelva el área y otro que devuelva el perímetro
# del círculo. Si se instancia la clase con radio <= 0 mostrar
# una excepción indicando un error amigable al usuario e impidiendo
# la instanciación.
# Si printeamos el objeto creado debe mostrarse una representación amigable.
# El objeto debe tener su atributo radio modificable, si se le intenta setear
# un valor <= 0 mostrar un error y no permitir modificación.
# Permitir la multiplicación del circulo: Circulo * n debe devolver un nuevo
# objeto con el radio multiplicado por n.
# No permitir la multiplicación por números <= 0

import os


# Cálculos matemáticos

class Circulo:
    
    PI = 3.14159

    def __init__(self, radio):
        self.radio = radio
            
    def area(self):
        print(f"""
El area del círculo con radio {self.radio} es:
{(Circulo.PI * (self.radio**2)):.2f}
""")

    def perimetro(self):
        print(f"""
El perímetro del círculo con radio {self.radio} es:
{(2 * Circulo.PI * self.radio):.2f}
""")


# Interfaz de usuario y lógica del programa

while True:
    try:
        os.system("clear")
        radio = int(input("Introduzca el radio del círculo: "))
        if radio <= 0:
            os.system("clear")
            print("""

###########################################
El radio no puede ser igual o menor a cero.
Se ha cerrado el programa.
###########################################

""")
            break

        else:
            c1 = Circulo(radio)
            c1.area()
            c1.perimetro()
                
            multiplicacion = input("""
Si desea multiplicar el radio y obtener un nuevo resultado
introduzca la letra 'S'. De lo contrario, presione la tecla 'Enter': """)
            
            if multiplicacion.lower() == "s":
                radio2 = int(input("\nMultiplicar el radio por: "))
                        
                if radio2 <= 0:
                    os.system("clear")
                    print("""

###########################################
El radio no puede ser igual o menor a cero.
Se ha cerrado el programa.
###########################################

""")
                    break

                else:
                    c2 = Circulo(radio * radio2)
                    c2.area()
                    c2.perimetro()
                    break

            else:
                print("""
##########################
Se ha cerrado el programa.
##########################
""")
                break

    except ValueError:
        os.system("clear")
        print("""

###########################################
El radio no puede contener letras.
Se ha cerrado el programa.
###########################################

""")
        break
