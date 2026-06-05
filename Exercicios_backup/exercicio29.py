def equipar_arma(dano_base):
    def calcular(forca):
        return dano_base + forca
    return calcular
machado = equipar_arma(50)
espada = equipar_arma(10)
print(f'o dano do machado é {machado(60)}, e o dano da espada é {espada(70)}')