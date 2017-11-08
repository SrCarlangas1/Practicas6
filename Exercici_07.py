print "Dime cuantas palabras tiene la primera lista"
ca=input()
lista=[]
for b in range(1,ca+1):
    print "Dime la palabra" , b
    ui=raw_input()
    lista.append(ui)
print "La primera lista es" , lista

print "Dime cuantas palabras tiene la segunda lista"
ca=input()
lista2=[]
for b in range(1,ca+1):
    print "Dime la palabra" , b
    ui=raw_input()
    lista2.append(ui)
print "La segunda lista es" , lista2

comun = []
for b in lista:
    if b in lista2:
                comun.append(b)
print "Palabras que aparecen en las dos listas:", comun
solPrimera = []
for b in lista:
    if b not in lista2:
         solPrimera.append(b)
print "Palabras que solo aparecen en la primera lista:", solPrimera

solSegunda = []
for i in lista2:
    if i not in lista:
        solSegunda.append(b)
print "Palabras que solo aparecen en la segunda lista:", solSegunda
tod = comun + solPrimera + solSegunda
print "Todas las palabras:", tod


