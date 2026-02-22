import numpy as np
from generator import generate_portfolio
from simulator import run_stochastic_simulation
from weather import get_hail_intensity
from engine import calculate_loss
from visualizer import plot_vulnerability_curve, plot_impact_map, plot_ep_curve

# 1. Création du portefeuille
portfolio = generate_portfolio(1500)

# 2. CALCUL D'UN SCÉNARIO PRÉCIS (pour la carte)
# On définit un centre d'orage au milieu de la zone
STORM_LAT = 44.2 
# On calcule l'intensité pour chaque maison
portfolio['hail_mm'] = portfolio.apply(lambda r: get_hail_intensity(r.lat, r.lon, STORM_LAT), axis=1)
# On calcule la perte pour chaque maison (C'est ici qu'on crée la colonne manquante !)
portfolio['loss_amount'] = portfolio.apply(lambda r: calculate_loss(r, r['hail_mm']), axis=1)

# 3. Simulation stochastique (Monte-Carlo pour les stats globales)
results = run_stochastic_simulation(portfolio, n_simulations=100)

# 4. Visualisations
print("Génération des analyses visuelles...")

# La carte fonctionnera maintenant car 'loss_amount' existe dans portfolio
plot_impact_map(portfolio)

# Le reste des graphiques
plot_vulnerability_curve()
plot_ep_curve(results['gross_loss'].values)
