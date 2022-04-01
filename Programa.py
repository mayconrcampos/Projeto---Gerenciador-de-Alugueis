from tkinter import *
from tkinter import ttk, messagebox
from modulos.calendarios import Calendario
from modulos.listas import Listas
from modulos.funcs import Funcs
from modulos.db import BancoDeDados


root = Tk()

class Janela_Principal(Funcs, Calendario, Listas, BancoDeDados):
    def __init__(self):
        self.root = root
        self.tela()
        self.frame_cima()
        self.frame_baixo()
        self.notebook_abas() 
        self.widgets_aba_01()
        self.widgets_aba_02()
        self.widgets_aba_03()
        self.widgets_aba_04()
        self.widgets_aba_05()

        self.treeview_aba01()
        self.treeview_aba02()
        self.treeview_aba03()

        self.treeview_seleciona_locador_aba_04()
        self.treeview_seleciona_locatario_aba_04()
        self.treeview_seleciona_imovel_aba_04()
        self.treeview_adiciona_contrato_aba_04()
        self.treeview_seleciona_contrato_aba_05()
        self.treeview_mensalidades_aba_05()
        # Funções externas
        self.cria_db()
        self.insere_locador_na_lista_aba_01()
        self.insere_locatario_na_lista_aba_02()
        self.insere_imovel_na_lista_aba_03()

        self.insere_locador_aba_04()
        self.insere_locatario_aba_04()
        self.insere_imovel_aba_04()
        self.insere_contrato_aba_04()

        self.insere_contrato_aba_05()
        #self.insere_mensalidades_aba_05()

        self.root.mainloop()

    def tela(self):
        self.root.title("Gerenciador de Contratos V1.0")
        self.root.geometry("1100x650")
        self.root.configure(background="#345574")
        self.root.resizable(False, False)
    
    def frame_cima(self):
        self.frame_de_cima = Frame(self.root, bd=10, bg="#1b39a9", highlightbackground="lightgrey", highlightthickness=4)
        self.frame_de_cima.place(relx=0.01, rely=0.001, relwidth=0.98, relheight=0.1)
    
        # Label Titulo do Programa
        self.lb_titulo_frame_de_cima = Label(self.frame_de_cima, text="Controle de Contratos de Aluguel v1.0", bg="#1b39a9", fg="lightgrey")
        self.lb_titulo_frame_de_cima['font'] = "Verdana", 18
        self.lb_titulo_frame_de_cima.place(relx=0.05, rely=0.15, relwidth=0.9, relheight=0.8)
    
    def frame_baixo(self):
        self.frame_de_baixo = Frame(self.root, bd=10, bg="#1b39a9", highlightbackground="lightgrey", highlightthickness=4)
        self.frame_de_baixo.place(relx=0.01, rely=0.11, relwidth=0.98, relheight=0.875)
    
    def notebook_abas(self):
        self.note = ttk.Notebook(self.frame_de_baixo)
        self.note.place(relx=0.0001, rely=0.0001, relwidth=1, relheight=1)
        # Aba 01, 02, 03, 04 e 05
        self.aba_01 = Frame(self.note, bg="#0e47a1")
        self.note.add(self.aba_01, text="Cadastro de Locatários")

        self.aba_02 = Frame(self.frame_de_baixo, bg="#0e47a1")
        self.note.add(self.aba_02, text="Cadastro de Inquilinos")

        self.aba_03 = Frame(self.frame_de_baixo, bg="#0e47a1")
        self.note.add(self.aba_03, text="Imóveis")

        self.aba_04 = Frame(self.frame_de_baixo, bg="#0e47a1")
        self.note.add(self.aba_04, text="Contratos")

        self.aba_05 = Frame(self.frame_de_baixo, bg="#0e47a1")
        self.note.add(self.aba_05, text="Mensalidades / Recibos")

        self.aba_06 = Frame(self.frame_de_baixo, bg="#0e47a1")
        self.note.add(self.aba_06, text="Resumo")

        self.aba_07 = Frame(self.frame_de_baixo, bg="#0e47a1")
        self.note.add(self.aba_07, text="Sobre")
    
    def widgets_aba_01(self):
        # Label - Cadastro de Locatários
        self.lb_titulo_aba_01 = Label(self.aba_01, text="Cadastro de Locatário", bg="#0e47a1", fg="lightgrey")
        self.lb_titulo_aba_01['font'] = "Arial", 14
        self.lb_titulo_aba_01.place(relx=0.35, rely=0.01, relwidth=0.3, relheight=0.03)

        """Frame Dados Pessoais"""
        self.frame_dados_pessoais_aba_01 = Frame(self.aba_01, bg="#1b39a9", highlightbackground="lightgrey", highlightthickness=1)
        self.frame_dados_pessoais_aba_01.place(relx=0.02, rely=0.05, relwidth=0.96, relheight=0.3)

        # Label Dados Pessoais
        self.lb_dados_pessoais_aba_01 = Label(self.aba_01, text="Dados Pessoais / Locatário", bg="#1b39a9", fg="lightgrey")
        self.lb_dados_pessoais_aba_01['font'] = "Arial", 12
        self.lb_dados_pessoais_aba_01.place(relx=0.03, rely=0.035, relwidth=0.2, relheight=0.025)

        # Label Nome e Entry nome Aba 01
        self.lb_nome_aba_01 = Label(self.frame_dados_pessoais_aba_01, text="Nome Completo", bg="#1b39a9", fg="lightgrey")
        self.lb_nome_aba_01['font'] = "Arial", 11
        self.lb_nome_aba_01.place(relx=0.01, rely=0.07, relwidth=0.12, relheight=0.1)
        
        self.entry_nome_aba_01 = Entry(self.frame_dados_pessoais_aba_01, bg="#345574", fg="lightgrey")
        self.entry_nome_aba_01['font'] = "Arial", 12
        self.entry_nome_aba_01.focus_force()
        self.entry_nome_aba_01.place(relx=0.01, rely=0.22, relwidth=0.25)# relheight=0.18)

        # Label e Entry Nacionalidade
        self.lb_nacionalidade_aba_01 = Label(self.frame_dados_pessoais_aba_01, text="Nacionalidade", bg="#1b39a9", fg="lightgrey")
        self.lb_nacionalidade_aba_01['font'] = "Arial", 11
        self.lb_nacionalidade_aba_01.place(relx=0.27, rely=0.07, relwidth=0.11, relheight=0.1)

        self.entry_nacionalidade_aba_01 = Entry(self.frame_dados_pessoais_aba_01, bg="#345574", fg="lightgrey")
        self.entry_nacionalidade_aba_01['font'] = "Arial", 12
        self.entry_nacionalidade_aba_01.place(relx=0.27, rely=0.22, relwidth=0.12)# relheight=0.18)

        # Label e Combobox - Estado Civil
        self.lb_estCivil_aba_01 = Label(self.frame_dados_pessoais_aba_01, text="Estado Civil", bg="#1b39a9", fg="lightgrey")
        self.lb_estCivil_aba_01['font'] = "Arial", 11
        self.lb_estCivil_aba_01.place(relx=0.4, rely=0.07, relwidth=0.09, relheight=0.1)

        self.est_civis = ["Casado(a)", "Solteiro(a)", "Divorciado(a)", "Viúvo(a)"]
        self.combo_estadoCivil_aba_01 = ttk.Combobox(self.frame_dados_pessoais_aba_01, values=self.est_civis)
        self.combo_estadoCivil_aba_01['font'] = "Arial", 12
        self.combo_estadoCivil_aba_01.place(relx=0.4, rely=0.22, relwidth=0.12)# relheight=0.18)

        # Label e Entry ID
        self.lb_id_aba_01 = Label(self.frame_dados_pessoais_aba_01, text="ID", bg="#1b39a9", fg="lightgrey")
        self.lb_id_aba_01['font'] = "Arial", 11
        self.lb_id_aba_01.place(relx=0.52, rely=0.07, relwidth=0.04, relheight=0.1)

        self.entry_ID_aba_01 = Entry(self.frame_dados_pessoais_aba_01, bg="#345574", fg="lightgrey")
        self.entry_ID_aba_01['font'] = "Arial", 12
        self.entry_ID_aba_01.place(relx=0.53, rely=0.22, relwidth=0.03)# relheight=0.18)

        # Label e Entry Profissão
        self.lb_profissao_aba_01 = Label(self.frame_dados_pessoais_aba_01, text="Profissão", bg="#1b39a9", fg="lightgrey")
        self.lb_profissao_aba_01['font'] = "Arial", 11
        self.lb_profissao_aba_01.place(relx=0.01, rely=0.47, relwidth=0.082, relheight=0.1)

        self.entry_profissao_aba_01 = Entry(self.frame_dados_pessoais_aba_01, bg="#345574", fg="lightgrey")
        self.entry_profissao_aba_01['font'] = "Arial", 12
        self.entry_profissao_aba_01.place(relx=0.01, rely=0.63, relwidth=0.17)# relheight=0.18)

        # Label e Entry RG
        self.lb_rg_aba_01 = Label(self.frame_dados_pessoais_aba_01, text="RG", bg="#1b39a9", fg="lightgrey")
        self.lb_rg_aba_01['font'] = "Arial", 11
        self.lb_rg_aba_01.place(relx=0.105, rely=0.47, relwidth=0.2, relheight=0.1)

        self.entry_rg_aba_01 = Entry(self.frame_dados_pessoais_aba_01, bg="#345574", fg="lightgrey")
        self.entry_rg_aba_01['font'] = "Arial", 12
        self.entry_rg_aba_01.place(relx=0.187, rely=0.63, relwidth=0.085)# relheight=0.18)
    
        # Label e Entry CPF <- Terá função de validação de formatação de CPF
        self.lb_cpf_aba_01 = Label(self.frame_dados_pessoais_aba_01, text="CPF", bg="#1b39a9", fg="lightgrey")
        self.lb_cpf_aba_01['font'] = "Arial", 11
        self.lb_cpf_aba_01.place(relx=0.275, rely=0.47, relwidth=0.05, relheight=0.1)

        self.entry_cpf_aba_01 = Entry(self.frame_dados_pessoais_aba_01, width=12, bg="#345574", fg="lightgrey")
        self.entry_cpf_aba_01['font'] = "Arial", 12
        self.entry_cpf_aba_01.place(relx=0.279, rely=0.63, relwidth=0.11)# relheight=0.18)

        # Label e Combobox = Data Nascimento
        self.lb_data_nasc_aba_01 = Label(self.frame_dados_pessoais_aba_01, text="Data Nasc.", bg="#1b39a9", fg="lightgrey")
        self.lb_data_nasc_aba_01['font'] = "Arial", 11
        self.lb_data_nasc_aba_01.place(relx=0.399, rely=0.47, relwidth=0.09, relheight=0.1)

        
        self.carrega_listas()
        self.combo_data_nasc_DIA_aba_01 = ttk.Combobox(self.frame_dados_pessoais_aba_01, values=self.lista_dia)
        self.combo_data_nasc_DIA_aba_01['font'] = "Arial", 12
        self.combo_data_nasc_DIA_aba_01.place(relx=0.4, rely=0.63, relwidth=0.037)# relheight=0.18)

        self.combo_data_nasc_MES_aba_01 = ttk.Combobox(self.frame_dados_pessoais_aba_01, values=self.lista_mes)
        self.combo_data_nasc_MES_aba_01['font'] = "Arial", 12
        self.combo_data_nasc_MES_aba_01.place(relx=0.45, rely=0.63, relwidth=0.037)# relheight=0.18)

        self.combo_data_nasc_ANO_aba_01 = ttk.Combobox(self.frame_dados_pessoais_aba_01, values=self.lista_ano)
        self.combo_data_nasc_ANO_aba_01['font'] = "Arial", 12
        self.combo_data_nasc_ANO_aba_01.place(relx=0.504, rely=0.63, relwidth=0.055)# relheight=0.18)

        """Frame Endereço do Locatário"""
        self.frame_endereco_aba_01 = Frame(self.aba_01, bg="#1b39a9", highlightbackground="lightgrey", highlightthickness=1)
        self.frame_endereco_aba_01.place(relx=0.02, rely=0.38, relwidth=0.96, relheight=0.3)

        # Label Endereço Locatário
        self.lb_titulo_endereco_aba_01 = Label(self.aba_01, text="Endereço / Locatário", bg="#1b39a9", fg="lightgrey")
        self.lb_titulo_endereco_aba_01['font'] = "Arial", 11
        self.lb_titulo_endereco_aba_01.place(relx=0.03, rely=0.365, relwidth=0.15, relheight=0.025)
        # Label e Combobox Tipo
        self.lb_tipo_aba_01 = Label(self.frame_endereco_aba_01, text="Tipo", bg="#1b39a9", fg="lightgrey")
        self.lb_tipo_aba_01['font'] = "Arial", 11
        self.lb_tipo_aba_01.place(relx=0.01, rely=0.1, relwidth=0.04, relheight=0.13)

        self.carrega_listas()
        self.combo_Tipo_aba_01 = ttk.Combobox(self.frame_endereco_aba_01, values=self.lista_tipo)
        self.combo_Tipo_aba_01['font'] = "Arial", 12
        self.combo_Tipo_aba_01.place(relx=0.01, rely=0.27, relwidth=0.08)# relheight=0.18)

        # Label e Entry - Logradouro
        self.lb_logradouro_aba_01 = Label(self.frame_endereco_aba_01, text="Logradouro", bg="#1b39a9", fg="lightgrey")
        self.lb_logradouro_aba_01['font'] = "Arial", 11
        self.lb_logradouro_aba_01.place(relx=0.1, rely=0.1, relwidth=0.09, relheight=0.13)

        self.entry_logradouro_aba_01 = Entry(self.frame_endereco_aba_01, bg="#345574", fg="lightgrey")
        self.entry_logradouro_aba_01['font'] = "Arial", 12
        self.entry_logradouro_aba_01.place(relx=0.1, rely=0.27, relwidth=0.3)# relheight=0.18)

        # Label e Entry Nº
        self.lb_numero_aba_01 = Label(self.frame_endereco_aba_01, text="Nº", bg="#1b39a9", fg="lightgrey")
        self.lb_numero_aba_01['font'] = "Arial", 11
        self.lb_numero_aba_01.place(relx=0.4, rely=0.1, relwidth=0.04, relheight=0.13)

        self.entry_numero_aba_01 = Entry(self.frame_endereco_aba_01, bg="#345574", fg="lightgrey")
        self.entry_numero_aba_01['font'] = "Arial", 12
        self.entry_numero_aba_01.place(relx=0.409, rely=0.27, relwidth=0.05)# relheight=0.18)

        # Label e Entry Complemento
        self.lb_complemento_aba_01 = Label(self.frame_endereco_aba_01, text="Complemento", bg="#1b39a9", fg="lightgrey")
        self.lb_complemento_aba_01['font'] = "Arial", 11
        self.lb_complemento_aba_01.place(relx=0.465, rely=0.1, relwidth=0.1, relheight=0.13)

        self.entry_complemento_aba_01 = Entry(self.frame_endereco_aba_01, bg="#345574", fg="lightgrey")
        self.entry_complemento_aba_01['font'] = "Arial", 12
        self.entry_complemento_aba_01.place(relx=0.465, rely=0.27, relwidth=0.095)# relheight=0.18)

        # Label e Entry Bairro
        self.lb_bairro_aba_01 = Label(self.frame_endereco_aba_01, text="Bairro", bg="#1b39a9", fg="lightgrey")
        self.lb_bairro_aba_01['font'] = "Arial", 11
        self.lb_bairro_aba_01.place(relx=0.01, rely=0.5, relwidth=0.05, relheight=0.13)

        self.entry_bairro_aba_01 = Entry(self.frame_endereco_aba_01, bg="#345574", fg="lightgrey")
        self.entry_bairro_aba_01['font'] = "Arial", 12
        self.entry_bairro_aba_01.place(relx=0.01, rely=0.66, relwidth=0.15)# relheight=0.18)

        # Label e Entry Cidade
        self.lb_cidade_aba_01 = Label(self.frame_endereco_aba_01, text="Cidade", bg="#1b39a9", fg="lightgrey")
        self.lb_cidade_aba_01['font'] = "Arial", 11
        self.lb_cidade_aba_01.place(relx=0.17, rely=0.5, relwidth=0.07, relheight=0.13)

        self.entry_cidade_aba_01 = Entry(self.frame_endereco_aba_01, bg="#345574", fg="lightgrey")
        self.entry_cidade_aba_01['font'] = "Arial", 12
        self.entry_cidade_aba_01.place(relx=0.17, rely=0.66, relwidth=0.15)# relheight=0.18)

        # Label e Combobox UF
        self.lb_UF_aba_01 = Label(self.frame_endereco_aba_01, text="UF", bg="#1b39a9", fg="lightgrey")
        self.lb_UF_aba_01['font'] = "Arial", 11
        self.lb_UF_aba_01.place(relx=0.33, rely=0.5, relwidth=0.03, relheight=0.13)

        self.combo_UF_aba_01 = ttk.Combobox(self.frame_endereco_aba_01, values=self.lista_UF)
        self.combo_UF_aba_01['font'] = "Arial", 12
        self.combo_UF_aba_01.place(relx=0.33, rely=0.66, relwidth=0.05)# relheight=0.18)

        self.lb_CEP_aba_01 = Label(self.frame_endereco_aba_01, text="CEP", bg="#1b39a9", fg="lightgrey")
        self.lb_CEP_aba_01['font'] = "Arial", 11
        self.lb_CEP_aba_01.place(relx=0.45, rely=0.5, relwidth=0.03, relheight=0.13)

        self.entry_CEP01_aba_01 = Entry(self.frame_endereco_aba_01, bg="#345574", fg="lightgrey", width=5)
        self.entry_CEP01_aba_01['font'] = "Arial", 12
        self.entry_CEP01_aba_01.place(relx=0.45, rely=0.66, relwidth=0.05)# relheight=0.18)

        self.lb_separaCep_aba_01 = Label(self.frame_endereco_aba_01, text="-", bg="#1b39a9", fg="lightgrey")
        self.lb_separaCep_aba_01['font'] = "Arial", 12
        self.lb_separaCep_aba_01.place(relx=0.508, rely=0.667, relwidth=0.01, relheight=0.13)

        self.entry_CEP02_aba_01 = Entry(self.frame_endereco_aba_01, bg="#345574", fg="lightgrey", width=3)
        self.entry_CEP02_aba_01['font'] = "Arial", 12
        self.entry_CEP02_aba_01.place(relx=0.523, rely=0.66, relwidth=0.035)# relheight=0.18)

        # Botão Adiciona
        self.btn_adiciona_aba_01 = Button(self.aba_01, text="Adiciona", bg="lightblue", fg="black", command=self.add_locador)
        self.btn_adiciona_aba_01['font'] = "Arial", 9
        self.btn_adiciona_aba_01.place(relx=0.05, rely=0.66, relwidth=0.08, relheight=0.04)
        # Botão Atualiza
        self.btn_atualiza_aba_01 = Button(self.aba_01, text="Atualiza", bg="lightblue", fg="black", command=self.atualiza_Cadastro_aba_01)
        self.btn_atualiza_aba_01['font'] = "Arial", 9
        self.btn_atualiza_aba_01.place(relx=0.135, rely=0.66, relwidth=0.08, relheight=0.04)
        # Botão Delete
        self.btn_remove_aba_01 = Button(self.aba_01, text="Remove", bg="lightblue", fg="black", command=self.remove_Cadastro_aba_01)
        self.btn_remove_aba_01['font'] = "Arial", 9
        self.btn_remove_aba_01.place(relx=0.219, rely=0.66, relwidth=0.08, relheight=0.04)
        # Botão limpar
        self.btn_limpaCampos_aba_01 = Button(self.aba_01, text="Limpar Casas", bg="lightblue", fg="black", command=self.limpa_aba_01)
        self.btn_limpaCampos_aba_01['font'] = "Arial", 9
        self.btn_limpaCampos_aba_01.place(relx=0.303, rely=0.66, relwidth=0.1, relheight=0.04)

        self.lb_frase_clique_aba_01 = Label(self.aba_01, text="Clique Duplo sobre o registro para visualizar todos os dados.", bg="#1b39a9", fg="lightgrey")
        self.lb_frase_clique_aba_01['font'] = "Arial", 11
        self.lb_frase_clique_aba_01.place(relx=0.3, rely=0.95)
    
    def treeview_aba01(self):
        self.tview_aba_01 = ttk.Treeview(self.aba_01, height=3, 
        column=("col1", "col2", "col3"))
        # ID, nome, data_nasc, CPF
        self.tview_aba_01.heading("#0", text="")
        self.tview_aba_01.heading("#1", text="Nome")
        self.tview_aba_01.heading("#2", text="CPF")
        self.tview_aba_01.heading("#3", text="Data Nascimento")

        # Largura de cada coluna
        self.tview_aba_01.column("#0", width=0)
        self.tview_aba_01.column("#1", width=300)
        self.tview_aba_01.column("#2", width=100)
        self.tview_aba_01.column("#3", width=80)
        self.tview_aba_01.place(relx=0.018, rely=0.71, relwidth=0.95, relheight=0.24)

        # Barra de Rolagem
        self.barra_rolagem_aba_01 = Scrollbar(self.aba_01, orient="vertical")
        self.tview_aba_01.configure(yscroll=self.barra_rolagem_aba_01.set)
        self.barra_rolagem_aba_01.place(relx=0.965, rely=0.71, relwidth=0.015, relheight=0.24)

        # Binding Evento Clique Duplo Aba 01
        self.tview_aba_01.bind("<Double-1>", self.clique_duplo_aba_01)
    
    def widgets_aba_02(self):
        # Label - Cadastro de Inquilinos
        self.lb_titulo_aba_02 = Label(self.aba_02, text="Cadastro de Locador / Inquilino", bg="#0e47a1", fg="lightgrey")
        self.lb_titulo_aba_02['font'] = "Arial", 14
        self.lb_titulo_aba_02.place(relx=0.35, rely=0.01, relwidth=0.3, relheight=0.03)

        """Frame Dados Pessoais"""
        self.frame_dados_pessoais_aba_02 = Frame(self.aba_02, bg="#1b39a9", highlightbackground="lightgrey", highlightthickness=1)
        self.frame_dados_pessoais_aba_02.place(relx=0.02, rely=0.05, relwidth=0.96, relheight=0.3)

        # Label Dados Pessoais
        self.lb_dados_pessoais_aba_02 = Label(self.aba_02, text="Dados Pessoais / Locador", bg="#1b39a9", fg="lightgrey")
        self.lb_dados_pessoais_aba_02['font'] = "Arial", 12
        self.lb_dados_pessoais_aba_02.place(relx=0.03, rely=0.035, relwidth=0.2, relheight=0.025)

        # Label Nome e Entry nome Aba 02
        self.lb_nome_aba_02 = Label(self.frame_dados_pessoais_aba_02, text="Nome Completo", bg="#1b39a9", fg="lightgrey")
        self.lb_nome_aba_02['font'] = "Arial", 11
        self.lb_nome_aba_02.place(relx=0.01, rely=0.07, relwidth=0.12, relheight=0.1)
        
        self.entry_nome_aba_02 = Entry(self.frame_dados_pessoais_aba_02, bg="#345574", fg="lightgrey")
        self.entry_nome_aba_02['font'] = "Arial", 12
        self.entry_nome_aba_02.focus_force()
        self.entry_nome_aba_02.place(relx=0.01, rely=0.22, relwidth=0.25)# relheight=0.18)

        # Label e Entry Nacionalidade
        self.lb_nacionalidade_aba_02 = Label(self.frame_dados_pessoais_aba_02, text="Nacionalidade", bg="#1b39a9", fg="lightgrey")
        self.lb_nacionalidade_aba_02['font'] = "Arial", 11
        self.lb_nacionalidade_aba_02.place(relx=0.27, rely=0.07, relwidth=0.11, relheight=0.1)

        self.entry_nacionalidade_aba_02 = Entry(self.frame_dados_pessoais_aba_02, bg="#345574", fg="lightgrey")
        self.entry_nacionalidade_aba_02['font'] = "Arial", 12
        self.entry_nacionalidade_aba_02.place(relx=0.27, rely=0.22, relwidth=0.12)# relheight=0.18)

        # Label e Combobox - Estado Civil
        self.lb_estCivil_aba_02 = Label(self.frame_dados_pessoais_aba_02, text="Estado Civil", bg="#1b39a9", fg="lightgrey")
        self.lb_estCivil_aba_02['font'] = "Arial", 11
        self.lb_estCivil_aba_02.place(relx=0.4, rely=0.07, relwidth=0.09, relheight=0.1)

        self.est_civis = ["Casado(a)", "Solteiro(a)", "Divorciado(a)", "Viúvo(a)"]
        self.combo_estadoCivil_aba_02 = ttk.Combobox(self.frame_dados_pessoais_aba_02, values=self.est_civis)
        self.combo_estadoCivil_aba_02['font'] = "Arial", 12
        self.combo_estadoCivil_aba_02.place(relx=0.4, rely=0.22, relwidth=0.12)# relheight=0.18)

        # Label e Entry ID
        self.lb_id_aba_02 = Label(self.frame_dados_pessoais_aba_02, text="ID", bg="#1b39a9", fg="lightgrey")
        self.lb_id_aba_02['font'] = "Arial", 11
        self.lb_id_aba_02.place(relx=0.52, rely=0.07, relwidth=0.04, relheight=0.1)

        self.entry_ID_aba_02 = Entry(self.frame_dados_pessoais_aba_02, bg="#345574", fg="lightgrey")
        self.entry_ID_aba_02['font'] = "Arial", 12
        self.entry_ID_aba_02.place(relx=0.53, rely=0.22, relwidth=0.03)# relheight=0.18)

        # Label e Entry Profissão
        self.lb_profissao_aba_02 = Label(self.frame_dados_pessoais_aba_02, text="Profissão", bg="#1b39a9", fg="lightgrey")
        self.lb_profissao_aba_02['font'] = "Arial", 11
        self.lb_profissao_aba_02.place(relx=0.01, rely=0.47, relwidth=0.082, relheight=0.1)

        self.entry_profissao_aba_02 = Entry(self.frame_dados_pessoais_aba_02, bg="#345574", fg="lightgrey")
        self.entry_profissao_aba_02['font'] = "Arial", 12
        self.entry_profissao_aba_02.place(relx=0.01, rely=0.63, relwidth=0.17)# relheight=0.18)

        # Label e Entry RG
        self.lb_rg_aba_02 = Label(self.frame_dados_pessoais_aba_02, text="RG", bg="#1b39a9", fg="lightgrey")
        self.lb_rg_aba_02['font'] = "Arial", 11
        self.lb_rg_aba_02.place(relx=0.105, rely=0.47, relwidth=0.2, relheight=0.1)

        self.entry_rg_aba_02 = Entry(self.frame_dados_pessoais_aba_02, bg="#345574", fg="lightgrey")
        self.entry_rg_aba_02['font'] = "Arial", 12
        self.entry_rg_aba_02.place(relx=0.187, rely=0.63, relwidth=0.085)# relheight=0.18)
    
        # Label e Entry CPF <- Terá função de validação de formatação de CPF
        self.lb_cpf_aba_02 = Label(self.frame_dados_pessoais_aba_02, text="CPF", bg="#1b39a9", fg="lightgrey")
        self.lb_cpf_aba_02['font'] = "Arial", 11
        self.lb_cpf_aba_02.place(relx=0.275, rely=0.47, relwidth=0.05, relheight=0.1)

        self.entry_cpf_aba_02 = Entry(self.frame_dados_pessoais_aba_02, width=12, bg="#345574", fg="lightgrey")
        self.entry_cpf_aba_02['font'] = "Arial", 12
        self.entry_cpf_aba_02.place(relx=0.279, rely=0.63, relwidth=0.11)# relheight=0.18)

        # Label e Combobox = Data Nascimento
        self.lb_data_nasc_aba_02 = Label(self.frame_dados_pessoais_aba_02, text="Data Nasc.", bg="#1b39a9", fg="lightgrey")
        self.lb_data_nasc_aba_02['font'] = "Arial", 11
        self.lb_data_nasc_aba_02.place(relx=0.399, rely=0.47, relwidth=0.09, relheight=0.1)

        
        self.carrega_listas()
        self.combo_data_nasc_DIA_aba_02 = ttk.Combobox(self.frame_dados_pessoais_aba_02, values=self.lista_dia)
        self.combo_data_nasc_DIA_aba_02['font'] = "Arial", 12
        self.combo_data_nasc_DIA_aba_02.place(relx=0.4, rely=0.63, relwidth=0.037)# relheight=0.18)

        self.combo_data_nasc_MES_aba_02 = ttk.Combobox(self.frame_dados_pessoais_aba_02, values=self.lista_mes)
        self.combo_data_nasc_MES_aba_02['font'] = "Arial", 12
        self.combo_data_nasc_MES_aba_02.place(relx=0.45, rely=0.63, relwidth=0.037)# relheight=0.18)

        self.combo_data_nasc_ANO_aba_02 = ttk.Combobox(self.frame_dados_pessoais_aba_02, values=self.lista_ano)
        self.combo_data_nasc_ANO_aba_02['font'] = "Arial", 12
        self.combo_data_nasc_ANO_aba_02.place(relx=0.504, rely=0.63, relwidth=0.055)# relheight=0.18)

        """Frame Endereço do Locador"""
        self.frame_endereco_aba_02 = Frame(self.aba_02, bg="#1b39a9", highlightbackground="lightgrey", highlightthickness=1)
        self.frame_endereco_aba_02.place(relx=0.02, rely=0.38, relwidth=0.96, relheight=0.3)

        # Label Endereço Locador
        self.lb_titulo_endereco_aba_02 = Label(self.aba_02, text="Endereço / Locador", bg="#1b39a9", fg="lightgrey")
        self.lb_titulo_endereco_aba_02['font'] = "Arial", 11
        self.lb_titulo_endereco_aba_02.place(relx=0.03, rely=0.365, relwidth=0.15, relheight=0.025)
        # Label e Combobox Tipo
        self.lb_tipo_aba_02 = Label(self.frame_endereco_aba_02, text="Tipo", bg="#1b39a9", fg="lightgrey")
        self.lb_tipo_aba_02['font'] = "Arial", 11
        self.lb_tipo_aba_02.place(relx=0.01, rely=0.1, relwidth=0.04, relheight=0.13)

        self.carrega_listas()
        self.combo_Tipo_aba_02 = ttk.Combobox(self.frame_endereco_aba_02, values=self.lista_tipo)
        self.combo_Tipo_aba_02['font'] = "Arial", 12
        self.combo_Tipo_aba_02.place(relx=0.01, rely=0.27, relwidth=0.08)# relheight=0.18)

        # Label e Entry - Logradouro
        self.lb_logradouro_aba_02 = Label(self.frame_endereco_aba_02, text="Logradouro", bg="#1b39a9", fg="lightgrey")
        self.lb_logradouro_aba_02['font'] = "Arial", 11
        self.lb_logradouro_aba_02.place(relx=0.1, rely=0.1, relwidth=0.09, relheight=0.13)

        self.entry_logradouro_aba_02 = Entry(self.frame_endereco_aba_02, bg="#345574", fg="lightgrey")
        self.entry_logradouro_aba_02['font'] = "Arial", 12
        self.entry_logradouro_aba_02.place(relx=0.1, rely=0.27, relwidth=0.3)# relheight=0.18)

        # Label e Entry Nº
        self.lb_numero_aba_02 = Label(self.frame_endereco_aba_02, text="Nº", bg="#1b39a9", fg="lightgrey")
        self.lb_numero_aba_02['font'] = "Arial", 11
        self.lb_numero_aba_02.place(relx=0.4, rely=0.1, relwidth=0.04, relheight=0.13)

        self.entry_numero_aba_02 = Entry(self.frame_endereco_aba_02, bg="#345574", fg="lightgrey")
        self.entry_numero_aba_02['font'] = "Arial", 12
        self.entry_numero_aba_02.place(relx=0.409, rely=0.27, relwidth=0.05)# relheight=0.18)

        # Label e Entry Complemento
        self.lb_complemento_aba_02 = Label(self.frame_endereco_aba_02, text="Complemento", bg="#1b39a9", fg="lightgrey")
        self.lb_complemento_aba_02['font'] = "Arial", 11
        self.lb_complemento_aba_02.place(relx=0.465, rely=0.1, relwidth=0.1, relheight=0.13)

        self.entry_complemento_aba_02 = Entry(self.frame_endereco_aba_02, bg="#345574", fg="lightgrey")
        self.entry_complemento_aba_02['font'] = "Arial", 12
        self.entry_complemento_aba_02.place(relx=0.465, rely=0.27, relwidth=0.095)# relheight=0.18)

        # Label e Entry Bairro
        self.lb_bairro_aba_02 = Label(self.frame_endereco_aba_02, text="Bairro", bg="#1b39a9", fg="lightgrey")
        self.lb_bairro_aba_02['font'] = "Arial", 11
        self.lb_bairro_aba_02.place(relx=0.01, rely=0.5, relwidth=0.05, relheight=0.13)

        self.entry_bairro_aba_02 = Entry(self.frame_endereco_aba_02, bg="#345574", fg="lightgrey")
        self.entry_bairro_aba_02['font'] = "Arial", 12
        self.entry_bairro_aba_02.place(relx=0.01, rely=0.66, relwidth=0.15)# relheight=0.18)

        # Label e Entry Cidade
        self.lb_cidade_aba_02 = Label(self.frame_endereco_aba_02, text="Cidade", bg="#1b39a9", fg="lightgrey")
        self.lb_cidade_aba_02['font'] = "Arial", 11
        self.lb_cidade_aba_02.place(relx=0.17, rely=0.5, relwidth=0.07, relheight=0.13)

        self.entry_cidade_aba_02 = Entry(self.frame_endereco_aba_02, bg="#345574", fg="lightgrey")
        self.entry_cidade_aba_02['font'] = "Arial", 12
        self.entry_cidade_aba_02.place(relx=0.17, rely=0.66, relwidth=0.15)# relheight=0.18)

        # Label e Combobox UF
        self.lb_UF_aba_02 = Label(self.frame_endereco_aba_02, text="UF", bg="#1b39a9", fg="lightgrey")
        self.lb_UF_aba_02['font'] = "Arial", 11
        self.lb_UF_aba_02.place(relx=0.33, rely=0.5, relwidth=0.03, relheight=0.13)

        self.combo_UF_aba_02 = ttk.Combobox(self.frame_endereco_aba_02, values=self.lista_UF)
        self.combo_UF_aba_02['font'] = "Arial", 12
        self.combo_UF_aba_02.place(relx=0.33, rely=0.66, relwidth=0.05)# relheight=0.18)

        self.lb_CEP_aba_02 = Label(self.frame_endereco_aba_02, text="CEP", bg="#1b39a9", fg="lightgrey")
        self.lb_CEP_aba_02['font'] = "Arial", 11
        self.lb_CEP_aba_02.place(relx=0.45, rely=0.5, relwidth=0.03, relheight=0.13)

        self.entry_CEP01_aba_02 = Entry(self.frame_endereco_aba_02, bg="#345574", fg="lightgrey", width=5)
        self.entry_CEP01_aba_02['font'] = "Arial", 12
        self.entry_CEP01_aba_02.place(relx=0.45, rely=0.66, relwidth=0.05)# relheight=0.18)

        self.lb_separaCep_aba_02 = Label(self.frame_endereco_aba_02, text="-", bg="#1b39a9", fg="lightgrey")
        self.lb_separaCep_aba_02['font'] = "Arial", 12
        self.lb_separaCep_aba_02.place(relx=0.508, rely=0.667, relwidth=0.01, relheight=0.13)

        self.entry_CEP02_aba_02 = Entry(self.frame_endereco_aba_02, bg="#345574", fg="lightgrey", width=3)
        self.entry_CEP02_aba_02['font'] = "Arial", 12
        self.entry_CEP02_aba_02.place(relx=0.523, rely=0.66, relwidth=0.035)# relheight=0.18)

        # Botão Adiciona
        self.btn_adiciona_aba_02 = Button(self.aba_02, text="Adiciona", bg="lightblue", fg="black", command=self.add_locatario)
        self.btn_adiciona_aba_02['font'] = "Arial", 9
        self.btn_adiciona_aba_02.place(relx=0.05, rely=0.66, relwidth=0.08, relheight=0.04)
        # Botão Atualiza
        self.btn_atualiza_aba_02 = Button(self.aba_02, text="Atualiza", bg="lightblue", fg="black", command=self.atualiza_Cadastro_aba_02)
        self.btn_atualiza_aba_02['font'] = "Arial", 9
        self.btn_atualiza_aba_02.place(relx=0.135, rely=0.66, relwidth=0.08, relheight=0.04)
        # Botão Delete
        self.btn_remove_aba_02 = Button(self.aba_02, text="Remove", bg="lightblue", fg="black", command=self.remove_Cadastro_aba_02)
        self.btn_remove_aba_02['font'] = "Arial", 9
        self.btn_remove_aba_02.place(relx=0.219, rely=0.66, relwidth=0.08, relheight=0.04)
        # Botão limpar
        self.btn_limpaCampos_aba_02 = Button(self.aba_02, text="Limpar Casas", bg="lightblue", fg="black", command=self.limpa_aba_02)
        self.btn_limpaCampos_aba_02['font'] = "Arial", 9
        self.btn_limpaCampos_aba_02.place(relx=0.303, rely=0.66, relwidth=0.1, relheight=0.04)

        self.lb_frase_clique_aba_02 = Label(self.aba_02, text="Clique Duplo sobre o registro para visualizar todos os dados.", bg="#1b39a9", fg="lightgrey")
        self.lb_frase_clique_aba_02['font'] = "Arial", 11
        self.lb_frase_clique_aba_02.place(relx=0.3, rely=0.95)
    
    def treeview_aba02(self):
        self.tview_aba_02 = ttk.Treeview(self.aba_02, height=3, 
        column=("col1", "col2", "col3"))
        # ID, nome, data_nasc, CPF
        self.tview_aba_02.heading("#0", text="")
        self.tview_aba_02.heading("#1", text="Nome")
        self.tview_aba_02.heading("#2", text="CPF")
        self.tview_aba_02.heading("#3", text="Data Nascimento")

        # Largura de cada coluna
        self.tview_aba_02.column("#0", width=0)
        self.tview_aba_02.column("#1", width=300)
        self.tview_aba_02.column("#2", width=100)
        self.tview_aba_02.column("#3", width=80)
        self.tview_aba_02.place(relx=0.018, rely=0.71, relwidth=0.95, relheight=0.24)

        # Barra de Rolagem
        self.barra_rolagem_aba_02 = Scrollbar(self.aba_02, orient="vertical")
        self.tview_aba_02.configure(yscroll=self.barra_rolagem_aba_02.set)
        self.barra_rolagem_aba_02.place(relx=0.965, rely=0.71, relwidth=0.015, relheight=0.24)
        
        # Binding Evento Clique Duplo Aba 01
        self.tview_aba_02.bind("<Double-1>", self.clique_duplo_aba_02)

    def widgets_aba_03(self):
        # Label - Cadastro de Contratos
        self.lb_titulo_aba_03 = Label(self.aba_03, text='Cadastro de Imóveis', bg="#0e47a1", fg="lightgrey")
        self.lb_titulo_aba_03['font'] = "Arial", 14
        self.lb_titulo_aba_03.place(relx=0.35, rely=0.01, relwidth=0.3, relheight=0.03)

        """Frame Dados do Imóvel"""
        self.frame_dados_imovel_aba_03 = Frame(self.aba_03, bg="#1b39a9", highlightbackground="lightgrey", highlightthickness=1)
        self.frame_dados_imovel_aba_03.place(relx=0.02, rely=0.05, relwidth=0.96, relheight=0.35)

        # Label Dados Pessoais
        self.lb_dados_imovel_aba_03 = Label(self.aba_03, text="Dados do Imóvel", bg="#1b39a9", fg="lightgrey")
        self.lb_dados_imovel_aba_03['font'] = "Arial", 12
        self.lb_dados_imovel_aba_03.place(relx=0.03, rely=0.035, relwidth=0.14, relheight=0.025)

         # Label e Combobox tipo do imóvel
        self.lb_tipo_imovel_aba_03 = Label(self.frame_dados_imovel_aba_03, text="Utilização", bg="#1b39a9", fg="lightgrey")
        self.lb_tipo_imovel_aba_03['font'] = "Arial", 11
        self.lb_tipo_imovel_aba_03.place(relx=0.001, rely=0.04, relwidth=0.08, relheight=0.1)

        self.carrega_listas()
        self.combo_tipo_imovel_aba_03 = ttk.Combobox(self.frame_dados_imovel_aba_03, values=self.lista_tipo_imovel)
        self.combo_tipo_imovel_aba_03['font'] = "Arial", 12
        self.combo_tipo_imovel_aba_03.place(relx=0.01, rely=0.16, relwidth=0.1)

        # Label e Entry Área M²
        self.lb_area_aba_03 = Label(self.frame_dados_imovel_aba_03, text="Área (m²)", bg="#1b39a9", fg="lightgrey")
        self.lb_area_aba_03['font'] = "Arial", 11
        self.lb_area_aba_03.place(relx=0.12, rely=0.04, relwidth=0.08, relheight=0.1)

        self.entry_area_aba_03 = Entry(self.frame_dados_imovel_aba_03, bg="#345574", fg="lightgrey")
        self.entry_area_aba_03['font'] = "Arial", 12
        self.entry_area_aba_03.place(relx=0.12, rely=0.16, relwidth=0.08)

        # Label e Combobox W.C
        self.lb_WC_aba_03 = Label(self.frame_dados_imovel_aba_03, text="W.C", bg="#1b39a9", fg="lightgrey")
        self.lb_WC_aba_03['font'] = "Arial", 11
        self.lb_WC_aba_03.place(relx=0.21, rely=0.04, relwidth=0.05, relheight=0.1)

        self.combo_WC_aba_03 = ttk.Combobox(self.frame_dados_imovel_aba_03, values=self.lista_numero_banheiros)
        self.combo_WC_aba_03['font'] = "Arial", 12
        self.combo_WC_aba_03.place(relx=0.21, rely=0.16, relwidth=0.08)

        # Label e Combobox - Garagem Tipo
        self.lb_garagem_tp_aba_03 = Label(self.frame_dados_imovel_aba_03, text='Tipo Garagem', bg="#1b39a9", fg="lightgrey")
        self.lb_garagem_tp_aba_03['font'] = "Arial", 11
        self.lb_garagem_tp_aba_03.place(relx=0.3, rely=0.04, relwidth=0.1, relheight=0.1)

        self.combo_garagem_tp_aba_03 = ttk.Combobox(self.frame_dados_imovel_aba_03, values=self.lista_garagem)
        self.combo_garagem_tp_aba_03['font'] = "Arial", 12
        self.combo_garagem_tp_aba_03.place(relx=0.3, rely=0.16, relwidth=0.2)

        # Label e Entry - Constituída Por
        self.lb_constituida_por_aba_03 = Label(self.frame_dados_imovel_aba_03, text="Constituída por:", bg="#1b39a9", fg="lightgrey")
        self.lb_constituida_por_aba_03['font'] = "Arial", 11
        self.lb_constituida_por_aba_03.place(relx=0.5, rely=0.04, relwidth=0.12, relheight=0.1)

        self.entry_constituida_por_aba_03 = Entry(self.frame_dados_imovel_aba_03, bg="#345574", fg="lightgrey")
        self.entry_constituida_por_aba_03['font'] = "Arial", 12
        self.entry_constituida_por_aba_03.place(relx=0.508, rely=0.16, relwidth=0.1)

        """Widgets de entrada de Endereço"""
        # Label e Combobox - Tipo de Imóvel
        self.lb_tipo_aba_03 = Label(self.frame_dados_imovel_aba_03, text="Tipo", bg="#1b39a9", fg="lightgrey")
        self.lb_tipo_aba_03['font'] = "Arial", 11
        self.lb_tipo_aba_03.place(relx=0.01, rely=0.31, relwidth=0.03, relheight=0.1)

        self.carrega_listas()
        self.combo_Tipo_aba_03 = ttk.Combobox(self.frame_dados_imovel_aba_03, values=self.lista_tipo)
        self.combo_Tipo_aba_03['font'] = "Arial", 12
        self.combo_Tipo_aba_03.place(relx=0.01, rely=0.43, relwidth=0.1)# relheight=0.18)

        # Label e Entry - Logradouro
        self.lb_logradouro_aba_03 = Label(self.frame_dados_imovel_aba_03, text="Logradouro", bg="#1b39a9", fg="lightgrey")
        self.lb_logradouro_aba_03['font'] = "Arial", 11
        self.lb_logradouro_aba_03.place(relx=0.12, rely=0.31, relwidth=0.08, relheight=0.1)

        self.entry_logradouro_aba_03 = Entry(self.frame_dados_imovel_aba_03, bg="#345574", fg="lightgrey")
        self.entry_logradouro_aba_03['font'] = "Arial", 12
        self.entry_logradouro_aba_03.place(relx=0.12, rely=0.43, relwidth=0.325)# relheight=0.18)

        # Label e Entry Nº
        self.lb_numero_aba_03 = Label(self.frame_dados_imovel_aba_03, text="Nº", bg="#1b39a9", fg="lightgrey")
        self.lb_numero_aba_03['font'] = "Arial", 11
        self.lb_numero_aba_03.place(relx=0.455, rely=0.31, relwidth=0.02, relheight=0.1)

        self.entry_numero_aba_03 = Entry(self.frame_dados_imovel_aba_03, bg="#345574", fg="lightgrey")
        self.entry_numero_aba_03['font'] = "Arial", 12
        self.entry_numero_aba_03.place(relx=0.45, rely=0.43, relwidth=0.05)# relheight=0.18)

        # Label e Entry Complemento
        self.lb_complemento_aba_03 = Label(self.frame_dados_imovel_aba_03, text="Complemento", bg="#1b39a9", fg="lightgrey")
        self.lb_complemento_aba_03['font'] = "Arial", 11
        self.lb_complemento_aba_03.place(relx=0.505, rely=0.31, relwidth=0.1, relheight=0.1)

        self.entry_complemento_aba_03 = Entry(self.frame_dados_imovel_aba_03, bg="#345574", fg="lightgrey")
        self.entry_complemento_aba_03['font'] = "Arial", 12
        self.entry_complemento_aba_03.place(relx=0.508, rely=0.43, relwidth=0.1)# relheight=0.18)

        # Label e Entry Bairro
        self.lb_bairro_aba_03 = Label(self.frame_dados_imovel_aba_03, text="Bairro", bg="#1b39a9", fg="lightgrey")
        self.lb_bairro_aba_03['font'] = "Arial", 11
        self.lb_bairro_aba_03.place(relx=0.01, rely=0.58, relwidth=0.04, relheight=0.1)

        self.entry_bairro_aba_03 = Entry(self.frame_dados_imovel_aba_03, bg="#345574", fg="lightgrey")
        self.entry_bairro_aba_03['font'] = "Arial", 12
        self.entry_bairro_aba_03.place(relx=0.01, rely=0.7, relwidth=0.11)# relheight=0.18)

        # Label e Entry Cidade
        self.lb_cidade_aba_03 = Label(self.frame_dados_imovel_aba_03, text="Cidade", bg="#1b39a9", fg="lightgrey")
        self.lb_cidade_aba_03['font'] = "Arial", 11
        self.lb_cidade_aba_03.place(relx=0.13, rely=0.58, relwidth=0.05, relheight=0.1)

        self.entry_cidade_aba_03 = Entry(self.frame_dados_imovel_aba_03, bg="#345574", fg="lightgrey")
        self.entry_cidade_aba_03['font'] = "Arial", 12
        self.entry_cidade_aba_03.place(relx=0.128, rely=0.7, relwidth=0.15)# relheight=0.18)

        # Label e Combobox UF
        self.lb_UF_aba_03 = Label(self.frame_dados_imovel_aba_03, text="UF", bg="#1b39a9", fg="lightgrey")
        self.lb_UF_aba_03['font'] = "Arial", 11
        self.lb_UF_aba_03.place(relx=0.29, rely=0.58, relwidth=0.02, relheight=0.1)

        self.combo_UF_aba_03 = ttk.Combobox(self.frame_dados_imovel_aba_03, values=self.lista_UF)
        self.combo_UF_aba_03['font'] = "Arial", 12
        self.combo_UF_aba_03.place(relx=0.287, rely=0.7, relwidth=0.04)# relheight=0.18)

        self.lb_CEP_aba_03 = Label(self.frame_dados_imovel_aba_03, text="CEP", bg="#1b39a9", fg="lightgrey")
        self.lb_CEP_aba_03['font'] = "Arial", 11
        self.lb_CEP_aba_03.place(relx=0.455, rely=0.58, relwidth=0.03, relheight=0.1)

        self.entry_CEP01_aba_03 = Entry(self.frame_dados_imovel_aba_03, bg="#345574", fg="lightgrey", width=5)
        self.entry_CEP01_aba_03['font'] = "Arial", 12
        self.entry_CEP01_aba_03.place(relx=0.45, rely=0.7, relwidth=0.05)# relheight=0.18)

        self.lb_separaCep_aba_03 = Label(self.frame_dados_imovel_aba_03, text="-", bg="#1b39a9", fg="lightgrey")
        self.lb_separaCep_aba_03['font'] = "Arial", 12
        self.lb_separaCep_aba_03.place(relx=0.5, rely=0.71, relwidth=0.01, relheight=0.1)

        self.entry_CEP02_aba_03 = Entry(self.frame_dados_imovel_aba_03, bg="#345574", fg="lightgrey", width=3)
        self.entry_CEP02_aba_03['font'] = "Arial", 12
        self.entry_CEP02_aba_03.place(relx=0.51, rely=0.7, relwidth=0.034)# relheight=0.18)

        # Label e Entry ID
        self.lb_id_aba_03 = Label(self.frame_dados_imovel_aba_03, text="ID", bg="#1b39a9", fg="lightgrey")
        self.lb_id_aba_03['font'] = "Arial", 11
        self.lb_id_aba_03.place(relx=0.573, rely=0.58, relwidth=0.02, relheight=0.1)

        self.entry_ID_aba_03 = Entry(self.frame_dados_imovel_aba_03, bg="#345574", fg="lightgrey", width=3)
        self.entry_ID_aba_03['font'] = "Arial", 12
        self.entry_ID_aba_03.place(relx=0.574, rely=0.7)

        # Botões Adiciona - Atualiza - Remove

        """Frame Entrys DB - Para clique Duplo E Alterar"""
        self.btn_adiciona_aba_03 = Button(self.aba_03, text="Adiciona", bg="lightblue", fg="black", command=self.add_imovel)
        self.btn_adiciona_aba_03['font'] = "Arial", 9
        self.btn_adiciona_aba_03.place(relx=0.05, rely=0.38, relwidth=0.08, relheight=0.04)
        # Botão Atualiza
        self.btn_atualiza_aba_03 = Button(self.aba_03, text="Atualiza", bg="lightblue", fg="black", command=self.atualiza_Cadastro_aba_03)
        self.btn_atualiza_aba_03['font'] = "Arial", 9
        self.btn_atualiza_aba_03.place(relx=0.135, rely=0.38, relwidth=0.08, relheight=0.04)
        # Botão Delete
        self.btn_remove_aba_03 = Button(self.aba_03, text="Remove", bg="lightblue", fg="black", command=self.remove_Cadastro_aba_03)
        self.btn_remove_aba_03['font'] = "Arial", 9
        self.btn_remove_aba_03.place(relx=0.219, rely=0.38, relwidth=0.08, relheight=0.04)
         # Botão limpar
        self.btn_limpaCampos_aba_03 = Button(self.aba_03, text="Limpar Casas", bg="lightblue", fg="black", command=self.limpa_aba_03)
        self.btn_limpaCampos_aba_03['font'] = "Arial", 9
        self.btn_limpaCampos_aba_03.place(relx=0.303, rely=0.38, relwidth=0.1, relheight=0.04)

        self.lb_frase_clique_aba_03 = Label(self.aba_03, text="Clique Duplo sobre o registro para visualizar todos os dados.", bg="#1b39a9", fg="lightgrey")
        self.lb_frase_clique_aba_03['font'] = "Arial", 11
        self.lb_frase_clique_aba_03.place(relx=0.3, rely=0.95)

    def treeview_aba03(self):
        self.tview_aba_03 = ttk.Treeview(self.aba_03, height=3, 
        column=("col1", "col2", "col3", "col4", "col5", "col6", "col7"))
        # ID, nome, data_nasc, CPF
        self.tview_aba_03.heading("#0", text="")
        self.tview_aba_03.heading("#1", text="Tipo")
        self.tview_aba_03.heading("#2", text="Imóvel")
        self.tview_aba_03.heading("#3", text="Logradouro")
        self.tview_aba_03.heading("#4", text="Bairro")
        self.tview_aba_03.heading("#5", text="Cidade")
        self.tview_aba_03.heading("#6", text="UF")
        self.tview_aba_03.heading("#7", text="Alugado")

        # Largura de cada coluna
        self.tview_aba_03.column("#0", width=0)
        self.tview_aba_03.column("#1", width=25)
        self.tview_aba_03.column("#2", width=15)
        self.tview_aba_03.column("#3", width=250)
        self.tview_aba_03.column("#4", width=100)
        self.tview_aba_03.column("#5", width=100)
        self.tview_aba_03.column("#6", width=5)
        self.tview_aba_03.column("#7", width=10)
        self.tview_aba_03.place(relx=0.018, rely=0.43, relwidth=0.95, relheight=0.52)

        # Barra de Rolagem
        self.barra_rolagem_aba_03 = Scrollbar(self.aba_03, orient="vertical")
        self.tview_aba_03.configure(yscroll=self.barra_rolagem_aba_03.set)
        self.barra_rolagem_aba_03.place(relx=0.965, rely=0.43, relwidth=0.015, relheight=0.52)
        
        # Binding Evento Clique Duplo Aba 01
        self.tview_aba_03.bind("<Double-1>", self.clique_duplo_aba_03)


    def widgets_aba_04(self):
        # Label - Cadastro de Contratos
        self.lb_titulo_aba_04 = Label(self.aba_04, text='Cadastro de Contratos', bg="#0e47a1", fg="lightgrey")
        self.lb_titulo_aba_04['font'] = "Arial", 14
        self.lb_titulo_aba_04.place(relx=0.35, rely=0.01, relwidth=0.3, relheight=0.03)
        # Frame esquerda Aba 04
        self.frame_esquerda_aba_04 = Frame(self.aba_04, bg="#1b39a9", highlightbackground="lightgrey", highlightthickness=1)
        self.frame_esquerda_aba_04.place(relx=0.04, rely=0.05, relwidth=0.3, relheight=0.2)
        # Widgets Frame Esquerda
        self.lb_seleciona_locador = Label(self.frame_esquerda_aba_04, text="Selecione o Locador", bg="#0e47a1", fg="lightgrey")
        self.lb_seleciona_locador['font'] = "Arial", 11
        self.lb_seleciona_locador.place(relx=0.01, rely=0.001)
         # Frame meio Aba 04
        self.frame_meio_aba_04 = Frame(self.aba_04, bg="#1b39a9", highlightbackground="lightgrey", highlightthickness=1)
        self.frame_meio_aba_04.place(relx=0.35, rely=0.05, relwidth=0.3, relheight=0.2)
        # Widgets Frame do meio - Label selecionar locatário
        self.lb_seleciona_locatario = Label(self.frame_meio_aba_04, text="Selecione o Locatário", bg="#0e47a1", fg="lightgrey")
        self.lb_seleciona_locatario['font'] = "Arial", 11
        self.lb_seleciona_locatario.place(relx=0.01, rely=0.001)
        # Frame Direita Aba 04
        self.frame_direita_aba_04 = Frame(self.aba_04, bg="#1b39a9", highlightbackground="lightgrey", highlightthickness=1)
        self.frame_direita_aba_04.place(relx=0.66, rely=0.05, relwidth=0.3, relheight=0.2)
        # Widgets Frame da Direita
        # Label selecionar imóvel
        self.lb_seleciona_imovel = Label(self.frame_direita_aba_04, text="Selecione o Imóvel", bg="#0e47a1", fg="lightgrey")
        self.lb_seleciona_imovel['font'] = "Arial", 11
        self.lb_seleciona_imovel.place(relx=0.01, rely=0.001)

        # Frame dados contratuais
        self.frame_dados_contratuais_aba_04 = Frame(self.aba_04, bg="#1b39a9", highlightbackground="lightgrey", highlightthickness=1)
        self.frame_dados_contratuais_aba_04.place(relx=0.01, rely=0.28, relwidth=0.98, relheight=0.3)
        # Label Dados Contratuais
        self.lb_dados_contratuais_aba_04 = Label(self.aba_04, text="Cadastra Contratos / Dados Contratuais", bg="#0e47a1", fg="lightgrey")
        self.lb_dados_contratuais_aba_04['font'] = "Arial", 12
        self.lb_dados_contratuais_aba_04.place(relx=0.34, rely=0.262, relwidth=0.3, relheight=0.03)

        # Label e Entry = Locador Nome
        self.lb_locador_nome_aba_04 = Label(self.frame_dados_contratuais_aba_04, text="Nome Locador", bg="#1b39a9", fg="lightgrey")
        self.lb_locador_nome_aba_04['font'] = "Arial", 11
        self.lb_locador_nome_aba_04.place(relx=0.01, rely=0.01)

        self.entry_locador_nome_aba_04 = Entry(self.frame_dados_contratuais_aba_04, bg="#345574", fg="lightgrey")
        self.entry_locador_nome_aba_04['font'] = "Arial", 12
        self.entry_locador_nome_aba_04.focus()
        self.entry_locador_nome_aba_04.place(relx=0.01, rely=0.15, relwidth=0.21)
        # Label e Entry = CPF locador

        self.lb_CPF_locador_aba_04 = Label(self.frame_dados_contratuais_aba_04, text="CPF", bg="#1b39a9", fg="lightgrey")
        self.lb_CPF_locador_aba_04['font'] = "Arial", 11
        self.lb_CPF_locador_aba_04.place(relx=0.225, rely=0.01)

        self.entry_CPF_locador_aba_04 = Entry(self.frame_dados_contratuais_aba_04, bg="#345574", fg="lightgrey")
        self.entry_CPF_locador_aba_04['font'] = "Arial", 12
        self.entry_CPF_locador_aba_04.place(relx=0.225, rely=0.15, relwidth=0.11)
        # Label e Entry = Locatário Nome
        self.lb_locatario_nome_aba_04 = Label(self.frame_dados_contratuais_aba_04, text="Nome Locatário", bg="#1b39a9", fg="lightgrey")
        self.lb_locatario_nome_aba_04['font'] = "Arial", 11
        self.lb_locatario_nome_aba_04.place(relx=0.01, rely=0.33)

        self.entry_locatario_nome_aba_04 = Entry(self.frame_dados_contratuais_aba_04, bg="#345574", fg="lightgrey")
        self.entry_locatario_nome_aba_04['font'] = "Arial", 12
        self.entry_locatario_nome_aba_04.place(relx=0.01, rely=0.47, relwidth=0.21)
        # Label e Entry = CPF locatário
        self.lb_CPF_locatario_aba_04 = Label(self.frame_dados_contratuais_aba_04, text="CPF", bg="#1b39a9", fg="lightgrey")
        self.lb_CPF_locatario_aba_04['font'] = "Arial", 11
        self.lb_CPF_locatario_aba_04.place(relx=0.225, rely=0.33)

        self.entry_CPF_locatario_aba_04 = Entry(self.frame_dados_contratuais_aba_04, bg="#345574", fg="lightgrey")
        self.entry_CPF_locatario_aba_04['font'] = "Arial", 12
        self.entry_CPF_locatario_aba_04.place(relx=0.225, rely=0.47, relwidth=0.11)
        # Label e Entry = Tipo e Imóvel (Sala 04, Apto 05)
        self.lb_imovel_tipo_aba_04 = Label(self.frame_dados_contratuais_aba_04, text="Tipo / Utilização", bg="#1b39a9", fg="lightgrey")
        self.lb_imovel_tipo_aba_04['font'] = "Arial", 11
        self.lb_imovel_tipo_aba_04.place(relx=0.01, rely=0.65)

        self.entry_imovel_tipo_aba_04 = Entry(self.frame_dados_contratuais_aba_04, bg="#345574", fg="lightgrey")
        self.entry_imovel_tipo_aba_04['font'] = "Arial", 12
        self.entry_imovel_tipo_aba_04.place(relx=0.01, rely=0.79, relwidth=0.21)

        self.lb_denominacao_aba_04 = Label(self.frame_dados_contratuais_aba_04, text="Denominado", bg="#1b39a9", fg="lightgrey")
        self.lb_denominacao_aba_04['font'] = "Arial", 11
        self.lb_denominacao_aba_04.place(relx=0.225, rely=0.65)

        self.entry_denominacao_aba_04 = Entry(self.frame_dados_contratuais_aba_04, bg="#345574", fg="lightgrey")
        self.entry_denominacao_aba_04['font'] = "Arial", 12
        self.entry_denominacao_aba_04.place(relx=0.225, rely=0.79, relwidth=0.11)


        # Label e Combobox = Prazo do Contrato (6 ou 12 meses)
        self.lb_prazo_aba_04 = Label(self.frame_dados_contratuais_aba_04, text="Prazo/Contrato", bg="#1b39a9", fg="lightgrey")
        self.lb_prazo_aba_04['font'] = "Arial", 11
        self.lb_prazo_aba_04.place(relx=0.35, rely=0.01)

        self.combo_prazo_aba_04 = ttk.Combobox(self.frame_dados_contratuais_aba_04, values=
        ("Curto - 6 meses", "Normal - 12 meses", "Longo - 3 anos"))
        self.combo_prazo_aba_04['font'] = "Arial", 12
        self.combo_prazo_aba_04.place(relx=0.35, rely=0.15, relwidth=0.15)

        # Label, botão e Entry - Data da Assinatura do Contrato
        self.lb_data_ass_contrato_aba_04 = Label(self.frame_dados_contratuais_aba_04, text="Data Assinatura",  bg="#1b39a9", fg="lightgrey")
        self.lb_data_ass_contrato_aba_04['font'] = "Arial", 11
        self.lb_data_ass_contrato_aba_04.place(relx=0.35, rely=0.33)

        self.btn_insere_data_ass_aba_04 = Button(self.frame_dados_contratuais_aba_04, text="Data>>", bg="lightblue", fg="black", command=self.calendario_data_assinatura_aba_04)
        self.btn_insere_data_ass_aba_04['font'] = "Arial", 11
        self.btn_insere_data_ass_aba_04.place(relx=0.35 , rely=0.47, relwidth=0.065, relheight=0.159)

        self.entry_data_ass_aba_04 = Entry(self.frame_dados_contratuais_aba_04, bg="#345574", fg="lightgrey")
        self.entry_data_ass_aba_04['font'] = "Arial", 12
        self.entry_data_ass_aba_04.place(relx=0.416, rely=0.47, relwidth=0.084)
        # Label, botao e Entry - Data pagamento do cauçao
        self.lb_data_pagto_caucao_aba_04 = Label(self.frame_dados_contratuais_aba_04, text="Data Pagto Caução", bg="#1b39a9", fg="lightgrey")
        self.lb_data_pagto_caucao_aba_04['font'] = "Arial", 11
        self.lb_data_pagto_caucao_aba_04.place(relx=0.35, rely=0.65)

        self.btn_insere_data_caucao_aba_04 = Button(self.frame_dados_contratuais_aba_04, text="Data>>", bg="lightblue", fg="black", command=self.calendario_data_caucao_aba_04)
        self.btn_insere_data_caucao_aba_04['font'] = "Arial", 11
        self.btn_insere_data_caucao_aba_04.place(relx=0.35 , rely=0.79, relwidth=0.065, relheight=0.159)

        self.entry_data_caucao_aba_04 = Entry(self.frame_dados_contratuais_aba_04, bg="#345574", fg="lightgrey")
        self.entry_data_caucao_aba_04['font'] = "Arial", 12
        self.entry_data_caucao_aba_04.place(relx=0.416, rely=0.79, relwidth=0.084)

        # Label e Entry = Valor do Aluguel
        self.lb_valor_aluguel_aba_04 = Label(self.frame_dados_contratuais_aba_04, text="Valor/Mês (R$)", bg="#1b39a9", fg="lightgrey")
        self.lb_valor_aluguel_aba_04['font'] = "Arial", 11
        self.lb_valor_aluguel_aba_04.place(relx=0.515, rely=0.01)

        self.entry_valor_aluguel_aba_04 = Entry(self.frame_dados_contratuais_aba_04, bg="#345574", fg="lightgrey")
        self.entry_valor_aluguel_aba_04['font'] = "Arial", 12
        self.entry_valor_aluguel_aba_04.place(relx=0.515, rely=0.15, relwidth=0.15)
        # Data da Entrega das Chaves
        self.lb_entrega_chaves_aba_04 = Label(self.frame_dados_contratuais_aba_04, text="Entrega das Chaves", bg="#1b39a9", fg="lightgrey")
        self.lb_entrega_chaves_aba_04['font'] = "Arial", 11
        self.lb_entrega_chaves_aba_04.place(relx=0.515, rely=0.33)

        self.btn_data_entrega_aba_04 = Button(self.frame_dados_contratuais_aba_04, text="Data>>", bg="lightblue", fg="black", command=self.calendario_data_entrega_aba_04)
        self.btn_data_entrega_aba_04['font'] = "Arial", 11
        self.btn_data_entrega_aba_04.place(relx=0.515, rely=0.47, relwidth=0.065, relheight=0.159)

        self.entry_data_entrega_aba_04 = Entry(self.frame_dados_contratuais_aba_04, bg="#345574", fg="lightgrey")
        self.entry_data_entrega_aba_04['font'] = "Arial", 12
        self.entry_data_entrega_aba_04.place(relx=0.581, rely=0.47, relwidth=0.084)
        # Label e Entry - Valor do caucao
        self.lb_valor_caucao_aba_04 = Label(self.frame_dados_contratuais_aba_04, text="Valor/Caução (R$)", bg="#1b39a9", fg="lightgrey")
        self.lb_valor_caucao_aba_04['font'] = "Arial", 11
        self.lb_valor_caucao_aba_04.place(relx=0.515, rely=0.65)

        self.entry_valor_caucao_aba_04 = Entry(self.frame_dados_contratuais_aba_04, bg="#345574", fg="lightgrey")
        self.entry_valor_caucao_aba_04['font'] = "Arial", 12
        self.entry_valor_caucao_aba_04.place(relx=0.515, rely=0.79, relwidth=0.15)
        # Label e Combobox - Dia de Vencimento Parcelas
        self.lb_dia_vencto_aba_04 = Label(self.frame_dados_contratuais_aba_04, text="Dia/Vencto", bg="#1b39a9", fg="lightgrey")
        self.lb_dia_vencto_aba_04['font'] = "Arial", 11
        self.lb_dia_vencto_aba_04.place(relx=0.68, rely=0.01)

        self.combo_dia_vencto_aba_04 = ttk.Combobox(self.frame_dados_contratuais_aba_04, values=(5, 10, 15, 20, 25))
        self.combo_dia_vencto_aba_04.place(relx=0.68, rely=0.15, relwidth=0.05)

        # Label e Entry - ID
        self.lb_id_aba_04 = Label(self.frame_dados_contratuais_aba_04, text="ID", bg="#1b39a9", fg="lightgrey")
        self.lb_id_aba_04['font'] = "Arial", 11
        self.lb_id_aba_04.place(relx=0.94, rely=0.01)

        self.entry_ID_aba_04 = Entry(self.frame_dados_contratuais_aba_04, bg="#345574", fg="lightgrey")
        self.entry_ID_aba_04['font'] = "Arial", 12
        self.entry_ID_aba_04.place(relx=0.94, rely=0.15, relwidth=0.03)

        # Label e Texto - Observação
        self.lb_observacao_aba_04 = Label(self.frame_dados_contratuais_aba_04, text="Observação:", bg="#1b39a9", fg="lightgrey")
        self.lb_observacao_aba_04['font'] = "Arial", 11
        self.lb_observacao_aba_04.place(relx=0.68, rely=0.33)

        self.txt_observacao_aba_04 = Text(self.frame_dados_contratuais_aba_04, bg="white", fg="black")
        self.txt_observacao_aba_04['font'] = "Arial", 11
        self.txt_observacao_aba_04.place(relx=0.68, rely=0.47, relwidth=0.29, relheight=0.49)

        # Botões Adiciona - Atualiza - Remove
        self.btn_adiciona_aba_04 = Button(self.aba_04, text="Adiciona", bg="lightblue", fg="black", command=self.add_contrato)
        self.btn_adiciona_aba_04['font'] = "Arial", 9
        self.btn_adiciona_aba_04.place(relx=0.05, rely=0.57, relwidth=0.08, relheight=0.04)
        # Botão Atualiza
        self.btn_atualiza_aba_04 = Button(self.aba_04, text="Atualiza", bg="lightblue", fg="black", command=self.atualiza_Contrato_aba_04)
        self.btn_atualiza_aba_04['font'] = "Arial", 9
        self.btn_atualiza_aba_04.place(relx=0.135, rely=0.57, relwidth=0.08, relheight=0.04)
        # Botão Delete
        self.btn_remove_aba_04 = Button(self.aba_04, text="Remove", bg="lightblue", fg="black", command=self.remove_Cadastro_aba_04)
        self.btn_remove_aba_04['font'] = "Arial", 9
        self.btn_remove_aba_04.place(relx=0.219, rely=0.57, relwidth=0.08, relheight=0.04)

        # Botão - Visualizar Contrato
        self.btn_visu_parcelas_aba_04 = Button(self.aba_04, text="Visualizar Parcelas", bg="lightblue", fg="black")
        self.btn_visu_parcelas_aba_04['font'] = "Arial", 9
        self.btn_visu_parcelas_aba_04.place(relx=0.303, rely=0.57, relwidth=0.12, relheight=0.04)

        # Dar Baixa em Contrato
        self.btn_dar_baixa_aba_04 = Button(self.aba_04, text="Dar Baixa", bg="lightblue", fg="black")
        self.btn_dar_baixa_aba_04['font'] = "Arial", 9
        self.btn_dar_baixa_aba_04.place(relx=0.427, rely=0.57, relwidth=0.08, relheight=0.04)

        self.btn_dar_baixa_aba_04 = Button(self.aba_04, text="Limpar Casas", bg="lightblue", fg="black", command=self.limpa_aba_04)
        self.btn_dar_baixa_aba_04['font'] = "Arial", 9
        self.btn_dar_baixa_aba_04.place(relx=0.5107, rely=0.57, relwidth=0.08, relheight=0.04)

        # Label clique duas vezes sobre o registro para visualizar todos os dados
        self.lb_frase_clique_aba_04 = Label(self.aba_04, text="Clique Duplo sobre o registro para visualizar todos os dados.", bg="#1b39a9", fg="lightgrey")
        self.lb_frase_clique_aba_04['font'] = "Arial", 11
        self.lb_frase_clique_aba_04.place(relx=0.3, rely=0.95)

    def treeview_seleciona_locador_aba_04(self):
        self.tview_seleciona_locador_aba_04 = ttk.Treeview(self.frame_esquerda_aba_04, height=3, 
        column=("col1", "col2"))
        # ID, nome, data_nasc, CPF
        self.tview_seleciona_locador_aba_04.heading("#0", text="")
        self.tview_seleciona_locador_aba_04.heading("#1", text="Nome")
        self.tview_seleciona_locador_aba_04.heading("#2", text="CPF")
        # Largura de cada coluna
        self.tview_seleciona_locador_aba_04.column("#0", width=0)
        self.tview_seleciona_locador_aba_04.column("#1", width=150)
        self.tview_seleciona_locador_aba_04.column("#2", width=100)
        self.tview_seleciona_locador_aba_04.place(relx=0.01, rely=0.22, relwidth=0.95, relheight=0.7)

        # Barra de Rolagem
        self.barra_rolagem_frame_esquerda_aba_04 = Scrollbar(self.frame_esquerda_aba_04, orient="vertical")
        self.tview_seleciona_locador_aba_04.configure(yscroll=self.barra_rolagem_frame_esquerda_aba_04.set)
        self.barra_rolagem_frame_esquerda_aba_04.place(relx=0.955, rely=0.22, relwidth=0.04, relheight=0.7)
        
        # Binding Evento Clique Duplo Aba 04
        self.tview_seleciona_locador_aba_04.bind("<Double-1>", self.clique_duplo_locador_aba_04)

        
    def treeview_seleciona_locatario_aba_04(self):
        self.tview_seleciona_locatario_aba_04 = ttk.Treeview(self.frame_meio_aba_04, height=3, 
        column=("col1", "col2"))
        # ID, nome, data_nasc, CPF
        self.tview_seleciona_locatario_aba_04.heading("#0", text="")
        self.tview_seleciona_locatario_aba_04.heading("#1", text="Nome")
        self.tview_seleciona_locatario_aba_04.heading("#2", text="CPF")
        # Largura de cada coluna
        self.tview_seleciona_locatario_aba_04.column("#0", width=0)
        self.tview_seleciona_locatario_aba_04.column("#1", width=150)
        self.tview_seleciona_locatario_aba_04.column("#2", width=100)
        self.tview_seleciona_locatario_aba_04.place(relx=0.01, rely=0.22, relwidth=0.95, relheight=0.7)

        # Barra de Rolagem
        self.barra_rolagem_frame_meio_aba_04 = Scrollbar(self.frame_meio_aba_04, orient="vertical")
        self.tview_seleciona_locatario_aba_04.configure(yscroll=self.barra_rolagem_frame_meio_aba_04.set)
        self.barra_rolagem_frame_meio_aba_04.place(relx=0.955, rely=0.22, relwidth=0.04, relheight=0.7)

        # Binding Evento Clique Duplo Aba 04
        self.tview_seleciona_locatario_aba_04.bind("<Double-1>", self.clique_duplo_locatario_aba_04)


    def treeview_seleciona_imovel_aba_04(self):
        self.tview_seleciona_imovel_aba_04 = ttk.Treeview(self.frame_direita_aba_04, height=3, 
        column=("col1", "col2"))
        # ID, nome, data_nasc, CPF
        self.tview_seleciona_imovel_aba_04.heading("#0", text="")
        self.tview_seleciona_imovel_aba_04.heading("#1", text="Tipo")
        self.tview_seleciona_imovel_aba_04.heading("#2", text="Imóvel")
        # Largura de cada coluna
        self.tview_seleciona_imovel_aba_04.column("#0", width=0)
        self.tview_seleciona_imovel_aba_04.column("#1", width=100)
        self.tview_seleciona_imovel_aba_04.column("#2", width=150)
        self.tview_seleciona_imovel_aba_04.place(relx=0.01, rely=0.22, relwidth=0.95, relheight=0.7)

        # Barra de Rolagem
        self.barra_rolagem_frame_direita_aba_04 = Scrollbar(self.frame_direita_aba_04, orient="vertical")
        self.tview_seleciona_imovel_aba_04.configure(yscroll=self.barra_rolagem_frame_direita_aba_04.set)
        self.barra_rolagem_frame_direita_aba_04.place(relx=0.955, rely=0.22, relwidth=0.04, relheight=0.7)

        # Binding Evento Clique Duplo Aba 04
        self.tview_seleciona_imovel_aba_04.bind("<Double-1>", self.clique_duplo_imovel_aba_04)
    
    def treeview_adiciona_contrato_aba_04(self):
        # Locador, Locatário, Uso, Denominado, Data Assinatura, Vencto, Valor
        self.tview_contrato_aba_04 = ttk.Treeview(self.aba_04, height=3, 
        column=("col1", "col2", "col3", "col4", "col5", "col6", "col7"))
        # ID, nome, data_nasc, CPF
        self.tview_contrato_aba_04.heading("#0", text="")
        self.tview_contrato_aba_04.heading("#1", text="Locador")
        self.tview_contrato_aba_04.heading("#2", text="Locatário")
        self.tview_contrato_aba_04.heading("#3", text="Uso")
        self.tview_contrato_aba_04.heading("#4", text="Codinome")
        self.tview_contrato_aba_04.heading("#5", text="Data")
        self.tview_contrato_aba_04.heading("#6", text="Vencto")
        self.tview_contrato_aba_04.heading("#7", text="Aluguel (R$)")
        # Largura de cada coluna
        self.tview_contrato_aba_04.column("#0", width=0)
        self.tview_contrato_aba_04.column("#1", width=150)
        self.tview_contrato_aba_04.column("#2", width=150)
        self.tview_contrato_aba_04.column("#3", width=50)
        self.tview_contrato_aba_04.column("#4", width=50)
        self.tview_contrato_aba_04.column("#5", width=50)
        self.tview_contrato_aba_04.column("#6", width=10)
        self.tview_contrato_aba_04.column("#7", width=40)
        self.tview_contrato_aba_04.place(relx=0.01, rely=0.62, relwidth=0.97, relheight=0.33)

        # Barra de Rolagem
        self.barra_rolagem_contrato_aba_04 = Scrollbar(self.aba_04, orient="vertical")
        self.tview_contrato_aba_04.configure(yscroll=self.barra_rolagem_contrato_aba_04.set)
        self.barra_rolagem_contrato_aba_04.place(relx=0.98, rely=0.62, relwidth=0.015, relheight=0.33)
        
        # Binding Evento Clique Duplo Aba 04
        self.tview_contrato_aba_04.bind("<Double-1>", self.clique_duplo_contrato_aba_04)
    
    def widgets_aba_05(self):
        # Label Mensalidades e Recibos
        self.lb_titulo_aba_05 = Label(self.aba_05, text="Mensalidades e Recibos", bg="#1b39a9", fg="lightgrey")
        self.lb_titulo_aba_05['font'] = "Arial", 14
        self.lb_titulo_aba_05.place(relx=0.4, rely=0.001)
        # Frame Treeview das Mensalidades
        self.frame_tview_mensalidades_aba_05 = Frame(self.aba_05, bg="#1b39a9", highlightbackground="lightgrey", highlightthickness=1)
        self.frame_tview_mensalidades_aba_05.place(relx=0.01, rely=0.05, relwidth=0.67, relheight=0.3)

        # Widgets frame tview Mensalidades
        self.lb_id_aba_05 = Label(self.frame_tview_mensalidades_aba_05, text="ID", bg="#1b39a9", fg="lightgrey")
        self.lb_id_aba_05['font'] = "Arial", 11
        self.lb_id_aba_05.place(relx=0.01, rely=0.6)

        self.entry_ID_aba_05 = Entry(self.frame_tview_mensalidades_aba_05, bg="#345574", fg="lightgrey")
        self.entry_ID_aba_05['font'] = "Arial", 12
        self.entry_ID_aba_05.focus()
        self.entry_ID_aba_05.place(relx=0.01, rely=0.74, relwidth=0.08)

        ## Label e Entry Locatario
        self.lb_locatario_nome_aba_05 = Label(self.frame_tview_mensalidades_aba_05, text="Locatário", bg="#1b39a9", fg="lightgrey")
        self.lb_locatario_nome_aba_05['font'] = "Arial", 11
        self.lb_locatario_nome_aba_05.place(relx=0.1, rely=0.6)

        self.entry_locatario_nome_aba_05 = Entry(self.frame_tview_mensalidades_aba_05, bg="#345574", fg="lightgrey")
        self.entry_locatario_nome_aba_05['font'] = "Arial", 12
        self.entry_locatario_nome_aba_05.place(relx=0.1, rely=0.74, relwidth=0.24)
        # Label e Entry Imóvel
        self.lb_denominacao_aba_05 = Label(self.frame_tview_mensalidades_aba_05, text="Denominado", bg="#1b39a9", fg="lightgrey")
        self.lb_denominacao_aba_05['font'] = "Arial", 11
        self.lb_denominacao_aba_05.place(relx=0.35, rely=0.6)

        self.entry_denominacao_aba_05 = Entry(self.frame_tview_mensalidades_aba_05, bg="#345574", fg="lightgrey")
        self.entry_denominacao_aba_05['font'] = "Arial", 12
        self.entry_denominacao_aba_05.place(relx=0.35, rely=0.74, relwidth=0.14)
        # Label Entry Vencimento
        self.lb_dia_vencto_aba_05 = Label(self.frame_tview_mensalidades_aba_05, text="Dia", bg="#1b39a9", fg="lightgrey")
        self.lb_dia_vencto_aba_05['font'] = "Arial", 11
        self.lb_dia_vencto_aba_05.place(relx=0.5, rely=0.6)

        self.entry_dia_vencto_aba_05 = Entry(self.frame_tview_mensalidades_aba_05, bg="#345574", fg="lightgrey")
        self.entry_dia_vencto_aba_05['font'] = "Arial", 12
        self.entry_dia_vencto_aba_05.place(relx=0.5, rely=0.74, relwidth=0.04)

        # Label e Combo Mês
        self.lb_mes_aba_05 = Label(self.frame_tview_mensalidades_aba_05, text='Mês', bg="#1b39a9", fg="lightgrey")
        self.lb_mes_aba_05['font'] = "Arial", 11
        self.lb_mes_aba_05.place(relx=0.575, rely=0.6)

        self.combo_mes_aba_05 = ttk.Combobox(self.frame_tview_mensalidades_aba_05, values=self.lista_mes)
        self.combo_mes_aba_05.place(relx=0.575, rely=0.74, relwidth=0.06)

        # Label e Combo Ano
        self.lb_ano_aba_05 = Label(self.frame_tview_mensalidades_aba_05, text="Ano", bg="#1b39a9", fg="lightgrey")
        self.lb_ano_aba_05['font'] = "Arial", 11
        self.lb_ano_aba_05.place(relx=0.65, rely=0.6)

        self.combo_ano_aba_05 = ttk.Combobox(self.frame_tview_mensalidades_aba_05, values=self.lista_ano_mensalidades)
        self.combo_ano_aba_05.place(relx=0.65, rely=0.74, relwidth=0.08)

        # Botões de Comando - Add Parcelas - Altera - Remove - Gerar Recibo
        self.btn_adiciona_aba_05 = Button(self.aba_05, text="Adiciona", bg="lightblue", fg="black", command=self.add_mensalidade)
        self.btn_adiciona_aba_05['font'] = "Arial", 9
        self.btn_adiciona_aba_05.place(relx=0.4, rely=0.325, relwidth=0.08, relheight=0.04)
        # Botão Atualiza
        self.btn_atualiza_aba_05 = Button(self.aba_05, text="Atualiza", bg="lightblue", fg="black", command=self.atualiza_mensalidades_aba_05)
        self.btn_atualiza_aba_05['font'] = "Arial", 9
        self.btn_atualiza_aba_05.place(relx=0.487, rely=0.325, relwidth=0.08, relheight=0.04)
        # Botão Delete
        self.btn_remove_aba_05 = Button(self.aba_05, text="Remove", bg="lightblue", fg="black", command=self.remove_mensalidade_aba_05)
        self.btn_remove_aba_05['font'] = "Arial", 9
        self.btn_remove_aba_05.place(relx=0.574, rely=0.325, relwidth=0.08, relheight=0.04)

        # Frame Entra com Mensalidades
        self.frame_cadastra_pagamentos_aba_05 = Frame(self.aba_05, bg="#1b39a9", highlightbackground="lightgrey", highlightthickness=1)
        self.frame_cadastra_pagamentos_aba_05.place(relx=0.69, rely=0.05, relwidth=0.3, relheight=0.3)

        # Widgets Frame cadastra pagamentos
        self.lb_quitacao_recibo_aba_05 = Label(self.aba_05, text="Quitação/Emissão de Recibo", bg="#1b39a9", fg="lightgrey")
        self.lb_quitacao_recibo_aba_05['font'] = "Arial", 11
        self.lb_quitacao_recibo_aba_05.place(relx=0.8, rely=0.03)

        # Label e Entry Data de Pagamento
        self.lb_data_pagto_aba_05 = Label(self.frame_cadastra_pagamentos_aba_05, text="Data Pagamento", bg="#1b39a9", fg="lightgrey")
        self.lb_data_pagto_aba_05['font'] = "Arial", 9
        self.lb_data_pagto_aba_05.place(relx=0.01, rely=0.01)

        self.btn_data_pagto_aba_05 = Button(self.frame_cadastra_pagamentos_aba_05, text=">>", bg="lightblue", fg="black", command=self.calendario_data_pagto_aba_05)
        self.btn_data_pagto_aba_05['font'] = "Arial", 9
        self.btn_data_pagto_aba_05.place(relx=0.01, rely=0.14, relwidth=0.09, relheight=0.16)

        self.entry_data_pagto_aba_05 = Entry(self.frame_cadastra_pagamentos_aba_05, bg="#345574", fg="lightgrey", width=10)
        self.entry_data_pagto_aba_05['font'] = "Arial", 12
        self.entry_data_pagto_aba_05.place(relx=0.103, rely=0.14, relwidth=0.27, relheight=0.16)
        # Label e Combo - Tipo Pagamento - Aluguel ou Caução
        self.lb_tipo_aba_05 = Label(self.frame_cadastra_pagamentos_aba_05, text="Tipo Pagamento", bg="#1b39a9", fg="lightgrey")
        self.lb_tipo_aba_05['font'] = "Arial", 9
        self.lb_tipo_aba_05.place(relx=0.01, rely=0.3)

        self.combo_tipo_aba_05 = ttk.Combobox(self.frame_cadastra_pagamentos_aba_05, values=("Aluguel", "Caução"))
        self.combo_tipo_aba_05.place(relx=0.01, rely=0.43, relwidth=0.36, relheight=0.16)
        # Label e Entry - Valor por Extenso
        self.lb_valor_extenso_aba_05 = Label(self.frame_cadastra_pagamentos_aba_05, text="Valor por Extenso (Para Recibo)", bg="#1b39a9", fg="lightgrey")
        self.lb_valor_extenso_aba_05['font'] = "Arial", 9
        self.lb_valor_extenso_aba_05.place(relx=0.01, rely=0.61)

        self.entry_valor_extenso_aba_05 = Entry(self.frame_cadastra_pagamentos_aba_05, bg="#345574", fg="lightgrey")
        self.entry_valor_extenso_aba_05['font'] = "Arial", 10
        self.entry_valor_extenso_aba_05.place(relx=0.01, rely=0.74, relwidth=0.97, relheight=0.16)
        # Botão Quitar Parcela
        self.btn_quita_parcela_aba_05 = Button(self.aba_05, text="Pagar Parcela", bg="lightblue", fg="black", command=self.quitar_mensalidade_aba_05)
        self.btn_quita_parcela_aba_05['font'] = "Arial", 9
        self.btn_quita_parcela_aba_05.place(relx=0.7, rely=0.325, relwidth=0.1, relheight=0.04)
        # Botão Gerar Recibo
        self.btn_gerar_recibo_aba_05 = Button(self.aba_05, text="Gerar Recibo", bg="lightblue", fg="black", command=self.gera_relatorio_aba_05)
        self.btn_gerar_recibo_aba_05['font'] = "Arial", 9
        self.btn_gerar_recibo_aba_05.place(relx=0.805, rely=0.325, relwidth=0.1, relheight=0.04)
    
    def treeview_seleciona_contrato_aba_05(self):
        # ID, Locatário, Uso, Codinome,
        self.tview_seleciona_contrato_aba_05 = ttk.Treeview(self.frame_tview_mensalidades_aba_05, height=3, 
        column=("col1", "col2", "col3", "col4", "col5", "col6"))
        # ID, locatário, uso , codinome
        self.tview_seleciona_contrato_aba_05.heading("#0", text="")
        self.tview_seleciona_contrato_aba_05.heading("#1", text="ID")
        self.tview_seleciona_contrato_aba_05.heading("#2", text="Locatário")
        self.tview_seleciona_contrato_aba_05.heading("#3", text="Uso")
        self.tview_seleciona_contrato_aba_05.heading("#4", text="Codinome")
        self.tview_seleciona_contrato_aba_05.heading("#5", text="Vencto")
        self.tview_seleciona_contrato_aba_05.heading("#6", text="Aluguel (R$)")
        # Largura de cada coluna
        self.tview_seleciona_contrato_aba_05.column("#0", width=0)
        self.tview_seleciona_contrato_aba_05.column("#1", width=20)
        self.tview_seleciona_contrato_aba_05.column("#2", width=250)
        self.tview_seleciona_contrato_aba_05.column("#3", width=80)
        self.tview_seleciona_contrato_aba_05.column("#4", width=80)
        self.tview_seleciona_contrato_aba_05.column("#5", width=80)
        self.tview_seleciona_contrato_aba_05.column("#6", width=120)
        self.tview_seleciona_contrato_aba_05.place(relx=0.001, rely=0.01, relwidth=0.98, relheight=0.58)

        # Barra de Rolagem
        self.barra_rolagem_contrato_aba_05 = Scrollbar(self.frame_tview_mensalidades_aba_05, orient="vertical")
        self.tview_seleciona_contrato_aba_05.configure(yscroll=self.barra_rolagem_contrato_aba_05.set)
        self.barra_rolagem_contrato_aba_05.place(relx=0.98, rely=0.01, relwidth=0.015, relheight=0.58)
        # Binding Evento Clique Duplo Aba 05
        self.tview_seleciona_contrato_aba_05.bind("<Double-1>", self.clique_duplo_contrato_aba_05)
    
    def treeview_mensalidades_aba_05(self):
         # ID, Locatario - Denominado - Uso - Data_vencto - Data_pagto - Valor - Tipo Parcela - Situação
        self.tview_mensalidade_aba_05 = ttk.Treeview(self.aba_05, height=3, 
        column=("col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8", "col9"))
        # ID, locatário, uso , codinome
        self.tview_mensalidade_aba_05.heading("#0", text="")
        self.tview_mensalidade_aba_05.heading("#1", text="ID")
        self.tview_mensalidade_aba_05.heading("#2", text="Locatário")
        self.tview_mensalidade_aba_05.heading("#3", text="Denominado")
        self.tview_mensalidade_aba_05.heading("#4", text="Utilização")
        self.tview_mensalidade_aba_05.heading("#5", text="Data Vencto")
        self.tview_mensalidade_aba_05.heading("#6", text="Data Pagto")
        self.tview_mensalidade_aba_05.heading("#7", text="Valor (R$)")
        self.tview_mensalidade_aba_05.heading("#8", text="Tipo")
        self.tview_mensalidade_aba_05.heading("#9", text="Quitado")
        # Largura dmensalidade    self.tview_mensalidade_aba_05.column("#0", width=0)
        self.tview_mensalidade_aba_05.column("#0", width=0)
        self.tview_mensalidade_aba_05.column("#1", width=30)
        self.tview_mensalidade_aba_05.column("#2", width=200)
        self.tview_mensalidade_aba_05.column("#3", width=130)
        self.tview_mensalidade_aba_05.column("#4", width=100)
        self.tview_mensalidade_aba_05.column("#5", width=100)
        self.tview_mensalidade_aba_05.column("#6", width=90)
        self.tview_mensalidade_aba_05.column("#7", width=90)
        self.tview_mensalidade_aba_05.column("#8", width=70)
        self.tview_mensalidade_aba_05.column("#9", width=70)
        self.tview_mensalidade_aba_05.place(relx=0.001, rely=0.4, relwidth=0.98, relheight=0.5)

        # Barra de Rolagem
        self.barra_rolagem_mensalidade_aba_05 = Scrollbar(self.aba_05, orient="vertical")
        self.tview_mensalidade_aba_05.configure(yscroll=self.barra_rolagem_mensalidade_aba_05.set)
        self.barra_rolagem_mensalidade_aba_05.place(relx=0.98, rely=0.4, relwidth=0.015, relheight=0.5)

         # Binding Evento Clique Duplo Aba 05
        self.tview_mensalidade_aba_05.bind("<Double-1>", self.clique_duplo_mensalidades_aba_05)


        




Janela_Principal()

        
