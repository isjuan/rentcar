
class TelaAluguel():

  def tela_opcoes(self):
    print("-------- Aluguel ----------")
    print("Escolha a opcao")
    print("1 - Criar aluguel")   
    print("2 - Listar alugueis")
    print("3 - Excluir aluguel")
    print("0 - Retornar")

    opcao = self.le_int("Escolha a opcao: ", [1, 2, 3, 0])
    return opcao

  def le_int(self, mensagem: str = " ", intervalo: [] = None):
    while True:
      lido = input(mensagem)
      try:
        inteiro = int(lido)
        if intervalo and inteiro not in intervalo:
          raise ValueError
        return inteiro
      except ValueError:
        print ("Valor incorreto: Digite um valor valido")
        if intervalo:
          print("Valores validos:", intervalo)

  def dados_cadastrar(self):
    print("-------- CRIAR ALUGUEL ----------")
    placa = input("Insira a placa do carro: ")
    nome_cliente = input("Insira o nome do cliente: ")
    nome_funcionario = input("Insira o nome do funcionario: ")
    data = input("Codigo de registro do aluguel(unico): ")
    return {"carro": placa, "cliente": nome_cliente, "funcionario": nome_funcionario,  "data": data}

  def mostra_aluguel(self, dados_aluguel):
    print("------------------", "\n", "Carro: ", dados_aluguel["carro"])
    print("Cliente: ", dados_aluguel["cliente"])
    print("Funcionario: ", dados_aluguel["funcionario"])
    print("Codigo do aluguel: ", dados_aluguel["data"])

      
  def exclui_aluguel(self):
    codigo = input("Qual o codigo do aluguel?")
    return codigo
  
  def exclui_aluguel_return(self, bol):
    if bol == False:
      print ("Codigo invalido! Retornando a tela Aluguel")
    if bol == True:
      print ("Aluguel terminado!")

  def cadastro(self, verificador):
    if verificador == False:
      print ("Erro no cadastro! Retornando a tela Aluguel")
    if verificador == True:
      print ("Aluguel criado")
