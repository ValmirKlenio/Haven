def verifica_itens():
  item = input('Item que deseja verificar: ')
  condicao = input('Condição: ')
  while item not in itens_cadastrados:
    print('Item não cadastrado! Verifique novamente ou cadastre o item.')
    break
  if condicao == 'Novo' or condicao == 'novo':
    credito_item = '50'
    print('Produto NOVO, em ótimas condições!')
    print('APROVADO PARA DOAÇÃO')
    pontuacao = input('Atribua uma pontuação para esse produto: ')
  elif condicao == 'Seminovo' or condicao == 'seminovo':
    credito_item = '35'
    print('Produto SEMINOVO, em boas condições')
    print('APROVADO PARA TROCA')
    pontuacao = input('Atribua uma pontuação para esse produto: ')
  elif condicao == 'Usado' or condicao == 'usado':
    credito_item = '15'
    print(f'Produto USADO, mas conservado.')
    print('APROVADO PARA DOAÇÃO')
    pontuacao = input('Atribua uma pontuação para esse produto: ')
  else:
    print('Condição inválida! O produto não tem chances de ser vendido. Seu estado não é bom!')
    print('NÃO APROVADO')
