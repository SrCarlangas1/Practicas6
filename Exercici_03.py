print "Dime cuantas palabras tiene la lista"
prime=int(raw_input())
lista=[]
for i in range(1,prime+1):
    print "Dime la palabra" , i
    f=raw_input()
    lista=lista+[f]
print "La lista creada es;" , lista
print "Sustuir la palabra"
secu=raw_input()
print "por la palabra"
ter=raw_input()
while secu in lista:
    pepe=lista.index(secu)
    lista.remove(secu)
    lista.insert(pepe,ter)
print "La lista es ahora" , lista
