print "Dime cuantas palabras tiene la lista"
prime=int(raw_input())
lista=[]
for i in range(1,prime+1):
    print "Dime la palabra" , i
    f=raw_input()
    lista=lista+[f]
print "La lista creada es;" , lista
print "Dime una palabra"
secu=raw_input()
c=0
for a in range(prime):
    if secu in lista:
        lista.remove(secu)
print "La lista es ahora" , lista    
