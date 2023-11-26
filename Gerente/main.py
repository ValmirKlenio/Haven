from datetime import datetime

class Item:
    def __init__(self, avaliado=False, trocado=False, doado=False):
        self.avaliado = avaliado
        self.trocado = trocado
        self.doado = doado

class Transacao:
    def __init__(self, data, tipo, categoria, produto, valor):
        self.data = data
        self.tipo = tipo
        self.categoria = categoria
        self.produto = produto
        self.valor = valor

class Sistema:
    def __init__(self):
        self.dados_sistema = []
        self.transacoes = []

    def adicionar_item(self, item):
        self.dados_sistema.append(item)

    def realizar_transacao(self, transacao):
        self.transacoes.append(transacao)

class Gerente:
    def __init__(self, nome, sistema):
        self.nome = nome
        self.sistema = sistema

    def gerar_relatorio_geral(self):
        total_cadastrados = len(self.sistema.dados_sistema)
        total_avaliados = sum(item.avaliado for item in self.sistema.dados_sistema)
        total_trocados = sum(item.trocado for item in self.sistema.dados_sistema)
        total_doados = sum(item.doado for item in self.sistema.dados_sistema)

        print(f"Relatório Geral - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Número de itens cadastrados: {total_cadastrados}")
        print(f"Número de itens avaliados: {total_avaliados}")
        print(f"Número de itens trocados: {total_trocados}")
        print(f"Número de itens doados: {total_doados}")

    def exportar_relatorio_txt(self):
        with open("relatorio.txt", 'w') as arquivo:
            arquivo.write(f"Relatório Geral - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            arquivo.write(f"Número de itens cadastrados: {len(self.sistema.dados_sistema)}\n")
            arquivo.write(f"Número de itens avaliados: {sum(item.avaliado for item in self.sistema.dados_sistema)}\n")
            arquivo.write(f"Número de itens trocados: {sum(item.trocado for item in self.sistema.dados_sistema)}\n")
            arquivo.write(f"Número de itens doados: {sum(item.doado for item in self.sistema.dados_sistema)}\n")

    def balanco_vendas(self, data_inicio, data_fim, categoria=None, valor_min=None, valor_max=None):
        vendas_filtradas = []

        # Converta as strings de data para objetos datetime
        data_inicio = datetime.strptime(data_inicio, '%Y-%m-%d')
        data_fim = datetime.strptime(data_fim, '%Y-%m-%d')

        for transacao in self.sistema.transacoes:
            data_transacao = datetime.strptime(transacao.data, '%Y-%m-%d')
            if data_inicio <= data_transacao <= data_fim:
                if categoria is None or transacao.categoria == categoria:
                    if valor_min is None or valor_min <= transacao.valor <= valor_max:
                        vendas_filtradas.append(transacao)

        print(f"Balanço de Vendas - {data_inicio.strftime('%Y-%m-%d')} a {data_fim.strftime('%Y-%m-%d')}")
        for venda in vendas_filtradas:
            print(f"Data: {venda.data}, Categoria: {venda.categoria}, Valor: {venda.valor}")

    def relatorio_estatistico(self):
        total_vendas = sum(transacao.valor for transacao in self.sistema.transacoes if transacao.tipo == 'venda')
        total_trocas = sum(transacao.valor for transacao in self.sistema.transacoes if transacao.tipo == 'troca')
        produtos_mais_populares = self.encontrar_produtos_mais_populares()

        print("Relatório Estatístico")
        print(f"Total de Vendas: {total_vendas}")
        print(f"Total de Trocas: {total_trocas}")
        print("Produtos Mais Populares:")
        for produto, quantidade in produtos_mais_populares.items():
            print(f"{produto}: {quantidade}")

    def encontrar_produtos_mais_populares(self):
        produtos_mais_populares = {}
        for transacao in self.sistema.transacoes:
            produto = transacao.produto
            produtos_mais_populares[produto] = produtos_mais_populares.get(produto, 0) + 1
        return produtos_mais_populares

def exibir_menu():
    print("\nMenu:")
    print("1. Adicionar Item")
    print("2. Realizar Transação")
    print("3. Gerar Relatório Geral")
    print("4. Exportar Relatório em TXT")
    print("5. Balanço de Vendas")
    print("6. Relatório Estatístico")
    print("0. Sair")
    return input("Escolha uma opção: ")

def main():
    sistema = Sistema()
    gerente = Gerente("Nome do Gerente", sistema)

    while True:
        escolha = exibir_menu()

        if escolha == "1":
            avaliado = input("O item foi avaliado? (S/N): ").upper() == 'S'
            trocado = input("O item foi trocado? (S/N): ").upper() == 'S'
            doado = input("O item foi doado? (S/N): ").upper() == 'S'
            novo_item = Item(avaliado=avaliado, trocado=trocado, doado=doado)
            gerente.sistema.adicionar_item(novo_item)
            print("Item adicionado com sucesso.")
        elif escolha == "2":
            data = input("Digite a data da transação (formato YYYY-MM-DD): ")
            tipo = input("Digite o tipo da transação (venda/troca): ").lower()
            categoria = input("Digite a categoria da transação: ")
            produto = input("Digite o produto da transação: ")
            valor = float(input("Digite o valor da transação: "))
            nova_transacao = Transacao(data, tipo, categoria, produto, valor)
            gerente.sistema.realizar_transacao(nova_transacao)
            print("Transação realizada com sucesso.")
        elif escolha == "3":
            gerente.gerar_relatorio_geral()
        elif escolha == "4":
            gerente.exportar_relatorio_txt()
            print("Relatório exportado para 'relatorio.txt'.")
        elif escolha == "5":
            data_inicio = input("Digite a data de início (formato YYYY-MM-DD): ")
            data_fim = input("Digite a data de fim (formato YYYY-MM-DD): ")
            gerente.balanco_vendas(data_inicio, data_fim)
        elif escolha == "6":
            gerente.relatorio_estatistico()
        elif escolha == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
