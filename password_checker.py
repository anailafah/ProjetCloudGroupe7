import re

def analyze_password(password: str):

    score = 0
    ameliorations = []

    if len(password) >= 8:
        score += 1
    else:
        ameliorations.append("Trop court (min 8 caractères)")

    if re.search(r'[A-Z]', password):
        score += 1
    else:
        ameliorations.append("Ajouter une majuscule")

    if re.search(r'[a-z]', password):
        score += 1
    else:
        ameliorations.append("Ajouter une minuscule")

    if re.search(r'\d', password):
        score += 1
    else:
        ameliorations.append("Ajouter un chiffre")

    if re.search(r'[!@#$%^&*(),.?\":{}|<>]', password):
        score += 1
    else:
        ameliorations.append("Ajouter un caractère spécial")

    niveaux = {
        5: "Fort",
        4: "Moyen",
        3: "Faible",
        2: "Très faible",
        1: "Critique",
        0: "Critique"
    }

    return {
        "score": f"{score}/5",
        "niveau": niveaux[score],
        "ameliorations": ameliorations
    }