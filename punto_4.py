# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 20:14:10 2022

@author: rordonez
"""

taller_1 = float(input("ingrese la nota del taller 1: "))
taller_2 = float(input("ingrese la nota del taller 2: "))
taller_3 = float(input("ingrese la nota del taller 3: "))
nota_talleres = ((taller_1 + taller_2 + taller_3)) / 3  * 0.5

examen = float(input("ingrese la nota del examen: "))
nota_examen = examen * 0.3

proyecto = float(input("ingrese la nota del proyecto: "))
nota_proyecto = proyecto * 0.2

nota_final = (nota_talleres + nota_examen + nota_proyecto) * 10

print(f'la nota de final del estudiante es: {nota_final}')
