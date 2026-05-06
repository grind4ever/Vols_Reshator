import math 
f = int(input("Введите частоту как в бумажке 3-4 цифры(): "))
grunt = float(input("Введите удельную проводимость грунта(в бумажке вашей): "))
f = f*1000
print(f'частота: {f} Гц')
aye =  1.01
mark = int(input("Кабель какой марки(введите номер): МКС-1, МКПАБ-2, МКБАБ-3: "))
match mark:
    case 1:
        chetverki = 7 #количество четвёрок 6+1 у нас было это смотрится в маркировке кабеля 
        Rt = 5.5
        d0 = 1.2
        delta = 0.8
        sigma = 0
        piramida = 0.05
        d1 = d0 + 2 * delta * (1-sigma) + 2 * piramida
        epsilon = 1.25
        if f >= 10**(3):
            tgd = 3
        elif f >= 100**(3):
            tgd = 7
        elif f >= 250**(3):
            tgd = 12
        elif f >= 550**(3):
            tgd = 20
        print(f'диаметр голой жилы: {d0}')
        print('кордельно-стирофлексная изоляция: ')
        print("Марка кабеля МКС")
    case 2:
        Rt = 2.0 # вот тут не уверен если че таблица 1.3 какой то движ с оболочками и повивами
        d0 = 1.05
        d1 = 2.3 * d0
        epsilon = 1.25
        if f >= 10**(3):
            tgd = 2
        elif f >= 100**(3):
            tgd = 6
        elif f >= 250**(3):
            tgd = 8
        elif f >= 550**(3):
            tgd = 12
        print(f'диаметр голой жилы: {d0}')
        print("Марка кабеля МКПАБ")
    case 3:
        Rt = 2.0 #вот тут не уверен
        d0 = 1.2
        delta = 0.8
        sigma = 0.5
        piramida = 0.17
        d1 = d0 + 2 * delta * (1-sigma) + 2 * piramida
        epsilon = 1.25
        if f >= 10**(3):
            tgd = 55
        elif f >= 100**(3):
            tgd = 113
        elif f >= 250**(3):
            tgd = 160
        elif f >= 550**(3):
            tgd = 280
        print(f'кордельно бумажнаяя изоляция: d1 = {d1}')
        print(f'диаметр голой жилы: {d0}')
        print("Марка кабеля МКБАБ")

metal = int(input('Выберите материал: 1 - медь, 2 - алюминий: '))
match metal:
    case 1:
        print("Материал - медь")
        ro = 0.0178
        kr = 0.0105*d0*math.sqrt(f)
        at = 0.0039
    case 2:
        print("Материал - алюминий") 
        ro = 0.0292
        kr = 0.0082*d0*math.sqrt(f)
        at = 0.0037
kr = round(kr,2)
print(f'kr = {kr} ,бери ближайшее значение из таблицы')
if kr >= 11: #потенциальное место для бага че с этим делать я пока хуй знает
    kr = 11.0
Fun_kr = {0:{'Fkr': 0, #кароче заковыка надо добавить функционал чтобы находил ближайшее к kr число из словаря 
               'Gkr': (kr**4)/64,
               'Hkr': 0.04107,
               'Qkr': 1.0},
        1.0:{'Fkr': 0.00519,
               'Gkr': 0.01519,
               'Hkr': 0.053,
               'Qkr': 0.997},
        2.0:{'Fkr': 0.0782,
               'Gkr': 0.1724,
               'Hkr': 0.169,
               'Qkr': 0.961},
        2.5:{'Fkr': 0.1756,
               'Gkr': 0.295,
               'Hkr': 0.263,
               'Qkr': 0.913},
        3.0:{'Fkr': 0.318,
               'Gkr': 0.405,
               'Hkr': 0.248,
               'Qkr': 0.845},
        3.5:{'Fkr': 0.492,
               'Gkr': 0.499,
               'Hkr': 0.416,
               'Qkr': 0.766},
        4.0:{'Fkr': 0.678,
               'Gkr': 0.584,
               'Hkr': 0.466,
               'Qkr': 0.686},
        4.5:{'Fkr': 0.862,
               'Gkr': 0.669,
               'Hkr': 0.503,
               'Qkr': 0.616},
        5.0:{'Fkr': 1.042,
               'Gkr': 0.755,
                'Hkr': 0.530,
                'Qkr': 0.556},
        7.0:{'Fkr': 1.743,
                'Gkr': 1.109,
                'Hkr': 0.596,
                'Qkr': 0.400},
        10.0:{'Fkr': 2.799,
                'Gkr': 1.641,
                'Hkr': 0.643,
                'Qkr': 0.282},
        11.0:{'Fkr': round((((math.sqrt(2)*kr)-3)/4),3),
                'Gkr': round(((math.sqrt(2)*kr)-1)/8,3),
                'Hkr': 0.750,
                'Qkr': round(2*math.sqrt(2)/kr,3)}
}

for kr in Fun_kr:
    print(f'При kr = {kr} Fkr = {Fun_kr[kr]['Fkr']}, Gkr = {Fun_kr[kr]['Gkr']}, Hkr = {Fun_kr[kr]['Hkr']}, Qkr = {Fun_kr[kr]['Qkr']}')
kr = float(input('Введите kr, выбрав ближайшее значение из таблицы: '))
t = input('Какая температура(20 по умолчанию просто Enter нажать)')
if t == '':
    t = 20

p = input('Введите тип скрутки, парная = введите 1 (по умолчанию звёздная, просто Enter нажать)')
if p == '':
    p = 5
    dgr = 2.41*d1
elif p == '1':
    p = 1
    dgr = 1.71*d1
Rt = round((ro*(2550/d0**2)*abs(1+at*(t-20))),3)
print(f'Rt = {Rt} ')
a = 1.41 * d1
Rstrix = round(aye*Rt*
               (1 + Fun_kr[kr]['Fkr']+
                ((p*Fun_kr[kr]['Gkr']*(d0/a))/(1-Fun_kr[kr]['Hkr']*math.sqrt(d0/a)))
                ),3)
print(f'Rstrix = {Rstrix}')
Rm = round((Rt*math.sqrt(f/200000)),3)
print(f'Rm = {Rm}')
R = Rm + Rstrix
print(f'R = {R}')
r = round((d0/2),3)
print(f'R = {R} Ом, r = {r}')
L = round(((1.01*(4*math.log(math.log((a-r)/r))+Fun_kr[kr]['Qkr'])*10**(-4))*10**(4)),3)
print(f'L = {L} *10^(-4) Гн/км')
vilka = round(((((dgr+d1-d0)**2)-a**2)/((dgr+d1-d0)**2)+a**2),3)
print(f'vilka = {vilka}')
C = round(((aye*epsilon*10**(-6))/(36*math.log(vilka*(2*a/d0)))*10**(8)),10)
print(f'C = {C} *10^(-8) Ф/км')
C = C*10**(-8)
L = L*10**(-4)
G = round((2*math.pi*f*C*tgd),10)
print(f'G = {G} *10^(-6) С/км')