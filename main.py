#janela => 500 x 500
#título
#campos de selecionar moedas de origem e destino
#botão para converter
#lista de exibição com os nomes das moedas
 
#importar a biblioteca que vai fazer a janela
import customtkinter
 
#criar e configurar a janela
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")
 
janela = customtkinter.CTk()
janela.geometry("500x500")
 
#criar os botões, textos e demais elementos
titulo = customtkinter.CTkLabel(janela, text="Conversor de Moedas", font=("", 20))
texto_moeda_origem = customtkinter.CTkLabel(janela, text="Selecione a moeda de origem")
campo_moeda_origem = customtkinter.CTkOptionMenu(janela, values= ["USD", "EUR", "BRL", "BTC",])
texto_moeda_destino = customtkinter.CTkLabel(janela, text="Selecione a moeda de destino")
campo_moeda_destino = customtkinter.CTkOptionMenu(janela, values= ["USD", "EUR", "BRL", "BTC",])
lista_moedas = customtkinter.CTkScrollableFrame(janela)



moedas_disponiveis = ["USD: DOLLAR AMERICANO","EUR: EURO", "BRL: REAL BRASILEIRO", "BTC: BITCOIN"]
for moeda in moedas_disponiveis:
    texto_moeda = customtkinter.CTkLabel(lista_moedas, text= moeda)
    text = moeda
    texto_moeda.pack()


def converter_moeda():
    print("Converter moeda")
botao_converter = customtkinter.CTkButton( janela, text= "Converter", command= converter_moeda) 


#colocar os elementos criados na tela
titulo.pack()
texto_moeda_origem.pack(padx = 5, pady = 5)
campo_moeda_origem.pack(padx = 5, pady = 5)
texto_moeda_destino.pack(padx = 5, pady = 5)
campo_moeda_destino.pack(padx = 5, pady = 5)
botao_converter.pack(padx = 5, pady = 5)
lista_moedas.pack(padx = 5, pady = 5)






#rodar a janela
janela.mainloop()

