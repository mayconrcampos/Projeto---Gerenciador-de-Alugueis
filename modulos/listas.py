from datetime import date

class Listas:
    def carrega_listas(self):
        self.lista_dia = []
        self.lista_mes = []
        self.lista_ano = []
        self.lista_ano_mensalidades = []
        self.lista_numero_banheiros = [0, 1, 2, 3, 4]
        self.lista_garagem = ["01 - Sem Garagem", "02 - Vagas Rotativas", "03 - Garagem Fechada"]
        self.lista_tipo_imovel = ["Residencial", "Comercial"]
        self.lista_tipo = ["Aeroporto", "Alameda", "Avenida", "Campo",
                "Chácara", "Colônia", "Condomínio", "Conjunto", "Estrada",
                "Loteamento", "Largo", "Ladeira", "Loteamento", "Parque",
                "Praça", "Residencial", "Rodovia", "Rua", "Travessa", "Viela"]
        self.lista_UF = ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO",
                        "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI",
                        "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"]

        for dia in range(1, 32):
            if dia < 10:
                self.lista_dia.append(f"0{str(dia)}")
            else:
                self.lista_dia.append(str(dia))

        for mes in range(1, 13):
            if mes < 10:
                self.lista_mes.append(f"0{str(mes)}")
            else:
                self.lista_mes.append(str(mes))

        for ano in range(1900, 2030):
            self.lista_ano.append(str(ano))
        


        for ano in range(int(self.data_formatada()[6:]), int(self.data_formatada()[6:]) + 2):
            self.lista_ano_mensalidades.append(str(ano))
            

    def data_formatada(self):
        dt = date.today()
        data_form = dt.strftime("%d/%m/%Y")
        return data_form


