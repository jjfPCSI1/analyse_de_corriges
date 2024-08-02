# Mesure du champ magnétique terrestre avec l'expérience d'Oersted

![](images/oersted.webp)

## Énoncé

On souhaite mesurer la composante horizontale du champ magnétique terrestre $$B_H$$ à l'aide d'une expérience inspirée de celle réalisée par Oersted. Pour ce faire, on utilise un fil rectiligne parcouru par un courant $$I$$, suspendu au-dessus d'une aiguille aimantée horizontale. L'aiguille est initialement alignée avec le champ magnétique terrestre.

Lorsque le courant circule dans le fil, l'aiguille subit l'influence combinée du champ magnétique créé par le fil et du champ magnétique terrestre. L'aiguille s'aligne alors selon une nouvelle direction formant un angle $$\theta$$ par rapport à la direction du champ magnétique terrestre.

On suppose que l'aiguille aimantée est suffisamment éloignée du fil pour que le champ magnétique créé par le fil soit approximativement uniforme au niveau de l'aiguille. Le champ magnétique créé par un fil infini rectiligne à une distance $$d$$ est donné par $$B_f = \frac{\mu_0 I}{2\pi d}$$, où $$\mu_0$$ est la perméabilité magnétique du vide.

1. **Expression du champ magnétique résultant** : Établissez l'expression du champ magnétique résultant qui agit sur l'aiguille en fonction de $$B_H$$, $$B_f$$, et $$\theta$$.

2. **Détermination de la composante horizontale** : Montrez que la composante horizontale du champ magnétique terrestre $$B_H$$ est donnée par $$B_H = B_f \tan(\theta)$$.

3. **Calcul de $$B_H$$** : Calculez $$B_H$$ pour un courant de $$I = 5 \, \text{A}$$, une distance $$d = 10 \, \text{cm}$$, et un angle $$\theta = 30^\circ$$.

4. **Estimation de l'incertitude** : Estimez l'incertitude sur la mesure de $$B_H$$ si les incertitudes sur $$I$$, $$d$$, et $$\theta$$ sont respectivement $$\Delta I = 0{,}1 \, \text{A}$$, $$\Delta d = 0{,}5 \, \text{cm}$$, et $$\Delta \theta = 1^\circ$$.

## Corrigé

### 1. Expression du champ magnétique résultant

L'aiguille aimantée est soumise à deux champs magnétiques :

- Le champ magnétique terrestre $$\vec{B_H}$$, dirigé selon la direction initiale de l'aiguille.
- Le champ magnétique $$\vec{B_f}$$ créé par le courant dans le fil, perpendiculaire à l'aiguille et au champ terrestre.

Le champ magnétique résultant $$\vec{B_{\text{res}}}$$ qui agit sur l'aiguille est la somme vectorielle de ces deux champs :

$$
\vec{B_{\text{res}}} = \vec{B_H} + \vec{B_f}
$$

En utilisant la règle de l'addition vectorielle, le module du champ magnétique résultant est donné par :

$$
B_{\text{res}} = \sqrt{B_H^2 + B_f^2 + 2B_H B_f \cos(90^\circ - \theta)}
$$

Puisque $$B_f$$ est perpendiculaire à $$B_H$$, l'angle entre $$B_f$$ et $$B_H$$ est $$90^\circ - \theta$$, ce qui donne :

$$
B_{\text{res}} = \sqrt{B_H^2 + B_f^2}
$$

### 2. Détermination de la composante horizontale

Lorsque l'aiguille s'aligne dans la direction du champ magnétique résultant, l'angle entre $$\vec{B_H}$$ et $$\vec{B_{\text{res}}}$$ est $$\theta$$. La tangente de cet angle est donnée par :

$$
\tan(\theta) = \frac{B_f}{B_H}
$$

D'où la relation pour la composante horizontale du champ magnétique terrestre :

$$
B_H = B_f \tan(\theta)
$$

### 3. Calcul de $$B_H$$

Donnons les valeurs numériques :

- $$I = 5 \, \text{A}$$
- $$d = 10 \, \text{cm} = 0{,}1 \, \text{m}$$
- $$\theta = 30^\circ$$

Le champ magnétique créé par le fil est :

$$
B_f = \frac{\mu_0 I}{2\pi d} = \frac{4\pi \times 10^{-7} \times 5}{2\pi \times 0{,}1} = 10^{-6} \times \frac{5}{0{,}1} = 5 \times 10^{-6} \, \text{T}
$$

La composante horizontale du champ magnétique terrestre est alors :

$$
B_H = B_f \tan(30^\circ) = 5 \times 10^{-6} \times \frac{1}{\sqrt{3}} \approx 2{,}89 \times 10^{-6} \, \text{T}
$$

### 4. Estimation de l'incertitude

L'incertitude sur $$B_H$$ est calculée en utilisant la propagation des incertitudes :

$$
\left(\frac{\Delta B_H}{B_H}\right)^2 = \left(\frac{\Delta I}{I}\right)^2 + \left(\frac{\Delta d}{d}\right)^2 + \left(\frac{\Delta \theta}{\tan(\theta)}\right)^2
$$

Avec :

- $$\Delta I = 0{,}1 \, \text{A}$$
- $$\Delta d = 0{,}5 \, \text{cm} = 0{,}005 \, \text{m}$$
- $$\Delta \theta = 1^\circ = \frac{\pi}{180} \, \text{rad}$$
- $$\tan(\theta) = \tan(30^\circ) = \frac{1}{\sqrt{3}}$$

Calculons chaque contribution :

$$
\frac{\Delta I}{I} = \frac{0{,}1}{5} = 0{,}02
$$

$$
\frac{\Delta d}{d} = \frac{0{,}005}{0{,}1} = 0{,}05
$$

$$
\frac{\Delta \theta}{\tan(\theta)} = \frac{\frac{\pi}{180}}{\frac{1}{\sqrt{3}}} = \frac{\pi}{180\sqrt{3}} \approx 0{,}0101
$$

Ainsi, l'incertitude relative totale est :

$$
\left(\frac{\Delta B_H}{B_H}\right)^2 = (0{,}02)^2 + (0{,}05)^2 + (0{,}0101)^2 \approx 0{,}0004 + 0{,}0025 + 0{,}0001 = 0{,}0026
$$

L'incertitude sur $$B_H$$ est donc :

$$
\Delta B_H = B_H \times \sqrt{0{,}0026} \approx 2{,}89 \times 10^{-6} \times 0{,}051 \approx 1{,}48 \times 10^{-7} \, \text{T}
$$

Le champ magnétique terrestre mesuré est donc :

$$
B_H \approx (2{,}89 \pm 0{,}15) \times 10^{-6} \, \text{T}
$$

## Questions d'analyse

1. **Méthode** : Pourquoi est-il important de considérer la composante horizontale du champ magnétique terrestre plutôt que sa valeur totale ?

2. **Hypothèses** : Quelles sont les principales hypothèses faites dans cet exercice, et comment pourraient-elles affecter la précision de la mesure ?

3. **Analyse des incertitudes** : Quel paramètre contribue le plus à l'incertitude totale de la mesure de $$B_H$$, et pourquoi ?

4. **Amélioration de la précision** : Que pourriez-vous modifier dans cette expérience pour améliorer la précision de la mesure du champ magnétique terrestre ?

5. **Interprétation physique** : Expliquez pourquoi l'angle $$\theta$$ formé par l'aiguille dépend de la valeur du courant et de la distance entre l'aiguille et le fil.

## Corrigé des questions d'analyse

1. **Méthode** : La composante horizontale $$B_H$$ du champ magnétique terrestre est importante car l'aiguille aimantée se trouve principalement influencée par cette composante lorsqu'elle est alignée horizontalement. La composante verticale du champ magnétique terrestre n'affecte pas directement la direction de l'aiguille dans ce contexte.

2. **Hypothèses** : Les hypothèses principales sont que le champ magnétique généré par le fil est uniforme au niveau de l'aiguille et que les effets de bord sont négligeables. Toute déviation de ces hypothèses peut introduire des erreurs dans la mesure, par exemple si le fil est trop proche de l'aiguille ou si le champ n'est pas suffisamment uniforme.

3. **Analyse des incertitudes** : La contribution la plus significative à l'incertitude totale provient de la mesure de la distance $$d$$. L'incertitude relative de $$d$$ est plus élevée que celle des autres paramètres, amplifiant ainsi son effet sur l'incertitude totale de $$B_H$$.

4. **Amélioration de la précision** : Pour améliorer la précision, on pourrait augmenter la distance $$d$$ pour minimiser les effets de bord et garantir un champ plus uniforme, réduire l'incertitude sur la mesure de l'angle $$\theta$$ en utilisant un appareil de mesure plus précis, et stabiliser la source de courant pour maintenir un $$I$$ constant.

5. **Interprétation physique** : L'angle $$\theta$$ formé par l'aiguille dépend du rapport entre le champ magnétique produit par le courant et celui du champ magnétique terrestre. Une augmentation du courant ou une réduction de la distance amplifie le champ $$B_f$$, modifiant l'orientation de l'aiguille par rapport à $$B_H$$.
