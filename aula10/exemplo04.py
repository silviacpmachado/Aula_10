print(' === Cálculo de Produtividade ===')

try:

   total_produzido = float(input('Valor total da venda:'))
   funcionarios = int(input('Total de Funcionários: '))
 

   media_por_funcionario = total_produzido / funcionarios
   print(f"Média por funcionário: {media_por_funcionario:.2f}")
except (ValueError, TypeError):
   print('O valor precisa ser numérico')
except ZeroDivisionError:
   print('Funcionário não pode ser Zero. ')
except KeyboardInterrupt:
   print('Operação cancelada pelo usuário')
else:
   print(f"Média por funcionário: {media_por_funcionario:.2f}")

#Executa sempre. Com erro ou não, o bloco finally sempre irá executar.
finally:
   print('Programa encerrado!')