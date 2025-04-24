import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox

df = pd.read_csv('dados.csv')
vendas = df['vendas'].values
vendedores = df['vendedor'].values

def mostrar_estatisticas():
    media = np.mean(vendas)
    mediana = np.median(vendas)
    minimo = np.min(vendas)
    maximo = np.max(vendas)
    desvio = np.std(vendas)

    estatisticas = (
        f"Média: {media:.2f}\n"
        f"Mediana: {mediana}\n"
        f"Mínimo: {minimo}\n"
        f"Máximo: {maximo}\n"
        f"Desvio Padrão: {desvio:.2f}"
    )
    messagebox.showinfo("Estatísticas", estatisticas)

def grafico_linha():
    plt.plot(vendedores, vendas, marker='o')
    plt.title("Vendas por Vendedor - Linha")
    plt.xlabel("Vendedor")
    plt.ylabel("Vendas")
    plt.grid(True)
    plt.show()

def grafico_barras():
    plt.bar(vendedores, vendas, color='skyblue')
    plt.title("Vendas por Vendedor - Barras")
    plt.xlabel("Vendedor")
    plt.ylabel("Vendas")
    plt.show()

def grafico_pizza():
    plt.pie(vendas, labels=vendedores, autopct='%1.1f%%', startangle=90)
    plt.title("Distribuição de Vendas - Pizza")
    plt.axis('equal')
    plt.show()

def grafico_dispersao():
    plt.scatter(vendedores, vendas, color='green')
    plt.title("Vendas por Vendedor - Dispersão")
    plt.xlabel("Vendedor")
    plt.ylabel("Vendas")
    plt.show()

def grafico_barras_horizontal():
    plt.barh(vendedores, vendas, color='coral')
    plt.title("Vendas por Vendedor - Barras Horizontais")
    plt.xlabel("Vendas")
    plt.ylabel("Vendedor")
    plt.show()

janela = tk.Tk()
janela.title("Sistema de Vendas com Gráficos")

tk.Button(janela, text="Gráfico de Linha", command=grafico_linha, width=30).pack(pady=5)
tk.Button(janela, text="Gráfico de Barras", command=grafico_barras, width=30).pack(pady=5)
tk.Button(janela, text="Gráfico de Pizza", command=grafico_pizza, width=30).pack(pady=5)
tk.Button(janela, text="Gráfico de Dispersão", command=grafico_dispersao, width=30).pack(pady=5)
tk.Button(janela, text="Gráfico de Barras Horizontais", command=grafico_barras_horizontal, width=30).pack(pady=5)
tk.Button(janela, text="Mostrar Estatísticas", command=mostrar_estatisticas, width=30).pack(pady=10)

janela.mainloop()
