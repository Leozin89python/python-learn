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
    #Exercicio aula 45

def countimp( ):
 max = 9
 min = 0
 for count in range(min,max,1):
  print(count)
  
 
def countdec( ):
 max = 11
 min  = 2
 while max > min:
  max -= 1
  print(max)

  
countimp( )
print( )
print( )
countdec( )
#=================================================================================
    #aula 52
#exercicio 1
def saudacaoFala(saud,nome):
    print(saud)
    print(nome)
    
    
saudacaoFala('oi','Leo')

#exercicio 2
def soma(n1,n2,n3):
    return n1 + n2 +n3
    
print(soma(1,5,4))  

#exercicio 3
def porcentagem(numero,perc):
    percentual = (perc/100)
    total = numero + (numero * percentual)
    return total
        
        
print(porcentagem(10,1))  

#exercicio 4 (houve correção Ex:de ordem dos elementos e etc..)
def fizzBuzz(n):
    if n % 5 == 0 and n % 3 == 0:
        print('fizzbuzz')
    elif n % 2 == 0:
        print( 'fizz' )
    elif n % 5 == 0:
        print('buzz')
    else:
        print(n)
        
fizzBuzz(15)
fizzBuzz(4)
fizzBuzz(25)

#exercicio 4 (versão errada)
#=================================================================================
   #elementos {     args    } em {  kwargs  } 
#=================================================================================
   conta = 354006

def banco():
    global conta
    print(conta)

banco()
----------------------------------------------------------------------------------   
preco = 3.65
quantidade = 24


def valorAPagar():
    global preco, quantidade
    total = preco * quantidade
    return total
    
print(valorAPagar())
#=================================================================================
   #aula 56
   #exercicio 1
   def calc():
    function = calculatorMachine(1,3)
    return function
    
    
def calculatorMachine(num1,num2):
    soma = num1 + num2
    mult = num1 * num2
    sub  = num2 - num1 
    div  = num2 / num1
    return soma, mult, sub, div
    
    
print(calc())

 #exercicio 2
 #resposta do prof°
def mestre(funcao, *args, **Kwargs):
    return funcao(*args, **Kwargs)
    
    
def fala_oi(nome):
    return f'Oi {nome} como vai?'
    
    
def saudacao(nome,saudacao):
    return f'{saudacao} {nome}'
    
    
executando  = mestre(fala_oi,'Leo')
executando2 = mestre(saudacao, 'Leo!','estudar')
print(executando) 
print(executando2)  
#=================================================================================
def calc(num1,num2):
    return  num1 * num2
    
variavel = calc(6,3)
print(variavel)
    
arrow = lambda a,s: a * s
print(arrow(6,3))
----------------------------------------------------------------------------------   

lista = [
    ['p1',13],
    ['p2',6],
    ['p3',4],
    ['p4',50],
]

lista.sort(key=lambda item: item[1], reverse=False)
print(lista)
#=================================================================================

print( '==========================')

print('tuplas')

t1 = (1,2,3,'nome')

for v in t1:
 print(v)
 
 
 
t2 = (1,3,7,5,0)
t2 = list(t2)
t2[  2  ] = 'newList( )'
print(t2)

print( '==========================')


print('dicionarios')
d1 = {  'chave1' : 'valor da chave' }
d2 = dict(  chave2='valor da chave 2', chave3='valor da chave 3')

d3 = {   
       'str':'String',
       123:'next-value',
       (3,5):'tupla'
}

print(d1)
print(d2)

print()
print('acessando posição no dicionario:')
print(   d3[(   123   )]    )

print('inserindo valor no dicionario')
d3[7] = 'sabado'
d3.update({ 101 : 'binario' }) 
print(d3)

#apagando
#EX:
#del d3[  7  ]   outro ex: del d3[  123   ]


clientes ={
      'cliente1' : {
          'nome':'Leleu',
          'sobrenome':'Arruda'
      },
      'cliente2' : {
          'nome':'Ayla',
          'sobrenome':'Smith'
      }
}
#chama tudo
#for cliente_k, cliente_v in clientes.items( ):
#print(cliente_k,cliente_v)


#esta chamada é mais estilizada
#arvore de dados
for clientesK, clientesV in clientes.items( ):
 print(f'Exibindo: { clientesK }')
 for dadosK, dadosV in clientesV.items( ):
  print(f'\t{ dadosK }  = { dadosV } ')

print( '==========================' )

print( '==========================' )

print( '==========================' )
#=================================================================================
   #códigos ou descrição
#=================================================================================
   #códigos ou descrição
#=================================================================================