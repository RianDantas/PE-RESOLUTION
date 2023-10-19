'''
Escreva uma função chamada saudacao 
que aceita um nome como argumento e imprime "Olá, [nome]!".
'''

def saudacao(nome):
  return f"Olá, {nome}!"

'''
Crie uma função dobro que aceita um 
número como argumento e retorna o dobro desse número.
'''

def dobro(numero):
  return numero * 2

'''
Crie uma função chamada saudacao_personalizada 
que aceita um nome e um idioma como argumentos. 
O idioma é opcional e padrão para "inglês". 
A função deve retornar uma saudação no idioma especificado.
'''

def saudacao_personalizada(nome, idioma):

  if idioma == "inglês":
    return f"Hello, {nome}!"

  elif idioma == "espanhol":
    return f"Hola, {nome}!"

  elif idioma == "francês":
    return f"Bonjour, {nome}!"

'''
Escreva uma função potencia que aceita uma 
base e um expoente (com expoente padrão igual a 2) 
e retorna a base elevada ao expoente
'''

def potencia(base, expoente):
  return base ** expoente

'''
Crie uma função chamada idade_valida que verifica 
se a idade fornecida como argumento é um número 
inteiro válido entre 0 e 150.
'''

def idade_valida(idade):
  if idade <= 150:
    return True

  else:
    return False


'''
Implemente uma função validar_email que verifica se uma 
string fornecida como argumento representa um endereço de 
e-mail válido. Considere que um email válido não deve ter espaços, 
deve conter 01 arroba e terminar com .com
'''
import re
def validar_email(email):

  reg = r"^\S+@\S+\.\S+$"
  x = re.compile(reg)
  return x.match(email) is not None

'''
Escreva uma função calcular_pagamento que aceita os parâmetros 
nomeados horas_trabalhadas e taxa_hora e retorna o pagamento total.
'''

def calcular_pagamento(horas_trabalhadas, taxa_hora):
  return horas_trabalhadas * taxa_hora


'''
Crie uma função que retorne o maior número dentre 3 elementos.
'''

def maior_numero(a, b, c):
  if a > b and a > c:
    return a
  elif b > a and b > c:
    return b
  else:
    return c

'''
Escreva uma função em Python function que aceita uma string e retorna a quantidade de letras maiúsculas e minúsculas.
'''
def contagem_letras(string):
  maiusculas = 0
  minusculas = 0

  for letra in string:
    if letra.isupper():
      maiusculas += 1

    elif letra.islower():
      minusculas +=1
    
    else:
      pass
  
  
  return maiusculas, minusculas
  
'''
Crie uma função chamada len_custom que aceita um iterável (por exemplo, uma lista ou uma string) como argumento e retorna o número de elementos no iterável. Ela deve ter o mesmo comportamento que a função embutida len().
'''

def len_custom(iteravel):
  indice = 0
  
  for i in iteravel:
    indice += 1

  return indice

'''
Crie uma função chamada sum_custom que aceita uma lista de números como argumento e retorna a soma de todos os números na lista. Ela deve ter o mesmo comportamento que a função embutida sum().
'''

def sum_custom(lista_numeros):
  num = 0

  for i in lista_numeros:
    num += i

  return num

'''
Crie uma função chamada max_custom que aceita uma lista de números como argumento e retorna o maior número na lista. Ela deve ter o mesmo comportamento que a função embutida 

'''

def max_custom(lista_numeros):
  
  if len(lista_numeros) == 0:
    return None
  max = lista_numeros[0]
  for i in lista_numeros:
    
    if i > max:
      max = i

    

  return max


'''
Crie uma função chamada min_custom que aceita uma lista de números como argumento e retorna o menor número na lista. Ela deve ter o mesmo comportamento que a função embutida min().
'''
def min_custom(lista_numeros):
  if len(lista_numeros) == 0:
    return None
  min = lista_numeros[0]
  for i in lista_numeros:

    if i < min:
      min = i



  return min


'''
Crie uma função chamada startswith_custom que aceita uma string e um prefixo como argumentos e retorna True se a string começar com o prefixo, caso contrário, retorna False. Ela deve ter o mesmo comportamento que o método str.startswith()
'''
def startswith_custom(string, prefixo):
  tam = len(prefixo)
  str = string[:tam]
  
  if str == prefixo:
    return True
  else:
    return False

'''
Crie uma função chamada endswith_custom que aceita uma string e um sufixo como argumentos e retorna True se a string terminar com o sufixo, caso contrário, retorna False. Ela deve ter o mesmo comportamento que o método str.endswith().
'''

def endswith_custom(string, prefixo):
  tam = len(prefixo)
  str = string[-tam:]

  if str == prefixo:
    return True
  else:
    return False


'''
Crie uma função chamada split_custom que aceita uma string e um caractere de separação como argumentos e retorna uma lista de substrings separadas pelo caractere de separação. Ela deve ter o mesmo comportamento que o método str.split().
'''

def split_custom(string, caracteres_remover):
  list = []  
  str = string
  t = str.find(caracteres_remover)
  tam = len(str[:t])
  str1 = ''
  str2 = ''


  for i in str[:tam]:
    str1 += i

  for i in str[-tam:]:
    str2 += i

  list.append(str1)
  list.append(str2)

  return(list)






  


