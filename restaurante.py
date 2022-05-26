class Restaurante: 

  def __init__(self, nome, tipo_cozinha):
      self.restaurante = nome
      self.tipo = tipo_cozinha
      self.status = 'Aberto'
      self.pessoas_atendidas = 0
      
  def set_pessoas_atendidas(self):
      pessoas_atendidas = int(input("Insira a quantidade de clientes atendidos: "))
      return pessoas_atendidas

  
  def exibir(self):
    descricao= f'Restaurante {self.restaurante}: cozinha:{self.tipo}'
    return descricao

  def situacao(self):
    print(f'O restaurante está {self.status}. Verifique o horário de funcionamento')

  def horario(self):
    horarios = f'Seg a Sex: 12h-16h\nSab: 12h- 22h\n Dom: fechado.'
    return horarios

  def __str__(self):
   return f'<Restaurante: {self.restaurante}>'


class Usuario:
   
  def __init__(self,primeiro_nome,segundo_nome,tipo_pagamento, tentativas_login): 
     self.primeiro_nome = primeiro_nome
     self.segundo_nome = segundo_nome
     self.tipo_pagamento = tipo_pagamento
     self.tentativas_login = tentativas_login

  def descricaoUsuario(self): 
    return f'Primeiro nome: {self.primeiro_nome}\nSegundo nome: {self.segundo_nome}\nTipo de pagamento: {self.tipo_pagamento}'

  def greet_usuario(self):
     print(f'Olá {self.primeiro_nome}')

  def incrementar_tentativas(self, tentativas_login): 
      tentativas_login += 1
      return tentativas_login

  def reset_tentativas(self, tentativas_login):
     tentativas_login -=1
     return tentativas_login
   