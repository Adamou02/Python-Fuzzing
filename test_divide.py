import atheris
import sys


# 1. Fonction de division - Vérifie les inputs pour éviter une division par zéro
def divide(data):
    if len(data) < 2:
        return  # Ignore les inputs trop courts

    a = data[0]
    b = data[1]

    if b == 0:
        raise ValueError("Division par zéro détectée")
    if a is None or b is None:
        raise TypeError("Valeur null détectée dans la division")
    
    return a / b
    

# 4. Fonction principale pour exécuter les tests
def test_input(data):
    # Split input data into chunks for testing multiple functions
    if len(data) < 2:
        return

    try:
        # Test sur la fonction de division
        divide(data)

    except Exception as e:
        print(f"Crash détecté : {e}")


# Configuration et lancement d'Atheris
def main():
    atheris.Setup([sys.argv[0], "-runs=100"], test_input)
    print("Fuzzing en cours...")
    atheris.Fuzz()


if __name__ == "__main__":
    main()
