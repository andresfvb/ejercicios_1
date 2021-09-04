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

# punto 3 ---------------------------------------------------------------------

inv1 = int(input('Dinero del inversor 1: $'))
inv2 = int(input('Dinero del inversor 2: $'))
inv3 = int(input('Dinero del inversor 3: $'))
suma = inv1+inv2+inv3
print("fLos inversores depositaron el dinero dando como total: ${suma}")
print("El dinero quedo suministrado de la siguiente manera")
print(f"Inversor 1: ${inv1} dando como porcentaje {(inv1/suma)*100}%")
print(f"Inversor 1: ${inv1} dando como porcentaje {(inv2/suma)*100}%")
print(f"Inversor 1: ${inv1} dando como porcentaje {(inv3/suma)*100}%")

# punto 4 ---------------------------------------------------------------------

base = int(input('Digite el salario base del empleado: $'))
interes = (base*0.015)

print(f"El valor a descontantar del 1.5% es de ${interes}")
print(f"El valor a pagar es de ${base-interes}")

# punto 5 ---------------------------------------------------------------------

base = int(input('Digite el salario base del empleado: $'))
dp = base*0.01
ss = base*0.04
sf = base*0.005
ca = base*0.05

print(f"Salario del empleado: ${base}")
print(f"Descuento de politica publica ${dp}")
print(f"Descuento de seguro social ${ss}")
print(f"Descuento de seguro forzoso ${sf}")
print(f"Descuento de caja de ahorro ${ca}")
print(f"Valor a pagar: ${base-(dp+ss+sf+ca)}")

# punto 6 ---------------------------------------------------------------------

npa = int(input('Digite la cantidad de palabras que llevara su clasificado: '))
ncm = int(input('Digite los centimetros de su clasificado: '))
nco = int(input('Digite cuantos colores desea usar: '))
pa = 20000*npa
cm = 15000*ncm
co = 25000*nco
cobro = pa+cm+co
print(f"El valor de su clasificado es de ${cobro}")
