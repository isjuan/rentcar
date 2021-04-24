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
  
  def exclui_carro_return(self, bol):
    if bol == False:
      print ("Placa invalida! Retornando a tela Carro")
    if bol == True:
      print ("Carro excluido!")

      
