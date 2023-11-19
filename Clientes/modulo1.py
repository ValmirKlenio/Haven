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

def main():
    cadastrar_item()

if __name__ == "__main__":
    main()
