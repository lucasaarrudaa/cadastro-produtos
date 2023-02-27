import tkinter as tk
from tkinter import ttk
import datetime as dt
import os
from insere_codigo_db import insere
import os
import re

sistema = os.environ
janela = tk.Tk()

lista_tipos = ['1 - Notebook','2 - Acessório Notebook','3 - Acessório Celular','4 - Celular','5 - TV','6 - Eletrônicos']
lista_id_tipos_str = []
lista_id_tipos_int = []

#lista dos tipos(categorias) em numeros inteiros, ou seja, o numero do ID da categoria.
for item_int in lista_tipos:
    item_int = re.sub('[^0-9]','', item_int)
    lista_id_tipos_int.append(int(item_int))

#lista dos tipos(categorias) em forma de string, ou seja, o numero da categoria.
for item_str in lista_tipos:
    item_str = re.sub('[0-9]', '', item_str)
    item_str = re.sub('-', '', item_str)
    item_str = item_str.lstrip()
    lista_id_tipos_str.append(item_str)

lista_guarda_inseridos = []

def inserir_codigo():

    tipo = combobox_selecionar_tipo.get()
    tipo_str = re.sub('[0-9]', '', tipo)
    tipo_str = re.sub('-', '', tipo_str)
    tipo_str = tipo_str.lstrip()
    tipo_id = re.sub('[^0-9]', '', tipo)
    tipo_id.strip()
    tipo_id_int = int(tipo_id)
    descricao = str(entry_descricao.get()).strip().capitalize()
    quantidade = int(entry_quantidade.get().strip())

    while True:
        try:
            if not (0 <= quantidade <= 100000):
                    raise ValueError("Essa quantidade é impossível")
                    break
        except ValueError as e:
            print("Por favor, digite outro valor.", e)
            break

        data_criacao = dt.datetime.now()
        data_criacao = data_criacao.strftime("%Y-%m-%d %H:%M:%S")
        lista_guarda_inseridos.append((f"PRODUTO: {descricao}", f"CATEGORIA: ({tipo_str}, ID: {tipo_id_int})", f"QUANTIDADE: {quantidade}", f"EM: {data_criacao}"))
        global sql
        sql = f"""
                INSERT INTO tabela_produtos
                (usuario, nome, id_categoria, tipo, quantidade, data_criacao)
                VALUES
                ('{sistema['USERNAME']}', '{descricao}', {tipo_id_int}, '{tipo_str}', {quantidade}, '{data_criacao}')
                """
        # insere os dados no banco
        insere(sql)
        break
    else: print("Não foi possível inserir os dados no sistema.")

print(sistema['USERNAME'])
janela.title('Ferramenta de cadastro de produtos')

label_descricao = tk.Label(janela, text='Nome do Produto')
label_descricao.grid(row=1,
                     column=0,
                     padx=10,
                     pady=5,
                     sticky='nswe',
                     columnspan=4)
entry_descricao = tk.Entry(janela)
entry_descricao.grid(row=2,
                     column=0,
                     padx=10,
                     pady=2,
                     sticky='nswe',
                     columnspan=4)

label_tipo_unidade = tk.Label(janela, text='Categoria do Produto')
label_tipo_unidade.grid(row=3,
                        padx=10,
                        pady=10,
                        column=0,
                        sticky='nswe',
                        columnspan=2)

combobox_selecionar_tipo = ttk.Combobox(state="readonly", values=lista_tipos)
combobox_selecionar_tipo.grid(row=3,
                              column=2,
                              padx=10,
                              pady=10,
                              sticky='nswe',
                              columnspan=2)


label_quantidade = tk.Label(janela, text='Quantidade por unidade do Produto')
label_quantidade.grid(row=4,
                      padx=10,
                      pady=10,
                      column=0,
                      columnspan=2,
                      sticky='nswe')
entry_quantidade = tk.Entry(janela)
entry_quantidade.grid(row=4,
                      column=2,
                      columnspan=2,
                      padx=10,
                      pady=10,
                      sticky='nswe')

botao_criar_codigo = tk.Button(janela, text="Criar Código", command=inserir_codigo)
botao_criar_codigo.grid(row=5, column=0, columnspan=4, pady=10, padx=10, sticky='nswe')
janela.mainloop()

if __name__ == '__main__':
    # [print(nome) for nome in lista_guarda_inseridos]
    print(f"Foram inseridos no banco de dados pelo usuário"
          f" {sistema['USERNAME']}, os produtos: ")
    for prod in lista_guarda_inseridos: print(prod)
    print("Encerrando a inserção de produtos no sistema.")


