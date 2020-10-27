import csv
import array
import statistics
       
archivo = open("insurance.csv")

for linea in csv.DictReader(archivo):
    print (linea)
    break
edad=int("age")
a= linea[edad]
mediana= statistics.median(a)
