# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 19:59:11 2021

@author: Andres Vasquez
"""

# Seccion 1

# punto 1 ---------------------------------------------------------------------

y = ((pow((5+2-5), 2))*5+8/2-30)/2*5-3

print(f"y = ((5+2-5)^2*5+8/2-30)/2*5-3 = {y}")

# punto 2 ---------------------------------------------------------------------

z = 5
n = 3
m = z-n
y = pow((pow(z+2-n, 2)*m+8/2-30)/2*5-3, 5)+15*3-9/3

print(f"y =(((z+2-n)^2*m+8/2-30)/2*5-3)^5+15*3-9/3 = {y}")

# punto 3 ---------------------------------------------------------------------

z = 5
n = (pow(8+2-4, 2)*5+8+7/2-30*5)/2*5-3
m = pow(z, 2)*3+n
y = (pow(pow((pow(z+2-n, 2)*m+8/2-30)/2*5-3, 5)+15*3-9/3, 2)-5/4)

print(y)

# Seccion 2

# punto 1 ---------------------------------------------------------------------

presion = float(input('Digite el valor de la Presion: '))
volumen = float(input('Digite el valor del Volúmen: '))
temperatura = float(input('Digite el valor de la Temperatura: '))
masa = (presion*volumen)/(0.37*(temperatura+460))

print("Haga un algoritmo que calcule la masa de la siguiente fórmula: ")
print("Masa = (presión * volúmen) / (0.37 * (temperatura + 460))")
print(f"masa = ({presion}*{volumen}/(0.37*{temperatura+460})) = {masa}")

# punto 2 ---------------------------------------------------------------------

edad = int(input('Cuantos años tiene?: '))
npul = (200-edad)/10

print(f"La cantidad de pulsaciones que tiene cada 10 segundos es de: {npul}")
