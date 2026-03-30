Multiplicación de matrices 
- Caso base: Multiplicar una sola matriz, es decir solo tener una matriz que operar costo(i,i)=0
- Recurrencia: 

```costo(i,j) = min {costo(i,k) + costo(k+1,j) + p[i-1]* p[k]*p[j]} para todo k entre i y j - 1```

- Estado: par (i,j) que se representa en matrices

```M1 * M2 * M3 * Mn```

```M[i,j] = M[i,k]* M[k+1,j] para i <= k < j```

$$ 
M[i,j] =
\begin{cases}
0 & \text{si } i = j \\
\min\limits_{i \leq k < j} \left\{M[i,k] + 
M[k-1, j] + p_{i-1} \cdot p_k \cdot p_j \right\}&
\text{si } i < j
\end{cases}
$$

Resolver un problema.

M[1,4]

| 1   | M[1,1] | M[1,2] | M[1,3] | M[1,4] |
| --- | ------ | ------ | ------ | ------ |
| 2   | 0      | M[2,2] | M[2,3] | M[2,4] |
| 3   | 0      | 0      | M[3,3] | M[3,4] |
| 4   | 0      | 0      | 0      | M[4,4] |

casos base: 
$$M[1,1], M[2,2] M[3,3] y M[4,4]$$

para calcular M[1,2] necesito:

$$k= 1 M[1,1] y M[1,2]$$

para calcular M[1,3] necesito:

$$k = 1 M[1,1]  M[2,3]$$$$k = 2 M[1,2]  M[3,3]$$

para calcular M[1,4] necesito

$$k = 1 M[1,1]  M[2,4]$$
$$k = 2 M [1,2] M[3,4]$$
$$k = 3 M [1,3] M[4,4]$$

para calcular M[2,3] necesito

$$k = 2 M[2,2] M[3,3]$$

para calcular M[2,4] necesito

$$k = 2 M[2,2] M[3,4]$$
$$k = 3 M[2,3]M[4,4]$$

para calcular M[3,4] necesito

$$k = 3 M[3,3] M[4,4]$$

Ejemplo ce multiplicación 

$$M_1 = 10x500$$
$$M_2 = 500x5$$
$$M_3 = 5x80$$
$$M_4 = 80x30$$

$$ P = [ 10, 500, 5, 80, 30]$$

## Matriz de costos:

| i/j | 1   | 2     | 3      | 4     |
| --- | --- | ----- | ------ | ----- |
| 1   | 0   | 25000 | 29000  | 38500 |
| 2   | x   | 0     | 200000 | 87000 |
| 3   | x   | x     | 0      | 12000 |
| 4   | x   | x     | x      | 0     |

## Matriz de decisiones

| i/j | 1   | 2   | 3   | 4   |
| --- | --- | --- | --- | --- |
| 1   | 1   | 1   | 2   | 2   |
| 2   | x   | 2   | 2   | 2   |
| 3   | x   | x   | 3   | 3   |
| 4   | x   | x   | x   | 4   |

Análisis del problema con este ejemplo paso a paso: 

1. $$M[1,2] = M[1,1] + M[2,2] + p[0]*p[1]*p[2] => 0 + 0 + (10*500*5) = 25000$$

2. $$M[2,3] = M[2,2]+ M[3,3] + p[1]*p[2]*p[3] => 0+0 + (500*5*80) = 200000$$

3. $$M[3,4] = M[3,3] + M[4,4] + p[2]*p[3]*p[4]=> 0 + 0 + (5*80*30)= 12000$$

4. $$M[1,3]$$

	1. $$k=1 => M[1,1] + M[2,3] + p[0]*p[1]*p[3]=> 0 + 200000 + (10*500*80)= 600000$$

	2. $$k=2 => M[1,2] + M[3,3]+p[0]*p[2]*p[3]=> 25000 + 0 + (10*5*80)=29000$$

5.  $$M[2,4]$$

	1. $$k=2 => M[2,2]+M[3,4]+p[1]*p[2]*p[4]=> 0 + 12000 + (500*5*30)= 87000$$

	2. $$k= 3 => M[2,3]+M[4,4]+p[1]*p[3]*p[4]=> 200000+0+(10*5*30)= 201500$$

6.  $$M[1,4]$$

	1. $$k=1 => M[1,1]+M[2,4]+p[0]*p[1]*p[4] => 0 + 87000 +(10*500*30)= 237000$$

	2. $$k=2 => M[1,2]+M[3,4]+p[0]*p[2]*p[4]=> 25000 + 12000 + (10*5*30)= 38500$$

	3. $$k=3 => M[1,3]+M[4,4]+p[0]*p[3]*p[4]=> 29000 + 0 + (10*80*30) = 53000$$

### Solución

1. $$M[1,4] = M[1,2] y M[3,4]$$

2. $$M[1,2] = M[1,1] y M[2,2]$$

3. $$M[3,4]= M[3,3] y M[4,4]$$

$$((M_1*M_2)*(M_3*M_4))$$
