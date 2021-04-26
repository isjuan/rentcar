class TelaCarro():

  def tela_opcoes(self):
    
    print("-------- Carro ----------")
    print("Escolha a opcao")
    print("1 - Incluir carro")
    print("2 - Listar carros")
    print("3 - Excluir carro")
    print("0 - Retornar")

    opcao = self.le_int("Escolha a opcao: ", [1, 2, 3, 4, 0])
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
    print("-------- INCLUIR CARRO ----------")
    placa = input("Placa: ")
    modelo = input("Modelo: ")
    cor = input("Cor: ")  
    return {"placa": placa, "modelo": modelo, "cor": cor}
  
  def mostrar_carro(self, dados_carro):
    print("------------------", "\n", "Modelo do carro: ", dados_carro["modelo"])
    print("Placa: ", dados_carro["placa"])
    print("Cor: ", dados_carro["cor"])
      
  def exclui_carro(self):
    placa = input("Qual a placa do carro?")
    return placa
  
  def exclui_carro_return(self, verificador):
    if verificador == 0:
      print ("Nome invalido! Retornando a tela Carro")
    if verificador == 1:
      print ("O carro está em um aluguel ativo! Falha ao remover.")
    if verificador == 2:
      print ("Carro removido do cadastro!")

  def aluguel_erro(self, carro_verificador):
    if carro_verificador == 0:
      print ("O carro informado nao foi encontrado!")
    if carro_verificador == 1:
      print ("O carro informado ja esta alugado!")

      
