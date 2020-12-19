from pwn import *
import math
import numpy as np


url = 'challs.xmas.htsp.ro'
port = 6053

conn = remote(url, port)

def exponentiation(bas, exp): 
    t = np.identity(N, dtype=np.int64); 
    while(exp > 0):  
        if (exp % 2 != 0): 
            t = (t.dot(bas)) % 666013; 
  
        bas = (bas.dot(bas)) % 666013; 
        exp = int(exp / 2); 
    return t % 666013;

def get_num_paths_3(mat, forbidden, L, N):
	for i in range(N):
		for node in forbidden:
			mat[i][node - 1] = 0

	base = np.asarray(mat, dtype=np.int64)
	pow_mat = exponentiation(base, L)
	return str(pow_mat[0][N - 1])


def get_num_paths(mat, forbidden, L, N):
	for i in range(N):
		for node in forbidden:
			mat[i][node - 1] = 0

	for node in forbidden:
		for i in range(N):
			mat[node - 1][i] = 0
	# print(mat)

	np_mat = np.asarray(mat)
	pow_mat = np.asarray(mat)
	for i in range(L-1):
		pow_mat = np.dot(pow_mat, np_mat) % 666013
		print(pow_mat)
		print()
	return str(pow_mat[0][N - 1])



intro = str(conn.recvuntil('\n\n').decode('utf-8'))
print(intro)

for i in range(40):
	test = conn.recvline().strip()
	print(test)

	N = int(str(conn.recvline().strip()).split('=')[1][:-1])
	conn.recvline()

	mat = []
	for i in range(N):
		line = str(conn.recvline().strip())[2:-1].split(',')
		mat.append(list(map(int, line)))

	forbidden = str(conn.recvline())
	forbidden = forbidden[forbidden.index('[') + 1:forbidden.index(']')].split(',')
	if forbidden == ['']:
		forbidden = []
	else:
		forbidden = list(map(int, forbidden))
	# print(forbidden)

	L = int(str(conn.recvline().strip()).split('=')[1][:-1])
	# print(N, mat, forbidden, L)
	# ans = get_num_paths(mat, forbidden, L, N)
	# print(ans)

	ans = get_num_paths_3(mat, forbidden, L, N)
	print(ans)

	conn.sendline(ans)
	print(L)
	print(conn.recvline())
	print(conn.recvline())

print(conn.recvline())
print(conn.recvline())


