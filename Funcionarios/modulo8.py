def cadastro_itens():
  item = input('Item: ')
  categoria = input('Categoria: ')
  preço = float(input('Preço: '))
  estoque.append({'Item': item, 'Categoria': categoria, 'Preço': preço})
  print(estoque)
  if item in estoque:
    print(f'A quantidade do item no estoque é {len(item)}')

def vendas():
  item = input('Item: ')
  for i in estoque:
    item, categoria, preco = i
    print(i)
    print(f'Item disponível no estoque!')
    opc = int(input('Deseja comprá-lo? '))
    if opc == 'Ss' or opc == 'SIM' or opc == 'Sim' or opc == 'sim':
      estoque.remove(i)
  else:
    print('Item não encontrado')
