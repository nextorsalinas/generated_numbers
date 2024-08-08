import random

def generate_unique_numbers(initial_prefixes, count):
    numbers = set()  # Usamos un conjunto para asegurar la unicidad
    
    # Asegúrate de que se proporcionen exactamente 5 prefijos iniciales
    if len(initial_prefixes) != 5:
        raise ValueError("Debe proporcionar exactamente 5 prefijos iniciales.")
    
    # Asegúrate de que cada prefijo inicial tenga al menos 5 dígitos
    for prefix in initial_prefixes:
        if len(str(prefix)) < 5:
            raise ValueError("Cada prefijo inicial debe tener al menos 5 dígitos.")
    
    # Generar números hasta alcanzar el conteo deseado
    while len(numbers) < count:
        # Elegir un prefijo inicial aleatorio de la lista proporcionada
        prefix = random.choice(initial_prefixes)
        # Generar una parte aleatoria para completar los 13 dígitos (8 dígitos restantes)
        random_suffix = random.randint(10000000, 99999999)  # 8 dígitos aleatorios
        # Concatenar el prefijo inicial con la parte aleatoria y asegurarse de que sea de 13 dígitos
        number = f"{prefix}{random_suffix:08d}"  # Aseguramos que el sufijo tenga 8 dígitos con relleno
        # Agregar el número generado al conjunto (automáticamente evita duplicados)
        numbers.add(number)
    
    return list(numbers)

# Prefijos iniciales proporcionados por el usuario
initial_prefixes = [99916, 99916, 99916, 99916, 99916]  # Aquí defines los 5 prefijos iniciales

# Cantidad de números de 13 dígitos a generar
count = 1000

# Generar los números únicos
generated_numbers = generate_unique_numbers(initial_prefixes, count)

# Guardar los números generados en un archivo de texto
with open("generated_numbers.txt", "w") as file:
    for number in generated_numbers:
        file.write(number + "\n")

print(f"{count} números únicos de 13 dígitos generados y guardados en 'generated_numbers.txt'.")

