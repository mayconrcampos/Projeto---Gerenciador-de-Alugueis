from datetime import date

data = ["26/08/1982", "25/05/1950"]
print(data[0][:2], data[0][3:5], data[1][6:])

cep = ["88780-000", "88080-400"]
print(cep[0][:5], cep[0][6:])

def gera_mensalidades(dia_vencto):
    anos = ["2020", "2021", "2022"]
    meses = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
    parcelas = []
    for ano in anos:
        for mes in meses:
            parcelas.append(f"{dia_vencto}/{mes}/{ano}")

    for parcela in parcelas:
        print(parcela)


            


