import numpy as np
from config import VULNERABILITY_PARAMS, REINSURANCE

def calculate_loss(row, hail_mm):
    if hail_mm < 20: return 0  # Pas de dégâts significatifs sous 20mm
    
    alpha = VULNERABILITY_PARAMS['ALPHA']
    beta = VULNERABILITY_PARAMS['BETA']
    res = VULNERABILITY_PARAMS['RESISTANCE'][row['roof_type']]
    
    # Normalisation du grêlon pour la fonction (cm)
    d = hail_mm / 10
    damage_ratio = (1 / (1 + np.exp(-alpha * (d - beta)))) * res
    return damage_ratio * row['capital']

def apply_reinsurance(gross_loss):
    prio = REINSURANCE['PRIORITY']
    lim = REINSURANCE['LIMIT']
    
    ceded_loss = min(max(0, gross_loss - prio), lim)
    net_loss = gross_loss - ceded_loss
    return net_loss, ceded_loss
