from itertools import cycle  


def validar_rut(rut):

    rut = rut.upper().replace("-", "").replace(".", "")


    rut_aux = rut[:-1]
    dv = rut[-1]


    if not rut_aux.isdigit() or not (1_000_000 <= int(rut_aux) <= 25_000_000):
        return False


    revertido = map(int, reversed(rut_aux))
    factors = cycle(range(2, 8))
    suma = sum(d * f for d, f in zip(revertido, factors))
    residuo = 11 - (suma % 11)


    if residuo == 11:
        dv_calculado = '0'
    elif residuo == 10:
        dv_calculado = 'K'
    else:
        dv_calculado = str(residuo)


    return dv == dv_calculado


def main():
    rut_usuario = input("Ingrese un RUT para validar (con o sin puntos y guión): ")
    if validar_rut(rut_usuario):
        print("El RUT ingresado es válido.")
    else:
        print("El RUT ingresado es inválido.")


if __name__ == "__main__":
    main()

#Creacion,
#MMOVET.
