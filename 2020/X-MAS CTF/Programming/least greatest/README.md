# Least Greatest

> Points: 50 [100]

## Description

> Hey, you there! You look like you know your way with complex alogrithms.
> There's this weird task that I can't get my head around. It goes something like this:
> Given two numbers g and l, tell me how many pairs of numbers (x, y) exist such that gcd(x, y) = g and lcm(x, y) = l
> Also, i have to answer 100 such questions in at most 90 seconds.

## Solution

After searching on [mathstackexchange](https://math.stackexchange.com/questions/486444/finding-the-number-of-pairs-with-given-gcd-and-lcm-proof) for a while, I found an efficient way to find the number of pairs of number. Basically, take the LCM // GCD, then prime factorize the result and take 2 to the power of the number of unique prime numbers to get the answer.
```
def get_pairs(gcd, lcm):
    n = lcm // gcd
    
    count = 0;  
    if ((n % 2) == 0):  
        count += 1;  
        while ((n % 2) == 0):  
            n >>= 1;  
            
    i = 3; 
    while (i * i <= n):
        if ((n % i) == 0):  
            count += 1;  
            while ((n % i) == 0):  
                n //= i;  
        i += 2; 
        
    if (n > 2):  
        count += 1;  
        
    return str(1 << count);  
```

## Flag
`X-MAS{gr347es7_c0mm0n_d1v1s0r_4nd_l345t_c0mmon_mult1pl3_4r3_1n73rc0nn3ct3d}`