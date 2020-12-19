# Many Paths

> Points: 167 [200]

## Description

This was a really tricky one...
> I swear that Santa is going crazy with those problems, this time we're really screwed!
> The new problem asks us the following:
> Given an undirected graph of size N by its adjacency matrix and a set of forbidden nodes, tell me how many paths from node 1 to node N of exactly length L that don't pass through any of the forbidden nodes exist (please note that a node can be visited multiple times)?
> And if that wasn't enough, we need to answer 40 of those problems in 45 seconds and to give each output modulo 666013. What does that even mean!?

## Solution

Okay so we know that the number of ways to get from node 1 to node N would be the first row and last column of the adjacent matrix raised to the power of L. However, there is no quick way to compute this resulting power matrix.

My first solution was just to multiply the result with the adjacency matrix L times, however, towards the last few test cases, the matrix became really large and it takes a really long time. 

My next solution was using eigenvalues to compute the matrix. However, even though I could extract the eigen vectors and values, the numbers in the resulting matrix were simply too large and resulted in an integer overflow.

My final solution was then to use the fast exponentiation algorithm for integers but adapted to matrices

<p align='center'>
    <img src='https://mazx.xyz/content/images/2020/12/exponentiation.png'>
</p>

```
import numpy as np

def exponentiation(bas, exp): 
    t = np.identity(N, dtype=np.int64); 
    while(exp > 0):  
        if (exp % 2 != 0): 
            t = (t.dot(bas)) % 666013; 
  
        bas = (bas.dot(bas)) % 666013; 
        exp = int(exp / 2); 
    return t % 666013;

def get_num_paths(mat, forbidden, L, N):
	for i in range(N):
		for node in forbidden:
			mat[i][node - 1] = 0

	base = np.asarray(mat, dtype=np.int64)
	pow_mat = exponentiation(base, L)
	return str(pow_mat[0][N - 1])
```

## Flag
`X-MAS{n0b0dy_3xp3c73d_th3_m47r1x_3xp0n3n71a7i0n}`