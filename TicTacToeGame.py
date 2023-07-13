import tkinter
from tkinter import *
from tkinter import ttk

#cores----------------------------

co0 = "#FFFFFF"  # branco
co1 = "#333333"  # preto pesado
co2 = "#fcc058"  # laranja
co3 = "#38576b"  # valor / value
co4 = "#3297a8"   # azul
co5 = "#fff873"   # amarelo
co6 = "#fcc058"  # laranja
co7 = "#e85151"   # vermelho
co8 = co4   # + verde
co10 ="#fcfbf7"
fundo = "#3b3b3b" # preto normal

#criação da janela principal--------------

tamanhoJanela = '370x390'
janela = Tk()
janela.title('Jogo da Velha - Trabalho Elson')
janela.geometry(tamanhoJanela)
janela.configure(bg=fundo)


#criando frame de cima e do corpo ------------------------

frame_cima = Frame(janela, width= 350, height= 100, bg=co1, relief="raised")
frame_cima.grid(row=0, column= 0, sticky=NW, padx= 10, pady= 10)

frame_corpo = Frame(janela, width= 350, height= 270, bg=fundo, relief="flat")
frame_corpo.grid(row=1, column= 0, sticky=N)

#configurando o frame de cima -----------------------------

app_x = Label(frame_cima, text= 'X', height= 1, relief='flat', anchor= 'center', font=('Ivy 40 bold'), bg= co1, fg=co7)
app_x.place(x=65, y=10)

app_x = Label(frame_cima, text= 'Jogador 1', height= 1, relief='flat', anchor= 'center', font=('Ivy 8 bold'), bg= co1, fg=co0)
app_x.place(x=56, y=70)

app_x_pontos = Label(frame_cima, text= '0', height= 1, relief='flat', anchor= 'center', font=('Ivy 30 bold'), bg= co1, fg=co0)
app_x_pontos.place(x=130, y=20)


app_separador = Label(frame_cima, text= ':', height= 1, relief='flat', anchor= 'center', font=('Ivy 30 bold'), bg= co1, fg=co0)
app_separador.place(x=170, y=20)



app_o = Label(frame_cima, text= 'O', height= 1, relief='flat', anchor= 'center', font=('Ivy 40 bold'), bg= co1, fg=co8)
app_o.place(x=255, y=10)

app_o = Label(frame_cima, text= 'Jogador 2', height= 1, relief='flat', anchor= 'center', font=('Ivy 8 bold'), bg= co1, fg=co0)
app_o.place(x=248, y=70)

app_o_pontos = Label(frame_cima, text= '0', height= 1, relief='flat', anchor= 'center', font=('Ivy 30 bold'), bg= co1, fg=co0)
app_o_pontos.place(x=201, y=20)






# Criando Lógica do Jogo


jogador_1 = 'X'
jogador_2 = 'O'

pontuacao_1 = 0
pontuacao_2 = 0

tabela = [['1','2','3'] , ['4','5','6'] , ['7','8','9']]


jogando = 'X'
jogar = ''
contador = 0
contador_rodadas = 0


def iniciar_jogo():
    # pra controlar o jogo
    def controlar(i):
        global jogando
        global contador
        global jogar

        if i == str(1):
            #verificando se a posição está vazia ou não
            if b_0['text'] == '':
                #verificando quem está jogando pra definir a cor do símbolo
                if jogando == 'X':
                    cor = co7
                elif jogando == 'O':
                    cor = co8
                # definindo a cor do texto do botão e marcando com o símbolo do jogador atual
                b_0['fg'] = cor
                b_0['text'] = jogando
                tabela[0][0] = jogando
                # verificando quem está jogando para a troca dos jogadores
                if jogando == 'X':
                    jogando = 'O'
                    jogar = 'Jogador 1'
                else:
                    jogando = 'X'
                    jogar = 'Jogador 2'
                #incrementar contador para a próxima rodada
                contador += 1


        if i == str(2):
            #verificando se a posição está vazia ou não
            if b_1['text'] == '':
                #verificando quem está jogando pra definir a cor do símbolo
                if jogando == 'X':
                    cor = co7
                elif jogando == 'O':
                    cor = co8
                # definindo a cor do texto do botão e marcando com o símbolo do jogador atual
                b_1['fg'] = cor
                b_1['text'] = jogando
                tabela[0][1] = jogando
                # verificando quem está jogando para a troca dos jogadores
                if jogando == 'X':
                    jogando = 'O'
                    jogar = 'Jogador 1'
                else:
                    jogando = 'X'
                    jogar = 'Jogador 2'
                #incrementar contador para a próxima rodada
                contador += 1

        if i == str(3):
            #verificando se a posição está vazia ou não
            if b_2['text'] == '':
                #verificando quem está jogando pra definir a cor do símbolo
                if jogando == 'X':
                    cor = co7
                elif jogando == 'O':
                    cor = co8
                # definindo a cor do texto do botão e marcando com o símbolo do jogador atual
                b_2['fg'] = cor
                b_2['text'] = jogando
                tabela[0][2] = jogando
                # verificando quem está jogando para a troca dos jogadores
                if jogando == 'X':
                    jogando = 'O'
                    jogar = 'Jogador 1'
                else:
                    jogando = 'X'
                    jogar = 'Jogador 2'
                #incrementar contador para a próxima rodada
                contador += 1
        
        if i == str(4):
            #verificando se a posição está vazia ou não
            if b_3['text'] == '':
                #verificando quem está jogando pra definir a cor do símbolo
                if jogando == 'X':
                    cor = co7
                elif jogando == 'O':
                    cor = co8
                # definindo a cor do texto do botão e marcando com o símbolo do jogador atual
                b_3['fg'] = cor
                b_3['text'] = jogando
                tabela[1][0] = jogando
                # verificando quem está jogando para a troca dos jogadores
                if jogando == 'X':
                    jogando = 'O'
                    jogar = 'Jogador 1'
                else:
                    jogando = 'X'
                    jogar = 'Jogador 2'
                #incrementar contador para a próxima rodada
                contador += 1

        if i == str(5):
            #verificando se a posição está vazia ou não
            if b_4['text'] == '':
                #verificando quem está jogando pra definir a cor do símbolo
                if jogando == 'X':
                    cor = co7
                elif jogando == 'O':
                    cor = co8
                # definindo a cor do texto do botão e marcando com o símbolo do jogador atual
                b_4['fg'] = cor
                b_4['text'] = jogando
                tabela[1][1] = jogando
                # verificando quem está jogando para a troca dos jogadores
                if jogando == 'X':
                    jogando = 'O'
                    jogar = 'Jogador 1'
                else:
                    jogando = 'X'
                    jogar = 'Jogador 2'
                #incrementar contador para a próxima rodada
                contador += 1

        if i == str(6):
            #verificando se a posição está vazia ou não
            if b_5['text'] == '':
                #verificando quem está jogando pra definir a cor do símbolo
                if jogando == 'X':
                    cor = co7
                elif jogando == 'O':
                    cor = co8
                # definindo a cor do texto do botão e marcando com o símbolo do jogador atual
                b_5['fg'] = cor
                b_5['text'] = jogando
                tabela[1][2] = jogando
                # verificando quem está jogando para a troca dos jogadores
                if jogando == 'X':
                    jogando = 'O'
                    jogar = 'Jogador 1'
                else:
                    jogando = 'X'
                    jogar = 'Jogador 2'
                #incrementar contador para a próxima rodada
                contador += 1
                #Apos o contador ser igual ou maior que 5, verifica se há algum vencedor
                    
        if i == str(7):
            #verificando se a posição está vazia ou não
            if b_6['text'] == '':
                #verificando quem está jogando pra definir a cor do símbolo
                if jogando == 'X':
                    cor = co7
                elif jogando == 'O':
                    cor = co8
                # definindo a cor do texto do botão e marcando com o símbolo do jogador atual
                b_6['fg'] = cor
                b_6['text'] = jogando
                tabela[2][0] = jogando
                # verificando quem está jogando para a troca dos jogadores
                if jogando == 'X':
                    jogando = 'O'
                    jogar = 'Jogador 1'
                else:
                    jogando = 'X'
                    jogar = 'Jogador 2'
                #incrementar contador para a próxima rodada
                contador += 1

        if i == str(8):
            #verificando se a posição está vazia ou não
            if b_7['text'] == '':
                #verificando quem está jogando pra definir a cor do símbolo
                if jogando == 'X':
                    cor = co7
                elif jogando == 'O':
                    cor = co8
                # definindo a cor do texto do botão e marcando com o símbolo do jogador atual
                b_7['fg'] = cor
                b_7['text'] = jogando
                tabela[2][1] = jogando
                # verificando quem está jogando para a troca dos jogadores
                if jogando == 'X':
                    jogando = 'O'
                    jogar = 'Jogador 1'
                else:
                    jogando = 'X'
                    jogar = 'Jogador 2'
                #incrementar contador para a próxima rodada
                contador += 1
                #Apos o contador ser igual ou maior que 5, verifica se há algum vencedor

        if i == str(9):
            #verificando se a posição está vazia ou não
            if b_8['text'] == '':
                #verificando quem está jogando pra definir a cor do símbolo
                if jogando == 'X':
                    cor = co7
                elif jogando == 'O':
                    cor = co8
                # definindo a cor do texto do botão e marcando com o símbolo do jogador atual
                b_8['fg'] = cor
                b_8['text'] = jogando
                tabela[2][2] = jogando
                # verificando quem está jogando para a troca dos jogadores
                if jogando == 'X':
                    jogando = 'O'
                    jogar = 'Jogador 1'
                else:
                    jogando = 'X'
                    jogar = 'Jogador 2'
                #incrementar contador para a próxima rodada
                contador += 1
        
        #Apos o contador ser igual ou maior que 5, verifica se há algum vencedor
        if contador >= 5:
            #linhas
            if tabela[0][0] == tabela[0][1] == tabela[0][2] != '':
                vencedor(jogando)
            elif tabela[1][0] == tabela[1][1] == tabela[1][2] != '':
                vencedor(jogando)
            elif tabela[2][0] == tabela[2][1] == tabela[2][2] != '':
                vencedor(jogando)            
            #colunas
            if tabela[0][0] == tabela[1][0] == tabela[2][0] != '':
                vencedor(jogando)
            elif tabela[0][1] == tabela[1][1] == tabela[2][1] != '':
                vencedor(jogando)
            elif tabela[0][2] == tabela[1][2] == tabela[2][2] != '':
                vencedor(jogando)
            #diagonal (to me confundindo todo)
            if tabela[0][0] == tabela[1][1] == tabela[2][2] != '':
                vencedor(jogando)
            elif tabela[0][2] == tabela[1][1] == tabela[2][0] != '':
                vencedor(jogando)
            #Empate
            if contador >= 9:
                 vencedor('VELHA!')
            
    # pra determinar o vencedor
    def vencedor(i):
        global pontuacao_1
        global pontuacao_2
        global tabela
        global contador_rodadas
        global contador

        #bloqueando o uso dos botões
        b_0['state']='disable'
        b_1['state']='disable'
        b_2['state']='disable'
        b_3['state']='disable'
        b_4['state']='disable'
        b_5['state']='disable'
        b_6['state']='disable'
        b_7['state']='disable'
        b_8['state']='disable'

        app_vencedor = Label(frame_corpo, text= 'Vencedor',width = 17, relief='flat', anchor= 'center', font=('Ivy 13 bold'), bg= co1, fg=co0)
        app_vencedor.place(x=90, y=0)    

        if i == 'X':
            pontuacao_2+=1
            app_vencedor ['text'] = 'Circulo Venceu!'
            app_o_pontos ['text'] = pontuacao_2
        if i == 'O':
            pontuacao_1+=1
            app_vencedor ['text'] = 'Cruz Venceu!'
            app_x_pontos ['text'] = pontuacao_1
        if i == 'VELHA!':
            app_vencedor ['text'] = 'Velha!'
        
        def start():
            global tabela
            global contador
            global contador_rodadas
            global pontuacao_1
            global pontuacao_2
            #limpando os botoes
            b_0['text']=''
            b_1['text']=''
            b_2['text']=''
            b_3['text']=''
            b_4['text']=''
            b_5['text']=''
            b_6['text']=''
            b_7['text']=''
            b_8['text']=''
            #limpando os botoes
            b_0['state']='normal'
            b_1['state']='normal'
            b_2['state']='normal'
            b_3['state']='normal'
            b_4['state']='normal'
            b_5['state']='normal'
            b_6['state']='normal'
            b_7['state']='normal'
            b_8['state']='normal'
            
            app_vencedor.destroy()
            b_jogar.destroy()
                
        b_jogar = Button(frame_corpo, command=start , text= 'Próxima rodada',height=1, overrelief=RIDGE, relief ='raised',font=('Ivy 10 bold'),bg=co0, fg=fundo )
        b_jogar.place(x=123,y=235)
        
        def jogo_acabou():
            b_jogar.destroy()
            app_vencedor.destroy()
            terminar()
        

        if contador_rodadas >= 5 or pontuacao_1 + pontuacao_2 >= 5 or pontuacao_1 == 3 or pontuacao_2 == 3 :
            jogo_acabou()
        else:
            contador_rodadas += 1
            tabela = [['1','2','3'] , ['4','5','6'] , ['7','8','9']]
            contador = 0
        

    # pra terminar o jogo  
    def terminar():
        global tabela
        global contador_rodadas
        global pontuacao_1
        global pontuacao_2
        global contador
        
        tabela = [['1','2','3'],['4','5','6'],['7','8','9']]
        contador_rodadas = 0
        pontuacao_1 = 0
        pontuacao_2 = 0
        contador = 0

        #bloqueando o uso dos botões
        b_0['state']='disable'
        b_1['state']='disable'
        b_2['state']='disable'
        b_3['state']='disable'
        b_4['state']='disable'
        b_5['state']='disable'
        b_6['state']='disable'
        b_7['state']='disable'
        b_8['state']='disable'

        
        app_fim = Label(frame_corpo, text= 'Jogo Acabou! Verifique o Ganhador acima!', relief='flat', anchor= 'center', font=('Ivy 13 bold'), bg= co1, fg=co0)
        app_fim.place(x=10, y=0) 

        def try_again():
            app_x_pontos ['text'] = '0'
            app_o_pontos ['text'] = '0'
            app_fim.destroy()
            b_jogar.destroy()
            ## chamando a funcao de reiniciar o jogo
            iniciar_jogo()
        #botao de jogar de novo
        b_jogar = Button(frame_corpo, command=try_again , text= 'Jogar de novo',height=1, overrelief=RIDGE, relief ='raised',font=('Ivy 10 bold'),bg=co0, fg=fundo )
        b_jogar.place(x=128,y=235)



        pass


    #configurando o frame do corpo -----------------------------

    ###### linhas verticais


    app_linhasv = Label(frame_corpo, text= '',height=26,relief='flat',pady=5, anchor='center', font=('Ivy 5 bold'),bg=co0, fg=co0 )
    app_linhasv.place(x=130,y=30)

    app_linhasv = Label(frame_corpo, text= '',height=26,relief='flat',pady=5, anchor='center', font=('Ivy 5 bold'),bg=co0, fg=co0 )
    app_linhasv.place(x=220,y=30)



    ###### linhas horizontais


    app_linhash = Label(frame_corpo, text= '',width=220,relief='flat',padx=2,pady= 0, anchor='center', font=('Ivy 1 bold'),bg=co0, fg=co0 )
    app_linhash.place(x=63,y=80)

    app_linhash = Label(frame_corpo, text= '',width=220,relief='flat',padx=2,pady= 0,  anchor='center', font=('Ivy 1 bold'),bg=co0, fg=co0 )
    app_linhash.place(x=63,y=160)






    ###### criando os botões de suas respectivas linhas 

    #linha 0

    b_0 = Button(frame_corpo,command = lambda:controlar('1'), text= '',width=3,relief='flat',padx=2,pady= 0, anchor='center', font=('Ivy 20 bold'),bg=fundo, fg=fundo )
    b_0.place(x=65,y=25)

    b_1 = Button(frame_corpo,command = lambda:controlar('2'), text= '',width=4,relief='flat',padx=2,pady= 0, anchor='center', font=('Ivy 20 bold'),bg=fundo, fg=fundo )
    b_1.place(x=138,y=25)

    b_2 = Button(frame_corpo,command = lambda:controlar('3'), text= '',width=3,relief='flat',padx=2,pady= 0, anchor='center', font=('Ivy 20 bold'),bg=fundo, fg=fundo )
    b_2.place(x=227,y=25)


    #linha 1

    b_3 = Button(frame_corpo,command = lambda:controlar('4'), text= '', width=3, height=1, relief='flat', padx=2, pady= 0, anchor='center', font=('Ivy 23 bold'),bg=fundo, fg=fundo )
    b_3.place(x=61,y=92)

    b_4 = Button(frame_corpo,command = lambda:controlar('5'), text= '', width=3, height=1, relief='flat', padx=2, pady= 0, anchor='center', font=('Ivy 26 bold'),bg=fundo, fg=fundo )
    b_4.place(x=140,y=88)

    b_5 = Button(frame_corpo,command = lambda:controlar('6'), text= '', width=3, height=1, relief='flat', padx=2, pady= 0, anchor='center', font=('Ivy 23 bold'),bg=fundo, fg=fundo )
    b_5.place(x=227,y=92)


    #linha 2

    b_6 = Button(frame_corpo,command = lambda:controlar('7'), text= '',width=3,relief='flat',padx=2,pady= 0, anchor='center', font=('Ivy 20 bold'),bg=fundo, fg=fundo )
    b_6.place(x=65,y=170)

    b_7 = Button(frame_corpo,command = lambda:controlar('8'), text= '',width=4,relief='flat',padx=2,pady= 0, anchor='center', font=('Ivy 20 bold'),bg=fundo, fg=fundo )
    b_7.place(x=138,y=170)

    b_8 = Button(frame_corpo,command = lambda:controlar('9'), text= '',width=3,relief='flat',padx=2,pady= 0, anchor='center', font=('Ivy 20 bold'),bg=fundo, fg=fundo )
    b_8.place(x=227,y=170)

# Botão de jogar

b_jogar = Button(frame_corpo, command=iniciar_jogo , text= 'Jogar',width=10,height=1, overrelief=RIDGE, relief ='raised',font=('Ivy 10 bold'),bg=co0, fg=fundo )
b_jogar.place(x=133,y=235)



janela.mainloop()
