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

# Exemplo de uso da função
estoque_inicial = {"camiseta": 50, "calca": 30, "sapato": 20}
gestor_estoque = GestorEstoque(estoque_inicial)

# Vende 10 unidades de camiseta
venda = gestor_estoque.vender_produto("camiseta", 10)

if venda:
  print("Venda bem-sucedida!")
else:
  print("A venda não pôde ser concluída devido à falta de estoque.")
