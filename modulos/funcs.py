from tkinter import *
from tkinter import messagebox

class Funcs:
    def data_de_nascimento(self, dia, mes, ano):
        if dia and mes and ano:
            return f"{dia}/{mes}/{ano}"
        else:
            return False
    

    def variaveis_aba_01(self):
        self.id = self.entry_ID_aba_01.get()
        self.nome = self.entry_nome_aba_01.get()
        self.nacionalidade = self.entry_nacionalidade_aba_01.get()
        self.est_civil = self.combo_estadoCivil_aba_01.get()
        self.profissao = self.entry_profissao_aba_01.get()
        self.rg = self.entry_rg_aba_01.get()
        self.cpf = self.entry_cpf_aba_01.get()
        dia = self.combo_data_nasc_DIA_aba_01.get()
        mes = self.combo_data_nasc_MES_aba_01.get()
        ano = self.combo_data_nasc_ANO_aba_01.get()
        self.data_nasc = f"{dia}/{mes}/{ano}"
        self.tipo = self.combo_Tipo_aba_01.get()
        self.logradouro = self.entry_logradouro_aba_01.get()
        self.numero = self.entry_numero_aba_01.get()
        self.complemento = self.entry_complemento_aba_01.get()
        self.bairro = self.entry_bairro_aba_01.get()
        self.cidade = self.entry_cidade_aba_01.get()
        self.uf = self.combo_UF_aba_01.get()
        cep1 = self.entry_CEP01_aba_01.get()
        cep2 = self.entry_CEP02_aba_01.get()
        self.cep = f"{cep1}-{cep2}"
    
    def variaveis_aba_02(self):
        self.id = self.entry_ID_aba_02.get()
        self.nome = self.entry_nome_aba_02.get()
        self.nacionalidade = self.entry_nacionalidade_aba_02.get()
        self.est_civil = self.combo_estadoCivil_aba_02.get()
        self.profissao = self.entry_profissao_aba_02.get()
        self.rg = self.entry_rg_aba_02.get()
        self.cpf = self.entry_cpf_aba_02.get()
        dia = self.combo_data_nasc_DIA_aba_02.get()
        mes = self.combo_data_nasc_MES_aba_02.get()
        ano = self.combo_data_nasc_ANO_aba_02.get()
        self.data_nasc = f"{dia}/{mes}/{ano}"
        self.tipo = self.combo_Tipo_aba_02.get()
        self.logradouro = self.entry_logradouro_aba_02.get()
        self.numero = self.entry_numero_aba_02.get()
        self.complemento = self.entry_complemento_aba_02.get()
        self.bairro = self.entry_bairro_aba_02.get()
        self.cidade = self.entry_cidade_aba_02.get()
        self.uf = self.combo_UF_aba_02.get()
        cep1 = self.entry_CEP01_aba_02.get()
        cep2 = self.entry_CEP02_aba_02.get()
        self.cep = f"{cep1}-{cep2}"
    
    def variaveis_aba_03(self):
        self.id = self.entry_ID_aba_03.get()
        self.util = self.combo_tipo_imovel_aba_03.get()
        self.area = self.entry_area_aba_03.get()
        self.wc = self.combo_WC_aba_03.get()
        self.garagem = self.combo_garagem_tp_aba_03.get()
        self.const = self.entry_constituida_por_aba_03.get()
        self.tipo = self.combo_Tipo_aba_03.get()
        self.logradouro = self.entry_logradouro_aba_03.get()
        self.numero = self.entry_numero_aba_03.get()
        self.complemento = self.entry_complemento_aba_03.get()
        self.bairro = self.entry_bairro_aba_03.get()
        self.cidade = self.entry_cidade_aba_03.get()
        self.uf = self.combo_UF_aba_03.get()
        cep1 = self.entry_CEP01_aba_03.get()
        cep2 = self.entry_CEP02_aba_03.get()
        self.cep = f"{cep1}-{cep2}"
        self.alugado = "Não"

    
    def valida_valor(self, numero):
        numero = numero.strip()
        if numero.isnumeric():
            return float(numero)
        else:
            c = 0
            for i in numero:
                if i in ",.":
                    c += 1
                    
            if c == 1:
                numero = numero.replace(",", ".")
                return float(numero)
            elif c > 1:
                messagebox.showerror("ERRO", "Valor numérico inválido.")
                return False
            else:
                messagebox.showerror("ERRO", "Valor numérico inválido.")
                return False
    
    
    def variaveis_aba_04(self):
        self.locador_nome = self.entry_locador_nome_aba_04.get()
        self.locador_cpf = self.entry_CPF_locador_aba_04.get()
        self.locatario_nome = self.entry_locatario_nome_aba_04.get()
        self.locatario_cpf = self.entry_CPF_locatario_aba_04.get()
        self.imovel_tipo = self.entry_imovel_tipo_aba_04.get()
        self.denominacao = self.entry_denominacao_aba_04.get()
        self.prazo_contrato = self.combo_prazo_aba_04.get()
        self.data_ass = self.entry_data_ass_aba_04.get()
        self.data_caucao = self.entry_data_caucao_aba_04.get()
        self.valor_aluguel = self.valida_valor(self.entry_valor_aluguel_aba_04.get())
        self.data_entrega = self.entry_data_entrega_aba_04.get()
        self.valor_caucao = self.valida_valor(self.entry_valor_caucao_aba_04.get())
        self.dia_vencto = self.combo_dia_vencto_aba_04.get()
        self.id = self.entry_ID_aba_04.get()
        self.obs = self.txt_observacao_aba_04.get(1.0, END)
    
    def variaveis_aba_05(self):
        self.ide = self.entry_ID_aba_05.get()
        self.locatario = self.entry_locatario_nome_aba_05.get()
        self.denominacao = self.entry_denominacao_aba_05.get()
        dia = self.entry_dia_vencto_aba_05.get()
        mes = self.combo_mes_aba_05.get()
        ano = self.combo_ano_aba_05.get()
        self.data_vencto = f"{dia}/{mes}/{ano}"
    
    def variaveis_quitacao_aba_05(self):
        self.ide = self.entry_ID_aba_05.get()
        self.data_pagto = self.entry_data_pagto_aba_05.get()
        self.tipo_pagto = self.combo_tipo_aba_05.get()
        self.extenso = self.entry_valor_extenso_aba_05.get()
        self.denominacao = self.entry_denominacao_aba_05.get()
    
   
    def limpa_aba_01(self):
        self.entry_ID_aba_01.delete(0, END)
        self.entry_nome_aba_01.delete(0, END)
        self.entry_nacionalidade_aba_01.delete(0, END)
        self.combo_estadoCivil_aba_01.set("")
        self.entry_profissao_aba_01.delete(0, END)
        self.entry_rg_aba_01.delete(0, END)
        self.entry_cpf_aba_01.delete(0, END)
        self.combo_data_nasc_DIA_aba_01.set("")
        self.combo_data_nasc_MES_aba_01.set("")
        self.combo_data_nasc_ANO_aba_01.set("")
        self.combo_Tipo_aba_01.set("")
        self.entry_logradouro_aba_01.delete(0, END)
        self.entry_numero_aba_01.delete(0, END)
        self.entry_complemento_aba_01.delete(0, END)
        self.entry_bairro_aba_01.delete(0, END)
        self.entry_cidade_aba_01.delete(0, END)
        self.combo_UF_aba_01.set("")
        self.entry_CEP01_aba_01.delete(0, END)
        self.entry_CEP02_aba_01.delete(0, END)
    
    def limpa_aba_02(self):
        self.entry_ID_aba_02.delete(0, END)
        self.entry_nome_aba_02.delete(0, END)
        self.entry_nacionalidade_aba_02.delete(0, END)
        self.combo_estadoCivil_aba_02.set("")
        self.entry_profissao_aba_02.delete(0, END)
        self.entry_rg_aba_02.delete(0, END)
        self.entry_cpf_aba_02.delete(0, END)
        self.combo_data_nasc_DIA_aba_02.set("")
        self.combo_data_nasc_MES_aba_02.set("")
        self.combo_data_nasc_ANO_aba_02.set("")
        self.combo_Tipo_aba_02.set("")
        self.entry_logradouro_aba_02.delete(0, END)
        self.entry_numero_aba_02.delete(0, END)
        self.entry_complemento_aba_02.delete(0, END)
        self.entry_bairro_aba_02.delete(0, END)
        self.entry_cidade_aba_02.delete(0, END)
        self.combo_UF_aba_02.set("")
        self.entry_CEP01_aba_02.delete(0, END)
        self.entry_CEP02_aba_02.delete(0, END)
    

    def limpa_aba_03(self):
        self.entry_ID_aba_03.delete(0, END)
        self.combo_tipo_imovel_aba_03.set("")
        self.entry_area_aba_03.delete(0, END)
        self.combo_WC_aba_03.set("")
        self.combo_garagem_tp_aba_03.set("")
        self.entry_constituida_por_aba_03.delete(0, END)
        self.combo_Tipo_aba_03.set("")
        self.entry_logradouro_aba_03.delete(0, END)
        self.entry_numero_aba_03.delete(0, END)
        self.entry_complemento_aba_03.delete(0, END)
        self.entry_bairro_aba_03.delete(0, END)
        self.entry_cidade_aba_03.delete(0, END)
        self.combo_UF_aba_03.set("")
        self.entry_CEP01_aba_03.delete(0, END)
        self.entry_CEP02_aba_03.delete(0, END)

    def limpa_aba_04(self):
        self.entry_locador_nome_aba_04.delete(0, END)
        self.entry_CPF_locador_aba_04.delete(0, END)
        self.entry_locatario_nome_aba_04.delete(0, END)
        self.entry_CPF_locatario_aba_04.delete(0, END)
        self.entry_imovel_tipo_aba_04.delete(0, END)
        self.entry_denominacao_aba_04.delete(0, END)
        self.combo_prazo_aba_04.set("")
        self.entry_data_ass_aba_04.delete(0, END)
        self.entry_data_caucao_aba_04.delete(0, END)
        self.entry_valor_aluguel_aba_04.delete(0, END)
        self.entry_data_entrega_aba_04.delete(0, END)
        self.entry_valor_caucao_aba_04.delete(0, END)
        self.combo_dia_vencto_aba_04.set("")
        self.entry_ID_aba_04.delete(0, END)
        self.txt_observacao_aba_04.delete(1.0, END)

    def limpa_contrato_aba_05(self):
        self.entry_locatario_nome_aba_05.delete(0, END)
        self.entry_denominacao_aba_05.delete(0, END)
        self.entry_dia_vencto_aba_05.delete(0, END)
    
    def limpa_tudo_aba_05(self):
        self.entry_ID_aba_05.delete(0, END)
        self.entry_locatario_nome_aba_05.delete(0, END)
        self.entry_denominacao_aba_05.delete(0, END)
        self.entry_dia_vencto_aba_05.delete(0, END)
        self.combo_mes_aba_05.set("")
        self.combo_ano_aba_05.set("")
        self.entry_data_pagto_aba_05.delete(0, END)
        self.combo_tipo_aba_05.set("")
        self.entry_valor_extenso_aba_05.delete(0, END)

    def limpa_parcial_aba_05(self):
         self.combo_mes_aba_05.delete(0, END)
         #self.combo_ano_aba_05.delete(0, END)


    def formatDataNascimento(self):
        dia = self.combo_data_nasc_DIA_aba_01.get()
        mes = self.combo_data_nasc_MES_aba_01.get()
        ano = self.combo_data_nasc_ANO_aba_01.get()
        if dia and mes and ano:
            return f"{dia}/{mes}/{ano}"
        else:
            return False 
    

    def mes_por_extenso(self, mes):
        if mes == "01":
            return "Janeiro"
        elif mes == "02":
            return "Fevereiro"
        elif mes == "03":
            return "Março"
        elif mes == "04":
            return "Abril"
        elif mes == "05":
            return "Maio"
        elif mes == "06":
            return "Junho"
        elif mes == "07":
            return "Julho"
        elif mes == "08":
            return "Agosto"
        elif mes == "09":
            return "Setembro"
        elif mes == "10":
            return "Outubro"
        elif mes == "11":
            return "Novembro"
        elif mes == "12":
            return "Dezembro"