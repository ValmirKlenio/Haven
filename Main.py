# bibliotecas / imports
import os
import urllib.request

# listas / dicionários
itens_cadastrados = []
estoque = []
credito_item = ''

# menu
def menu():
  print('''Escolha uma opção:
  [ 1 ]  - Cadastrar Itens
  [ 2 ]  - Avaliar Itens
  [ 3 ]  - Gestão de Créditos
  [ 4 ]  - Catálogo de Itens
  [ 5 ]  - Troca de Itens
  [ 6 ]  - Doação de Itens
  [ 7 ]  - Relatórios e Estatísticas
  [ 8 ]  - Gestão de Estoque de Produtos
  [ 9 ]  - Balanço de Vendas
  [ 10 ] - Relatórios Estatísticos''')

# módulo 1
class Item:
  def __init__(self, nome, descricao, condicao, foto=None):
      self.codigo = self.gerar_codigo()
      self.nome = nome
      self.descricao = descricao
      self.condicao = condicao
      self.foto = foto

  def gerar_codigo(self):
      return str(hash(self.nome + self.descricao))[:8]

  def exibir_detalhes(self):
      print(f"Código: {self.codigo}")
      print(f"Nome: {self.nome}")
      print(f"Descrição: {self.descricao}")
      print(f"Condição: {self.condicao}")
      if self.foto:
          print(f"Foto: {self.foto}")
      print("\n")

def cadastrar_item():
    nome = input("Digite o nome do item: ")
    descricao = input("Digite a descrição do item: ")
    condicao = input("Digite a condição do item: ")

    foto_url = input("Digite a URL da foto (opcional): ")
    if foto_url:
        foto_path = f"{nome}_{descricao}.jpg"
        urllib.request.urlretrieve(foto_url, foto_path)
    else:
        foto_path = None

    novo_item = Item(nome, descricao, condicao, foto_path)

    print("\nItem cadastrado com sucesso:")
    novo_item.exibir_detalhes()

def principal():
    cadastrar_item()

if __name__ == "__main__":
    principal()

# módulo 2
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

# módulo 3
class GestorDoacao:
  def __init__(self, credito_inicial):
      self.creditos_disponiveis = credito_inicial

  def aprovar_doacao(self, valor_doacao):
    if valor_doacao <= self.creditos_disponiveis:
        self.creditos_disponiveis -= valor_doacao
        print(f"Doação aprovada! Créditos restantes: {self.creditos_disponiveis}")
        return True
    else:
        print("Desculpe, não há créditos suficientes para aprovar esta doação.")
        return False

# módulo 4
class Item:
  def __init__(self, nome, descricao, creditos):
      self.nome = nome
      self.descricao = descricao
      self.creditos = creditos

def exibir_catalogo(itens):
  print("Catálogo de Itens Disponíveis:")
  for i, item in enumerate(itens, start=1):
      print(f"{i}. {item.nome} - {item.descricao} (Créditos: {item.creditos})")

def main():
  item1 = Item("Livro", "História interessante", 5)
  item2 = Item("Brinquedo", "Para todas as idades", 3)
  item3 = Item("Roupas", "Diversos tamanhos e estilos", 7)

  catalogo_itens = [item1, item2, item3]

  exibir_catalogo(catalogo_itens)

if __name__ == "__main__":
  main()

# módulo 5
class TrocaItens:
  def __init__(self, saldo_credito):
    self.saldo_credito = saldo_credito

  def trocar_itens(self, item, valor_troca):
    item = input('Item que deseja trocar: ')
    valor_troca = int(input('Valor do item que deseja trocar: '))
    if valor_troca <= self.saldo_credito:
      self.saldo_credito -= valor_troca
      print(f"Troca realizada! {item} trocado por {valor_troca} créditos.")
      print(f"Saldo de crédito restante: {self.saldo_credito}")
      return True
    else:
      print("Desculpe, não há créditos suficientes para realizar esta troca.")
      return False
# módulo 6
class SistemaDoacao:
  def __init__(self):
      self.historico_doacoes = []

  def realizar_doacao(self, item, quantidade):
    item = input('Item que deseja doar: ')
    quantidade = int(input('Quantos pretende doar? '))
    if quantidade <= 0:
      print("A quantidade de itens para doação deve ser maior que zero.")
      return False
    doacao = {"item": item, "quantidade": quantidade}
    self.historico_doacoes.append(doacao)
    print(f"Doação registrada: {quantidade} unidades de {item}")

    return True

  def exibir_historico_doacoes(self):
    print("\nHistórico de Doações:")
    for i, doacao in enumerate(self.historico_doacoes, start=1):
        print(f"{i}. Item: {doacao['item']}, Quantidade: {doacao['quantidade']}")

# módulo 7

# módulo 8 #REVISAR
def cadastro_itens():
  item = input('Item: ')
  categoria = input('Categoria: ')
  preço = float(input('Preço: '))
  estoque.append({'Item': item, 'Categoria': categoria, 'Preço': preço})
  print(estoque)
  if item in estoque:
    print(f'A quantidade do item no estoque é {len(item)}')

class GestorEstoque:
  def __init__(self, estoque_inicial):
    self.estoque = estoque_inicial

  def vender_produto(self, item, quantidade):
    item = input('Item: ')
    quantidade = int(input('Quantidade: '))
    if item in self.estoque and self.estoque[item] >= quantidade:
      self.estoque[item] -= quantidade
      print(f"Venda concluída! {quantidade} unidades de {item} vendidas.")
      print(f"Estoque restante de {item}: {self.estoque[item]} unidades.")
      return True
    else:
      print(f"Desculpe, não há estoque suficiente de {item}. Venda não concluída.")
      return False

# módulo 9

# módulo 10

# chamada de funções
while True:
  menu()
  opcao = int(input('Digite a opção desejada: '))
  if opcao == 1:
    print('-*' * 20)
    print('...::: CADASTRAR ITENS :::...')
    print()
    principal()
    print()
  elif opcao == 2:
    print('-*' * 20)
    print('...::: AVALIAR ITENS :::...')
    print()
    # Exemplo de uso da função
    item_doado = "roupa"
    condicao_item = "usado"
    itens_desejados = ["roupa", "brinquedo", "alimento"]
    doacao = avaliar_doacao(item_doado, condicao_item, itens_desejados)
    if doacao:
      print('Pode doar o item')
    else:
      print('Infelizmente, o item não pode ser doado neste momento.')
    print()
  elif opcao == 3:
    print('-*' * 20)
    print('...::: GESTÃO DE CRÉDITOS :::...')
    print()
    gestor = GestorDoacao(100)
    doacao_aprovada = gestor.aprovar_doacao(30)
    if doacao_aprovada:
      print("Doação bem-sucedida!")
    else:
      print("A doação não pôde ser concluída devido à falta de créditos.")
    print()
  elif opcao == 4:
    print('-*' * 20)
    print('...::: CATÁLOGO DE ITENS :::...')
    print()
    main()
    print()
  elif opcao == 5:
    print('-*' * 20)
    print('...::: TROCA DE ITENS :::...')
    print()
    saldo_inicial = 100  # Saldo inicial de crédito
    sistema_troca = TrocaItens(saldo_inicial)
    # Troca um item no valor de 30 créditos
    troca_concluida = sistema_troca.trocar_itens("livro", 30)
    if troca_concluida:
      print("Troca bem-sucedida!")
    else:
      print("A troca não pôde ser concluída devido à falta de créditos.")
    print()
  elif opcao == 6:
    print('-*' * 20)
    print('...::: DOAÇÃO DE ITENS :::...')
    print()
    sistema_doacao = SistemaDoacao()
    # Realiza doações
    sistema_doacao.realizar_doacao("roupa", 5)
    sistema_doacao.realizar_doacao("brinquedo", 3)
    # Exibe o histórico de doações
    sistema_doacao.exibir_historico_doacoes()
    print()
  elif opcao == 7:
    print('-*' * 20)
    print('...::: RELATÓRIO E ESTATÍSTICAS :::...')
    print()
    # chamada da função
    print()
  elif opcao == 8:
    print('-*' * 20)
    print('...::: GESTÃO DE ESTOQUE DE PRODUTOS :::...')
    print()
    print('''Escolha uma opção:
    1 - Cadastrar Iten
    2 - Vender item''')
    opc = int(input('Opção: '))
    if opc == 1:
      cadastro_itens()
    elif opc == 2:
      estoque_inicial = {"camiseta": 50, "calca": 30, "sapato": 20}
      gestor_estoque = GestorEstoque(estoque_inicial)
      # Vende 10 unidades de camiseta
      venda = gestor_estoque.vender_produto("camiseta", 10)
      if venda:
        print("Venda bem-sucedida!")
      else:
        print("A venda não pôde ser concluída devido à falta de estoque.")
    else:
      print('OPÇÃO INVÁLIDA!')
    print()
  elif opcao == 9:
    print('-*' * 20)
    print('...::: BALANÇO DE VENDAS :::...')
    print()
    # chamada da função
    print()
  elif opcao == 10:
    print('-*' * 20)
    print('...::: RELATÓRIOS ESTATÍSTICOS :::...')
    print()
    # chamada da função
    print()
