# Oscillateur harmonique LC

![](images/oscillateur_harmonique_LC.webp)

## Énoncé

1. Considérez un circuit LC composé d'une bobine de self-inductance $$L$$ et d'un condensateur de capacité $$C$$, initialement chargé avec une charge $$Q_0$$. Écrivez l'équation différentielle gouvernant l'évolution de la charge $$Q(t)$$ sur le condensateur.
2. Trouvez la solution générale de cette équation différentielle.
3. Déterminez la fréquence angulaire des oscillations et la période du circuit.
4. Si $$L = 10 \, \text{mH}$$ et $$C = 1 \, \mu\text{F}$$, calculez la fréquence des oscillations en Hertz.

## Corrigé

1. L'équation différentielle gouvernant l'évolution de la charge $$Q(t)$$ sur le condensateur dans un circuit LC est obtenue en utilisant la loi des mailles de Kirchhoff :
   $$
   V_L + V_C = 0
   $$
   où $$V_L = L \frac{\mathrm{d}I}{\mathrm{d}t}$$ et $$V_C = \frac{Q}{C}$$. 

   En utilisant $$I = \frac{\mathrm{d}Q}{\mathrm{d}t}$$, nous avons :
   $$
   L \frac{\mathrm{d}^2Q}{\mathrm{d}t^2} + \frac{Q}{C} = 0
   $$

2. Cette équation différentielle est une équation homogène du second ordre :
   $$
   L \frac{\mathrm{d}^2Q}{\mathrm{d}t^2} + \frac{Q}{C} = 0
   $$

   La solution générale de cette équation est :
   $$
   Q(t) = Q_0 \cos(\omega_0 t + \phi)
   $$
   où $$\omega_0 = \frac{1}{\sqrt{LC}}$$ est la fréquence angulaire et $$\phi$$ est une constante de phase déterminée par les conditions initiales.

3. La fréquence angulaire des oscillations est :
   $$
   \omega_0 = \frac{1}{\sqrt{LC}}
   $$

   La période des oscillations est :
   $$
   T = \frac{2\pi}{\omega_0} = 2\pi \sqrt{LC}
   $$

4. Pour $$L = 10 \, \text{mH}$$ et $$C = 1 \, \mu\text{F}$$, la fréquence angulaire est :
   $$
   \omega_0 = \frac{1}{\sqrt{10 \times 10^{-3} \times 1 \times 10^{-6}}} = \frac{1}{\sqrt{10^{-8}}} = 10^4 \, \text{rad/s}
   $$

   La fréquence des oscillations en Hertz est :
   $$
   f = \frac{\omega_0}{2\pi} = \frac{10^4}{2\pi} \approx 1591.55 \, \text{Hz}
   $$

## Questions d'analyse

1. Pourquoi utilise-t-on une équation différentielle pour modéliser le circuit LC ? 
2. Quel est le rôle de la constante de phase $$\phi$$ dans la solution de l'équation différentielle ?
3. Si la capacité $$C$$ était doublée, comment cela affecterait-il la fréquence des oscillations ? Montrez votre raisonnement.
4. Vérifiez que les unités de $$\omega_0$$ sont correctes en utilisant les unités de $$L$$ et $$C$$.
5. Quelle énergie est échangée entre la bobine et le condensateur lors des oscillations ? Comment cette énergie est-elle répartie au cours du temps ?

## Corrigé des questions d'analyse

1. Une équation différentielle est utilisée pour modéliser le circuit LC car la relation entre la tension et le courant dans les composants du circuit (bobine et condensateur) implique des dérivées par rapport au temps. Cela permet de décrire l'évolution temporelle des grandeurs électriques (charge, courant, tension) de manière rigoureuse.
2. La constante de phase $$\phi$$ dans la solution de l'équation différentielle tient compte des conditions initiales du système (par exemple, la charge initiale du condensateur ou le courant initial dans le circuit). Elle permet d'ajuster la solution générale à des situations spécifiques.
3. Si la capacité $$C$$ était doublée, la nouvelle fréquence angulaire serait :
   $$
   \omega_0' = \frac{1}{\sqrt{L \cdot 2C}} = \frac{1}{\sqrt{2} \cdot \sqrt{LC}} = \frac{\omega_0}{\sqrt{2}}
   $$
   Donc, la nouvelle fréquence serait plus faible d'un facteur $$\sqrt{2}$$ :
   $$
   f' = \frac{\omega_0'}{2\pi} = \frac{\omega_0}{\sqrt{2} \cdot 2\pi} = \frac{f}{\sqrt{2}}
   $$

4. Vérifions les unités de $$\omega_0$$ :
   - $$[L] = \text{H} = \text{kg} \cdot \text{m}^2 \cdot \text{s}^{-2} \cdot \text{A}^{-2}$$
   - $$[C] = \text{F} = \text{s}^4 \cdot \text{A}^2 \cdot \text{kg}^{-1} \cdot \text{m}^{-2}$$
   Donc,
   $$
   [LC] = \left(\text{kg} \cdot \text{m}^2 \cdot \text{s}^{-2} \cdot \text{A}^{-2}\right) \cdot \left(\text{s}^4 \cdot \text{A}^2 \cdot \text{kg}^{-1} \cdot \text{m}^{-2}\right) = \text{s}^2
   $$
   et
   $$
   [\omega_0] = \left[\frac{1}{\sqrt{LC}}\right] = \left[\frac{1}{\text{s}}\right] = \text{s}^{-1}
   $$
   Les unités de $$\omega_0$$ sont donc correctes.

5. L'énergie échangée entre la bobine et le condensateur est l'énergie électromagnétique, alternant entre énergie électrique stockée dans le condensateur $$E_C = \frac{1}{2} \frac{Q(t)^2}{C}$$ et énergie magnétique stockée dans la bobine $$E_L = \frac{1}{2} L I(t)^2$$. Au cours du temps, cette énergie oscille entre les deux formes sans perte dans un circuit idéalement sans résistance.
