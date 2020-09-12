#Script made by Xavi Fortes
# GitHub -> https://github.com/XaviFortes/

import math
import os

c = 299792458

ms = 0

def lorentz(x, y):
    return x*math.sqrt(1 - (y/3.6)**2/ c**2)

def ms(num2):
    return num2/3.6



def percentage(owo):
    return (owo/c)*100

def englishcalc():
    while True:

        choice = input("Enter choice(0): ")

        if choice in ('0', '10001', 'admin'):
            num1 = float(input("Enter original time on V=0 perspective: "))
            num2 = float(input("Enter the speed km/h: "))

            if choice == '0':
                nig = num2
                print("The Result is", lorentz(num1, num2), "seconds")
                print("Speed is", ms(nig), "meters per second")
                mss = ms(nig)
                percent = round(percentage(mss), 2)
                print("You were at", percent, "% of the speed of light")
                print("")
                exit(0)

            elif choice == 'admin':
                print("Veo que eres el admin")
                print("Speed is", ms(num2), "meters per second")
                mss = ms(num2)
                percent = int(percentage(mss))
                print("You were at", percent, "% of the speed of light")
                print("")

            elif choice == '10001':
                print("Woah you may decrypted the code or put a rand number. Congrats!!!")
            break
        else:
            print("It seems that this option is not available yet.")

def languagesel():
    print('Select your Language')
    print('')
    print("0. [ENG] English ")


    while True:
        langsel = input("Enter Language (0):")

        if langsel in ('0'):
            print("Changing Language... ")

            if langsel == '0':
                print("Configurating for English")
                print("Get the Time Dilation (sec) on V=X perspective")
                print("")
                englishcalc()

            break
        else:
            print("It seems that this option is not available yet.")




# Res 999.9999999995707
os.system('cls')
#print('Select Language.')
print("")

languagesel()

#print("0. [ENG] Get the Dilated Time (sec) on V=0 perspective")
#print("1. [ESP] Obtén el tiempo dilatado en segundos, desde la perspectiva del observador siendo v=0")
#print("2. [RUS] Получите увеличенное время в секундах с точки зрения наблюдателя, где v = 0")
#print("3. [FR] Obtenir le temps dilaté en secondes, du point de vue de l'observateur où v = 0")
#print("4. [GER] Ermitteln Sie die erweiterte Zeit in Sekunden aus der Sicht des Beobachters, wobei v = 0 ist")
print("")
exit(0)