import os
import re
regra = re.compile(r"(0|-?[1-9][0-9]*)")
os.system('cls')
#Função para calcular o salário e o banco de horas
def banco(extra,setor,salario):
    if setor == 1:
        valor = extra * 4.5
        salario_total = salario + valor
        return f'{salario_total:0.2f}\nValor das horas extras: R${valor:0.2f}'
    elif setor == 2:
        valor = extra * 3.5
        salario_total = salario + valor
        return f'{salario_total:0.2f}\nValor das horas extras: R${valor:0.2f}'
def INSS_FGTS(salario):
    if salario <1212 or salario == 1212:
        sn = salario - (salario*7.5)/100
        return sn
    elif salario <1212.01 or salario <= 2427.35:
        sn = salario - (salario * 9)/100
        return sn
    elif salario <2427.36 or salario <= 3641.03:
        sn = salario - (salario * 12)/100
        return sn 
    else: 
        salario >= 3641.04
        sn = salario - (salario * 14)/100
        return sn
#Função principal de entrada e saída de dados 
def main():
    print("Bem-Vindo ao Banco de Funcionários!\nVersion 1.1v(Em desenvolvimento)")
    print()
    print("__________________________________________")
    print()
    while True:
        nome = input('Digite nome completo do funcionário: ').strip()
        if not nome:
            print("É necessário digitar algum caractere para continuar!")
        elif all(part.isalpha() or part.isspace() for part in nome.split()):
            break
        else:
            print("Nesse campo é válido apenas letras!\nTente novamente")
    while True:
        try:
           salario = float(input('Digite o salário do funcionário: ').strip())
           if salario <= 0 or salario > 1000000000:
               print("Esse número não é válido!\nPor favor, digite um salário válido")
           else:
               break
        except ValueError:
            print("Nesse campo é válido apenas números!\nTente novamente")
    while True:
        try:
           extra = float(input('Digite a quantidade de hora extra: ').strip())
           if extra > 4:
               hora = extra - 4
               extra = 4
               break
           else:
               hora = 0
               break
        except ValueError:
            print("Nesse campo é válido apenas números!\nTente novamente")
    while True:
        try:
            setor = int(input('Qual o setor do funcionário(1 para ADM/ 2 para OPR): ').strip())
            if setor == 1 or setor == 2:
                break
            else:
                print("Dado inválido!\nApenas digite apenas 1 para 'ADM' ou 2 para 'OPR'")
        except ValueError:
            print("Nesse campo é válido apenas números!\nTente novamente")

    os.system('cls')
    print('__________Funcionário__________')
    print()
    print(f'Nome Completo: {nome}')
    print(f'Salário: R${salario}')
    salario = INSS_FGTS(salario)
    print(f'Salário Total: R${banco(extra,setor,salario)}')
    print(f'Horas extras: {extra}h')
    print(f'Banco de horas: {hora}h')
    print(f'Setor do Funcionário: {setor}')
if __name__ == '__main__':
    main()