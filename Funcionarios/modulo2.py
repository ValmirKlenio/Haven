itens_cadastrados = []
    
def avaliar_doacao(item, condicao, itens_cadastrados):
  condicoes_aceitaveis = ["novo", "usado", "em bom estado"]
  item = input('Item que dese doar: ')
  condicao = input('Qual a condição do item? ')
  while condicao.lower() not in condicoes_aceitaveis:
    print('Desculpe, a condição do item não é aceitável para doação.')
    return False
  if item.lower() in itens_cadastrados:
    print('Ótimo! O item é desejado para doação.')
    return True
  else:
    print("O item não está na lista de itens desejados para doação.")
    return False

# Exemplo de uso da função
item_doado = "roupa"
condicao_item = "usado"
itens_desejados = ["roupa", "brinquedo", "alimento"]
doacao = avaliar_doacao(item_doado, condicao_item, itens_desejados)
if doacao:
  print('Pode doar o item')
else:
  print('Infelizmente, o item não pode ser doado neste momento.')
