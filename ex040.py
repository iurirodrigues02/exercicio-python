import colorama
colorama.init()

nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
nota3 = float(input('Digite a terceira nota do aluno: '))
média = (nota1+nota2+nota3)/3

if média < 5.0:
    print('\033[1;31mREPROVADO')
elif média >= 5.0 and média <= 6.9:
    print('\033[1;33mRECUPERAÇÃO')
else:
    print('\033[1;36mAPROVADO')