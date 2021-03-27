
class Carro:
  def __init__(self, placa: int, modelo: str, cor: str):
    self.__placa = placa
    self.__modelo = modelo
    self.__cor = cor

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