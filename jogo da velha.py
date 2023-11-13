import tkinter as tk

# Cria a janela principal
janela = tk.Tk()
janela.title('Jogo da Velha')

# Cria uma matriz 3x3 para representar o tabuleiro
tabuleiro = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Cria uma variável para controlar de quem é a vez
vez = 1

# Cria uma função para verificar se alguém ganhou
def verificar_ganhador():
    # Verifica se alguém ganhou na horizontal
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] != 0:
            return tabuleiro[i][0]
    # Verifica se alguém ganhou na vertical
    for i in range(3):
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] != 0:
            return tabuleiro[0][i]
    # Verifica se alguém ganhou na diagonal
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != 0:
        return tabuleiro[0][0]
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != 0:
        return tabuleiro[0][2]
    # Se ninguém ganhou, retorna 0
    return 0

# Cria uma função para atualizar o tabuleiro
def atualizar_tabuleiro(linha, coluna):
    global vez
    # Verifica se a posição está vazia
    if tabuleiro[linha][coluna] == 0:
        # Preenche a posição com o símbolo do jogador atual
        if vez == 1:
            tabuleiro[linha][coluna] = 'X'
            vez = 2
        else:
            tabuleiro[linha][coluna] = 'O'
            vez = 1
        # Atualiza o botão com o símbolo do jogador atual
        botoes[linha][coluna].config(text=tabuleiro[linha][coluna])
        # Verifica se alguém ganhou
        ganhador = verificar_ganhador()
        if ganhador != 0:
            # Exibe uma mensagem de vitória
            if ganhador == 'X':
                tk.messagebox.showinfo('Fim de jogo', 'O jogador 1 venceu!')
            else:
                tk.messagebox.showinfo('Fim de jogo', 'O jogador 2 venceu!')
            # Desabilita todos os botões
            for i in range(3):
                for j in range(3):
                    botoes[i][j].config(state='disabled')
        else:
            # Verifica se o jogo empatou
            if all(tabuleiro[i][j] != 0 for i in range(3) for j in range(3)):
                tk.messagebox.showinfo('Fim de jogo', 'O jogo empatou!')
                # Desabilita todos os botões
                for i in range(3):
                    for j in range(3):
                        botoes[i][j].config(state='disabled')

# Cria uma matriz de botões para representar o tabuleiro
botoes = []
for i in range(3):
    linha = []
    for j in range(3):
        # Cria um botão e adiciona-o à janela
        botao = tk.Button(janela, text='', font=('Arial', 20), width=4, height=2,
                          command=lambda linha=i, coluna=j: atualizar_tabuleiro(linha, coluna))
        botao.grid(row=i, column=j)
        linha.append(botao)
    botoes.append(linha)

# Inicia o loop principal da janela
janela.mainloop()