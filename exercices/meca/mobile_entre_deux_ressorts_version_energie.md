# Mouvement d'un mobile sous l'action de deux ressorts identiques

## Énoncé

Un mobile autoporteur peut effectuer un mouvement de translation suivant un axe $$Ox$$ horizontal sous l'action de deux ressorts identiques, chacun ayant une constante de raideur $$k$$ et une longueur à vide $$\ell_0$$. Les ressorts sont fixés à des points fixes situés aux positions $$x = -L$$ et $$x = L$$ sur l'axe $$Ox$$. Le mobile est initialement à la position $$x = 0$$, où les ressorts sont à leur longueur à vide.

1. Établissez l'expression de l'énergie potentielle élastique stockée dans chaque ressort lorsque le mobile est à une position $$x$$.
2. Écrivez l'expression de l'énergie mécanique totale du système.
3. En utilisant la conservation de l'énergie mécanique, déduisez l'équation différentielle du mouvement du mobile et montrez que son mouvement est harmonique simple. Déterminez la pulsation propre du système.
4. Calculez la période des oscillations.

## Corrigé

1. **Expression de l'énergie potentielle élastique dans chaque ressort** :

   Lorsqu'un ressort est allongé ou comprimé par une distance \(\Delta \ell\) par rapport à sa longueur à vide \(\ell_0\), l'énergie potentielle élastique \(U\) stockée dans le ressort est donnée par :

   $$
   U = \frac{1}{2} k (\Delta \ell)^2
   $$

   Considérons la position d'équilibre à \(x = 0\) où les ressorts sont à leur longueur à vide. Lorsque le mobile se déplace à une position \(x\) sur l'axe \(Ox\) :

   - Pour le ressort fixé à \(x = -L\):
     - La longueur initiale du ressort à \(x = 0\) est \(\ell_0 = L\).
     - À une position \(x\), la longueur du ressort devient \(|x + L|\).
     - La déformation du ressort est \(\Delta \ell_1 = |x + L| - L = |x|\).

   L'énergie potentielle dans le premier ressort est donc :
   
   $$
   U_1 = \frac{1}{2} k (x)^2
   $$

   - Pour le ressort fixé à \(x = L\):
     - La longueur initiale du ressort à \(x = 0\) est \(\ell_0 = L\).
     - À une position \(x\), la longueur du ressort devient \(|x - L|\).
     - La déformation du ressort est \(\Delta \ell_2 = |x - L| - L = |x|\).

   L'énergie potentielle dans le second ressort est donc :

   $$
   U_2 = \frac{1}{2} k (x)^2
   $$

2. **Expression de l'énergie mécanique totale du système** :

   L'énergie mécanique totale \(E\) est la somme de l'énergie cinétique \(K\) du mobile et des énergies potentielles élastiques des deux ressorts.

   - L'énergie cinétique du mobile est donnée par :

     $$
     K = \frac{1}{2} m \dot{x}^2
     $$

   - L'énergie mécanique totale est alors :

     $$
     E = K + U_1 + U_2
     $$

     $$
     E = \frac{1}{2} m \dot{x}^2 + \frac{1}{2} k (x)^2 + \frac{1}{2} k (x)^2
     $$

     $$
     E = \frac{1}{2} m \dot{x}^2 + k x^2
     $$

3. **Équation différentielle du mouvement par conservation de l'énergie** :

   La conservation de l'énergie mécanique implique que la dérivée de l'énergie mécanique totale par rapport au temps est nulle :

   $$
   \frac{dE}{dt} = 0
   $$

   Calculons la dérivée de chaque terme par rapport au temps :

   - La dérivée de l'énergie cinétique est :

     $$
     \frac{d}{dt}\left(\frac{1}{2} m \dot{x}^2\right) = m \dot{x} \ddot{x}
     $$

   - La dérivée de l'énergie potentielle élastique est :

     $$
     \frac{d}{dt}\left(k x^2\right) = 2k x \dot{x}
     $$

   L'équation de conservation de l'énergie mécanique devient :

   $$
   m \dot{x} \ddot{x} + 2k x \dot{x} = 0
   $$

   Divisons chaque terme par \(\dot{x}\) (en supposant \(\dot{x} \neq 0\)) :

   $$
   m \ddot{x} + 2k x = 0
   $$

   Ce qui montre que le mouvement est harmonique simple avec une pulsation propre \(\omega_0\) donnée par :

   $$
   \omega_0 = \sqrt{\frac{2k}{m}}
   $$

4. **Période des oscillations** :

   La période des oscillations \(T\) est reliée à la pulsation propre \(\omega_0\) par la relation :

   $$
   T = \frac{2\pi}{\omega_0}
   $$

   En remplaçant l'expression de \(\omega_0\) :

   $$
   T = \frac{2\pi}{\sqrt{\frac{2k}{m}}}
   $$

   $$
   T = 2\pi \sqrt{\frac{m}{2k}}
   $$

## Questions d'analyse

1. Pourquoi l'énergie mécanique totale est-elle conservée dans ce système ?
2. Expliquez pourquoi le terme en \(x\) dans l'énergie potentielle des ressorts n'apparaît pas dans l'équation finale.
3. Si la constante de raideur des ressorts doublait, comment cela affecterait-il la pulsation propre et la période des oscillations ?
4. Si la masse du mobile était quadruplée, comment cela affecterait-il la pulsation propre et la période des oscillations ?
5. Pourquoi est-il important que les ressorts soient identiques dans cet exercice ?

## Corrigé des questions d'analyse

1. L'énergie mécanique totale est conservée car il n'y a pas de forces dissipatives, comme le frottement, dans le système. Les seules forces présentes sont les forces de ressort, qui sont conservatives.
2. Le terme en \(x\) dans l'énergie potentielle n'apparaît pas dans l'équation finale car l'équation du mouvement, issue de la dérivée de l'énergie potentielle, ne dépend que des variations, et les contributions égales des ressorts se compensent pour le terme constant.
3. Si la constante de raideur des ressorts doublait, la pulsation propre \(\omega_0\) augmenterait d'un facteur \(\sqrt{2}\), et la période des oscillations \(T\) serait divisée par \(\sqrt{2}\).
4. Si la masse du mobile était quadruplée, la pulsation propre \(\omega_0\) serait divisée par 2, et la période des oscillations \(T\) doublerait.
5. Il est important que les ressorts soient identiques car cela garantit que le système est symétrique et que la force résultante dépend uniquement de la position du mobile. Si les ressorts étaient différents, les forces ne se compenseraient pas symétriquement, modifiant ainsi la dynamique.

