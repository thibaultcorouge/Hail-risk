import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from config import VULNERABILITY_PARAMS

# --- 1. LA SIGMOÏDE (Physique du risque) ---
def plot_vulnerability_curve():
    hail_sizes = np.linspace(0, 10, 100)
    alpha = VULNERABILITY_PARAMS['ALPHA']
    beta = VULNERABILITY_PARAMS['BETA']
    
    plt.figure(figsize=(8, 5))
    for roof, res in VULNERABILITY_PARAMS['RESISTANCE'].items():
        # Formule : DR = 1 / (1 + exp(-alpha * (d - beta)))
        dr = (1 / (1 + np.exp(-alpha * (hail_sizes - beta)))) * res
        plt.plot(hail_sizes, dr * 100, label=f'Toiture {roof}')

    plt.title("Fonction de dommage : Vulnérabilité du bâti")
    plt.xlabel("Diamètre du grêlon (cm)")
    plt.ylabel("Ratio de dommage (%)")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.show()

# --- 2. LA HEATMAP (Géographie du risque) ---
def plot_impact_map(df):
    impacted_df = df[df['loss_amount'] > 0]
    if impacted_df.empty:
        print("Aucune perte à afficher sur la carte.")
        return

    fig = px.density_mapbox(
        impacted_df, 
        lat='lat', lon='lon', z='loss_amount', 
        radius=15,
        center=dict(lat=df.lat.mean(), lon=df.lon.mean()), 
        zoom=7,
        mapbox_style="carto-positron",
        title="Localisation des pertes financières"
    )
    fig.show()

# --- 3. LA COURBE EP (Finance du risque) ---
def plot_ep_curve(losses):
    sorted_losses = np.sort(losses)[::-1]
    probabilities = np.arange(1, len(sorted_losses) + 1) / len(sorted_losses)
    
    aal = np.mean(losses)
    pml_99 = np.percentile(losses, 99)

    plt.figure(figsize=(10, 6))
    plt.plot(sorted_losses, probabilities, color='#2E86C1', lw=2)
    plt.axvline(aal, color='green', ls='--', label=f'AAL : {aal:,.0f}€')
    plt.axvline(pml_99, color='red', ls='--', label=f'PML 99% : {pml_99:,.0f}€')
    
    plt.yscale('log')
    plt.title("Courbe de Probabilité de Dépassement")
    plt.xlabel("Pertes (€)")
    plt.ylabel("Probabilité annuelle")
    plt.legend()
    plt.grid(True, which="both", alpha=0.2)
    plt.show()
