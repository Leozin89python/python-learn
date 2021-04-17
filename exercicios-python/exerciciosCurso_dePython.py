"""
                                            Curso de Python 3
"""

#=================================================================================
print('python 3')

nome = 'estudante'
idade = 27
altura = 1.95
e_maior = idade > 18
peso = 77
imc = (peso / altura**2)

print(nome, 'tem', idade,'anos de idade e seu IMC é', imc)
print(f'{nome} tem {idade} anos de idade e seu IMC é {imc:.2f}')

#=================================================================================
nome = input('nome')
print(f'nome{nome}')
print('o tipo da variável é' f'{type(nome)}')
#=================================================================================
numero1 = input('numero-1:')
numero2 = input('numero-2:')

total = int(numero1) + int(numero2)
print(total)
#=================================================================================
if False:
    print('verdadeiro')
elif True:
    print('falso')
else:
    print('ilógico')
----------------------------------------------------------------------------------        
cod  = int(1098)
cod2 = int(1098)
 
if cod == cod2:
    print(True)
else:
    print(False)
----------------------------------------------------------------------------------    
cod  = int(1098)
cod2 = int(1098)
 
if cod == cod2 or cod > cod2:
    print(True)
else:
    print(False)
----------------------------------------------------------------------------------    
cod  = input('codigo')
cod2 = input('codigo2')
 
if '123' in cod or '1234' in cod2:
    print('logado com sucesso!')
else:
    print('acesso negado!')
#=================================================================================
usuario = input('digite seu usuario:')
qtd_caracteres = len(usuario)

if qtd_caracteres < 6:
    print('digito minimo de 6 caracteres!')
else:
    print('cadastro realizado com sucesso!')
#=================================================================================
inteiro =  input('valor')
compare =  int(inteiro)

if compare % 2 == 0:
    print('par')
else:
    print('impar')
#=================================================================================
hora = input('horario:')
time_zone = int(hora)
    
if time_zone >= 0 and time_zone <= 11:
        print('bom dia!')
elif time_zone >= 12 and time_zone <= 17:
        print('bom tarde!')
elif time_zone >= 18 and time_zone <= 23:
        print('bom noite!')
elif time_zone < 0 or time_zone > 23:
        print('horario inexistente!')
#=================================================================================
nome = input('nome:')
char = len(nome)

if char <= 4:
    print('curto!')
elif char >= 5 and char <= 6:
    print('correto!')
elif char > 6:
    print('muito grande!')
#=================================================================================
    print('fatiando textos')
    print('')
    
    texto = 'leitura'
    
    print(texto[0],texto[1],texto[2],texto[3])
    print(texto[1])
    print(texto[2])
    print(texto[3])
    
    print('')
    url = 'www.google.com
    nova_url = url[4:10]
    print(nova_url)
    
    #url[de:até:passos*]
    #os passos seram os salto para chegar até o valor máximo*
    #exemplo indices 3 a 4 de 2 em 2 passos 
#=================================================================================
max = 7
min = 0

while min < max:
    min = min + 1
    print(min)
#=================================================================================
url = 'www.javadoc.com'

for path in url:
    print(path)
----------------------------------------------------------------------------------    

for n in range(1,9):
    print(n)
----------------------------------------------------------------------------------    
max = 9
min = 0
for n in range(min,max):
    print(n)
----------------------------------------------------------------------------------    
max = 9
min = 0
passos = 2
for n in range(min,max,passos):
    print(n) 
#=================================================================================
lista = ['a','b','c','d']
print(lista[3])
print(lista[0])
print(lista)

for n in lista:
    print(n)
    
----------------------------------------------------------------------------------   
lista = ['a','b','c','c','d']
print(lista[1:3])
----------------------------------------------------------------------------------   

l1 = [1,2,3]
l2 = [4,5,6]


l1.extend(l2)
l2.append(9)
del(l2[0])
l2.insert(0,'Pizza')

l3 = l1 + l2

print(l1)
print(l2)
print(l3)
----------------------------------------------------------------------------------   

l1 = [1,2,3]
l2 = [4,5,6]

for n in l2:
    if n > 5:
        print([])
    else:
        print(n)
#=================================================================================
    #códigos
#=================================================================================
    #códigos
#=================================================================================
   #códigos
#=================================================================================
   #códigos
#=================================================================================
   #códigos
#=================================================================================
   #códigos
#=================================================================================
   #códigos
#=================================================================================
   #códigos
#=================================================================================
   #códigos
#=================================================================================