#python:


print('=======================') 
print('|                     |')
print('|WELCOME TO THE SYSTEM|')
print('|                     |') 
print('=======================') 

#loading = "Carregando..."

loading = 'loading...'
print(loading)
print()

count = 'counting time'
print(count, '/')


def msg():
    return 'welcome again'
    
    
print(msg())

print()
print('calculation data:')
tax = (5/100)
salary = 942.35
time   = 30

print('tax: 5%' )
print('salary:',salary,'R$')
print('time/month:', time)

print()
total = (tax * salary * time)
print('total:',total,'R$  in this case')

def salary_calculation(tax,salary,time):
    tax_value = (tax/100)
    return 'total:',tax_value * salary * time
    
print('enter with your salary, tax and time to count below:')
print(salary_calculation(9,2145.36,27))


name = input('Now enter with your name:\n')
job  = input('Enter with your job: \n')
timeToJobIn = input('time to work: \n')

print('name:',name)
print('name:',job)
print('name:',timeToJobIn)

places = ['Valéria, Salvador-BA','Barris, Salvador-BA','Stella Mares, Salvador-BA','Imbuí, Salvador-BA']
print(places)

print()
print('choose one place above')
print()
choice_1 = 'Valéria, Salvador-BA'
choice_2 = 'Barris, Salvador-BA'
choice_3 = 'Stella Mares, Salvador-BA'
choice_4 = 'Imbuí, Salvador-BA'
    
def choices(choice):
    if(choice == choice_1):
       return 'downtown choose is:',choice_1
    elif(choice == choice_2):
       return 'downtown choose is:',choice_2
    elif(choice == choice_3):
        return 'downtown choose is:',choice_3
    elif(choice == choice_4):
       return 'downtown choose is:',choice_4
        
        
print(choices(choice_4))