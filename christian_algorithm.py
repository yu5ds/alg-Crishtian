import random

# Función que simula el algoritmo de Christian
def christian_algorithm(seed, num_randoms):
    random.seed(seed)  # Establecer la semilla para la generación de números aleatorios
    random_numbers = [random.randint(0, 100) for _ in range(num_randoms)]  # Generar números aleatorios
    return random_numbers

# Función principal para probar el algoritmo
def main():
    seed = 42  # Semilla para generar números aleatorios
    num_randoms = 10  # Cantidad de números aleatorios a generar
    
    # Llamada al algoritmo de Christian
    random_numbers = christian_algorithm(seed, num_randoms)
    
    # Mostrar los números aleatorios generados
    print(f"Números aleatorios generados: {random_numbers}")

# Ejecución del script
if __name__ == "__main__":
    main()
