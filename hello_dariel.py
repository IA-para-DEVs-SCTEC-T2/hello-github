# hello_dariel.py
# Calcula la sumatoria de las posiciones en el alfabeto de cada letra del nombre

def alphabet_position(letter):
    """Retorna la posición de una letra en el alfabeto (a=1, b=2, ..., z=26)."""
    letter = letter.lower()
    if letter.isalpha():
        return ord(letter) - ord('a') + 1
    return 0

def letter_sum(name):
    """Calcula la sumatoria de las posiciones alfabéticas de las letras del nombre."""
    total = 0
    details = []
    for letter in name:
        if letter.isalpha():
            pos = alphabet_position(letter)
            details.append(f"  {letter.upper()} = {pos}")
            total += pos
    return total, details

def hello_dariel():
    name = "Dariel"
    print(f"Hello, my name is {name}!")
    print()
    print(f"Sumatoria de letras del nombre '{name}' en el alfabeto:")
    print()

    total, details = letter_sum(name)

    for d in details:
        print(d)

    print(f"  {'─' * 10}")
    print(f"  Total = {total}")
    print()
    print(f"La sumatoria de las posiciones alfabéticas de '{name}' es: {total}")

if __name__ == "__main__":
    hello_dariel()
