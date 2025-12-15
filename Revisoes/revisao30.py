'''
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade(ruim)
'''
velocidade = 61
local_carro = 100

RADAR_1 = 60 #velocidade máxima o radar 1
LOCAL_1 = 100 #local onde o radar 1 está
RADAR_RANGE = 1 # A distância onde o radar pega
velocidade_passou_radar_1 = velocidade > RADAR_1
carro_multao =local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <=(LOCAL_1 + RADAR_RANGE)

if velocidade_passou_radar_1:
    print('Velocidade carro passou o radar 1')
if  carro_multao and velocidade_passou_radar_1:
    print('Carro multado em radar 1')