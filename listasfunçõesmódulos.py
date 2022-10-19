equipamentos = []
valores = []
seriais = []
departamentos = []
resposta = 'S'
while resposta == 'S':

  equipamentos.append(input('Equipamentos: '))
  valores.append(float(input('valor: ')))
  seriais.append(int(input('Número Serial: ')))
  departamentos.append(input('Departamentos: '))
  resposta = input('Digite \'S\' para continuar: ').upper()
  
  busca=input('\nDigite o nome do equipamento que deseja buscar: ')
for indice in range (0,len(equipamentos)):
  print('\nEquipamentos..: ', (indice+1))
  print('Nome.........: ', equipamentos[indice])
  print('Valor........: ', valores[indice])
  print('Serial.......: ', seriais[indice])
  print('Departamento.: ', departamentos[indice])
  
  
  
  
  
  
  
  
  