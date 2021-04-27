
from abc import ABC

class Pessoa(ABC):

  def __init__(self, nome: str, telefone: int, endereco: str):
    self.__nome = nome
    self.__telefone = telefone
    self.__endereco = endereco

  @property
  def nome(self):
    return self.__nome

  @property
  def telefone(self):
    return self.__telefone

  @property
  def endereco(self):
    return self.__endereco

  @nome.setter
  def nome(self):
  	self.__nome = nome
  
  @telefone.setter
  def telefone(self):
  	self.__telefone = telefone
      
  @endereco.setter
  def endereço(self):
  	self.__endereco = endereco
  
  