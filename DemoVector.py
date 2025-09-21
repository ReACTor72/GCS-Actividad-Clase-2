import random
import os

def main():

    os.system('cls' if os.name == 'nt' else 'clear')

    Limite_n_valores_vector = 20
    min_val_aleatorio = 1
    max_val_aleatorio = 500
    
    es_primo = lambda x: x > 1 and all(x % i != 0 for i in range(2, int(x**0.5) + 1))

    resultados = {}
    opcion_de_menu = '9'

    vector_num_aleatorios = []

    while opcion_de_menu != '4':
        contador_temporal_resultados = 0

        print("\n\t" + "~"*60, f"N={Limite_n_valores_vector}, Valores (Min={min_val_aleatorio}, Max={max_val_aleatorio})")
        print("\n\tVector generado:", vector_num_aleatorios)

        print("\n\t\tMENÚ DE OPCIONES")
        print("\t" + "~"*60)
        print(f"\n\t1. Suma de números del vector: \t\t\t{resultados.get('suma', 'No calculado')}")
        print(f"\t2. Contar los números que no son primos: \t{resultados.get('no_primos', 'No calculado')}")
        print(f"\t3. Contar los números capicúas: \t\t{resultados.get('capicuas', 'No calculado')}")
        print("\t4. Salir.")
        print("\t" + "~"*60)
        opcion_de_menu = input("\n\tSeleccione una opción: ")

        if opcion_de_menu == '1':
            print(f"\n-> Suma calculada: {resultados['suma']}")

        elif opcion_de_menu == '2':
            for numero_a_verificar in vector_num_aleatorios:
                contador_temporal_resultados += (0 if es_primo(numero_a_verificar) else 1)

            resultados['no_primos'] = contador_temporal_resultados            
            print(f"\n-> Cantidad de no primos: {resultados['no_primos']}")
            
        elif opcion_de_menu == '3':
            print(f"\n-> Cantidad de capicúas: {resultados['capicuas']}")

        elif opcion_de_menu == '4':
            print("\n\t-- Fin del ejercicio --")
            
        else:
            print("* "*15, "Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()