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
