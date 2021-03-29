
class TelaSistema:
  
  def tela_opcoes(self):
    print("-------- Aluguel ---------")
    print("Escolha sua opcao")
    print("1 - Cliente")
    print("2 - Funcionario")
    print("3 - Carro")
    print("4 - Aluguel")
    print("0 - Finalizar sistema")
    opcao = int(input("Escolha a opcao:"))
    return opcao