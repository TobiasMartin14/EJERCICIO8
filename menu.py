from conjunto import Conjunto


class Menu:
    __opcion = 0
    def __init__ (self):
        self.__opcion = 0
    def opciones(self, conjunto1, conjunto2):
        indice = True
        while indice:
            print ("Opcion 1: A + B")
            print ("Opcion 2: A - B")
            print ("Opcion 3: A = B")
            print ("Opcion 4: Salir")
            self.__opcion = int(input("Seleccione una opcion: "))
            while self.__opcion != 0:
                print("A: {}".format(conjunto1))
                print("B: {}".format(conjunto2))
            if (self.__opcion == 1):
                print("A+B= {}".format(conjunto1 + conjunto2))
            elif (self.__opcion == 2):
                print("A-B = {}".format(conjunto1 - conjunto2))
            elif (self.__opcion == 3):
                print("A=B : {}".format(conjunto1 == conjunto2))
            elif (self.__opcion == 4):
                indice = False
            else:
                print("La opcion ingresada no es valida.")