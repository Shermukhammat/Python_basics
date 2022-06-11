# 3.Oila a'zolaringiz (do'stlaringiz) dan 3 ta sevimli 
# kino-seriali haqida so'rang. Do'stingiz ismi kalit, uning
# sevimli kinolarini esa ro'yxat ko'rinishida lug'atga saqlang. 
# Natijani konsolga chiqaring.

kinola = {
    'SHermuhammad' : ['I am robot', 'doctor strenj 2', 'terminator', 'Iron man'],

    'isroil' : ['yovuzlik maskani', 'terminator', 'matritsa' ],

    'akam' : ['sheryurak', 'tro\'ya', 'vassabi'],

    'onam' : ['Yor yor', 'zuleyha', 'oiyla uchun']
}

for ism, kinolar in kinola.items():
    print(f"{ism.title()}ning sevimli kinolari : ", end = '')
    nuqta = ' '
    for kino in kinolar:
        if kino == kinolar[-1]:
            nuqta = '.'
        else:
            nuqta = ', '
        print(f"'{kino}'{nuqta}", end = '')
    print('\n')