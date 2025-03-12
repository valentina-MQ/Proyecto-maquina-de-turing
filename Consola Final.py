#Valentina Montenegro Quevedo / Laura Valeria Vargas Gomez / Juan Sebastian Acosta

import MaquinaTuring


def mostrar_menu():
    print("=" * 30)
    print("   CALCULADORA TURING")
    print("=" * 30)
    print("[1] Salir")
    print("[2] Suma")
    print("[3] Resta")
    print("[4] Multiplicación")
    print("[5] División")
    print("[6] Raíz cuadrada")
    print("[7] Potencia")
    print("[8] Logaritmo natural")
    print("[9] Seno")
    print("=" * 30)


def obtener_numero(mensaje):
    while True:
        valor = input(mensaje)
        if valor.replace('.', '', 1).isdigit():  # Permitir números decimales
            return float(valor)
        print("⚠ Error: Ingresa un número válido.")


def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if not opcion.isdigit():
            print("⚠ Error: Ingresa un número del menú.\n")
            continue

        opcion = int(opcion)

        if opcion == 1:
            print("👋 Saliendo del programa...")
            break

        if opcion not in range(2, 10):
            print("⚠ Error: Opción no válida. Intenta de nuevo.\n")
            continue

        if opcion in [2, 3, 4, 5, 7]:
            num1 = obtener_numero("Ingresa el primer número: ")
            num2 = obtener_numero("Ingresa el segundo número: ")

        elif opcion in [6, 8, 9]:
            num1 = obtener_numero("Ingresa el número: ")

        if opcion == 2:
            resultado = MaquinaTuring.suma(num1, num2)
        elif opcion == 3:
            resultado = MaquinaTuring.resta(num1, num2)
        elif opcion == 4:
            resultado = MaquinaTuring.multiplicacion(num1, num2)
        elif opcion == 5:
            if num2 == 0:
                print("⚠ Error: No se puede dividir por cero.\n")
                continue
            resultado = MaquinaTuring.division(num1, num2)
        elif opcion == 6:
            resultado = MaquinaTuring.raiz(num1)
        elif opcion == 7:
            resultado = MaquinaTuring.potencia(num1, num2)
        elif opcion == 8:
            resultado = MaquinaTuring.ln(num1)
        else:
            resultado = MaquinaTuring.sin(num1)

        print(f"\n✅ Resultado: {resultado}\n")


if __name__ == "__main__":
    main()