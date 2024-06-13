menu = """
==== MENU ====
  
  [d] Depositar
  [s] Sacar 
  [e] Extrato
  [q] Sair

==============
"""
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

  opcao = input(menu + "\nEscolha uma opção: ")

  if opcao == "d":
    valor_deposito = float(input("Informe o valor do deposito: "))
    if valor_deposito > 0: 
      saldo += valor_deposito
      extrato += f"""
  Deposito: R${valor_deposito}
  Saldo: R${saldo}\n

  """
    else:
      print("Valor inválido")
    
  elif opcao == "s":
    if numero_saques == LIMITE_SAQUES:
      print("Limites de saques atingido")
    else:
      valor_saque = float(input("Informe o valor do saque: "))
      if valor_saque > saldo:
        print("Saldo insuficiente")
      elif valor_saque < 0:
        print("Valor inválido")
      else:
        if valor_saque > 500:
          print("Valor maior do que o limite de saque permitido")
        else:
          saldo -= valor_saque
          numero_saques += 1
          extrato += f"""
Deposito: R${valor_saque}
Saldo: R${saldo}\n

  """

  elif opcao == "e":
    print("\n============ EXTRATO ============")
    print("Não foram feitas movimentações" if not extrato else extrato)
    print(f"Saldo: {saldo:.2f}")
    print("==================================")
  elif opcao == "q":
    break

  else: 
    print("Opção invalida, por favor selecione a opção desejada!")