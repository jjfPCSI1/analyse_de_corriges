# Travail de la force de frottement dans le cadre d'un lancé de curling

## Énoncé

Lors d'une partie de curling, une pierre de masse $$m = 20 \, \text{kg}$$ est lancée sur une piste de glace. La pierre glisse sur la glace avec une vitesse initiale $$v_0 = 3 \, \text{m/s}$$. La force de frottement entre la glace et la pierre est une force constante qui s'oppose au mouvement de la pierre. Le coefficient de frottement cinétique entre la pierre et la glace est $$\mu_k = 0.02$$. Déterminez la distance que parcourt la pierre avant de s'arrêter.

1. Calculez la force de frottement qui agit sur la pierre.
2. Exprimez le travail effectué par la force de frottement en fonction de la distance parcourue.
3. Calculez la distance parcourue par la pierre avant de s'arrêter en utilisant la conservation de l'énergie.

## Corrigé

1. **Calcul de la force de frottement qui agit sur la pierre** :

   La force de frottement $$F_f$$ est donnée par la relation :
   $$
   F_f = \mu_k \cdot N
   $$

   Où $$N$$ est la force normale. Pour une surface horizontale, $$N = mg$$, donc :
   $$
   F_f = \mu_k \cdot mg
   $$

2. **Expression du travail effectué par la force de frottement** :

   Le travail $$W$$ effectué par la force de frottement sur la distance $$d$$ est donné par :
   $$
   W = F_f \cdot d \cdot \cos(\theta)
   $$

   Puisque la force de frottement est opposée au mouvement, l'angle $$\theta$$ entre la force de frottement et le déplacement est de $$180^\circ$$, donc $$\cos(180^\circ) = -1$$. Ainsi :
   $$
   W = -F_f \cdot d
   $$

3. **Calcul de la distance parcourue par la pierre avant de s'arrêter** :

   L'énergie cinétique initiale de la pierre est donnée par :
   $$
   E_k = \frac{1}{2} mv_0^2
   $$

   La pierre s'arrête lorsque toute son énergie cinétique a été dissipée par le travail de la force de frottement :
   $$
   \frac{1}{2} mv_0^2 = F_f \cdot d
   $$

   En isolant la distance $$d$$, nous avons :
   $$
   d = \frac{\frac{1}{2} mv_0^2}{F_f}
   $$

   En remplaçant l'expression de la force de frottement :
   $$
   d = \frac{\frac{1}{2} mv_0^2}{\mu_k mg}
   $$

   Simplifions l'expression en annulant les masses \(m\) :
   $$
   d = \frac{v_0^2}{2 \mu_k g}
   $$

   Enfin, substituons les valeurs numériques pour calculer \(d\) :
   $$
   d = \frac{(3 \, \text{m/s})^2}{2 \times 0.02 \times 9.81 \, \text{m/s}^2}
   $$
   $$
   d = \frac{9}{0.3924} \approx 22.94 \, \text{m}
   $$

   La pierre de curling parcourt donc environ $$22.94 \, \text{m}$$ avant de s'arrêter.

## Questions d'analyse

1. Pourquoi la force de frottement effectue-t-elle un travail négatif sur la pierre ?
2. Comment le coefficient de frottement cinétique $$\mu_k$$ influence-t-il la distance parcourue par la pierre ?
3. Si la masse de la pierre était doublée, comment cela affecterait-il la distance parcourue avant de s'arrêter ?
4. Expliquez pourquoi la force normale $$N$$ est égale à $$mg$$ dans ce contexte.
5. Comment l'angle entre la force de frottement et le déplacement affecte-t-il le travail effectué par cette force ?

## Corrigé des questions d'analyse

1. La force de frottement effectue un travail négatif car elle s'oppose au mouvement de la pierre, ce qui signifie que l'énergie est retirée du système (dissipation).
2. Le coefficient de frottement cinétique $$\mu_k$$ détermine la magnitude de la force de frottement. Un coefficient plus élevé signifie plus de force de frottement et une distance plus courte parcourue par la pierre avant de s'arrêter.
3. Si la masse de la pierre était doublée, la distance parcourue avant de s'arrêter ne changerait pas car l'énergie cinétique initiale et la force de frottement dépendent toutes deux de la masse de la pierre, qui s'annule dans le calcul de la distance.
4. La force normale $$N$$ est égale à $$mg$$ car la pierre est sur une surface horizontale sans inclinaison, donc la force normale est simplement le poids de la pierre.
5. L'angle entre la force de frottement et le déplacement affecte le travail car le travail est calculé comme $$W = F_f \cdot d \cdot \cos(\theta)$$. Un angle de $$180^\circ$$ signifie que la force est complètement opposée au déplacement, donc le travail est négatif.

