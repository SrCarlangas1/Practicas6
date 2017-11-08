print "Dime cuantas palabras tiene la lista"
ca=input()
lista=[]
for a in range(1,ca+1):
    print "Dime la palabra" , a
    ui=raw_input()
    lista.append(ui)
print "La lista creada es" , lista
diferente=[]
for b in lista:
    diferente=[b]+diferente
print"La lista inversa es" , diferente

