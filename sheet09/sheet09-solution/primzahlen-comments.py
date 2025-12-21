def sieb_des_eratosthenes(n):
    if n < 2:
        return []

    # 1. Erstelle eine Liste von Booleans, initialisiert auf True
    # Index repräsentiert die Zahl, Wert repräsentiert "ist Primzahl"
    ist_prim = [True] * (n + 1)
    ist_prim[0] = ist_prim[1] = False  # 0 und 1 sind keine Primzahlen

    # 2. Gehe bis zur Quadratwurzel von n
    for p in range(2, int(n**0.5) + 1):
        # Wenn ist_prim[p] noch True ist, ist p eine Primzahl
        if ist_prim[p]:
            # Markiere alle Vielfachen von p als False (keine Primzahl)
            # Wir beginnen bei p*p, da kleinere Vielfache bereits markiert wurden
            for i in range(p * p, n + 1, p):
                ist_prim[i] = False

    # 3. Sammle alle Indizes, deren Wert noch True ist
    return [i for i, prim in enumerate(ist_prim) if prim]

# Test der Funktion
n_limit = 50
print(f"Primzahlen bis {n_limit}: {sieb_des_eratosthenes(n_limit)}")