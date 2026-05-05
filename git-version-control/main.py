import argparse


def somme(a, b):
    return a + b


def main():
    parser = argparse.ArgumentParser(description="Calculer la somme de deux nombres")
    parser.add_argument("-a", type=float, help="Premier nombre")
    parser.add_argument("-b", type=float, help="Deuxième nombre")

    args = parser.parse_args()

    resultat = somme(args.a, args.b)
    print(f"Résultat : {resultat}")


if __name__ == "__main__":
    main()
