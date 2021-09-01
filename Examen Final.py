from math import pi
import os
def Menu():
    """Funcion que Muestra el Menu"""
    print("""➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
♛ Calcular Areas De Figuras Geometricas♛
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
Menu
1) Triangulo 🔺
2) Cuadrado ◼
3) Rectangulo ▅
4) Rombo 🔷
5) Romboide 
6) Trapecio
7) Circulo 🔴
8) Semicirculo
9) Corona Circular ⭕
10) Elipse 
11) Pentagono
12) Hexagono
13) Heptagono
14) Salir 🚪""")


def Cal_areas():
    """Funcion para calcular areas de figulas geometricas"""
    
    while True:
        Menu()
        A = int(input("seleccione su opcion\n"))

        if A == 1:
            base = float(input("Introduzca la base de su triangulo: "))
            altura = float(input("Introduzca la altura de su triangulo: "))
            area_triangulo = (base * altura)/2
            os.system('cls')
            print("El area de su triangulo es: {}".format(area_triangulo))

        if A == 2:
            lado = float(input("Introduzca el lado de su cuatrado: "))
            area_cuadrado = (lado*lado)
            os.system('cls')
            print("El area de su cuadrado es: {}".format(area_cuadrado))
            
        if A == 3:
            base = float(input("Introduzca la base de su rectangulo: "))
            altura = float(input("Introduzca la altura de su rectangulo: "))
            area_rectangulo = (base*altura)
            os.system('cls')
            print("El area de su rectangulo es: {}".format(area_rectangulo))
            
        if A == 4:
            diag_menor = float(input("Introduzca la diagonal menor de su rombo: "))
            diag_mayor = float(input("Introduzca la diagonal mayor de su rombo: "))
            area_rombo = (diag_menor*diag_mayor)/2
            os.system('cls')
            print("El area de su rombo es: {}".format(area_rombo))
            
        if A == 5:
            base = float(input("Introduzca la base de su romboide: "))
            altura = float(input("Introduzca la altura de su romboide: "))
            area_romboide = (base*altura)
            os.system('cls')
            print("El area de su romboide es: {}".format(area_romboide))
            
        if A == 6:
            base_menor = float(input("Introduzca la base menor de su trapecio: "))
            base_mayor = float(input("Introduzca la base mayor de su trapecio: "))
            altura = float(input("Introduzca la altura de su trapecio: "))
            area_trapecio = (altura*((base_menor+base_mayor)/2) )
            os.system('cls')
            print("El area de su trapecio es: {}".format(area_trapecio)) 

        if A == 7:
            radio = float(input("Introduzca el radio de su circulo: "))
            area_circulo = (pi*radio**2)
            os.system('cls')
            print("El area de su circulo es: {}".format(f"{area_circulo:.2f}"))

        if A == 8:
            radio = float(input("Introduzca el radio de su semicirculo: "))
            area_semicirculo = (pi*radio**2)/2
            os.system('cls')
            print("El area de su semicirculo es: {}".format(round(area_semicirculo,2)))

        if A == 9:
            radio_mayor = float(input("Introduzca el radio mayor de su Corona Circular: "))
            radio_menor = float(input("Introduzca el radio menor de su Corona Circula: "))
            area_CoronaCircular = (pi*(radio_mayor**2 - radio_menor**2))
            os.system('cls')
            print("El area de su Corona Circular es: {}".format(f"{area_CoronaCircular:.2f}"))
            
        if A == 10:
            semieje1 = float(input("Introduzca el primer eje de su elipse: "))
            semieje2 = float(input("Introduzca el segundo eje de su elipse: "))
            area_elipse = (pi*semieje1*semieje2)
            os.system('cls')
            print("El area de su elipse es: {}".format(f"{area_elipse:.2f}"))

        if A == 11:
            longitud = float(input("Introduzca la longitud de su pentagono: "))
            apotema = float(input("Introduzca el apotema de su pentagono: "))
            area_pentagono = (5*longitud*apotema)/2
            os.system('cls')
            print("El area de su pentagono es: {}".format(f"{area_pentagono:.2f}"))

        if A == 12:
            longitud = float(input("Introduzca la longitud de su Hexagono: "))
            apotema = float(input("Introduzca el apotema de su Hexagono: "))
            area_hexagono = (3*longitud*apotema)
            os.system('cls')
            print("El area de su Hexagono es: {}".format(f"{area_hexagono:.2f}"))

        if A == 13:
            longitud = float(input("Introduzca la longitud de su Heptagono: "))
            apotema = float(input("Introduzca el apotema de su Heptagono: "))
            area_heptagono = (7*longitud*apotema)/2
            os.system('cls')
            print("El area de su Heptagono es: {}".format(f"{area_heptagono:.2f}"))


        if A == 14:
            os.system('cls')
            print("Espero que le haiga funcionado correctamente el programa, Pase feliz resto del dia")
            break
Cal_areas()

