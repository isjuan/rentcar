
class TelaSistema:
  
  def tela_opcoes(self):
    print("-------- Aluguel ---------")
    print("Escolha sua opcao")
    print("1 - Cliente")
    print("2 - Funcionario")
    print("3 - Carro")
    print("4 - Aluguel")
    print("0 - Finalizar sistema")
    
    opcao = self.le_int("Escolha a opcao: ", [1, 2, 3, 4, 0])
    return opcao

  def le_int(self, mensagem: str, intervalo: [] = None)
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