n1=float(input('Digite sua nota da AV1: '))
n2=float(input('Digite sua nota da AV2: '))
n3=float(input('Digite sua nota da AVd: '))

nota=n1+n2+n3/4

if nota >= 6:
    print('Parabens voce foi aprovado! sua nota foi:{}'.format(nota))
elif nota <= 6:
        print('Voce foi reprovado! sua nota foi:{}'.format(nota))
else:
    print('Voce nao digitou nada')   