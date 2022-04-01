import sqlite3
from tkinter import messagebox
from tkinter import *
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image


class BancoDeDados:
    # Cria Banco de Dados e as Tabelas
    def conecta_db(self):
        self.conn = sqlite3.connect("contratos.db")
        self.cursor = self.conn.cursor()
    
    def desconecta_db(self):
        self.conn.close()
    
    def cria_db(self):
        self.conecta_db()
        # Cria tabela locador
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS locador (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                nacionalidade TEXT,
                est_civil TEXT,
                profissao TEXT,
                rg TEXT,
                cpf TEXT,
                data_nasc timestamp NOT NULL,
                tipo TEXT,
                logradouro TEXT,
                numero TEXT,
                complem TEXT,
                bairro TEXT,
                cidade TEXT,
                uf TEXT,
                cep TEXT
                    );
                """)
        # Cria tabela locatário
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS locatario (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                nacionalidade TEXT,
                est_civil TEXT,
                profissao TEXT,
                rg TEXT,
                cpf TEXT,
                data_nasc timestamp NOT NULL,
                tipo TEXT,
                logradouro TEXT,
                numero TEXT,
                complem TEXT,
                bairro TEXT,
                cidade TEXT,
                uf TEXT,
                cep TEXT
                );
            """)
        # Cria tabela imóvel
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS imovel (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                util TEXT,
                area REAL,
                wc INTEGER,
                garagem TEXT,
                const TEXT,
                tipo TEXT,
                logradouro TEXT,
                numero TEXT,
                complem TEXT,
                bairro TEXT,
                cidade TEXT,
                uf TEXT,
                cep TEXT,
                alugado TEXT
                );
            """)
        
        # Cria tabela Contrato
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS contrato (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                locador TEXT,
                cpf_locad TEXT,
                locatario TEXT,
                cpf_locat TEXT,
                tipo TEXT,
                denominado TEXT,
                prazo_contrato TEXT,
                data_ass timestamp NOT NULL,
                data_caucao timestamp NOT NULL,
                valor_mensal REAL,
                data_chaves timestamp,
                valor_caucao REAL,
                dia_vencto TEXT,
                obs TEXT
                );
            """)
            # Cria tabela mensalidade
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS mensalidade (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                locatario TEXT,
                denominado TEXT,
                utilizacao TEXT,
                data_vencto timestamp NOT NULL,
                data_pagto timestamp,
                valor REAL,
                tipo_pagto TEXT,
                quitado TEXT,
                extenso TEXT
                );""")
        self.conn.commit()
        self.desconecta_db()
    





    # Funções da Aba_01
    def add_locador(self):
        variaveis = self.variaveis_aba_01()
        #print(self.nome, self.nacionalidade, self.est_civil, self.profissao, self.rg, self.cpf, self.data_nasc, self.tipo, self.logradouro, self.numero, self.complemento, self.bairro, self.cidade, self.uf, self.cep)
        if self.nome and self.nacionalidade and self.est_civil and self.profissao and self.rg and self.cpf and self.data_nasc and self.tipo and self.logradouro and self.numero and self.complemento and self.bairro and self.cidade and self.uf and self.cep:
            self.conecta_db()
            self.cursor.execute("""INSERT INTO locador
                (nome, 
                nacionalidade, 
                est_civil, 
                profissao, 
                rg, 
                cpf, 
                data_nasc, 
                tipo, 
                logradouro, 
                numero, 
                complem, 
                bairro, 
                cidade, 
                uf, 
                cep) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                (self.nome, 
                self.nacionalidade, 
                self.est_civil, 
                self.profissao, 
                self.rg, 
                self.cpf, 
                self.data_nasc, 
                self.tipo, 
                self.logradouro, 
                self.numero, 
                self.complemento, 
                self.bairro, 
                self.cidade, 
                self.uf, 
                self.cep,))
            self.conn.commit()
            self.desconecta_db()
            self.limpa_aba_01()
            self.insere_locador_na_lista_aba_01()
        else:
            messagebox.showerror("ERRO!", "É necessário preencher todos os campos, exceto ID.")

    def insere_locador_na_lista_aba_01(self):
        self.tview_aba_01.delete(*self.tview_aba_01.get_children())
        self.conecta_db()
        lista = self.cursor.execute(""" SELECT nome, cpf, data_nasc FROM locador
                    ORDER BY nome ASC; """)
        for item in lista:
            self.tview_aba_01.insert("", END, values=item)

        self.desconecta_db()
    
    def clique_duplo_aba_01(self, event):
        self.limpa_aba_01()
        tview = self.tview_aba_01.selection()
        self.conecta_db()
        lista = self.cursor.execute("""SELECT id, nome, nacionalidade, est_civil, profissao, rg, cpf,
                    data_nasc, tipo, logradouro, numero, complem, bairro, cidade, uf, cep FROM locador""")
                
        for linha_tview in tview:
            c1, c2, c3 = self.tview_aba_01.item(linha_tview, "values")
            for linha_db in lista:
                if c1 == linha_db[1]:
                    self.entry_ID_aba_01.insert(END, linha_db[0])
                    self.entry_nome_aba_01.insert(END, linha_db[1])
                    self.entry_nacionalidade_aba_01.insert(END, linha_db[2])
                    self.combo_estadoCivil_aba_01.set(linha_db[3])
                    self.entry_profissao_aba_01.insert(END, linha_db[4])
                    self.entry_rg_aba_01.insert(END, linha_db[5])
                    self.entry_cpf_aba_01.insert(END, linha_db[6])
                    self.combo_data_nasc_DIA_aba_01.set(linha_db[7][:2])
                    self.combo_data_nasc_MES_aba_01.set(linha_db[7][3:5])
                    self.combo_data_nasc_ANO_aba_01.set(linha_db[7][6:])
                    self.combo_Tipo_aba_01.set(linha_db[8])
                    self.entry_logradouro_aba_01.insert(END, linha_db[9])
                    self.entry_numero_aba_01.insert(END, linha_db[10])
                    self.entry_complemento_aba_01.insert(END, linha_db[11])
                    self.entry_bairro_aba_01.insert(END, linha_db[12])
                    self.entry_cidade_aba_01.insert(END, linha_db[13])
                    self.combo_UF_aba_01.set(linha_db[14])
                    self.entry_CEP01_aba_01.insert(END, linha_db[15][:5])
                    self.entry_CEP02_aba_01.insert(END, linha_db[15][6:])
            
        self.desconecta_db()
    
    def atualiza_Cadastro_aba_01(self):
        self.variaveis_aba_01()
        if self.id and self.nome and self.nacionalidade and self.est_civil and self.profissao and self.rg and self.cpf and self.data_nasc and self.tipo and self.logradouro and self.numero and self.complemento and self.bairro and self.cidade and self.uf and self.cep:
            self.conecta_db()
            self.cursor.execute("""UPDATE locador SET 
                        nome=?, 
                        nacionalidade=?, 
                        est_civil=?, 
                        profissao=?, 
                        rg=?, 
                        cpf=?, 
                        data_nasc=?, 
                        tipo=?, 
                        logradouro=?, 
                        numero=?, 
                        complem=?, 
                        bairro=?, 
                        cidade=?, 
                        uf=?, 
                        cep=?
                        WHERE id=?""",(
                            self.nome, 
                            self.nacionalidade, 
                            self.est_civil, 
                            self.profissao, 
                            self.rg, 
                            self.cpf, 
                            self.data_nasc, 
                            self.tipo, 
                            self.logradouro, 
                            self.numero, 
                            self.complemento, 
                            self.bairro, 
                            self.cidade, 
                            self.uf, 
                            self.cep, 
                            self.id))
            self.conn.commit()
            self.desconecta_db()
            self.insere_locador_na_lista_aba_01()
            self.limpa_aba_01()
        else:
            messagebox.showerror("ERRO!", "É Necessário Clique Duplo sobre o registro que deseja Atualizar.")
    
    def remove_Cadastro_aba_01(self):
        self.variaveis_aba_01()
        if self.id:
            resultado = messagebox.askyesno("", "Confirma exclusão?")
            if resultado:
                self.conecta_db()
                self.cursor.execute("""DELETE FROM locador WHERE id=?""",(self.id,))
                self.conn.commit()
                self.desconecta_db()
                self.insere_locador_na_lista_aba_01()
                self.limpa_aba_01()
            else:
                pass
        else:
            messagebox.showerror("Erro!", "É Necessário selecionar um Registro para excluir")
    
    
    





    
    # Funções da Aba 02
    def add_locatario(self):
        variaveis = self.variaveis_aba_02()
        #print(self.nome, self.nacionalidade, self.est_civil, self.profissao, self.rg, self.cpf, self.data_nasc, self.tipo, self.logradouro, self.numero, self.complemento, self.bairro, self.cidade, self.uf, self.cep)
        if self.nome and self.nacionalidade and self.est_civil and self.profissao and self.rg and self.cpf and self.data_nasc and self.tipo and self.logradouro and self.numero and self.complemento and self.bairro and self.cidade and self.uf and self.cep:
            self.conecta_db()
            self.cursor.execute("""INSERT INTO locatario
                (nome, 
                nacionalidade, 
                est_civil, 
                profissao, 
                rg, 
                cpf, 
                data_nasc, 
                tipo, 
                logradouro, 
                numero, 
                complem, 
                bairro, 
                cidade, 
                uf, 
                cep) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                (self.nome, 
                self.nacionalidade, 
                self.est_civil, 
                self.profissao, 
                self.rg, 
                self.cpf, 
                self.data_nasc, 
                self.tipo, 
                self.logradouro, 
                self.numero, 
                self.complemento, 
                self.bairro, 
                self.cidade, 
                self.uf, 
                self.cep,))
            self.conn.commit()
            self.desconecta_db()
            self.limpa_aba_02()
            self.insere_locatario_na_lista_aba_02()
        else:
            messagebox.showerror("ERRO!", "É necessário preencher todos os campos, exceto ID.")

    def insere_locatario_na_lista_aba_02(self):
        self.tview_aba_02.delete(*self.tview_aba_02.get_children())
        self.conecta_db()
        lista = self.cursor.execute(""" SELECT nome, cpf, data_nasc FROM locatario
                    ORDER BY nome ASC; """)
        for item in lista:
            self.tview_aba_02.insert("", END, values=item)

        self.desconecta_db()
    
    def clique_duplo_aba_02(self, event):
        self.limpa_aba_02()
        tview = self.tview_aba_02.selection()
        self.conecta_db()
        lista = self.cursor.execute("""SELECT id, nome, nacionalidade, est_civil, profissao, rg, cpf,
                    data_nasc, tipo, logradouro, numero, complem, bairro, cidade, uf, cep FROM locatario""")
                
        for linha_tview in tview:
            c1, c2, c3 = self.tview_aba_02.item(linha_tview, "values")
            for linha_db in lista:
                if c1 == linha_db[1]:
                    self.entry_ID_aba_02.insert(END, linha_db[0])
                    self.entry_nome_aba_02.insert(END, linha_db[1])
                    self.entry_nacionalidade_aba_02.insert(END, linha_db[2])
                    self.combo_estadoCivil_aba_02.set(linha_db[3])
                    self.entry_profissao_aba_02.insert(END, linha_db[4])
                    self.entry_rg_aba_02.insert(END, linha_db[5])
                    self.entry_cpf_aba_02.insert(END, linha_db[6])
                    self.combo_data_nasc_DIA_aba_02.set(linha_db[7][:2])
                    self.combo_data_nasc_MES_aba_02.set(linha_db[7][3:5])
                    self.combo_data_nasc_ANO_aba_02.set(linha_db[7][6:])
                    self.combo_Tipo_aba_02.set(linha_db[8])
                    self.entry_logradouro_aba_02.insert(END, linha_db[9])
                    self.entry_numero_aba_02.insert(END, linha_db[10])
                    self.entry_complemento_aba_02.insert(END, linha_db[11])
                    self.entry_bairro_aba_02.insert(END, linha_db[12])
                    self.entry_cidade_aba_02.insert(END, linha_db[13])
                    self.combo_UF_aba_02.set(linha_db[14])
                    self.entry_CEP01_aba_02.insert(END, linha_db[15][:5])
                    self.entry_CEP02_aba_02.insert(END, linha_db[15][6:])
            
        self.desconecta_db()
    
    def atualiza_Cadastro_aba_02(self):
        self.variaveis_aba_02()
        if self.id and self.nome and self.nacionalidade and self.est_civil and self.profissao and self.rg and self.cpf and self.data_nasc and self.tipo and self.logradouro and self.numero and self.complemento and self.bairro and self.cidade and self.uf and self.cep:
            self.conecta_db()
            self.cursor.execute("""UPDATE locatario SET 
                        nome=?, 
                        nacionalidade=?, 
                        est_civil=?, 
                        profissao=?, 
                        rg=?, 
                        cpf=?, 
                        data_nasc=?, 
                        tipo=?, 
                        logradouro=?, 
                        numero=?, 
                        complem=?, 
                        bairro=?, 
                        cidade=?, 
                        uf=?, 
                        cep=?
                        WHERE id=?""",(
                            self.nome, 
                            self.nacionalidade, 
                            self.est_civil, 
                            self.profissao, 
                            self.rg, 
                            self.cpf, 
                            self.data_nasc, 
                            self.tipo, 
                            self.logradouro, 
                            self.numero, 
                            self.complemento, 
                            self.bairro, 
                            self.cidade, 
                            self.uf, 
                            self.cep, 
                            self.id))
            self.conn.commit()
            self.desconecta_db()
            self.insere_locatario_na_lista_aba_02()
            self.limpa_aba_02()
        else:
            messagebox.showerror("ERRO!", "É Necessário Clique Duplo sobre o registro que deseja Atualizar.")
    
    def remove_Cadastro_aba_02(self):
        self.variaveis_aba_02()
        if self.id:
            resultado = messagebox.askyesno("", "Confirma exclusão?")
            if resultado:
                self.conecta_db()
                self.cursor.execute("""DELETE FROM locatario WHERE id=?""",(self.id,))
                self.conn.commit()
                self.desconecta_db()
                self.insere_locatario_na_lista_aba_02()
                self.limpa_aba_02()
            else:
                pass
        else:
            messagebox.showerror("Erro!", "É Necessário selecionar um Registro para excluir")
    
    
    
    
    



    # Funções da Aba 03
    def add_imovel(self):
        variaveis = self.variaveis_aba_03()
    
        if self.util and self.area and self.wc and self.garagem and self.const and self.tipo and self.logradouro and self.numero and self.complemento and self.bairro and self.cidade and self.uf and self.cep and self.alugado:
            self.conecta_db()
            self.cursor.execute("""INSERT INTO imovel
                (util, 
                area, 
                wc, 
                garagem, 
                const, 
                tipo, 
                logradouro, 
                numero, 
                complem, 
                bairro, 
                cidade, 
                uf, 
                cep, 
                alugado) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                (self.util, 
                self.area, 
                self.wc, 
                self.garagem, 
                self.const, 
                self.tipo, 
                self.logradouro, 
                self.numero, 
                self.complemento, 
                self.bairro, 
                self.cidade, 
                self.uf, 
                self.cep, 
                self.alugado,))
            self.conn.commit()
            self.desconecta_db()
            self.limpa_aba_03()
            self.insere_imovel_na_lista_aba_03()
        else:
            messagebox.showerror("ERRO!", "É necessário preencher todos os campos, exceto ID.")

    def insere_imovel_na_lista_aba_03(self):
        self.tview_aba_03.delete(*self.tview_aba_03.get_children())
        self.conecta_db()
        lista = self.cursor.execute(""" SELECT util, const, logradouro, bairro, cidade, uf, alugado FROM imovel
                    ORDER BY const ASC; """)
        for item in lista:
            self.tview_aba_03.insert("", END, values=item)

        self.desconecta_db()
    
    def clique_duplo_aba_03(self, event):
        self.limpa_aba_03()
        tview = self.tview_aba_03.selection()
        self.conecta_db()
        lista = self.cursor.execute("""SELECT id, util, area, wc, garagem, const, tipo, logradouro, numero, complem, bairro, cidade, uf, cep FROM imovel""")
                
        for linha_tview in tview:
            c1, c2, c3, c4, c5, c6, c7 = self.tview_aba_03.item(linha_tview, "values")
            for linha_db in lista:
                if c2 == linha_db[5]:
                    self.entry_ID_aba_03.insert(END, linha_db[0])
                    self.combo_tipo_imovel_aba_03.set(linha_db[1])
                    self.entry_area_aba_03.insert(END, linha_db[2])
                    self.combo_WC_aba_03.set(linha_db[3])
                    self.combo_garagem_tp_aba_03.set(linha_db[4])
                    self.entry_constituida_por_aba_03.insert(END, linha_db[5])
                    self.combo_Tipo_aba_03.set(linha_db[6])
                    self.entry_logradouro_aba_03.insert(END, linha_db[7])
                    self.entry_numero_aba_03.insert(END, linha_db[8])
                    self.entry_complemento_aba_03.insert(END, linha_db[9])
                    self.entry_bairro_aba_03.insert(END, linha_db[10])
                    self.entry_cidade_aba_03.insert(END, linha_db[11])
                    self.combo_UF_aba_03.set(linha_db[12])
                    self.entry_CEP01_aba_03.insert(END, linha_db[13][:5])
                    self.entry_CEP02_aba_03.insert(END, linha_db[13][6:])
            
        self.desconecta_db()
    
    def atualiza_Cadastro_aba_03(self):
        self.variaveis_aba_03()
        if self.util and self.area and self.wc and self.garagem and self.const and self.tipo and self.logradouro and self.numero and self.complemento and self.bairro and self.cidade and self.uf and self.cep and self.alugado:
            self.conecta_db()
            self.cursor.execute("""UPDATE imovel SET 
                        util=?, 
                        area=?, 
                        wc=?, 
                        garagem=?, 
                        const=?, 
                        tipo=?, 
                        logradouro=?, 
                        numero=?, 
                        complem=?, 
                        bairro=?, 
                        cidade=?, 
                        uf=?, 
                        cep=?, 
                        alugado=?
                        WHERE id=?""",(
                            self.util, 
                            self.area, 
                            self.wc, 
                            self.garagem, 
                            self.const, 
                            self.tipo, 
                            self.logradouro, 
                            self.numero, 
                            self.complemento, 
                            self.bairro, 
                            self.cidade, 
                            self.uf, 
                            self.cep, 
                            self.alugado,
                            self.id))
            self.conn.commit()
            self.desconecta_db()
            self.insere_imovel_na_lista_aba_03()
            self.limpa_aba_03()
        else:
            messagebox.showerror("ERRO!", "É Necessário Clique Duplo sobre o registro que deseja Atualizar.")
    
    def remove_Cadastro_aba_03(self):
        self.variaveis_aba_03()
        if self.id:
            resultado = messagebox.askyesno("", "Confirma exclusão?")
            if resultado:
                self.conecta_db()
                self.cursor.execute("""DELETE FROM imovel WHERE id=?""",(self.id,))
                self.conn.commit()
                self.desconecta_db()
                self.insere_imovel_na_lista_aba_03()
                self.limpa_aba_03()
            else:
                pass
        else:
            messagebox.showerror("Erro!", "É Necessário selecionar um Registro para excluir")





    # Funções da Aba 04
    def insere_locador_aba_04(self):
        self.tview_seleciona_locador_aba_04.delete(*self.tview_seleciona_locador_aba_04.get_children())
        self.conecta_db()
        lista = self.cursor.execute(""" SELECT nome, cpf FROM locador
                    ORDER BY nome ASC; """)
        for item in lista:
            self.tview_seleciona_locador_aba_04.insert("", END, values=item)  
        self.desconecta_db()
    
    def insere_locatario_aba_04(self):
        self.tview_seleciona_locatario_aba_04.delete(*self.tview_seleciona_locatario_aba_04.get_children())
        self.conecta_db()
        lista = self.cursor.execute(""" SELECT nome, cpf FROM locatario
                    ORDER BY nome ASC; """)
        for item in lista:
            self.tview_seleciona_locatario_aba_04.insert("", END, values=item)  
        self.desconecta_db()
    
    def insere_imovel_aba_04(self):
        self.tview_seleciona_imovel_aba_04.delete(*self.tview_seleciona_imovel_aba_04.get_children())
        self.conecta_db()
        lista = self.cursor.execute(""" SELECT util, const FROM imovel
                    ORDER BY const ASC; """)
        for item in lista:
            self.tview_seleciona_imovel_aba_04.insert("", END, values=item)  
        self.desconecta_db()
    
    def clique_duplo_locador_aba_04(self, event):
        self.entry_locador_nome_aba_04.delete(0, END)
        self.entry_CPF_locador_aba_04.delete(0, END)
        tview = self.tview_seleciona_locador_aba_04.selection()
        self.conecta_db()
        lista = self.cursor.execute("""SELECT nome, cpf FROM locador""")
                
        for linha_tview in tview:
            c1, c2 = self.tview_seleciona_locador_aba_04.item(linha_tview, "values")
            for linha_db in lista:
                #print(c1, c2)
                if c1 == linha_db[0]:
                    self.entry_locador_nome_aba_04.insert(END, linha_db[0])
                    self.entry_CPF_locador_aba_04.insert(END, linha_db[1])
                
        self.desconecta_db()
    
    def clique_duplo_locatario_aba_04(self, event):
        self.entry_locatario_nome_aba_04.delete(0, END)
        self.entry_CPF_locatario_aba_04.delete(0, END)
        tview = self.tview_seleciona_locatario_aba_04.selection()
        self.conecta_db()
        lista = self.cursor.execute("""SELECT nome, cpf FROM locatario""")
                
        for linha_tview in tview:
            c1, c2 = self.tview_seleciona_locatario_aba_04.item(linha_tview, "values")
            for linha_db in lista:
                #print(c1, c2)
                if c1 == linha_db[0]:
                    self.entry_locatario_nome_aba_04.insert(END, linha_db[0])
                    self.entry_CPF_locatario_aba_04.insert(END, linha_db[1])
                
        self.desconecta_db()
    
    def clique_duplo_imovel_aba_04(self, event):
        self.entry_imovel_tipo_aba_04.delete(0, END)
        self.entry_denominacao_aba_04.delete(0, END)
        tview = self.tview_seleciona_imovel_aba_04.selection()
        self.conecta_db()
        lista = self.cursor.execute("""SELECT util, const FROM imovel""")
                
        for linha_tview in tview:
            c1, c2 = self.tview_seleciona_imovel_aba_04.item(linha_tview, "values")
            for linha_db in lista:
                #print(c1, c2)
                if c2 == linha_db[1]:
                    self.entry_imovel_tipo_aba_04.insert(END, linha_db[0])
                    self.entry_denominacao_aba_04.insert(END, linha_db[1])
                
        self.desconecta_db()
    
    def add_contrato(self):
        self.variaveis_aba_04()
        if self.locador_nome and self.locador_cpf and self.locatario_nome and self.locatario_cpf and self.imovel_tipo and self.denominacao and self.prazo_contrato and self.data_ass and self.data_caucao and self.valor_aluguel and self.valor_caucao and self.obs:
            self.conecta_db()
            lista = self.cursor.execute("""SELECT const, alugado FROM imovel""")

            controle = 0
            for linha in lista:
                if linha[0] == self.denominacao and linha[1] == "Sim":
                    controle += 1
            
       
            if not controle:
                self.cursor.execute("""INSERT INTO contrato
                    (locador, 
                    cpf_locad, 
                    locatario, 
                    cpf_locat, 
                    tipo, 
                    denominado, 
                    prazo_contrato, 
                    data_ass, 
                    data_caucao, 
                    valor_mensal, 
                    data_chaves, 
                    valor_caucao, 
                    dia_vencto, 
                    obs) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                    (self.locador_nome, 
                    self.locador_cpf, 
                    self.locatario_nome, 
                    self.locatario_cpf, 
                    self.imovel_tipo, 
                    self.denominacao, 
                    self.prazo_contrato, 
                    self.data_ass, 
                    self.data_caucao, 
                    self.valor_aluguel, 
                    self.data_entrega, 
                    self.valor_caucao, 
                    self.dia_vencto, 
                    self.obs))
                self.conn.commit()
                self.desconecta_db()
                self.atualiza_Cadastro_Alugado_aba_04(self.denominacao)
                self.insere_contrato_aba_05()
                self.insere_imovel_na_lista_aba_04()
                self.limpa_aba_04()
            else:
                messagebox.showerror("ERRO!", "Este Imóvel já está Alugado e possui contrato ativo.")

            
        else:
            messagebox.showerror("ERRO!", "É necessário preencher todos os campos, exceto ID.")
        
    def insere_contrato_aba_04(self):
        self.tview_contrato_aba_04.delete(*self.tview_contrato_aba_04.get_children())
        self.conecta_db()
        lista = self.cursor.execute(""" SELECT locador, locatario, tipo, denominado, data_ass, dia_vencto, valor_mensal FROM contrato
                    ORDER BY locador ASC; """)
        for item in lista:
            self.tview_contrato_aba_04.insert("", END, values=item)  
        self.desconecta_db()
    
    def clique_duplo_contrato_aba_04(self, event):
        self.limpa_aba_04()
        tview = self.tview_contrato_aba_04.selection()
        self.conecta_db()
        lista = self.cursor.execute("""SELECT 
                id,
                locador, 
                cpf_locad, 
                locatario, 
                cpf_locat, 
                tipo, 
                denominado, 
                prazo_contrato, 
                data_ass, 
                data_caucao, 
                valor_mensal, 
                data_chaves, 
                valor_caucao, 
                dia_vencto, 
                obs FROM contrato""")
                
        for linha_tview in tview:
            c1, c2, c3, c4, c5, c6, c7 = self.tview_contrato_aba_04.item(linha_tview, "values")
            for linha_db in lista:
                #print(c1, c2)
                if c4 == linha_db[6]:
                    self.entry_locador_nome_aba_04.insert(END, linha_db[1])
                    self.entry_CPF_locador_aba_04.insert(END, linha_db[2])
                    self.entry_locatario_nome_aba_04.insert(END, linha_db[3])
                    self.entry_CPF_locatario_aba_04.insert(END, linha_db[4])
                    self.entry_imovel_tipo_aba_04.insert(END, linha_db[5])
                    self.entry_denominacao_aba_04.insert(END, linha_db[6])
                    self.combo_prazo_aba_04.set(linha_db[7])
                    self.entry_data_ass_aba_04.insert(END, linha_db[8])
                    self.entry_data_caucao_aba_04.insert(END, linha_db[9])
                    self.entry_valor_aluguel_aba_04.insert(END, linha_db[10])
                    self.entry_data_entrega_aba_04.insert(END, linha_db[11])
                    self.entry_valor_caucao_aba_04.insert(END, linha_db[12])
                    self.combo_dia_vencto_aba_04.set(linha_db[13])
                    self.txt_observacao_aba_04.insert(END, linha_db[14])
                    self.entry_ID_aba_04.insert(END, linha_db[0])
                
        self.desconecta_db()
    
    def atualiza_Contrato_aba_04(self):
        self.variaveis_aba_04()
        if self.locador_nome and self.locador_cpf and self.locatario_nome and self.locatario_cpf and self.imovel_tipo and self.denominacao and self.prazo_contrato and self.data_ass and self.data_caucao and self.valor_aluguel and self.obs:
            self.conecta_db()
            self.cursor.execute("""UPDATE contrato SET 
                        locador=?, 
                        cpf_locad=?, 
                        locatario=?, 
                        cpf_locat=?, 
                        tipo=?, 
                        denominado=?, 
                        prazo_contrato=?, 
                        data_ass=?, 
                        data_caucao=?, 
                        valor_mensal=?, 
                        data_chaves=?, 
                        valor_caucao=?, 
                        dia_vencto=?, 
                        obs=? WHERE id=?""",(
                            self.locador_nome, 
                            self.locador_cpf, 
                            self.locatario_nome, 
                            self.locatario_cpf, 
                            self.imovel_tipo, 
                            self.denominacao, 
                            self.prazo_contrato, 
                            self.data_ass, 
                            self.data_caucao, 
                            self.valor_aluguel, 
                            self.data_entrega, 
                            self.valor_caucao, 
                            self.dia_vencto, 
                            self.obs,
                            self.id))
            self.conn.commit()
            self.desconecta_db()
            self.insere_contrato_aba_04()
            self.insere_contrato_aba_05()
            self.limpa_aba_04()
        else:
            messagebox.showerror("ERRO!", "É Necessário Clique Duplo sobre o registro que deseja Atualizar.")
    
    def atualiza_Cadastro_Alugado_aba_04(self, denominado):
        self.conecta_db()
        self.cursor.execute("""UPDATE imovel SET alugado=? WHERE const=?""",("Sim", denominado))

        self.conn.commit()
        self.desconecta_db()

        self.insere_contrato_aba_04()
        self.insere_imovel_na_lista_aba_03()
        self.insere_contrato_aba_05()
        self.insere_mensalidades_aba_05()
    

    def atualiza_Cadastro_nao_Alugado_aba_04(self, denominado):
        self.conecta_db()
        self.cursor.execute("""UPDATE imovel SET alugado=? WHERE const=?""",("Não", denominado))

        self.conn.commit()
        self.desconecta_db()

        self.insere_contrato_aba_04()
        self.insere_imovel_na_lista_aba_03()
        self.insere_contrato_aba_05()
        self.insere_mensalidades_aba_05()
    

    def remove_Cadastro_aba_04(self):
        self.variaveis_aba_04()
        if self.id:
            resultado = messagebox.askyesno("", "Confirma exclusão?")
            if resultado:
                self.conecta_db()
                self.cursor.execute("""DELETE FROM contrato WHERE id=?""",(self.id,))
                #self.conn.commit()
                #self.desconecta_db()
                

                #self.conecta_db()
                self.cursor.execute("""DELETE FROM mensalidade WHERE denominado=?""",(self.denominacao,))
                self.conn.commit()
                self.desconecta_db()
                
                self.insere_contrato_aba_04()
                self.insere_imovel_na_lista_aba_03()
                self.atualiza_Cadastro_nao_Alugado_aba_04(self.denominacao)
                self.insere_imovel_aba_04()
                self.limpa_aba_04()
            else:
                pass
        else:
            messagebox.showerror("Erro!", "É Necessário selecionar um Registro para excluir")






    # Funções da Aba 05
    def insere_contrato_aba_05(self):
        self.tview_seleciona_contrato_aba_05.delete(*self.tview_seleciona_contrato_aba_05.get_children())
        self.conecta_db()
        lista = self.cursor.execute("""SELECT id, locatario, tipo, denominado, dia_vencto, valor_mensal FROM contrato
                    ORDER BY locatario ASC; """)
        for item in lista:
            self.tview_seleciona_contrato_aba_05.insert("", END, values=item)

        self.desconecta_db()
    

    def clique_duplo_contrato_aba_05(self, event):
        self.limpa_contrato_aba_05()
        tview = self.tview_seleciona_contrato_aba_05.selection()
   
        for linha_tview in tview:
            c1, c2, c3, c4, c5, c6 = self.tview_seleciona_contrato_aba_05.item(linha_tview, "values")
            if c1:
                self.entry_locatario_nome_aba_05.insert(END, c2)
                self.entry_denominacao_aba_05.insert(END, c4)
                self.entry_dia_vencto_aba_05.insert(END, c5)   
                self.insere_mensalidades_aba_05(c4)



    def add_mensalidade(self):
        self.variaveis_aba_05()
        if self.locatario and self.denominacao and self.data_vencto:
            self.conecta_db()
            lista = self.cursor.execute("""SELECT tipo, valor_mensal, denominado FROM contrato""")

            utilizacao = str
            valor = float
            for linha in lista:
                if linha[2] == self.denominacao:
                    utilizacao = linha[0]
                    valor = linha[1]
            
            print(utilizacao, valor)

            self.cursor.execute("""INSERT INTO mensalidade
                (locatario,
                denominado,
                utilizacao,
                data_vencto,
                valor,
                quitado) VALUES (?,?,?,?,?,?)""",
                (self.locatario, self.denominacao, utilizacao, self.data_vencto, valor, "Não"))

            self.conn.commit()
            self.desconecta_db()
        
            self.limpa_parcial_aba_05()
            self.insere_mensalidades_aba_05(self.denominacao)
        else:
            messagebox.showerror("ERRO!", "É necessário preencher todos os campos, exceto ID.")
    
    def insere_mensalidades_aba_05(self, denominado):
        self.tview_mensalidade_aba_05.delete(*self.tview_mensalidade_aba_05.get_children())
        self.conecta_db()
        lista = self.cursor.execute("""SELECT 
                id,
                locatario,
                denominado, 
                utilizacao, 
                data_vencto, 
                data_pagto, 
                valor, 
                tipo_pagto,
                quitado FROM mensalidade ORDER BY locatario ASC; """)
        for item in lista:
            #print(item[2], denominado)
            if denominado == item[2]:
                self.tview_mensalidade_aba_05.insert("", END, values=item)

        self.desconecta_db()


    def clique_duplo_mensalidades_aba_05(self, event):
        self.limpa_tudo_aba_05()
        tview = self.tview_mensalidade_aba_05.selection()
        self.conecta_db()
        linhas = self.cursor.execute("""SELECT 
                                            id,
                                            locatario, 
                                            denominado, 
                                            utilizacao, 
                                            data_vencto, 
                                            data_pagto,
                                            valor,
                                            tipo_pagto,
                                            quitado,
                                            extenso
                                             FROM mensalidade""")
   
        for linha_tview in tview:
            c1, c2, c3, c4, c5, c6, c7, c8, c9 = self.tview_mensalidade_aba_05.item(linha_tview, "values")
            for linha in linhas:
                if int(c1) == linha[0]:
                    self.entry_ID_aba_05.insert(END, linha[0])
                    self.entry_locatario_nome_aba_05.insert(END, linha[1])
                    self.entry_denominacao_aba_05.insert(END, linha[2])
                    
                    self.entry_dia_vencto_aba_05.insert(END, linha[4][:2])
                    self.combo_mes_aba_05.set(linha[4][3:5])
                    self.combo_ano_aba_05.set(linha[4][6:])
        
        self.desconecta_db()
    
    
    def atualiza_mensalidades_aba_05(self):
        self.variaveis_aba_05()
        self.variaveis_quitacao_aba_05()
        if self.ide and self.locatario and self.denominacao and self.data_vencto:
            dia = self.entry_dia_vencto_aba_05.get()
            mes = self.combo_mes_aba_05.get()
            ano = self.combo_ano_aba_05.get()
            data_vencto = f'{dia}/{mes}/{ano}'
            self.conecta_db()
            self.cursor.execute("""UPDATE mensalidade SET locatario=?, denominado=?, data_vencto=?, extenso=? WHERE id=?""",
                        (self.locatario, self.denominacao, data_vencto, self.extenso, self.ide,))
            self.conn.commit()
            self.desconecta_db()
            self.insere_mensalidades_aba_05(self.denominacao)
            self.limpa_tudo_aba_05()
    

    def remove_mensalidade_aba_05(self):
        self.variaveis_aba_05()
        if self.ide:
            self.conecta_db()
            self.cursor.execute("""DELETE FROM mensalidade WHERE id=?""",(self.ide,))
            self.conn.commit()
            self.desconecta_db()

            self.limpa_tudo_aba_05()
            self.insere_mensalidades_aba_05(self.denominacao)
        else:
            messagebox.showerror("Erro!", "Selecione um Registro para remover.")
    
    def quitar_mensalidade_aba_05(self):
        self.variaveis_quitacao_aba_05()
        if self.ide and self.data_pagto and self.tipo_pagto and self.extenso:
            self.conecta_db()
            self.cursor.execute("""UPDATE mensalidade SET data_pagto=?, tipo_pagto=?, quitado=?, extenso=? WHERE id=?""",
                        (self.data_pagto, self.tipo_pagto, "Sim", self.extenso, self.ide,))
            self.conn.commit()
            self.desconecta_db()
            self.insere_mensalidades_aba_05(self.denominacao)
            self.limpa_tudo_aba_05()
        else:
            messagebox.showerror("Erro!", "Selecione um registro e preencha todas as casas para quitar.")
    

    def salvar_em_PDF_aba_05(self):
        self.variaveis_aba_05()
        self.variaveis_quitacao_aba_05()
        self.data_pagto = self.data_pagto.replace("/", "-")
        self.nome_pdf = f"Recibo-{self.locatario}-{self.data_pagto}.pdf"
        

    def gera_relatorio_aba_05(self):
        self.variaveis_aba_05()
        self.variaveis_quitacao_aba_05()
        if self.ide:
            self.conecta_db()
            lista = self.cursor.execute("""SELECT id, denominado, data_pagto, valor, extenso FROM mensalidade""")
            data_pagto = ""
            valor = 0.00
            extenso = ""
            denominado = ""
            for linha in lista:
                if int(self.ide) == linha[0]:
                    denominado = linha[1]
                    data_pagto = linha[2]
                    valor = linha[3]
                    extenso = linha[4]

            print(self.ide, denominado, data_pagto[3:5], valor, extenso)
            self.desconecta_db()
            data_pagto = data_pagto.replace("/", "-")
            self.nomepdf = f"Recibo-{self.locatario}-{data_pagto}.pdf"
            self.c = canvas.Canvas(self.nomepdf)
            self.c.setFont("Helvetica", 24)
            self.c.drawString(80, 800, "RECIBO DE PAGAMENTO - ALUGUEL")
            self.c.drawString(50, 785, "___________________________________")
            self.c.setFont("Helvetica", 14) 
            self.c.drawString(40, 760, f"Recibo no valor de R${valor:.2f}.")
            self.c.drawString(40, 740, f"Recebemos do Sr(a). {self.locatario} o valor de")
            self.c.setFont("Helvetica", 22)

            self.c.drawString(40, 710, f"{extenso}.")
            #self.c.setFont("Helvetica", 18)
            #self.c.drawString(50, 735, f"Valor por extenso: {extenso}")
            self.c.setFont("Helvetica", 14)
            self.c.drawString(40, 670, f"Referente aluguel de imóvel denominado, {denominado}.")
            self.c.setFont("Helvetica", 22)
            self.c.drawString(40, 630, f"Imbituba, {data_pagto[:2]} de {self.mes_por_extenso(data_pagto[3:5])} de {data_pagto[6:]}.")
            self.c.setFont("Helvetica", 16)
            self.c.drawString(140, 580, "____________________________________")
            self.c.drawString(150, 560, "     Locador - Ariana Pires Dionel")
            self.c.showPage()
            self.c.save()
            self.salvar_em_PDF_aba_05()
        else:
            messagebox.showerror("Erro!", "Selecione um registro para gerar o Recibo.")

    # Funções da Aba 06
