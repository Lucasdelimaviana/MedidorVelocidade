#medidor de velocidade#
''''
# quais as variaveis?
 - VALOR MEDIDO
 - INTERVALOS ( 80/90,91/100,101/1000)
# o que fazer com as variaveis
 - COMPARAR O VALOR COM OS INTERVALOS E EXIBIR SEM MULTA,LEVE,GRAVE OU GRAVISSIMA
# quais restrições?
 - O VALOR DEVE SER DE > 0 E < 1000
# qual resultado esperado?
 - INFORMAR SE O USUARIO SEM MULTA, LEVE, GRAVE OU GRAVISSIMA
#qual a sequencia de passos a ser feito?
'''
valormedido=int(input("valor medido da sua velocidade "))
velocidademaxima = 80
if valormedido<=velocidademaxima:
  print("sem multa")
elif valormedido>velocidademaxima and valormedido <= velocidademaxima +10:
  print("multa leve")
elif valormedido>velocidademaxima and valormedido<= velocidademaxima +20:
  print("levou multa grave")
elif valormedido>velocidademaxima+20:
  print ("levou multa gravissima")
