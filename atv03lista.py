"""Ler uma lista com 4 notas, em seguida
o programa deve exibir as notas e a
média."""

#Primeiro jeito
soma = 0
contador = 0
lista_notas= []
for nota in range(4):
    notas =float(input(f"Sua nota {nota +1:}"))
    soma+=notas
    contador+=1
    lista_notas.append(notas)
    
print(soma/contador)

#Segundo jeito
for nota in range(4):
    notas =float(input(f"Sua nota {nota +1}:"))
    lista_notas.append(notas)
print("Sua media e {}".format(sum(lista_notas)/len(lista_notas)))
