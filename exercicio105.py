"""
Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)

Adicione também as docstrings dessa função para consulta pelo desenvolvedor.
"""
"""
def contador3 (*num) :
    tam = len(num)
    print (f'Recebi os valores {num} que não ao todo {tam} números')
""" 

notas = list ()
notasDic = dict ()
cont = 0
resp = 0
def notas1 (* resp) :

    sit = False
    notasDic ['notas'] = resp
    for c in len(notas) :
        cont +=1
    print (f'Total: {cont}, maior: , menor: , media: ')
    

"""
notasDic = list ()

while True :
    n = int (input ('Digite uma nota: '))
    notasDic.append(n)
    while True :
        pergunta = str (input ('Quer continuar? [S/N]: ')).strip().upper()
        if 'SN' != pergunta :
            print ('INVALIDO, Digite S ou N')
        if pergunta in 'N' :
            break
        if 'S' in pergunta :
            break
    if pergunta in 'N' :
        break 
"""
#resp = notas (5.5, 9.5, 10, 6.5, sit = True)
resp = notas (5.5, 9.5, 10, 6.5)
print (resp)




"""
print (f'Sua nota é {n} ')
print (f'Sua lista é {notasDic} ')

print ('FIm')
"""
