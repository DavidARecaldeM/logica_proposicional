# Función para imprimir la tabla de verdad de P implica Q (P => Q)
def tabla_verdad_implicacion():
    print("P\tQ\tP => Q")
    print("--------------------")
    for P in [0, 1]:
        for Q in [0, 1]:
            implicacion_resultado = (not P) or Q
            print(f"{P}\t{Q}\t{int(implicacion_resultado)}")

# Llamar a la función
tabla_verdad_implicacion()
 