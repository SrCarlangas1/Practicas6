print "Dime cuantas palabras tiene la primera lista"
ca=input()
lista=[]
for b in range(1,ca+1):
    print "Dime la palabra" , b
    ui=raw_input()
    lista.append(ui)
print "La primera lista es" , lista
print "La lista ordenada es" , sorted(lista)
