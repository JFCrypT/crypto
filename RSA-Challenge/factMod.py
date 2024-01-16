# https://en.wikipedia.org/wiki/RSA_numbers
# https://en.wikipedia.org/wiki/List_of_prime_numbers
# https://members.loria.fr/pzimmermann/records/rsa.html
# https://www.rapidtables.com/convert/number/hex-to-decimal.html

# Carta de Fermat a Mersenne: 100895598169 = 898423 * 112303

# RSA-20 (propio): 37858103304928612721 = 4868747809 * 7775737169

# RSA-59: 71641520761751435455133616475667090434063332228247871795429
# RSA-79: 7293469445285646172092483905177589838606665884410340391954917800303813280275279
# RSA-99: 256724393281137036243618548169692747168133997830674574560564321074494892576105743931776484232708881
# RSA-119: 55519750778717908277109380212290093527311630068956900635648324635249028602517209502369255464843035183207399415841257091

# RSA-100: 1522605027922533360535618378132637429718068114961380688657908494580122963258952897654000350692006139
# RSA-260: 22112825529529666435281085255026230927612089502470015394413748319128822941402001986512729726569746599085900330031400051170742204560859276357953757185954298838958709229238491006703034124620545784566413664540684214361293017694020846391065875914794251435144458199
# RSA-2048: 25195908475657893494027183240048398571429282126204032027777137836043662020707595556264018525880784406918290641249515082189298559149176184502808489120072844992687392807287776735971418347270261896375014971824691165077613379859095700097330459748808428401797429100642458691817195118746121515172654632282216869987549182422433637259085141865462043576798423387184774447920739934236584823824281198163815010674810451660377306056201619676256133844143603833904414952634432190114657544454178424020924616515723350778707749817125772467962926386356373289912154831438167899885040445364023527381951378636564391212010397122822120720357

import math
import random
import time

def factor(mod, longM):
    choice = int(input("Ingrese modo de operación (1. Secuencial | 2. Aleatorio | 3. Fermat): "))
    while choice < 1 or choice > 3:
        choice = int(input("¡ERROR! Ingrese un modo de operación válido (1. Secuencial | 2. Aleatorio | 3. Fermat): "))
    
    if choice == 1:
        inicRango = pow(10, ((longM // 2) - 1))
        longInic = len(str(inicRango))
        print("Inicio del rango de búsqueda: {}".format(inicRango))
        print("Cantidad de dígitos del primer número del rango de búsqueda: {}\n".format(longInic))
        
        finRango = pow(10, ((longM // 2) + 1))
        longFin = len(str(finRango))
        print("Fin del rango de búsqueda: {}".format(finRango))
        print("Cantidad de dígitos del primer número del rango de búsqueda: {}\n".format(longFin))
        
        cantNros = finRango - inicRango
        print("Cantidad de números a evaluar: {}\n".format(cantNros))

        seg = 3
        for i in range(1, 4):
            msj = "El test comienza en {} segundo{}".format(seg, "s" if seg != 1 else "\n")
            print(msj)
            time.sleep(1)
            seg -= 1
        
        for num in range(inicRango, finRango):
            print("Evaluando: {}".format(num))
            if mod % num == 0:
                intP = num
                intQ = mod // intP
                print("\n¡FACTOR PRIMO ENCONTRADO!")
                print("\nn = {}".format(mod))
                print("\np = {}\n".format(intP))
                print("q = {}\n".format(intQ))
                break
    
    elif choice == 2:
        inicRango = pow(10, ((longM // 2) - 1))
        longInic = len(str(inicRango))
        print("Inicio del rango de búsqueda: {}".format(inicRango))
        print("Cantidad de dígitos del primer número del rango de búsqueda: {}\n".format(longInic))
        
        finRango = pow(10, ((longM // 2) + 1))
        longFin = len(str(finRango))
        print("Fin del rango de búsqueda: {}".format(finRango))
        print("Cantidad de dígitos del primer número del rango de búsqueda: {}\n".format(longFin))
        
        cantNros = finRango - inicRango
        print("Cantidad de números a evaluar: {}\n".format(cantNros))

        seg = 3
        for i in range(1, 4):
            msj = "El test comienza en {} segundo{}".format(seg, "s" if seg != 1 else "\n")
            print(msj)
            time.sleep(1)
            seg -= 1
        
        found = False
        while not found:
            randP = random.randint(inicRango, finRango)
            print("Evaluando: {}".format(randP))
            if mod % randP == 0:
                found = True
                intP = randP
                intQ = mod // randP
                print("\n¡FACTOR PRIMO ENCONTRADO!")
                print("\nn = {}".format(mod))
                print("\np = {}\n".format(intP))
                print("q = {}\n".format(intQ))
    
    elif choice == 3:
        raiz = math.sqrt(mod)
        intRaiz = math.isqrt(mod) + 1
        print("Raíz cuadrada del módulo: {}".format(raiz))
        print("Aproximación al próximo entero: {}\n".format(intRaiz))

        seg = 3
        for i in range(1, 4):
            msj = "El test comienza en {} segundo{}".format(seg, "s" if seg != 1 else "\n")
            print(msj)
            time.sleep(1)
            seg -= 1

        found = False
        while not found:
            cuad = pow(intRaiz, 2) - mod
            print("Evaluando: {}² - {} = {}".format(intRaiz, mod, cuad))
            
            raizCuad = math.isqrt(cuad)
            if cuad == pow(raizCuad, 2):
                primo1 = intRaiz + raizCuad
                primo2 = intRaiz - raizCuad
                print("Cuadrado encontrado")
                print("Ecuación resultante:")
                print("{}² - {} = {}".format(intRaiz, mod, cuad))
                print("{}² - {} = {}²".format(intRaiz, mod, raizCuad))
                print("{} = {}² - {}²".format(mod, intRaiz, raizCuad))
                print("{} = ({} + {}) · ({} - {})".format(mod, intRaiz, raizCuad, intRaiz, raizCuad))
                print("{} = {} · {}".format(mod, primo1, primo2))
            
                esPrimo = True
                for i in range(2, primo1):
                    if primo1 % 1 == 0:
                        esPrimo = False
                        intRaiz += 1
                        break
            
                found = True
                
                if found == True and primo1 * primo2  == mod:
                    print("\n¡FACTOR PRIMO ENCONTRADO!")
                    print("\nn = {}".format(mod))
                    print("\np = {}\n".format(primo1))
                    print("q = {}\n".format(primo2))
                
            else:
                intRaiz += 1
                
def main():
    intN = int(input("Ingrese el módulo a factorizar (n) (DEC): "))
    print("Módulo (n) (DEC):", intN)
    longMod = len(str(intN))
    print("Cantidad de dígitos del módulo (n): {}\n".format(longMod))
    
    factor(intN, longMod)

main()