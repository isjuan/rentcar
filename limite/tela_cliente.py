class TelaCliente():

  def tela_opcoes(self):
    print("-------- Cliente ----------")
    print("Escolha a opcao")
    print("1 - Incluir cliente")
    print("2 - Listar clientes")
    print("3 - Excluir cliente")
    print("4 - Lista alugueis do cliente")
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
    print("-------- INCLUIR CLIENTE ----------")
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    endereco = input("Endereco: ")
    return {"nome": nome, "telefone": telefone, "endereco": endereco}
    

  def mostrar_cliente(self, dados_cliente):
    print("------------------", "\n", "Nome do cliente: ", dados_cliente["nome"])
    print("Telefone: ", dados_cliente["telefone"])
    print("Endereco: ", dados_cliente["endereco"])

  def retorna_cliente(self):
    nome = input("Qual a nome do cliente?")
    return nome
  
  def exclui_cliente_return(self, verificador):
    if verificador == 0:
      print ("Nome invalido! Retornando a tela Cliente")
    if verificador == 1:
      print ("O cliente tem um aluguel ativo! Falha ao remover.")
    if verificador == 2:
      print ("Cliente removido do cadastro!")

  def lista_alugueis(self, lis: list):
    if len(lis) == 0:
      print ("O cliente não tem alugueis!")
    else:
      print ("Os alugueis desse cliente são:", lis)
