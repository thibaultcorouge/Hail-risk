import pandas as pd
import numpy as np
from config import AREA_BOUNDS

def generate_portfolio(n=1000):
    np.random.seed(42)
    data = {
        'policy_id': range(n),
        'lat': np.random.uniform(AREA_BOUNDS['lat_min'], AREA_BOUNDS['lat_max'], n),
        'lon': np.random.uniform(AREA_BOUNDS['lon_min'], AREA_BOUNDS['lon_max'], n),
        # On utilise une loi Gamma pour simuler des valeurs de maisons réalistes
        'capital': np.random.gamma(shape=3, scale=70000, size=n),
        'roof_type': np.random.choice(['Tuile', 'Ardoise', 'Zinc'], n, p=[0.7, 0.2, 0.1])
    }
    return pd.DataFrame(data)
