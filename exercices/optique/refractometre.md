# Mesure de l'indice de réfraction avec un réfractomètre


![](images/refractometre.webp)

## Énoncé

Un réfractomètre est un instrument utilisé pour mesurer l'indice de réfraction $$n$$ d'un liquide. Le principe de fonctionnement repose sur la mesure de l'angle critique $$\theta_c$$, au-delà duquel la lumière est totalement réfléchie à l'interface entre le liquide et l'air.

1. Donner la relation reliant l'angle critique de réflexion totale aux indices des deux milieux
2. Lors de l'expérience, un angle critique de $$\theta_c = 45^\circ$$ est observé. Calculez l'indice de réfraction du liquide, sachant que l'indice de réfraction de l'air est $$n_{\text{air}} = 1$$.
3. En utilisant une autre méthode, l'angle critique mesuré est de $$\theta_c = 42^\circ$$. Calculez l'indice de réfraction du liquide dans ce cas.
4. Comparez les résultats obtenus avec les deux angles critiques et discutez des sources possibles d'erreur.

## Corrigé

1. **Principe du réfractomètre** :
   Un réfractomètre mesure l'indice de réfraction en utilisant le phénomène de réflexion totale interne. Lorsque la lumière passe du liquide (indice $$n$$) à l'air (indice $$n_{\text{air}}$$), il existe un angle critique $$\theta_c$$ pour lequel la lumière réfractée disparaît et toute la lumière est réfléchie à l'interface. Cet angle critique est lié aux indices de réfraction par la relation :
   $$
   \sin(\theta_c) = \frac{n_{\text{air}}}{n}
   $$

   Pour mesurer l'angle critique, on dirige un faisceau lumineux à travers le liquide et on observe l'angle au-delà duquel la lumière cesse de réfracter et commence à être totalement réfléchie.

2. **Calcul de l'indice de réfraction pour $$\theta_c = 45^\circ$$** :
   $$
   n = \frac{n_{\text{air}}}{\sin(\theta_c)}
   $$
   Pour $$\theta_c = 45^\circ$$ et $$n_{\text{air}} = 1$$ :
   $$
   n = \frac{1}{\sin(45^\circ)} = \frac{1}{\frac{\sqrt{2}}{2}} = \sqrt{2} \approx 1.414
   $$

3. **Calcul de l'indice de réfraction pour $$\theta_c = 42^\circ$$** :
   $$
   n = \frac{1}{\sin(42^\circ)}
   $$
   En utilisant une calculatrice pour trouver $$\sin(42^\circ) \approx 0.6691$$ :
   $$
   n = \frac{1}{0.6691} \approx 1.495
   $$

4. **Comparaison des résultats et discussion des erreurs** :
   Les résultats obtenus pour les deux angles critiques sont $$n \approx 1.414$$ pour $$\theta_c = 45^\circ$$ et $$n \approx 1.495$$ pour $$\theta_c = 42^\circ$$. Les différences peuvent être dues à :
   - Des erreurs de mesure de l'angle critique.
   - Des approximations dans les valeurs de $$\sin(\theta_c)$$.
   - Des variations dans la température ou la pureté du liquide.
   - La précision de l'instrument utilisé.

## Questions d'analyse

1. Pourquoi l'angle critique est-il utilisé pour mesurer l'indice de réfraction ?
2. Comment la précision de la mesure de l'angle critique affecte-t-elle la précision de l'indice de réfraction calculé ?
3. Si l'indice de réfraction de l'air n'était pas exactement 1 mais légèrement supérieur, comment cela affecterait-il le calcul de $$n$$ ?
4. Proposez une méthode pour améliorer la précision de la mesure de l'angle critique.
5. Quelle serait l'incertitude sur l'indice de réfraction si l'incertitude sur l'angle critique est de $$\pm 1^\circ$$ ?

## Corrigé des questions d'analyse

1. L'angle critique est utilisé pour mesurer l'indice de réfraction car il est directement lié à l'indice par la loi de Snell. Cela permet une mesure indirecte mais précise de l'indice de réfraction en observant un angle facilement mesurable.
2. La précision de la mesure de l'angle critique est cruciale car une petite erreur dans $$\theta_c$$ peut entraîner une erreur significative dans $$\sin(\theta_c)$$ et donc dans le calcul de $$n$$. Plus l'angle critique est mesuré avec précision, plus l'indice de réfraction calculé sera exact.
3. Si l'indice de réfraction de l'air était légèrement supérieur à 1, le calcul de $$n$$ serait affecté de telle sorte que $$n$$ du liquide serait légèrement surestimé. Par exemple, si $$n_{\text{air}} = 1.001$$, alors $$n = \frac{1.001}{\sin(\theta_c)}$$, ce qui donnerait un résultat un peu plus élevé pour $$n$$.
4. Pour améliorer la précision de la mesure de l'angle critique, on peut utiliser des instruments de mesure d'angle de haute précision, effectuer plusieurs mesures et en faire la moyenne, et s'assurer que le réfractomètre est correctement calibré.
5. Si l'incertitude sur l'angle critique est de $$\pm 1^\circ$$, l'incertitude sur $$\sin(\theta_c)$$ peut être estimée en évaluant $$\sin(\theta_c \pm 1^\circ)$$. Par exemple, pour $$\theta_c = 42^\circ$$ :
   $$
   \sin(41^\circ) \approx 0.6561
   $$
   $$
   \sin(43^\circ) \approx 0.6820
   $$
   L'incertitude relative sur $$\sin(\theta_c)$$ est donc environ $$\pm 0.0129$$. L'incertitude sur $$n$$ peut alors être calculée :
   $$
   \Delta n \approx n \times \frac{\Delta (\sin(\theta_c))}{\sin(\theta_c)} = 1.495 \times \frac{0.0129}{0.6691} \approx 0.029
   $$
   Donc, $$n = 1.495 \pm 0.029$$.
