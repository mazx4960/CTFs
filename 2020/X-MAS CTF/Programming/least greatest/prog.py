from pwn import *

url = 'challs.xmas.htsp.ro'
port = 6050

def primeFactors(n): 

	count = 0
	# Print the number of two's that divide n 
	if n % 2 == 0:
		count += 1
		while n % 2 == 0:
			n = n // 2

	# n must be odd at this point 
	# so a skip of 2 ( i = i + 2) can be used 
	for i in range(3,int(math.sqrt(n))+1,2):
		# while i divides n , print i ad divide n 
		if n % i == 0:
			count += 1
			while n % i== 0:
				n = n // i 
              
    # Condition if n is a prime 
    # number greater than 2 
	if n > 2:
		count += 1
	return count

# A function to find number of distinct  
# prime factors of a given number n  
def totalPrimeFactors(n):  
      
    # To keep track of count  
    count = 0;  
  
    # 2s that divide n  
    if ((n % 2) == 0):  
        count += 1;  
        while ((n % 2) == 0):  
            n >>= 1;  
  
    # n must be odd at this point.  
    # So we can skip one element  
    # (Note i = i +2) 
    i = 3; 
    while (i * i <= n):  
          
        # i divides n  
        if ((n % i) == 0):  
            count += 1;  
            while ((n % i) == 0):  
                n //= i;  
        i += 2; 
  
    # This condition is to handle the  
    # case when n is a prime number  
    # greater than 2  
    if (n > 2):  
        count += 1;  
  
    return count;  

def get_pairs(gcd, lcm):
	return str(1 << (totalPrimeFactors(lcm // gcd)))

conn = remote(url, port)

intro = conn.recvuntil('\n\n').decode('utf-8')
print(intro)
for i in range(100):
	test = conn.recvline().strip()
	print(test)

	gcd = int(str(conn.recvline().strip()).split('=')[1][:-1])
	lcm = int(str(conn.recvline().strip()).split('=')[1][:-1])
	print(gcd, lcm)
	ans = get_pairs(gcd, lcm)
	print(ans)
	conn.sendline(ans)
	print(conn.recvline())


print(conn.recvline())
print(conn.recvline())
# conn.interactive()


