# Función para imprimir la tabla de verdad del bicondicional (P <=> Q)
def tabla_verdad_bicondicional():
    print("P\tQ\tP <=> Q")
    print("--------------------")
    for P in [0, 1]:
        for Q in [0, 1]:
            bicondicional_resultado = (P and Q) or (not P and not Q)
            print(f"{P}\t{Q}\t{int(bicondicional_resultado)}")

# Llamar a la función
tabla_verdad_bicondicional()
