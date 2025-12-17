#função "print" serve para exibir as coisas na tela e ela recebe um argumento
#ou metodos, por exemplo (12,3) para fazer a separação é necessario usar virgula
#sep= é um separador que vc usa com as aspas simples ou duplas, que ira separa conforme oq a dentro da aspas.
#\r \n são duas quebras de linhas (para windowns) mec e linux usam somente \n
#print(12, 34, sep='-', end='\n')
#print(56, 78, sep='-', end='\n')
nove_digitos='075602615'
digito_1 = (sum(int(digito) * peso for digito, peso in zip(nove_digitos, range(10, 1, -1))) * 10 % 11) % 10
print(digito_1)