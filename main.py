from conjunto import Conjunto
from menu import Menu

def test ():
    conjunto1= Conjunto([1,2,3,4])
    conjunto2= Conjunto([3,6,9])
    M = Menu()
    M.opciones(conjunto1, conjunto2)

if __name__=='__main__':
    test()