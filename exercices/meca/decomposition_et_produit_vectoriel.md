# Décomposition d'un vecteur et produit vectoriel

![](images/decomposition_et_produit_vectoriel.webp)

## Énoncé

Considérez un vecteur $$\vec{A}$$ de norme $$A = 5 \, \text{m}$$ faisant un angle $$\alpha = 60^\circ$$ avec la verticale (axe y). Décomposez ce vecteur dans la base canonique $$ (\vec{i}, \vec{j}, \vec{k}) $$ et calculez le produit vectoriel $$ \vec{A} \times \vec{k} $$ où $$ \vec{k} $$ est le troisième vecteur de la base canonique.

1. Décomposez le vecteur $$ \vec{A} $$ dans la base canonique $$ (\vec{i}, \vec{j}, \vec{k}) $$.
2. Calculez le produit vectoriel $$ \vec{A} \times \vec{k} $$.

## Corrigé

1. **Décomposition du vecteur $$ \vec{A} $$ dans la base canonique** :

   Le vecteur $$ \vec{A} $$ fait un angle $$ \alpha $$ avec la verticale, donc ses composantes peuvent être trouvées en utilisant les fonctions trigonométriques.

   Composante selon l'axe y (verticale) :
   $$
   A_y = A \cos \alpha
   $$

   Composante selon l'axe x (horizontale) :
   $$
   A_x = A \sin \alpha
   $$

   Il n'y a pas de composante selon l'axe z, donc :
   $$
   A_z = 0
   $$

   En remplaçant les valeurs données :
   $$
   A_y = 5 \, \text{m} \times \cos 60^\circ = 5 \, \text{m} \times \frac{1}{2} = 2.5 \, \text{m}
   $$

   $$
   A_x = 5 \, \text{m} \times \sin 60^\circ = 5 \, \text{m} \times \frac{\sqrt{3}}{2} \approx 4.33 \, \text{m}
   $$

   Donc, le vecteur $$ \vec{A} $$ dans la base canonique est :
   $$
   \vec{A} = (A_x, A_y, A_z) = (4.33, 2.5, 0)
   $$

2. **Calcul du produit vectoriel $$ \vec{A} \times \vec{k} $$** :

   Le produit vectoriel de deux vecteurs $$ \vec{A} = (A_x, A_y, A_z) $$ et $$ \vec{k} = (0, 0, 1) $$ est donné par le déterminant de la matrice suivante :
   $$
   \vec{A} \times \vec{k} =
   \begin{vmatrix}
   \vec{i} & \vec{j} & \vec{k} \\
   A_x & A_y & A_z \\
   0 & 0 & 1
   \end{vmatrix}
   $$

   Calculons ce déterminant :
   $$
   \vec{A} \times \vec{k} = \vec{i} (A_y \cdot 1 - A_z \cdot 0) - \vec{j} (A_x \cdot 1 - A_z \cdot 0) + \vec{k} (A_x \cdot 0 - A_y \cdot 0)
   $$
   $$
   \vec{A} \times \vec{k} = \vec{i} (A_y) - \vec{j} (A_x) + \vec{k} (0)
   $$
   $$
   \vec{A} \times \vec{k} = (A_y, -A_x, 0)
   $$

   En remplaçant les valeurs de $$ A_x $$ et $$ A_y $$ :
   $$
   \vec{A} \times \vec{k} = (2.5, -4.33, 0)
   $$

## Questions d'analyse

1. Pourquoi les composantes du vecteur $$ \vec{A} $$ sont-elles déterminées en utilisant les fonctions trigonométriques ?
2. Expliquez pourquoi le produit vectoriel de deux vecteurs perpendiculaires est un vecteur qui est perpendiculaire aux deux vecteurs initiaux.
3. Que représente le résultat du produit vectoriel $$ \vec{A} \times \vec{k} $$ en termes de direction et de sens ?
4. Si l'angle $$ \alpha $$ était de 90°, comment cela affecterait-il la décomposition du vecteur $$ \vec{A} $$ ?
5. Quel est le module du produit vectoriel $$ \vec{A} \times \vec{k} $$ et comment peut-il être interprété géométriquement ?

## Corrigé des questions d'analyse

1. Les composantes du vecteur $$ \vec{A} $$ sont déterminées en utilisant les fonctions trigonométriques car le vecteur fait un angle $$ \alpha $$ avec la verticale. Les fonctions trigonométriques permettent de projeter ce vecteur sur les axes x et y.
2. Le produit vectoriel de deux vecteurs perpendiculaires est un vecteur qui est perpendiculaire aux deux vecteurs initiaux en raison de la définition du produit vectoriel. Il est orienté selon la règle de la main droite.
3. Le résultat du produit vectoriel $$ \vec{A} \times \vec{k} $$ est un vecteur qui est perpendiculaire à $$ \vec{A} $$ et à $$ \vec{k} $$. Dans ce cas, il pointe dans la direction opposée de $$ \vec{j} $$, indiquant une rotation dans le plan x-y.
4. Si l'angle $$ \alpha $$ était de 90°, cela signifierait que le vecteur $$ \vec{A} $$ serait entièrement horizontal, avec une composante en x égale à sa norme et une composante en y nulle.
5. Le module du produit vectoriel $$ \vec{A} \times \vec{k} $$ est donné par :
   $$
   \| \vec{A} \times \vec{k} \| = \sqrt{A_y^2 + (-A_x)^2} = \sqrt{(2.5)^2 + (-4.33)^2} = \sqrt{6.25 + 18.7489} = \sqrt{24.9989} \approx 5
   $$
   Ce module représente l'aire du parallélogramme formé par les vecteurs $$ \vec{A} $$ et $$ \vec{k} $$.

