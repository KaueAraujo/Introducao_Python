def calcSoma(num1, num2):
    result = num1+num2
    print(str(num1)+' + '+str(num2)+' = '+str(result))


def calcSub(num1, num2):
    result = num1-num2
    print(str(num1)+' - '+str(num2)+' = '+str(result))


def calcMult(num1, num2):
    result = num1*num2
    print(str(num1)+' * '+str(num2)+' = '+str(result))


def calcDiv(num1, num2):
    result = num1/num2
    if num1 % num2 == 0:
        print('Os números são divisíveis!')
        print(str(num1)+' / '+str(num2)+' = '+str(result))
    else:
        print('O resultado não é uma divisão exata. Podemos dizer que o resultado é:')
        print(str(num1)+' / '+str(num2)+' = '+str(result))
        quociente = num1//num2
        resto = num1 % num2
        print('Ou ainda que:')
        print(str(num1)+' / '+str(num2)+' é uma divisão com quociente ' +
              str(quociente)+' e resto '+str(resto))


print('######################## Calculadora Python ########################')
print('Selecione a operação desejada:')
print('')
print('1 - Soma')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão')
print('')
opcao = int(input('Digite a sua opção (1/2/3/4):'))
while opcao not in [1, 2, 3, 4]:
    print('Opcao inválida. Tente novamente.')
    print('')
    opcao = int(input('Digite a sua opção (1/2/3/4):'))
prim_num = float(input('Digite o primeiro número:'))
seg_num = float(input('Digite o segundo número:'))

if opcao == 1:
    print('Operação selecionada: Soma')
    calcSoma(prim_num, seg_num)
elif opcao == 2:
    print('Operação selecionada: Subtração')
    calcSub(prim_num, seg_num)
elif opcao == 3:
    print('Operação selecionada: Multiplicação')
    calcMult(prim_num, seg_num)
else:
    print('Operação selecionada: Divisão')
    calcDiv(prim_num, seg_num)

input()
