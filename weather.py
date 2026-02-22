import numpy as np

def get_hail_intensity(lat, lon, storm_center_lat, intensity_max=60):
    """Calcule la taille du grêlon (en mm) selon la distance au centre de l'orage"""
    # Simple modèle de couloir horizontal
    distance = abs(lat - storm_center_lat)
    # Décroissance de l'intensité (plus on s'éloigne du centre, plus c'est petit)
    intensity = intensity_max * np.exp(-5 * distance**2)
    return max(0, intensity)
