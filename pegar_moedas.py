import xmltodict 

def nomes_moedas():
    with open("moedas.xml", "rb") as arquivo_moedas: #em formato de bite 
        dic_moedas = xmltodict.parse(arquivo_moedas)

    moedas = dic_moedas["xml"]
    return moedas

def conversoes_disponiveis():
    with open("conversoes.xml", "rb") as arquivo_coversoes:
        dic_conversoes = xmltodict.parse(arquivo_coversoes)
        conversoes =dic_conversoes["xml"]
        dic_conversoes_disponiveis = {} #cria um dicionário vazio// 
        
        
        for par_conversao in conversoes:
            # usb-brl
            moeda_origem, moeda_destino = par_conversao.split("-") #split separa a palavra//
            if moeda_origem in dic_conversoes_disponiveis:
                dic_conversoes_disponiveis[moeda_origem]. append(moeda_destino)
            else:
                dic_conversoes_disponiveis[moeda_origem] = [moeda_destino   ]
        return dic_conversoes_disponiveis





#link = "https://economia.awesomeapi.com.br/last/USD-BRL"
