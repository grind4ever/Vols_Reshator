import math
a = float(input('Введите ширину паралельного сближения(a): '))

#Тут кароче дают индекс сигме
sigma = float(input('Введите удельную проводимость грунта(Сим/м): '))
if 10*10**(-3) >= sigma > 1*10**(-3) :
    sigma_index = 1
elif sigma > 10*10**(-3) and sigma <= 50*10**(-3):
    sigma_index = 2  
elif sigma > 50*10**(-3) and sigma <= 100*10**(-3):
    sigma_index = 3

#тут выбираем частоту
fa = int(input('Введите f (1-50Гц 2-800 Гц): '))
if fa == 1:
    f = 50
elif fa == 2:
    f = 800

#Тут делаем индекс для пути
put = int(input('Введите путность: 1- однопутный, 2-двупутный 3-многопутный (это из бумажки): '))
if put == 1:
    put = 'oneway'
elif put == 2:
    put ='twoway'
elif put == 3:
    put = 'anyway'

#Тут выбираем марку кабеля    
mark = int(input('Введите тип ккабеля: 1-МКС, 2-МКПАБ, 3-МКБАБ: '))
match mark:
    case 1:
        mark_string = 'MKS'
    case 2:
        mark_string = 'MKBAB'
    case 3:
        mark_string = 'MKPAB'
#Тут на основе марки кабеля Sоб выбираем ну а сами данные ниже
Sob = {50: 
        {'MKS': 0.54,
         'MKBAB': 0.1,
         'MKPAB': 0.1},
       800:
       {'MKS': 0.06,
        'MKBAB': 0.01,
        'MKPAB': 0.015}
}
print(f'Sob для {mark_string} = {Sob[f][mark_string]}')
#Тут считаем М
M = (10**(-4) * math.log(1+(6*10**(5)/((a**2)*sigma*f)))) #тут матх не импортировался к сожалнию
print(f'M = {M*10**(5)} 10^(-5) Гн/км')
#Тут считаем Um
K = 1.01
Um = K*2*3.14*f*M
print(f'Um = {Um}')
#Тут считаем Sp
Sp = {1: 
        {'oneway': 0.45,
         'twoway': 0.50,
         'anyway': 0.55},
       2:
        {'oneway': 0.40,
         'twoway': 0.45,
         'anyway': 0.50},
       3:
        {'oneway': 0.30,
         'twoway': 0.35,
         'anyway': 0.40}
}
