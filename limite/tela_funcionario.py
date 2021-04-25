class TelaFuncionario():

  def tela_opcoes(self):
    print("-------- Funcionario ----------")
    print("Escolha a opcao")
    print("1 - Incluir funcionario")
    print("2 - Listar funcionarios")
    print("3 - Excluir funcionario")
    print("4 - Ver alugueis do funcionario")
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
    print("-------- INCLUIR FUNCIONARIO ----------")
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    endereco = input("Endereco: ")
    return {"nome": nome, "telefone": telefone, "endereco": endereco}
    

  def mostrar_funcionario(self, dados_funcionario):
    print("------------------", "\n", "Nome do funcionario: ", dados_funcionario["nome"])
    print("Telefone: ", dados_funcionario["telefone"])
    print("Endereco: ", dados_funcionario["endereco"])

  def retorna_funcionario(self):
    nome = input("Qual a nome do funcionario?")
    return nome
  
  def exclui_funcionario_return(self, verificador):
    if verificador == 0:
      print ("Nome invalido! Retornando a tela Funcionario")
    if verificador == 1:
      print ("O funcionario tem um aluguel ativo! Falha ao remover.")
    if verificador == 2:
      print ("Funcionario removido do cadastro!")

  def lista_alugueis(self, lis: list):
    if len(lis) == 0:
      print ("O funcionario não tem alugueis!")
    else:
      print ("Os alugueis desse funcionario são:", lis)
