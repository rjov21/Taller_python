# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 20:27:17 2022

@author: rordonez
"""

redes = int(input('ingrese la cantidad de estudiantes en redes: '))

contabilidad = int(input('ingrese la cantidad de estudiantes en contabilidad: '))

diseño = int(input('ingrese la cantidad de estudiantes en diseño: '))

cantidad_total = redes + contabilidad + diseño
cantidad_redes = (redes * 100) / cantidad_total
cantidad_contabilidad = (contabilidad * 100) / cantidad_total
cantidad_diseño = (diseño * 100) / cantidad_total

print(f'el % de estudiantes de redes es: {cantidad_redes}%')

print(f'el % de estudiantes de contabilidad es: {cantidad_contabilidad}%')

print(f'el % de estudiantes de diseño es: {cantidad_diseño}%')
