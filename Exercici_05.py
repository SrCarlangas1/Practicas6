print "Dime cuantas palabras tiene la lista"
prime=int(raw_input())
lista=[]
for i in range(1,prime+1):
    print "Dime la palabra" , i
    f=raw_input()
    lista=lista+[f]
print "La lista creada es;" , lista
print "Dime cuantas pelabras tiene la lista de palabras para eliminar"
secu=int(raw_input())
lista2=[]
for o in range(1,secu+1):
    print "Dime la palabra" , o
    b=raw_input()
    lista2=lista2+[b]
print "La lista creada es;" , lista2
for p in range(1,secu+1):
    lista.remove(b)
print "La lista es ahora" , lista    
