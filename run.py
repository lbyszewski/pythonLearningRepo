# import nazwa modułu - cały moduł
# from nazwa modułu import funkcja - wybrana funkcja z modułu


import foo
from klasy import Calculator
from foo import fibb
from  foo import silnia
from  foo import ropietoscPrzedzialu
from klasy import Pegasus


n = int(input("podaj n: "))
print("Wartość ciągu fibbonacziego to: ", foo.fibb(n))
print("Silnia wynosi: ",foo.silnia(n))

begin = int(input("podaj początek: "))
end = int(input("podaj koniec: "))
devid = int(input("podaj dzielnik: "))
print(foo.ropietoscPrzedzialu(begin,end,devid))

a = int(input("podaj a: "))
b = int(input("podaj b: "))

calc = Calculator()
print("dodawanie: ", calc.dodaj(a,b))
print("odejmowanie ", calc.odejmij(a,b))

pega = Pegasus()
print("Wynik pegamega: " , pega.rastaFaja(a,b))