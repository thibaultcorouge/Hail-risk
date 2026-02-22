import numpy as np
import pandas as pd
from weather import get_hail_intensity
from engine import calculate_loss, apply_reinsurance
from config import AREA_BOUNDS

def run_stochastic_simulation(portfolio, n_simulations=100):
    all_losses = []
    
    print(f"Lancement de {n_simulations} simulations d'orages...")
    
    for i in range(n_simulations):
        # 1. On génère un centre d'orage aléatoire dans la zone
        random_lat = np.random.uniform(AREA_BOUNDS['lat_min'], AREA_BOUNDS['lat_max'])
        
        # 2. On calcule l'intensité pour chaque contrat
        hail_sizes = portfolio.apply(lambda r: get_hail_intensity(r.lat, r.lon, random_lat), axis=1)
        
        # 3. On calcule la perte brute de l'événement
        event_loss = portfolio.apply(lambda r: calculate_loss(r, hail_sizes[r.name]), axis=1).sum()
        
        # 4. On applique la réassurance
        net_loss, ceded_loss = apply_reinsurance(event_loss)
        
        all_losses.append({
            'sim_id': i,
            'storm_lat': random_lat,
            'gross_loss': event_loss,
            'net_loss': net_loss
        })
    
    return pd.DataFrame(all_losses)
