notas = []

for nota in range(1, 5, 1):
    notas.append(int(input(f'Informe a {nota}ª nota: ')))

media = sum(notas) / len(notas)
print(f'Sua média final foi {media}')
if media >= 7:
    print('Aprovado')
else:
    notas.append(int(input('Informe a nota da prova final: ')))
    media = sum(notas)/ len(notas)
    print(f'Sua média final foi {media}')
    if media >= 6:
        print('Aprovado')
    else:
        print('Reprovado')