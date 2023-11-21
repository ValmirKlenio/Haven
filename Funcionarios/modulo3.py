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

# Exemplo de uso da função
gestor = GestorDoacao(100)  # Inicializa o gestor de doação com 100 créditos

# Aprova uma doação de 30 créditos
doacao_aprovada = gestor.aprovar_doacao(30)

if doacao_aprovada:
  print("Doação bem-sucedida!")
else:
  print("A doação não pôde ser concluída devido à falta de créditos.")
