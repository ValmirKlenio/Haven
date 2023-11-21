import csv
import urllib.request

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

    # Salvando em CSV
    salvar_em_csv([novo_item], 'itens.csv')
    print("Dados salvos em itens.csv")

    # Salvando em TXT
    salvar_em_txt([novo_item], 'itens.txt')
    print("Dados salvos em itens.txt")

def salvar_em_csv(itens, nome_arquivo):
    with open(nome_arquivo, 'w', newline='') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)
        escritor_csv.writerow(["Código", "Nome", "Descrição", "Condição", "Foto"])
        for item in itens:
            escritor_csv.writerow([item.codigo, item.nome, item.descricao, item.condicao, item.foto])

def salvar_em_txt(itens, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo_txt:
        for item in itens:
            arquivo_txt.write(f"Código: {item.codigo}\n")
            arquivo_txt.write(f"Nome: {item.nome}\n")
            arquivo_txt.write(f"Descrição: {item.descricao}\n")
            arquivo_txt.write(f"Condição: {item.condicao}\n")
            if item.foto:
                arquivo_txt.write(f"Foto: {item.foto}\n")
            arquivo_txt.write("\n")

def main():
    cadastrar_item()

if __name__ == "__main__":
    main()
