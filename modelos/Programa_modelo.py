#coding<utf-8>
from tkinter import *
from tkinter import ttk, Canvas
from tkcalendar import Calendar, DateEntry
from tkinter import messagebox
import sqlite3
import webbrowser
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image
#import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure


root = Tk()

class Funcs:
    # Criação de banco de dados
    def conecta_db(self):
        self.conn = sqlite3.connect("contas.db")
        self.cursor = self.conn.cursor()
    
    def desconecta_db(self):
        self.conn.close()
    
    def cria_db(self):
        self.conecta_db()
        # Criando as tabelas
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS contas (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                descricao TEXT,
                valor REAL(6) NOT NULL,
                data timestamp NOT NULL,
                categoria TEXT,
                comentario TEXT,
                tipo TEXT
                    );
                """)
        # Cria tabela categorias de receitas
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS categorias (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                categoria TEXT
                    );
                """)
        # Cria tabela categorias de despesas
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS categorias01 (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                categoria TEXT
                    );
                """)
    
        self.conn.commit()
        self.desconecta_db()
    

    def limpa_aba_01(self):
        self.entry_id_aba_01.delete(0, END)
        self.entry_descricao_aba_01.delete(0, END)
        self.entry_valor_aba_01.delete(0, END)
        self.entry_data_aba_01.delete(0, END)
        self.entry_categoria_aba_01.delete(0, END)
        self.entry_comentario_aba_01.delete(0, END)
    

    def limpa_aba_02(self):
        self.entry_id_aba_02.delete(0, END)
        self.entry_descricao_aba_02.delete(0, END)
        self.entry_valor_aba_02.delete(0, END)
        self.entry_data_aba_02.delete(0, END)
        self.entry_categoria_aba_02.delete(0, END)
        self.entry_comentario_aba_02.delete(0, END)


    def insere_receitas_na_lista(self):
        self.treeview_aba_01.delete(*self.treeview_aba_01.get_children())
        self.conecta_db()
        lista = self.cursor.execute(""" SELECT id, descricao, valor, data, categoria, comentario, tipo FROM contas
                    ORDER BY data DESC; """)
        for i in lista:
            #print(i)
            if i[6] == "Receita":
                self.treeview_aba_01.insert("", END, values=i)

        self.desconecta_db()
    
    def insere_despesas_na_lista(self):
        self.treeview_aba_02.delete(*self.treeview_aba_02.get_children())
        self.conecta_db()
        lista = self.cursor.execute(""" SELECT id, descricao, valor, data, categoria, comentario, tipo FROM contas
                    ORDER BY data DESC; """)
        for linha in lista:
            if linha[6] == "Despesa":
                self.treeview_aba_02.insert("", END, values=linha)

        self.desconecta_db()
    
    def variaveis_aba_03(self):
        self.data_inicio = self.entry_data_inicio_aba_03.get()
        self.data_fim = self.entry_data_fim_aba_03.get()


    def insere_resumo_na_lista(self):
        self.treeview_aba_03.delete(*self.treeview_aba_03.get_children())
        self.variaveis_aba_03()
        self.conecta_db()
        lista = self.cursor.execute(""" SELECT id, descricao, valor, data, categoria, comentario, tipo FROM contas
                    ORDER BY data DESC; """)
        
        despesa = 0
        receita = 0
        for linha in lista:
            if linha[3] >= self.data_inicio and linha[3] <= self.data_fim:
                self.treeview_aba_03.insert("", END, values=linha)
                if linha[6] == "Despesa":
                    despesa += linha[2]
                elif linha[6] == "Receita":
                    receita += linha[2]

        saldo = receita - despesa
        self.lb_saida_valor_resumo_aba_03['text'] = f"R$ {despesa:.2f}"
        self.lb_entrada_valor_resumo_aba_03['text'] = f"R$ {receita:.2f}"
        self.lb_saldo_valor_resumo_aba_03['text'] = f"R$ {saldo:.2f}"
        self.desconecta_db()

        self.plotar_grafico()

    def valida_valor(self, numero):
        numero = numero.strip()
        if numero.isnumeric():
            return float(numero)
        else:
            c = 0
            for i in numero:
                if i in ",.":
                    c += 1
            if c:
                numero = numero.replace(",", ".")
                return float(numero)
            else:
                return False

    def variaveis_receita(self):
        self.ide = self.entry_id_aba_01.get()
        self.descricao = self.entry_descricao_aba_01.get()
        self.valor = self.valida_valor(self.entry_valor_aba_01.get())
        self.data = self.entry_data_aba_01.get()
        self.categoria = self.entry_categoria_aba_01.get()
        self.comentario = self.entry_comentario_aba_01.get()
        self.tipo = "Receita"
    
    def variaveis_despesa(self):
        self.ide1 = self.entry_id_aba_02.get()
        self.descricao1 = self.entry_descricao_aba_02.get()
        self.valor1 = self.valida_valor(self.entry_valor_aba_02.get())
        self.data1 = self.entry_data_aba_02.get()
        self.categoria1 = self.entry_categoria_aba_02.get()
        self.comentario1 = self.entry_comentario_aba_02.get()
        self.tipo1 = "Despesa"

    def adiciona_receita(self):
        self.variaveis_receita()
        if self.descricao and self.valor and self.data and self.categoria:
            self.conecta_db()
            self.cursor.execute("""INSERT INTO contas 
                (descricao, valor, data, categoria, comentario, tipo)
                VALUES (?,?,?,?,?,?)""",(self.descricao, self.valor, self.data, self.categoria, self.comentario, self.tipo))

            self.conn.commit()
            self.desconecta_db()
            self.limpa_aba_01()
            self.soma_receita()
            self.insere_receitas_na_lista()
        else:
            messagebox.showerror("ERRO!", "É preciso preencher todas as casas antes de Adicionar.")
    
    def adiciona_despesa(self):
        self.variaveis_despesa()
        if self.descricao1 and self.valor1 and self.data1 and self.categoria1:
            self.conecta_db()
            self.cursor.execute("""INSERT INTO contas
                (descricao, valor, data, categoria, comentario, tipo)
                VALUES (?,?,?,?,?,?)""",(self.descricao1, self.valor1, self.data1, self.categoria1, self.comentario1, self.tipo1))

            self.conn.commit()
            self.desconecta_db()
            self.limpa_aba_02()
            self.soma_despesa()
            self.insere_despesas_na_lista()
        else:
            messagebox.showerror("ERRO!", "É preciso preencher todas as casas antes de Adicionar.")
    

    def clique_duplo_aba_01(self, event):
        self.limpa_aba_01()
        self.treeview_aba_01.selection()
        for linha in self.treeview_aba_01.selection():
            col1, col2, col3, col4, col5, col6, col7 = self.treeview_aba_01.item(linha, "values")
            self.entry_id_aba_01.insert(END, col1)
            self.entry_descricao_aba_01.insert(END, col2)
            self.entry_valor_aba_01.insert(END, col3)
            self.entry_data_aba_01.insert(END, col4)
            self.entry_categoria_aba_01.insert(END, col5)
            self.entry_comentario_aba_01.insert(END, col6)
    
    def clique_duplo_aba_02(self, event):
        self.limpa_aba_02()
        treeview = self.treeview_aba_02.selection()
        for linha in treeview:
            col1, col2, col3, col4, col5, col6, col7 = self.treeview_aba_02.item(linha, "values")
            self.entry_id_aba_02.insert(END, col1)
            self.entry_descricao_aba_02.insert(END, col2)
            self.entry_valor_aba_02.insert(END, col3)
            self.entry_data_aba_02.insert(END, col4)
            self.entry_categoria_aba_02.insert(END, col5)
            self.entry_comentario_aba_02.insert(END, col6)


    def atualiza_receita(self):
        self.variaveis_receita()
               
        if self.ide and self.descricao and self.valor and self.data and self.categoria:
            self.conecta_db()


            self.cursor.execute(""" UPDATE contas SET descricao=?, valor=?, data=?, categoria=?, comentario=?, tipo=?
                            WHERE id=?""",(self.descricao, self.valor, self.data, self.categoria, self.comentario, self.tipo, self.ide))
            self.conn.commit()
            self.desconecta_db()
            self.insere_receitas_na_lista()
            self.soma_receita()
            self.limpa_aba_01()
        else:
            messagebox.showerror("ERRO!", "É preciso selecionar um registro para Atualizar.")
    

    def atualiza_despesa(self):
        self.variaveis_despesa()

        if self.ide1 and self.descricao1 and self.valor1 and self.data1 and self.categoria1:
            self.conecta_db()

            self.cursor.execute(""" UPDATE contas SET descricao=?, valor=?, data=?, categoria=?, comentario=?, tipo=?
                            WHERE id=?""",(self.descricao1, self.valor1, self.data1, self.categoria1, self.comentario1, self.tipo1, self.ide1))
            self.conn.commit()
            self.desconecta_db()
            self.insere_despesas_na_lista()
            self.soma_despesa()
            self.limpa_aba_02()
        else:
            messagebox.showerror("ERRO!", "É preciso selecionar um registro para Atualizar.")
    

    def deleta_receita(self):
        self.variaveis_receita()
        #print(self.ide)
        if self.ide:
            self.conecta_db()
            self.cursor.execute("""DELETE FROM contas WHERE id = ? """, (self.ide,))
            self.conn.commit()
            self.desconecta_db()
            self.insere_receitas_na_lista()
            self.soma_receita()
            self.limpa_aba_01()
        else:
            messagebox.showerror("ERRO!", "É preciso selecionar um registro para deletar.")


    def deleta_despesa(self):
        self.variaveis_despesa()
        if self.ide1:
            self.conecta_db()
            
            self.cursor.execute(""" DELETE FROM contas WHERE id=? """, (self.ide1,))
            
            self.conn.commit()
            self.desconecta_db()
            self.insere_despesas_na_lista()
            self.soma_despesa()
            self.limpa_aba_02()


   

    def calendario_aba_01(self):
        self.calendario1 = Calendar(self.aba_01, bg="#454545", locale="pt_br")
        self.calendario1['font'] = "Arial", 9
        self.calendario1.place(relx=0.545, rely=0.08)

        self.btn_calendar_data_aba_01 = Button(self.aba_01, text="Inserir Data", command=self.print_calendario_aba_01)
        self.btn_calendar_data_aba_01['font'] = "Arial", 12
        self.btn_calendar_data_aba_01.place(relx=0.545, rely=0.299, relwidth=0.08, relheight=0.04)

    def print_calendario_aba_01(self):
        dataIni = self.calendario1.get_date()
        self.calendario1.destroy()

        self.entry_data_aba_01.delete(0, END)
        self.entry_data_aba_01.insert(END, dataIni)
        self.btn_calendar_data_aba_01.destroy()
    
    def calendario_aba_02(self):
        self.calendario2 = Calendar(self.aba_02, bg="#454545", locale="pt_br")
        self.calendario2['font'] = "Arial", 9
        self.calendario2.place(relx=0.545, rely=0.08)

        self.btn_calendar_data_aba_02 = Button(self.aba_02, text="Inserir Data", command=self.print_calendario_aba_02)
        self.btn_calendar_data_aba_02['font'] = "Arial", 12
        self.btn_calendar_data_aba_02.place(relx=0.545, rely=0.299, relwidth=0.08, relheight=0.04)

    def print_calendario_aba_02(self):
        dataIni = self.calendario2.get_date()
        self.calendario2.destroy()

        self.entry_data_aba_02.delete(0, END)
        self.entry_data_aba_02.insert(END, dataIni)
        self.btn_calendar_data_aba_02.destroy()
    

    def calendario_data_inicio(self):
        self.calendario3 = Calendar(self.frame_resumo_aba_03, bg="#454545", locale="pt_br")
        self.calendario3['font'] = "Arial", 9
        self.calendario3.place(relx=0.21, rely=0.01)

        self.btn_add_data_inicio_aba_03 = Button(self.frame_resumo_aba_03, text="Inserir Data", command=self.print_calendario_data_inicio)
        self.btn_add_data_inicio_aba_03['font'] = "Arial", 12
        self.btn_add_data_inicio_aba_03.place(relx=0.21, rely=0.615, relwidth=0.15, relheight=0.08)
        

    def print_calendario_data_inicio(self):
        dataIni = self.calendario3.get_date()
        self.entry_data_inicio_aba_03.delete(0, END)
        self.entry_data_inicio_aba_03.insert(END, dataIni)
        self.calendario3.destroy()
        self.btn_add_data_inicio_aba_03.destroy()
    
    def calendario_data_fim(self):
        self.calendario4 = Calendar(self.frame_resumo_aba_03, bg="#454545", locale="pt_br")
        self.calendario4['font'] = "Arial", 9
        self.calendario4.place(relx=0.511, rely=0.01)

        self.btn_add_data_fim_aba_03 = Button(self.frame_resumo_aba_03, text="Inserir Data", command=self.print_calendario_data_fim)
        self.btn_add_data_fim_aba_03['font'] = "Arial", 12
        self.btn_add_data_fim_aba_03.place(relx=0.511, rely=0.615, relwidth=0.15, relheight=0.08)

    def print_calendario_data_fim(self):
        dataIni = self.calendario4.get_date()
        self.entry_data_fim_aba_03.delete(0, END)
        self.entry_data_fim_aba_03.insert(END, dataIni)
        self.calendario4.destroy()
        self.btn_add_data_fim_aba_03.destroy()
    

    def add_categorias_entradas(self):
        categoria = self.combo_categoria_aba_01.get().capitalize()
        if categoria:
            self.conecta_db()
            lista = self.cursor.execute("""SELECT id, categoria FROM categorias ORDER BY categoria; """)

            conta = 0
            for item in lista:
                if item[1] == categoria:
                    conta += 1

            if not conta:
                self.cursor.execute("""INSERT INTO categorias 
                    (categoria)
                    VALUES (?)""",(categoria,))

                self.conn.commit()
                self.desconecta_db()
                self.insere_categoria_lista()
                #self.combo_categoria_aba_01.delete(0, END)
    
            else:
                self.desconecta_db()
                messagebox.showerror("ERRO", f"{categoria} já está na lista.")
        else:
            messagebox.showerror("ERRO!", "É preciso preencher a casa.")
    
    def add_categorias_despesas(self):
        categoria = self.combo_categoria_aba_02.get().capitalize()
        if categoria:
            self.conecta_db()
            lista = self.cursor.execute("""SELECT id, categoria FROM categorias01 ORDER BY categoria; """)

            conta = 0
            for item in lista:
                if item[1] == categoria:
                    conta += 1
            
            if not conta:
                self.cursor.execute("""INSERT INTO categorias01
                    (categoria)
                    VALUES (?)""", (categoria,))
                
                self.conn.commit()
                self.desconecta_db()
            else:
                self.desconecta_db()
                messagebox.showerror("ERRO!", f"{categoria} já está na lista.")
        else:
            messagebox.showerror("ERRO!", "É preciso preencher a casa.")
    
    def delete_categoria_entradas(self):
        cat = self.combo_categoria_aba_01.get()
        self.conecta_db()
        if cat:
            conta = 0
            lista = self.cursor.execute("""SELECT id, categoria FROM categorias""")
            for item in lista:
                if item[1] == cat:
                    conta +=1

            if conta:
                self.cursor.execute("""DELETE FROM categorias WHERE categoria = ? """, (cat,))
                self.conn.commit()
                self.desconecta_db()
            else:
                self.desconecta_db()
                messagebox.showerror("ERRO!", f"Categoria ({cat}) já foi excluído.")
        else:
            messagebox.showerror("ERRO!", "É preciso selecionar uma categoria.")
        
    
    def delete_categorias_despesas(self):
        cat = self.combo_categoria_aba_02.get()
        self.conecta_db()
        if cat:
            conta = 0
            lista = self.cursor.execute("""SELECT id, categoria FROM categorias01""")
            for item in lista:
                if item[1] == cat:
                    conta +=1

            if conta:
                self.cursor.execute("""DELETE FROM categorias WHERE categoria = ? """, (cat,))
                self.conn.commit()
                self.desconecta_db()
            else:
                self.desconecta_db()
                messagebox.showerror("ERRO!", f"Categoria ({cat}) já foi excluído.")
        else:
            messagebox.showerror("ERRO!", "É preciso selecionar uma categoria.")
        
    
    def insere_categoria_lista(self):
        self.conecta_db()
        lista = self.cursor.execute("""SELECT id, categoria FROM categorias ORDER BY categoria; """)
        self.lista_itens = []
        for item in lista:
            if item[1]:
                self.lista_itens.append(item[1]) 
        
        self.desconecta_db()

    
    def insere_categoria_despesa_lista(self):
        self.conecta_db()
        lista = self.cursor.execute("""SELECT id, categoria FROM categorias01 ORDER BY categoria; """)
        self.lista_itens = []
        for item in lista:
            if item[1]:
                self.lista_itens.append(item[1])

        #self.combo_categoria_aba_01['values'] = self.lista_itens   
        self.desconecta_db()


    def insere_categoria_entry_aba_01(self):
        categoria = self.combo_categoria_aba_01.get().capitalize()
        if categoria:
            self.entry_categoria_aba_01.delete(0, END)
            self.entry_categoria_aba_01.insert(END, categoria)
        else:
            messagebox.showerror("ERRO!", "É preciso preencher a casa.")
    

    def insere_categoria_entry_aba_02(self):
        categoria = self.combo_categoria_aba_02.get().capitalize()
        if categoria:
            self.entry_categoria_aba_02.delete(0, END)
            self.entry_categoria_aba_02.insert(END, categoria)
        else:
            messagebox.showerror("ERRO!", "É preciso preencher a casa.")
    
    def soma_receita(self):
        self.conecta_db()
        lista = self.cursor.execute("""SELECT id, descricao, valor, data, categoria, comentario, tipo FROM contas
                    ORDER BY data ASC; """)
        
        soma = 0
        for linha in lista:
            if linha[6] == "Receita":
                #self.treeview_aba_02.insert("", END, values=linha)
                soma += linha[2]
        
        if soma:
            self.lb_total_valor_receitas_aba_01['text'] = f"R$ {soma:.2f}"
        
        self.desconecta_db()
        

    def soma_despesa(self):
        self.conecta_db()
        lista = self.cursor.execute("""SELECT id, descricao, valor, data, categoria, comentario, tipo FROM contas
                    ORDER BY data ASC; """)
        
        soma = 0
        for linha in lista:
            if linha[6] == "Despesa":
                soma += linha[2]
        
        if soma:
            self.lb_total_valor_despesas_aba_02['text'] = f"R$ {soma:.2f}"
        
        self.desconecta_db()

    def salvar_em_PDF(self):
        self.variaveis_aba_03()
        data_inicio = self.data_inicio.replace("/", "-")
        data_fim = self.data_fim.replace("/", "-")
        self.nome_pdf = f"Relatorio-{data_inicio}-{data_fim}.pdf"
        webbrowser.open(self.nome_pdf)

    def gera_relatorio(self):
        self.variaveis_aba_03()
        if self.data_inicio and self.data_fim:
            data_inicio = self.data_inicio.replace("/", "-")
            data_fim = self.data_fim.replace("/", "-")
            self.nomepdf = f"Relatorio-{data_inicio}-{data_fim}.pdf"
            self.c = canvas.Canvas(self.nomepdf)

            self.c.setFont("Helvetica", 22)
            self.c.drawString(100, 800, "          Relatório Financeiro v1.0")
            self.c.drawString(50, 785, "--------------------------------------------------------------")
            self.c.setFont("Helvetica", 14) 
            self.c.drawString(50, 770, f"                        Data Início : {self.data_inicio} | Data Fim: {self.data_fim}")
            self.c.setFont("Helvetica", 22)
            self.c.drawString(50, 755, "--------------------------------------------------------------")
            self.c.setFont("Helvetica", 11)
            self.c.drawString(20, 740, "         Valor (R$)           |      Data       |      Tipo         |               Categoria        ")
            self.comprimento = 730
            self.c.drawString(20, self.comprimento, "-----------------------------------------------------------------------------------------------------------------------------------------------------")

            self.conecta_db()

            lista = self.cursor.execute(""" SELECT id, descricao, valor, data, categoria, comentario, tipo FROM contas
                    ORDER BY data ASC; """)

            receitas = 0
            despesas = 0
            saldo = 0
            for linha in lista:
                if linha[3] >= self.data_inicio and linha[3] <= self.data_fim:
                    self.comprimento -= 13
                    self.c.drawString(20, self.comprimento, f"Valor R$:{linha[2]:_>10.2f}  |  {linha[3]} |   {linha[6]:<10}          {linha[4]:^25}")
                    
                    if linha[6] == "Receita":
                        receitas += linha[2]

                        
                    elif linha[6] == "Despesa":
                        despesas += linha[2]
            
  
            saldo = receitas - despesas       

            self.comprimento -= 13
            self.c.drawString(50, self.comprimento, f"{'-'*120}")
            self.comprimento -= 13
            self.c.drawString(70, self.comprimento, f"Receitas R${receitas:.2f}      Despesas R${despesas:.2f}       Saldo R${saldo:.2f}")
            self.comprimento -= 13
            self.c.drawString(50, self.comprimento, f"{'-'*120}")

            self.desconecta_db()

            self.c.showPage()
            self.c.save()
            self.salvar_em_PDF()

    def plotar_grafico(self):
        self.variaveis_aba_03()

        rotulos = ["Receita", "Despesa", "saldo"]
        valores = []

        self.conecta_db()
        lista = self.cursor.execute(""" SELECT id, descricao, valor, data, categoria, comentario, tipo FROM contas
                    ORDER BY data ASC; """)
        
        receita = 0
        despesa = 0
        saldo = 0
        for l in lista:
            if l[3] >= self.data_inicio and l[3] <= self.data_fim:
                pass
                if l[6] == "Despesa":
                    despesa += l[2]
                elif l[6] == "Receita":
                    receita += l[2]
        
        self.desconecta_db()

        saldo = receita - despesa
        valores.append(receita)
        valores.append(despesa)
        valores.append(saldo)

        #destaque = (0.1, 0.1, 0.1)
        fig = Figure(figsize=(10, 10), dpi=100)
        fig.add_subplot(111).pie(labels=rotulos, x=valores, autopct="%1.1f%%", startangle=90, shadow=True)

        canvas = FigureCanvasTkAgg(fig, master=self.frame_grafico_aba_03)
        canvas.draw()
        canvas.get_tk_widget().place(relx=0.0001, rely=0.0001, relwidth=1, relheight=1)

            
    
class Janela_Principal(Funcs):
    def __init__(self):
        self.root = root
        self.tela()
        self.frame_de_cima()
        self.frame_de_baixo()
        self.notebook_abas()
        self.widgets_aba01()
        self.treeview_aba01()
        self.widgets_aba02()
        self.treeview_aba02()
        self.widgets_aba03()
        self.treeview_aba03()

        # Funções externas a janela - Classe Funcs
        self.cria_db()
        self.insere_receitas_na_lista()
        self.insere_despesas_na_lista()
        self.insere_categoria_lista()
        self.insere_categoria_despesa_lista()
        self.soma_receita()
        self.soma_despesa()
        self.root.mainloop()
    
    def tela(self):
        self.root.title("Controle de Gastos v1.0")
        self.root.geometry("1300x900")
        self.root.configure(background="#454545")
        self.root.minsize(width=1100, height=600)
        self.root.maxsize(width=1350, height=900)
        
    def frame_de_cima(self):
        self.frame_cima = Frame(self.root, bd=10, bg="#454545", highlightbackground="#454545", highlightthickness=5)
        self.frame_cima.place(relx=0.002, rely=0.005, relwidth=0.996, relheight=0.10)

        self.lb_titulo = Label(self.frame_cima, text="Controle de Gastos v1.0", fg="white", bg="#454545")
        self.lb_titulo['font'] = "Arial", 24, "bold"
        self.lb_titulo.place(relx=0.2, rely=0.10, relwidth=0.6, relheight=0.53)

        self.lb_sub_titulo = Label(self.frame_cima, text="Gestor simples de finanças pessoais.", fg="white", bg="#454545")
        self.lb_sub_titulo['font'] = "Arial", 14
        self.lb_sub_titulo.place(relx=0.21, rely=0.7, relwidth=0.6, relheight=0.3)
    
    def frame_de_baixo(self):
        self.frame_baixo = Frame(self.root, bg="#454545", highlightbackground="#454545", highlightthickness=5)
        self.frame_baixo.place(relx=0.001, rely=0.11, relwidth=0.998, relheight=0.89)

    def notebook_abas(self):
        self.note = ttk.Notebook(self.frame_baixo)
        self.note.place(relx=0.0001, rely=0.0001, relwidth=1, relheight=1)
    
        # Aba Contas
        self.aba_01 = Frame(self.note, bg="#1b1b1b")
        self.note.add(self.aba_01, text="Entradas")
        # Aba Saídas
        self.aba_02 = Frame(self.note, bg="#1b1b1b")
        self.note.add(self.aba_02, text="Saídas")
        # Aba Entradas
        self.aba_03 = Frame(self.note, bg='#1b1b1b')
        self.note.add(self.aba_03, text="Resumo")
    
    def widgets_aba01(self):
        # Label titulo
        self.lb_titulo_aba_01 = Label(self.aba_01, text="Nova Entrada / Adiciona", bg="#1b1b1b")
        self.lb_titulo_aba_01['font'] = "Arial", 12
        self.lb_titulo_aba_01.place(relx=0.41, rely=0.01, relwidth=0.15, relheight=0.025)

        # Label Descrição
        self.lb_descricao_aba_01 = Label(self.aba_01, text="Descrição", bg="#1b1b1b")
        self.lb_descricao_aba_01['font'] = "Arial", 12
        self.lb_descricao_aba_01.place(relx=0.01, rely=0.05, relwidth=0.07, relheight=0.025)

        # Entry Descrição
        self.entry_descricao_aba_01 = Entry(self.aba_01, bg="lightgrey", fg="#1b1b1b")
        self.entry_descricao_aba_01['font'] = "Arial", 12
        self.entry_descricao_aba_01.focus()
        self.entry_descricao_aba_01.place(relx=0.01, rely=0.08, relwidth=0.3, relheight=0.03)

        # Label Custo
        self.lb_custo_aba_01 = Label(self.aba_01, text="Valor (R$)", bg="#1b1b1b")
        self.lb_custo_aba_01['font'] = "Arial", 12
        self.lb_custo_aba_01.place(relx=0.32, rely=0.05, relwidth=0.07, relheight=0.025)

        # Entry Custo
        self.entry_valor_aba_01 = Entry(self.aba_01, bg="lightgrey", fg="#1b1b1b")
        self.entry_valor_aba_01['font'] = "Arial", 12
        self.entry_valor_aba_01.place(relx=0.32, rely=0.08, relwidth=0.11, relheight=0.03)

        # Label Data
        self.lb_data_aba_01 = Label(self.aba_01, text="Data", bg="#1b1b1b")
        self.lb_data_aba_01['font'] = "Arial", 12
        self.lb_data_aba_01.place(relx=0.42, rely=0.05, relwidth=0.08, relheight=0.025)
    
        # Botão Calendário
        self.btn_calendario_aba_01 = Button(self.aba_01, text=">>", bg="lightgrey", fg="black", command=self.calendario_aba_01)
        self.btn_calendario_aba_01['font'] = "Arial", 12
        self.btn_calendario_aba_01.place(relx=0.44, rely=0.08, relwidth=0.03, relheight=0.03)

        # Entry Data
        self.entry_data_aba_01 = Entry(self.aba_01, bg="lightgrey", fg="#1b1b1b", width=10)
        self.entry_data_aba_01['font'] = "Arial", 12
        self.entry_data_aba_01.place(relx=0.472, rely=0.08, relwidth=0.07, relheight=0.03)

        # Label Categoria
        self.lb_categoria_aba_01 = Label(self.aba_01, text="Categoria", bg="#1b1b1b")
        self.lb_categoria_aba_01['font'] = "Arial", 12
        self.lb_categoria_aba_01.place(relx=0.01, rely=0.12, relwidth=0.069, relheight=0.025)

        # Combobox Categoria
        self.insere_categoria_lista()
        self.combo_categoria_aba_01 = ttk.Combobox(self.aba_01, values=self.lista_itens)
        self.combo_categoria_aba_01.place(relx=0.01, rely=0.15, relwidth=0.15, relheight=0.03)


        # Botão Add/Categoria
        self.btn_add_categoria_aba_01 = Button(self.aba_01, text="Add/Categoria", bg="lightgrey", fg="black")
        self.btn_add_categoria_aba_01['command'] = self.add_categorias_entradas
        self.btn_add_categoria_aba_01['font'] = "Arial", 9
        self.btn_add_categoria_aba_01.place(relx=0.01, rely=0.18, relwidth=0.07, relheight=0.02)
        # Botão Delete Categoria
        self.btn_del_categoria_aba_01 = Button(self.aba_01, text="Del/Categoria", bg="lightgrey", fg="black", command=self.delete_categoria_entradas)
        self.btn_del_categoria_aba_01['font'] = "Arial", 9
        self.btn_del_categoria_aba_01.place(relx=0.08, rely=0.18, relwidth=0.07, relheight=0.02)
        # Botão Categoria Add na Entry >>
        self.btn_add_entry_categoria_aba_01 = Button(self.aba_01, text=">>", bg="lightgrey", fg="black", command=self.insere_categoria_entry_aba_01)
        self.btn_add_entry_categoria_aba_01['font'] = "Arial", 12
        self.btn_add_entry_categoria_aba_01.place(relx=0.162, rely=0.15, relwidth=0.02, relheight=0.03)
        # Entry categoria
        self.entry_categoria_aba_01 = Entry(self.aba_01, bg="lightgrey", fg="#1b1b1b")
        self.entry_categoria_aba_01['font'] = "Arial", 12
        self.entry_categoria_aba_01.place(relx=0.182, rely=0.15, relwidth=0.129, relheight=0.03)
        # Label Comentário
        self.lb_comentario_aba_01 = Label(self.aba_01, text="Comentário", bg="#1b1b1b")
        self.lb_comentario_aba_01['font'] = "Arial", 12
        self.lb_comentario_aba_01.place(relx=0.32, rely=0.12, relwidth=0.0755, relheight=0.025)
        # Entry Comentário
        self.entry_comentario_aba_01 = Entry(self.aba_01, bg="lightgrey", fg="#1b1b1b")
        self.entry_comentario_aba_01['font'] = "Arial", 12
        self.entry_comentario_aba_01.place(relx=0.32, rely=0.15, relwidth=0.222, relheight=0.03)

        # Label ID
        self.lb_id_aba_01 = Label(self.aba_01, text="ID", bg="#1b1b1b")
        self.lb_id_aba_01['font'] = "Arial", 12
        self.lb_id_aba_01.place(relx=0.253, rely=0.205, relwidth=0.04, relheight=0.025)
        # Entry ID - Ready Only
        self.entry_id_aba_01 = Entry(self.aba_01, fg="white", bg="#1b1b1b")
        self.entry_id_aba_01['font'] = "Arial", 12
        self.entry_id_aba_01.place(relx=0.28, rely=0.2, relwidth=0.02, relheight=0.03)

        # Botões Adicionar / Atualizar / Delete
        self.btn_adicionar_aba_01 = Button(self.aba_01, text="Adicionar", bg="lightgrey", fg="black", command=self.adiciona_receita)
        self.btn_adicionar_aba_01['font'] = "Arial", 10
        self.btn_adicionar_aba_01.place(relx=0.322, rely=0.2, relwidth=0.07, relheight=0.03)

        self.btn_atualizar_aba_01 = Button(self.aba_01, text="Atualizar", bg="lightgrey", fg="black", command=self.atualiza_receita)
        self.btn_atualizar_aba_01['font'] = "Arial", 10
        self.btn_atualizar_aba_01.place(relx=0.397, rely=0.2, relwidth=0.07, relheight=0.03)

        self.btn_delete_aba_01 = Button(self.aba_01, text="Delete", bg="lightgrey", fg="black", command=self.deleta_receita)
        self.btn_delete_aba_01['font'] = "Arial", 10
        self.btn_delete_aba_01.place(relx=0.472, rely=0.2, relwidth=0.07, relheight=0.03)

        # Label Rodapé - Despesas Total
        self.lb_total_receitas_aba_01 = Label(self.aba_01, text="Receitas Acumulado", bg="#1b1b1b", fg="lightblue")
        self.lb_total_receitas_aba_01['font'] = "Arial", 18
        self.lb_total_receitas_aba_01.place(relx=0.01, rely=0.95, relwidth=0.25, relheight=0.04)

        self.lb_total_valor_receitas_aba_01 = Label(self.aba_01, text="", bg="#454545", fg='white')
        self.lb_total_valor_receitas_aba_01['font'] = "Arial", 18
        self.lb_total_valor_receitas_aba_01.place(relx=0.3, rely=0.95, relwidth=0.2, relheight=0.04)

    def treeview_aba01(self):
        self.treeview_aba_01 = ttk.Treeview(self.aba_01, height=3, 
        column=("col1", "col2", "col3", "col4", "col5", "col6", "col7"))
        # "ID", "Descrição", "Valor", "Data", "Categoria", "Comentário", "Tipo"
        self.treeview_aba_01.heading("#0", text="")
        self.treeview_aba_01.heading("#1", text="ID")
        self.treeview_aba_01.heading("#2", text="Descrição")
        self.treeview_aba_01.heading("#3", text="Valor(R$)")
        self.treeview_aba_01.heading("#4", text="Data")
        self.treeview_aba_01.heading("#5", text="Categoria")
        self.treeview_aba_01.heading("#6", text="Comentário")
        self.treeview_aba_01.heading("#7", text="Tipo")

        # Definindo a largura de cada coluna.
        self.treeview_aba_01.column("#0", width=1)
        self.treeview_aba_01.column("#1", width=1)
        self.treeview_aba_01.column("#2", width=200)
        self.treeview_aba_01.column("#3", width=10)
        self.treeview_aba_01.column("#4", width=10)
        self.treeview_aba_01.column("#5", width=200)
        self.treeview_aba_01.column("#6", width=200)
        self.treeview_aba_01.column("#7", width=10)
        self.treeview_aba_01.place(relx=0.001, rely=0.235, relwidth=0.99, relheight=0.7)

        # Barra de Rolagem da Treeview
        self.barra_rolagem_aba_01 = Scrollbar(self.aba_01, orient="vertical", bg="#1b1b1b")
        self.treeview_aba_01.configure(yscroll=self.barra_rolagem_aba_01.set)
        self.barra_rolagem_aba_01.place(relx=0.99, rely=0.26, relwidth=0.01, relheight=0.740)

        # Binding Evento clique duplo
        self.treeview_aba_01.bind("<Double-1>", self.clique_duplo_aba_01)


    def widgets_aba02(self):
        # Label titulo
        self.lb_titulo_aba_02 = Label(self.aba_02, text="Nova Saída / Adiciona", bg="#1b1b1b")
        self.lb_titulo_aba_02['font'] = "Arial", 12
        self.lb_titulo_aba_02.place(relx=0.41, rely=0.01, relwidth=0.15, relheight=0.025)

        # Label Descrição
        self.lb_descricao_aba_02 = Label(self.aba_02, text="Descrição", bg="#1b1b1b")
        self.lb_descricao_aba_02['font'] = "Arial", 12
        self.lb_descricao_aba_02.place(relx=0.01, rely=0.05, relwidth=0.07, relheight=0.025)

        # Entry Descrição
        self.entry_descricao_aba_02 = Entry(self.aba_02, bg="lightgrey", fg="#1b1b1b")
        self.entry_descricao_aba_02['font'] = "Arial", 12
        self.entry_descricao_aba_02.focus()
        self.entry_descricao_aba_02.place(relx=0.01, rely=0.08, relwidth=0.3, relheight=0.03)

        # Label Valor
        self.lb_custo_aba_02 = Label(self.aba_02, text="Valor (R$)", bg="#1b1b1b")
        self.lb_custo_aba_02['font'] = "Arial", 12
        self.lb_custo_aba_02.place(relx=0.32, rely=0.05, relwidth=0.07, relheight=0.025)

        # Entry Valor
        self.entry_valor_aba_02 = Entry(self.aba_02, bg="lightgrey", fg="#1b1b1b")
        self.entry_valor_aba_02['font'] = "Arial", 12
        self.entry_valor_aba_02.place(relx=0.32, rely=0.08, relwidth=0.11, relheight=0.03)

        # Label Data
        self.lb_data_aba_02 = Label(self.aba_02, text="Data", bg="#1b1b1b")
        self.lb_data_aba_02['font'] = "Arial", 12
        self.lb_data_aba_02.place(relx=0.42, rely=0.05, relwidth=0.08, relheight=0.025)
    
        # Botão Calendário
        self.btn_calendario_aba_02 = Button(self.aba_02, text=">>", bg="lightgrey", fg="black", command=self.calendario_aba_02)
        self.btn_calendario_aba_02['font'] = "Arial", 12
        self.btn_calendario_aba_02.place(relx=0.44, rely=0.08, relwidth=0.03, relheight=0.03)

        # Entry Data
        self.entry_data_aba_02 = Entry(self.aba_02, bg="lightgrey", fg="#1b1b1b", width=10)
        self.entry_data_aba_02['font'] = "Arial", 12
        self.entry_data_aba_02.place(relx=0.472, rely=0.08, relwidth=0.07, relheight=0.03)

        # Label Categoria
        self.lb_categoria_aba_02 = Label(self.aba_02, text="Categoria", bg="#1b1b1b")
        self.lb_categoria_aba_02['font'] = "Arial", 12
        self.lb_categoria_aba_02.place(relx=0.01, rely=0.12, relwidth=0.069, relheight=0.025)

        # Combobox Categoria
        self.insere_categoria_despesa_lista()
        self.combo_categoria_aba_02 = ttk.Combobox(self.aba_02, values=self.lista_itens)
        self.combo_categoria_aba_02.place(relx=0.01, rely=0.15, relwidth=0.15, relheight=0.03)

        # Botão Add/Categoria
        self.btn_add_categoria_aba_02 = Button(self.aba_02, text="Add/Categoria", bg="lightgrey", fg="black", command=self.add_categorias_despesas)
        #self.btn_add_categoria_aba_02['command'] = self.add_categorias
        self.btn_add_categoria_aba_02['font'] = "Arial", 9
        self.btn_add_categoria_aba_02.place(relx=0.01, rely=0.18, relwidth=0.07, relheight=0.02)
        # Botão Delete Categoria
        self.btn_del_categoria_aba_02 = Button(self.aba_02, text="Del/Categoria", bg="lightgrey", fg="black")
        self.btn_del_categoria_aba_02['font'] = "Arial", 9
        self.btn_del_categoria_aba_02.place(relx=0.08, rely=0.18, relwidth=0.07, relheight=0.02)
        # Botão Categoria Add na Entry >>
        self.btn_add_entry_categoria_aba_02 = Button(self.aba_02, text=">>", bg="lightgrey", fg="black", command=self.insere_categoria_entry_aba_02)
        self.btn_add_entry_categoria_aba_02['font'] = "Arial", 12
        self.btn_add_entry_categoria_aba_02.place(relx=0.162, rely=0.15, relwidth=0.02, relheight=0.03)
        # Entry categoria
        self.entry_categoria_aba_02 = Entry(self.aba_02, bg="lightgrey", fg="#1b1b1b")
        self.entry_categoria_aba_02['font'] = "Arial", 12
        self.entry_categoria_aba_02.place(relx=0.182, rely=0.15, relwidth=0.129, relheight=0.03)
        # Label Comentário
        self.lb_comentario_aba_02 = Label(self.aba_02, text="Comentário", bg="#1b1b1b")
        self.lb_comentario_aba_02['font'] = "Arial", 12
        self.lb_comentario_aba_02.place(relx=0.32, rely=0.12, relwidth=0.0755, relheight=0.025)
        # Entry Comentário
        self.entry_comentario_aba_02 = Entry(self.aba_02, bg="lightgrey", fg="#1b1b1b")
        self.entry_comentario_aba_02['font'] = "Arial", 12
        self.entry_comentario_aba_02.place(relx=0.32, rely=0.15, relwidth=0.222, relheight=0.03)

        # Label ID
        self.lb_id_aba_02 = Label(self.aba_02, text="ID", bg="#1b1b1b")
        self.lb_id_aba_02['font'] = "Arial", 12
        self.lb_id_aba_02.place(relx=0.253, rely=0.205, relwidth=0.04, relheight=0.025)
        # Entry ID - Ready Only
        self.entry_id_aba_02 = Entry(self.aba_02, fg="white", bg="#1b1b1b")
        self.entry_id_aba_02['font'] = "Arial", 12
        self.entry_id_aba_02.place(relx=0.28, rely=0.2, relwidth=0.02, relheight=0.03)

        # Botões Adicionar / Atualizar / Delete
        self.btn_adicionar_aba_02 = Button(self.aba_02, text="Adicionar", bg="lightgrey", fg="black", command=self.adiciona_despesa)
        self.btn_adicionar_aba_02['font'] = "Arial", 10
        self.btn_adicionar_aba_02.place(relx=0.322, rely=0.2, relwidth=0.07, relheight=0.03)

        self.btn_atualizar_aba_02 = Button(self.aba_02, text="Atualizar", bg="lightgrey", fg="black", command=self.atualiza_despesa)
        self.btn_atualizar_aba_02['font'] = "Arial", 10
        self.btn_atualizar_aba_02.place(relx=0.397, rely=0.2, relwidth=0.07, relheight=0.03)

        self.btn_delete_aba_02 = Button(self.aba_02, text="Delete", bg="lightgrey", fg="black", command=self.deleta_despesa)
        self.btn_delete_aba_02['font'] = "Arial", 10
        self.btn_delete_aba_02.place(relx=0.472, rely=0.2, relwidth=0.07, relheight=0.03)

        # Label Rodapé - Despesas Total
        self.lb_total_despesas_aba_02 = Label(self.aba_02, text="Despesas Acumulado", bg="#1b1b1b", fg="red")
        self.lb_total_despesas_aba_02['font'] = "Arial", 18
        self.lb_total_despesas_aba_02.place(relx=0.01, rely=0.95, relwidth=0.25, relheight=0.04)

        self.lb_total_valor_despesas_aba_02 = Label(self.aba_02, text="", bg="#454545", fg='white')
        self.lb_total_valor_despesas_aba_02['font'] = "Arial", 18
        self.lb_total_valor_despesas_aba_02.place(relx=0.3, rely=0.95, relwidth=0.2, relheight=0.04)
    
    def treeview_aba02(self):
        self.treeview_aba_02 = ttk.Treeview(self.aba_02, height=3, 
        column=("col1", "col2", "col3", "col4", "col5", "col6", "col7"))
        # "ID", "Descrição", "Valor", "Data", "Categoria", "Comentário", "tipo"
        self.treeview_aba_02.heading("#0", text="")
        self.treeview_aba_02.heading("#1", text="ID")
        self.treeview_aba_02.heading("#2", text="Descrição")
        self.treeview_aba_02.heading("#3", text="Valor(R$)")
        self.treeview_aba_02.heading("#4", text="Data")
        self.treeview_aba_02.heading("#5", text="Categoria")
        self.treeview_aba_02.heading("#6", text="Comentário")
        self.treeview_aba_02.heading("#7", text="Tipo")

        # Definindo a largura de cada coluna.
        self.treeview_aba_02.column("#0", width=1)
        self.treeview_aba_02.column("#1", width=1)
        self.treeview_aba_02.column("#2", width=200)
        self.treeview_aba_02.column("#3", width=10)
        self.treeview_aba_02.column("#4", width=10)
        self.treeview_aba_02.column("#5", width=200)
        self.treeview_aba_02.column("#6", width=200)
        self.treeview_aba_02.column("#7", width=10)
        self.treeview_aba_02.place(relx=0.001, rely=0.235, relwidth=0.99, relheight=0.7)

        # Barra de Rolagem da Treeview
        self.barra_rolagem_aba_02 = Scrollbar(self.aba_02, orient="vertical", bg="#1b1b1b")
        self.treeview_aba_02.configure(yscroll=self.barra_rolagem_aba_02.set)
        self.barra_rolagem_aba_02.place(relx=0.99, rely=0.26, relwidth=0.01, relheight=0.740)

        # Bind clique duplo aba 02
        self.treeview_aba_02.bind("<Double-1>", self.clique_duplo_aba_02)

    
    def widgets_aba03(self):
        # Label Resumo Financeiro
        self.lb_resumo_aba_03 = Label(self.aba_03, text="Resumo Financeiro", bg="#1b1b1b")
        self.lb_resumo_aba_03['font'] = "Arial", 12
        self.lb_resumo_aba_03.place(relx=0.43, rely=0.01)

        # Frame do Gráfico
        self.frame_grafico_aba_03 = Frame(self.aba_03, bd=10, bg="#1b1b1b", highlightbackground="#454545", highlightthickness=5)
        self.frame_grafico_aba_03.place(relx=0.505, rely=0.04, relwidth=0.48, relheight=0.4)

        # Frame do Resumo
        self.frame_resumo_aba_03 = Frame(self.aba_03, bd=10, bg="#1b1b1b", highlightbackground="#454545", highlightthickness=5)
        self.frame_resumo_aba_03.place(relx=0.01, rely=0.04, relwidth=0.49, relheight=0.4)

        # Label Data Inicio
        self.lb_data_inicio_aba_03 = Label(self.frame_resumo_aba_03, text="Início", bg="#1b1b1b")
        self.lb_data_inicio_aba_03['font'] = "Arial", 12
        self.lb_data_inicio_aba_03.place(relx=0.1, rely=0.01)
        # Botão >> Data inicio
        self.btn_add_data_inicio_aba_03 = Button(self.frame_resumo_aba_03, text=">>", bg="lightgrey", fg="black", command=self.calendario_data_inicio)
        self.btn_add_data_inicio_aba_03['font'] = "Arial", 10
        self.btn_add_data_inicio_aba_03.place(relx=0.17, rely=0.01, relwidth=0.04, relheight=0.08)
        # Entry Data Inicio
        self.entry_data_inicio_aba_03 = Entry(self.frame_resumo_aba_03, bg="lightgrey", fg="#1b1b1b", width=10)
        self.entry_data_inicio_aba_03['font'] = "Arial", 12
        self.entry_data_inicio_aba_03.place(relx=0.215, rely=0.01, relwidth=0.15, relheight=0.08)
        
        # Label Data Fim
        self.lb_data_fim_aba_03 = Label(self.frame_resumo_aba_03, text="Início", bg="#1b1b1b")
        self.lb_data_fim_aba_03['font'] = "Arial", 12
        self.lb_data_fim_aba_03.place(relx=0.4, rely=0.01)
        # Botão >> Data fim
        self.btn_add_data_fim_aba_03 = Button(self.frame_resumo_aba_03, text=">>", bg="lightgrey", fg="black", command=self.calendario_data_fim)
        self.btn_add_data_fim_aba_03['font'] = "Arial", 10
        self.btn_add_data_fim_aba_03.place(relx=0.47, rely=0.01, relwidth=0.04, relheight=0.08)
        # Entry Data fim
        self.entry_data_fim_aba_03 = Entry(self.frame_resumo_aba_03, bg="lightgrey", fg="#1b1b1b", width=10)
        self.entry_data_fim_aba_03['font'] = "Arial", 12
        self.entry_data_fim_aba_03.place(relx=0.515, rely=0.01, relwidth=0.15, relheight=0.08)
        # Botão Pesquisar
        self.btn_pesquisar_data = Button(self.frame_resumo_aba_03, text="Pesquisar", bg="lightgrey", fg="black", command=self.insere_resumo_na_lista)
        self.btn_pesquisar_data['font'] = "Arial", 12
        self.btn_pesquisar_data.place(relx=0.67, rely=0.01, relwidth=0.15, relheight=0.08)

        # Label Saldo e Label valor do saldo
        self.lb_entrada_frame_resumo_aba_03 = Label(self.frame_resumo_aba_03, text="Entrada", bg="#1b1b1b", fg="blue")
        self.lb_entrada_frame_resumo_aba_03['font'] = "Arial", 36
        self.lb_entrada_frame_resumo_aba_03.place(relx=0.01, rely=0.3, relheight=0.15)

        self.lb_entrada_valor_resumo_aba_03 = Label(self.frame_resumo_aba_03, text="R$ 0000,00", bg="#454545", fg="lightgrey")
        self.lb_entrada_valor_resumo_aba_03['font'] = "Arial", 24
        self.lb_entrada_valor_resumo_aba_03.place(relx=0.5, rely=0.3, relwidth=0.4, relheight=0.15)

        # Label Entrada e Label Valor da entrada
        self.lb_saida_frame_resumo_aba_03 = Label(self.frame_resumo_aba_03, text="Saída", bg="#1b1b1b", fg="red")
        self.lb_saida_frame_resumo_aba_03['font'] = "Arial", 36
        self.lb_saida_frame_resumo_aba_03.place(relx=0.01, rely=0.5, relheight=0.15)

        self.lb_saida_valor_resumo_aba_03 = Label(self.frame_resumo_aba_03, text="R$ 0000,00", bg="#454545", fg="lightgrey")
        self.lb_saida_valor_resumo_aba_03['font'] = "Arial", 24
        self.lb_saida_valor_resumo_aba_03.place(relx=0.5, rely=0.5, relwidth=0.4, relheight=0.15)

        # Label Saída e Label valor da Saida
        self.lb_saldo_frame_resumo_aba_03 = Label(self.frame_resumo_aba_03, text="Saldo", bg="#1b1b1b", fg="lightblue")
        self.lb_saldo_frame_resumo_aba_03['font'] = "Arial", 36
        self.lb_saldo_frame_resumo_aba_03.place(relx=0.01, rely=0.7, relheight=0.15)

        self.lb_saldo_valor_resumo_aba_03 = Label(self.frame_resumo_aba_03, text="R$ 0000,00", bg="#454545", fg="lightgrey")
        self.lb_saldo_valor_resumo_aba_03['font'] = "Arial", 24
        self.lb_saldo_valor_resumo_aba_03.place(relx=0.5, rely=0.7, relwidth=0.4, relheight=0.15)

        # Botão Gerar Relatório
        self.btn_gera_relatorio = Button(self.frame_resumo_aba_03, text="Gerar Relatório", bg="white", fg="#454545", command=self.gera_relatorio)
        self.btn_gera_relatorio['font'] = "Arial", 12
        self.btn_gera_relatorio.place(relx=0.5, rely=0.89, relwidth=0.4, relheight=0.13)


    def treeview_aba03(self):
        self.treeview_aba_03 = ttk.Treeview(self.aba_03, height=3, 
        column=("col1", "col2", "col3", "col4", "col5", "col6", "col7"))
        # "ID", "Descrição", "Valor", "Data", "Categoria", "Comentário"
        self.treeview_aba_03.heading("#0", text="")
        self.treeview_aba_03.heading("#1", text="ID")
        self.treeview_aba_03.heading("#2", text="Descrição")
        self.treeview_aba_03.heading("#3", text="Valor(R$)")
        self.treeview_aba_03.heading("#4", text="Data")
        self.treeview_aba_03.heading("#5", text="Categoria")
        self.treeview_aba_03.heading("#6", text="Comentário")
        self.treeview_aba_03.heading("#7", text="Tipo")

        # Definindo a largura de cada coluna.
        self.treeview_aba_03.column("#0", width=0)
        self.treeview_aba_03.column("#1", width=1)
        self.treeview_aba_03.column("#2", width=200)
        self.treeview_aba_03.column("#3", width=10)
        self.treeview_aba_03.column("#4", width=10)
        self.treeview_aba_03.column("#5", width=200)
        self.treeview_aba_03.column("#6", width=200)
        self.treeview_aba_03.column("#7", width=10)
        self.treeview_aba_03.place(relx=0.001, rely=0.45, relwidth=0.99, relheight=0.546)

        # Barra de Rolagem da Treeview
        self.barra_rolagem_aba_03 = Scrollbar(self.aba_03, orient="vertical", bg="#1b1b1b")
        self.treeview_aba_03.configure(yscroll=self.barra_rolagem_aba_03.set)
        self.barra_rolagem_aba_03.place(relx=0.99, rely=0.45, relwidth=0.01, relheight=0.546)
    

Janela_Principal()