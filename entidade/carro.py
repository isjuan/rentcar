
class Carro:
  def __init__(self, placa: int, modelo: str, cor: str):
    self.__placa = placa
    self.__modelo = modelo
    self.__cor = cor
    self.__aluguel = []
    self.__alugado = False

  def aluga(self, aluguel, bol):
    if bol == True:
      self.__alugado = True
      self.__aluguel.append(aluguel)
    if bol == False:
      self.__alugado = False
      self.__aluguel.remove(aluguel)

  def alugado(self):
    return self.__alugado


  @property
  def placa(self):
    return self.__placa

  @property
  def modelo(self):
    return self.__modelo

  @property
  def cor(self):
    return self.__cor

  @placa.setter
  def placa(self):
    self.__placa = placa
  
  @modelo.setter
  def modelo(self):
    self.__modelo = modelo

  @cor.setter
  def cor(self):
  	self.__cor = cor

  def novo(self, aluguel):
    self.__aluguel.apend(aluguel)

  def remove(self, aluguel):
    self.__aluguel.remove(aluguel)

  def lista(self):
    return self.__aluguel