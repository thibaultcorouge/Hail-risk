# Configuration des paramètres métier
AREA_BOUNDS = {'lat_min': 43.5, 'lat_max': 45.0, 'lon_min': 0.5, 'lon_max': 2.5}
#zone Sud-Ouest

# Paramètres de vulnérabilité (Sigmoïde)
# DR = 1 / (1 + exp(-ALPHA * (hail_size - BETA)))
VULNERABILITY_PARAMS = {
    'ALPHA': 0.8, 
    'BETA': 4.5,   # Le grêlon "moyen" qui cause 50% de dégâts
    'RESISTANCE': {'Tuile': 1.0, 'Ardoise': 0.8, 'Zinc': 0.5}
}

# Réassurance (Excess of Loss)
REINSURANCE = {
    'PRIORITY': 2_000_000, # L'assureur paie les 2 premiers millions
    'LIMIT': 10_000_000    # Le réassureur couvre jusqu'à 10M au-delà
}
