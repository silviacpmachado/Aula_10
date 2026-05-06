# Simule um caixa eletrônico. O sistema deve iniciar com saldo de R$ 1.000,00 e solicitar ao usuário 
# o valor que deseja sacar. Após as tentativas de saque, exiba mensagens adequadas informando o 
# resultado da operação e finaliza o programa.
# Utilize a estrutura de tratamento de erros. 

print('CAIXA ELETRÔNICO')

try:
   saldo = 1000
   saque = float(input('Informe o valor do saque: '))
   
except ValueError:
   print('Valor inválido')
except KeyboardInterrupt:
   print('Programa encerrado pelo usuário')
else:
   if saque > saldo:
      print('Saldo Insuficiente')
   elif saque <= 0:
      print('Saque precisa ser maior ou igual a R$ 2,00')
   else:
      saldo -= saque
      print('\nSaque realizado com sucesso')
      print(f'Saldo em conta R$ {saldo:.2f}')
finally:
   print('Operação realizada')

print('\nPrograma Encerrado') 

