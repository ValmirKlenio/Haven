import csv

class Item:
    def __init__(self, nome, descricao, creditos):
        self.nome = nome
        self.descricao = descricao
        self.creditos = creditos

def exibir_catalogo(itens):
    print("Catálogo de Itens Disponíveis:")
    for i, item in enumerate(itens, start=1):
        print(f"{i}. {item.nome} - {item.descricao} (Créditos: {item.creditos})")

def salvar_em_csv(itens, nome_arquivo):
    with open(nome_arquivo, 'w', newline='') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)
        escritor_csv.writerow(["Nome", "Descrição", "Créditos"])
        for item in itens:
            escritor_csv.writerow([item.nome, item.descricao, item.creditos])

def salvar_em_txt(itens, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo_txt:
        for item in itens:
            arquivo_txt.write(f"{item.nome} - {item.descricao} (Créditos: {item.creditos})\n")

def main():
    item1 = Item("Livro", "História interessante", 5)
    item2 = Item("Brinquedo", "Para todas as idades", 3)
    item3 = Item("Roupas", "Diversos tamanhos e estilos", 7)

    catalogo_itens = [item1, item2, item3]

    exibir_catalogo(catalogo_itens)

    # Salvando em CSV
    salvar_em_csv(catalogo_itens, 'catalogo.csv')
    print("Dados salvos em catalogo.csv")

    # Salvando em TXT
    salvar_em_txt(catalogo_itens, 'catalogo.txt')
    print("Dados salvos em catalogo.txt")

if __name__ == "__main__":
    main()
