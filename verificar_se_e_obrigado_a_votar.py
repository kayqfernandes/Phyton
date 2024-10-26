#Verificar se pode votar ou não

resposta = int(input("Qual é a sua Idade?: "))

if resposta >= 18 and resposta <= 65:
    print("Você é Obrigado a votar")

else:
    print("Você não é Obrigado a Votar")