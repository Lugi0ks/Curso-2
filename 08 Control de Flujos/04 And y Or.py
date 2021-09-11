print('-------------- And --------------')

if 2 < 5 and 6 > 3:
    print('Ambas son verdaderas')

if 2 > 5 and 6 > 3:
    print('Ambas son verdaderas')
else:
    print('Tenemos una falsa')

print('-------------- Or --------------')

if 2 > 5 or 6 > 3:
    print('Una de estas es verdaderas')
else:
    print('ambas son falsas')

if 2 > 5 or 6 < 3:
    print('Una de estas es verdaderas')
else:
    print('ambas son falsas')