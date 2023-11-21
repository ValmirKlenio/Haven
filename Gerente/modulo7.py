import csv
import urllib.request

class Item:
    codigo = 1

    def __init__(self, nome, descricao, condicao, foto, avaliado=False, trocado=False, doado=False):
        self.codigo = Item.codigo
        Item.codigo += 1
        self.nome = nome
        self.descricao = descricao
        self.condicao = condicao
        self.foto = foto
        self.avaliado = avaliado
        self.trocado = trocado
        self.doado = doado

    def exibir_detalhes(self):
        print(f"Código: {self.codigo}")
        print(f"Nome: {self.nome}")
        print(f"Descrição: {self.descricao}")
        print(f"Condição: {self.condicao}")
        if self.foto:
            print(f"Foto: {self.foto}")
        print(f"Avaliado: {self.avaliado}")
        print(f"Trocado: {self.trocado}")
        print(f"Doado: {self.doado}")
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

    return novo_item

def avaliar_item(item):
    if not item.avaliado:
        print(f"Item {item.codigo} foi avaliado com sucesso.")
        item.avaliado = True
    else:
        print(f"Item {item.codigo} já foi avaliado.")

def trocar_item(item):
    if item.avaliado and not item.trocado:
        print(f"Item {item.codigo} foi trocado com sucesso.")
        item.trocado = True
    elif not item.avaliado:
        print(f"Item {item.codigo} precisa ser avaliado antes de ser trocado.")
    else:
        print(f"Item {item.codigo} já foi trocado anteriormente.")

def doar_item(item):
    if item.avaliado and not item.trocado and not item.doado:
        print(f"Item {item.codigo} foi doado com sucesso.")
        item.doado = True
    elif not item.avaliado:
        print(f"Item {item.codigo} precisa ser avaliado antes de ser doado.")
    elif item.trocado:
        print(f"Item {item.codigo} já foi trocado e não pode ser doado.")
    else:
        print(f"Item {item.codigo} já foi doado anteriormente.")

def salvar_em_csv(itens, nome_arquivo):
    with open(nome_arquivo, 'w', newline='') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)
        escritor_csv.writerow(["Código", "Nome", "Descrição", "Condição", "Foto", "Avaliado", "Trocado", "Doado"])
        for item in itens:
            escritor_csv.writerow([item.codigo, item.nome, item.descricao, item.condicao,
                                   item.foto, item.avaliado, item.trocado, item.doado])

def salvar_em_txt(itens, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo_txt:
        for item in itens:
            arquivo_txt.write(f"Código: {item.codigo}\n")
            arquivo_txt.write(f"Nome: {item.nome}\n")
            arquivo_txt.write(f"Descrição: {item.descricao}\n")
            arquivo_txt.write(f"Condição: {item.condicao}\n")
            if item.foto:
                arquivo_txt.write(f"Foto: {item.foto}\n")
            arquivo_txt.write(f"Avaliado: {item.avaliado}\n")
            arquivo_txt.write(f"Trocado: {item.trocado}\n")
            arquivo_txt.write(f"Doado: {item.doado}\n")
            arquivo_txt.write("\n")

def gerar_relatorio(itens):
    print("\nRelatório de Atividade do Sistema:")
    print(f"Número total de itens cadastrados: {len(itens)}")
    print(f"Número de itens avaliados: {sum(1 for item in itens if item.avaliado)}")
    print(f"Número de itens trocados: {sum(1 for item in itens if item.trocado)}")
    print(f"Número de itens doados: {sum(1 for item in itens if item.doado)}")

    vendas = sum(1 for item in itens if item.avaliado and not item.trocado and not item.doado)
    trocas = sum(1 for item in itens if item.trocado)

    print("\nRelatório de Vendas e Trocas:")
    print(f"Número total de vendas: {vendas}")
    print(f"Número total de trocas: {trocas}")

    exportar_relatorio(itens, 'relatorio_completo.txt')
    print("Relatório exportado para relatorio_completo.txt")

def exportar_relatorio(itens, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo_txt:
        arquivo_txt.write("Relatório Completo\n\n")
        arquivo_txt.write(f"Número total de itens cadastrados: {len(itens)}\n")
        arquivo_txt.write(f"Número de itens avaliados: {sum(1 for item in itens if item.avaliado)}\n")
        arquivo_txt.write(f"Número de itens trocados: {sum(1 for item in itens if item.trocado)}\n")
        arquivo_txt.write(f"Número de itens doados: {sum(1 for item in itens if item.doado)}\n")

        vendas = sum(1 for item in itens if item.avaliado and not item.trocado and not item.doado)
        trocas = sum(1 for item in itens if item.trocado)

        arquivo_txt.write("\nRelatório de Vendas e Trocas\n\n")
        arquivo_txt.write(f"Número total de vendas: {vendas}\n")
        arquivo_txt.write(f"Número total de trocas: {trocas}\n")

if __name__ == "__main__":
    itens = []

    while True:
        print("\n=== Menu ===")
        print("1. Cadastrar Item")
        print("2. Avaliar Item")
        print("3. Trocar Item")
        print("4. Doar Item")
        print("5. Exibir Relatório")
        print("6. Sair")

        escolha = input("Escolha uma opção (1 a 6): ")

        if escolha == '1':
            novo_item = cadastrar_item()
            itens.append(novo_item)
        elif escolha == '2':
            codigo_item = int(input("Digite o código do item a ser avaliado: "))
            item_selecionado = next((item for item in itens if item.codigo == codigo_item), None)
            if item_selecionado:
                avaliar_item(item_selecionado)
            else:
                print(f"Item com código {codigo_item} não encontrado.")
        elif escolha == '3':
            codigo_item = int(input("Digite o código do item a ser trocado: "))
            item_selecionado = next((item for item in itens if item.codigo == codigo_item), None)
            if item_selecionado:
                trocar_item(item_selecionado)
            else:
                print(f"Item com código {codigo_item} não encontrado.")
        elif escolha == '4':
            codigo_item = int(input("Digite o código do item a ser doado: "))
            item_selecionado = next((item for item in itens if item.codigo == codigo_item), None)
            if item_selecionado:
                doar_item(item_selecionado)
            else:
                print(f"Item com código {codigo_item} não encontrado.")
        elif escolha == '5':
            gerar_relatorio(itens)
        elif escolha == '6':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")
