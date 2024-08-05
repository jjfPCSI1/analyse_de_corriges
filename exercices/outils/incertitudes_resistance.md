# Calcul d'incertitude pour la mesure d'une résistance

![](images/incertitudes_resistance.webp)

## Énoncé

Lors d'un TP, vous devez mesurer la résistance $$R$$ d'un composant en utilisant la loi d'Ohm : $$R = \frac{U}{I}$$, où $$U$$ est la tension aux bornes du composant et $$I$$ l'intensité du courant qui le traverse.

Les appareils de mesure utilisés fournissent les incertitudes suivantes :
   - Voltmètre : $$U = 10.0 \pm 0.1 \, V$$
   - Ampèremètre : $$I = 2.0 \pm 0.05 \, A$$

Calculez la résistance $$R$$ et son incertitude en utilisant la propagation des incertitudes.

## Corrigé

La résistance $$R$$ est donnée par :
$$
R = \frac{U}{I}
$$

En utilisant les valeurs mesurées :
$$
R = \frac{10.0 \, V}{2.0 \, A} = 5.0 \, \Omega
$$

Pour calculer l'incertitude sur $$R$$, on utilise la formule de propagation des incertitudes pour une division :
$$
\left( \frac{\Delta R}{R} \right)^2 = \left( \frac{\Delta U}{U} \right)^2 + \left( \frac{\Delta I}{I} \right)^2
$$

Avec $$\Delta U = 0.1 \, V$$ et $$\Delta I = 0.05 \, A$$, les incertitudes relatives sont :
$$
\frac{\Delta U}{U} = \frac{0.1}{10.0} = 0.01
$$
$$
\frac{\Delta I}{I} = \frac{0.05}{2.0} = 0.025
$$

On peut alors écrire :
$$
\left( \frac{\Delta R}{5.0} \right)^2 = 0.01^2 + 0.025^2
$$
$$
\left( \frac{\Delta R}{5.0} \right)^2 = 0.0001 + 0.000625
$$
$$
\left( \frac{\Delta R}{5.0} \right)^2 = 0.000725
$$
$$
\frac{\Delta R}{5.0} = \sqrt{0.000725}
$$
$$
\frac{\Delta R}{5.0} \approx 0.0269
$$

D'où l'incertitude absolue sur $$R$$ :
$$
\Delta R = 5.0 \times 0.0269 \approx 0.13 \, \Omega
$$

La valeur finale de la résistance avec son incertitude est donc :
$$
R = 5.0 \pm 0.13 \, \Omega
$$

## Questions d'analyse

1. Pourquoi est-il nécessaire de prendre en compte les incertitudes des mesures dans un calcul expérimental ?
2. Quelles seraient les conséquences de négliger l'incertitude de l'ampèremètre dans ce calcul ?
3. Pourquoi utilise-t-on la somme des carrés des incertitudes relatives dans la formule de propagation des incertitudes pour une division ?
4. Comment serait modifié le calcul si l'incertitude sur $$U$$ était de $$0.2 \, V$$ au lieu de $$0.1 \, V$$ ?
5. Quelle hypothèse sous-tend l'utilisation de la formule de propagation des incertitudes ? Est-elle toujours valide ?

## Corrigé des questions d'analyse

1. Les incertitudes des mesures doivent être prises en compte pour évaluer la précision des résultats obtenus. Elles permettent de quantifier l'erreur possible sur la mesure et d'estimer la fiabilité des résultats.
2. Négliger l'incertitude de l'ampèremètre fausserait l'évaluation de l'incertitude totale sur $$R$$. Cela donnerait une idée incorrecte de la précision de la mesure et pourrait conduire à des conclusions erronées.
3. La somme des carrés des incertitudes relatives est utilisée car les incertitudes relatives sont indépendantes et suivent une loi de propagation quadratique. Cela permet de combiner les erreurs de manière statistiquement appropriée.
4. Si l'incertitude sur $$U$$ était de $$0.2 \, V$$ :
   $$
   \frac{\Delta U}{U} = \frac{0.2}{10.0} = 0.02
   $$
   Le calcul deviendrait :
   $$
   \left( \frac{\Delta R}{5.0} \right)^2 = 0.02^2 + 0.025^2 = 0.0004 + 0.000625 = 0.001025
   $$
   $$
   \frac{\Delta R}{5.0} = \sqrt{0.001025} \approx 0.0320
   $$
   $$
   \Delta R = 5.0 \times 0.0320 = 0.16 \, \Omega
   $$
   La valeur finale serait alors :
   $$
   R = 5.0 \pm 0.16 \, \Omega
   $$
5. La formule de propagation des incertitudes suppose que les erreurs des différentes mesures sont indépendantes, suivent une distribution normale (gaussienne) et ne sont pas trop importantes. Ces hypothèses sont généralement valide pour des mesures répétées nombreuses et des erreurs aléatoires, mais elle peut ne pas tenir en cas d'erreurs systématiques ou de corrélations entre les mesures.
