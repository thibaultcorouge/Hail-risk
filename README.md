Résumé:

Ce projet propose un cadre de simulation visant à analyser l’impact financier d’événements de grêle sur un portefeuille d’assurance habitation (MRH).

L’objectif est de relier explicitement la dynamique atmosphérique
d’un aléa convectif à ses conséquences économiques, en intégrant :
- une modélisation spatiale du phénomène,
- une fonction de vulnérabilité non linéaire,
- un moteur de simulation stochastique (Monte Carlo),
- et un mécanisme de transfert de risque via réassurance en excédent de perte.

L’approche permet d’évaluer la distribution complète des pertes,
au-delà des indicateurs moyens, et d’analyser la robustesse du portefeuille face aux événements extrêmes.

1. Objectif

L’objectif principal est d’étudier la transformation
d’un événement météorologique localisé en perte assurantielle agrégée, et d’évaluer :
- la sensibilité du portefeuille à la structure spatiale de l’aléa,
- la contribution des événements extrêmes à la distribution des pertes,
- l’efficacité d’un traité de réassurance dans la stabilisation du résultat technique.

Le projet constitue un cadre expérimental permettant d’explorer
l’interface entre modélisation atmosphérique et ingénierie financière du risque.

2. Méthodologie

2.1 Génération du portefeuille

Un portefeuille synthétique est généré avec :
- une distribution spatiale des risques,
- des capitaux assurés simulés via une loi Gamma,
- différents coefficients de vulnérabilité selon le type de toiture.
Cette étape permet de modéliser l’exposition et les effets d’accumulation géographique.

2.2 Modélisation de l’aléa

L’événement de grêle est représenté par un couloir spatial caractérisé par :
- une trajectoire,
- une largeur,
- un gradient d’intensité.
Cette représentation permet d’introduire une hétérogénéité spatiale réaliste et
d’analyser l’interaction entre trajectoire de l’aléa et concentration des capitaux.

2.3 Modélisation de la vulnérabilité

Le taux de dommage est modélisé par une fonction sigmoïde reliant le diamètre du grêlon au ratio de perte.
Cette approche non linéaire permet de représenter :
- une phase de résistance initiale,
- un seuil de dégradation rapide,
- une saturation des dommages pour les intensités élevées.
Elle reflète de manière plus cohérente le comportement mécanique des matériaux qu’une relation proportionnelle simple.

2.4 Simulation stochastique

Un moteur Monte Carlo génère un grand nombre de scénarios d’événements afin d’estimer :
- la perte annuelle moyenne (AAL),
- la distribution complète des pertes,
- les indicateurs extrêmes tels que le PML 99 %.
L’analyse porte principalement sur la queue de distribution, déterminante pour l’évaluation de la solvabilité.

2.5 Réassurance

Le modèle intègre un traité en Excédent de Perte (XL) défini par :
- une priorité (rétention),
- une limite de couverture.
- La simulation permet de quantifier :
- l’écrêtage des pertes extrêmes,
- la réduction de la variance,
- l’impact sur la stabilité du ratio Sinistres/Primes.

3. Résultats et enseignements

Les simulations mettent en évidence plusieurs éléments structurants :

1. La structure spatiale de l’aléa influence significativement
la distribution des pertes, en raison des effets d’accumulation.

2. Les indicateurs moyens (AAL) ne capturent pas correctement le risque extrême.

3. La réassurance modifie substantiellement le profil de risque
en réduisant l’exposition aux scénarios de forte sévérité.

La courbe de probabilité de dépassement (EP Curve) constitue l’outil central d’analyse,
en permettant d’observer la fréquence associée aux différents niveaux de perte.

4. Perspectives d’évolution

Plusieurs extensions sont envisageables :

- intégration de paramètres atmosphériques supplémentaires (vent, énergie convective),
- introduction d’une dérive climatique affectant la distribution des intensités,
- analyse prospective de la solvabilité à horizon 2050,
- extension multi-périls.

5. Architecture du projet
.
├── config.py
├── generator.py
├── weather.py
├── engine.py
├── simulator.py
├── visualizer.py
└── main.py

La structure modulaire vise à garantir la traçabilité des hypothèses et la reproductibilité des simulations.

Conclusion

Ce projet constitue un cadre expérimental reliant modélisation météorologique et analyse actuarielle.
Il met en évidence le rôle déterminant :
de la dimension spatiale de l’aléa, des non-linéarités de vulnérabilité et du transfert de risque dans la stabilisation financière.
L’approche adoptée permet d’explorer la dynamique complète du risque, de l’événement physique à son impact bilanciel.
