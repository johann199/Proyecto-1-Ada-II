- ¿Necesitas la mejor opción en este momento para resolver el problema?
- ¿Necesitas una solución óptima (ya sea el valor mínimo o el valor máximo) 

R/ si.
R/ Necesito el valor mínimo de multiplicaciones entre un conjunto de matrices . 

Enfoque y definición esto cambia con respecto a dinámica porque mi estructura optima seria buscar los pares adyacentes que estarían enfocados a buscar los máximos y los mínimos, en el caso de multiplicar matrices estaría definido por

$$ cantidadmultmaxi $$
$$ cantidadmultimin $$
Mi algoritmo debe encontrar el mínimo de multiplicaciones, por tanto me sirve la cantidad mínima de multiplicaciones. 
esto se puede representar con un costo inmediato definido por
$$ p[i-1] · p[i] · p[i + 1]$$

## Criterio de selección
En cada iteración se calcula el costo inmedito para cad par adyacente $$p[i-1]·p[i]·p[i+1]$$
Se selecciona el valor mínimo.

## Justificación

Se elige el par de menor costo inmediato, porque reduce locamente el número de operaciones escalares en cada paso, sin reconsiderar decisiones pasadas. 

## ¿Es optimo ?
No siempre, en algunos casos puede dar el mismo valor de programación dinámica sin embargo, no será el resultado para todos los casos en voraz, por tanto es más rápido en ejecución más no me garantiza una decisión optima. 



|             | PD          | PV                                   |
| ----------- | ----------- | ------------------------------------ |
| Complejidad | $$O(n³)$$   | $$O(n²)$$                            |
| Optima      | Siempre     | No garantiza siempre el valor optimo |
| Decisiones  | Evalúa Todo | Solo el momento actual.              |
