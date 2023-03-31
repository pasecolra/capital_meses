#input

capital=int(input("ingrese la capital: "))

int=0
mes=0
capital2= capital + capital

while capital < capital2:
    int= capital*0.05
    capital= capital + int
    mes= mes + 1
print("los meses donde la capital se duplica es: " ,mes, "meses")