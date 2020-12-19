from pwn import *


url = 'challs.xmas.htsp.ro'
port = 6055

conn = remote(url, port)

def get_vals(arr):
	return (int(w.split('=')[1]) for w in arr)

def build_v(v, N, a, c, mod):
	for i in range(1, N):
		v[i] = (a * v[i - 1] + c) % mod
	return v

def get_min_days_2(v, N, K, P, Q):
	days = 0
	# print(K, P, Q)
	mult = (K * P) + ((N - K) * Q)
	factor = min(v) // mult
	for i in range(N):
		v[i] -= mult * factor
	days = factor * N

	print(days)

	if P > Q:
		rev = True
	else:
		rev = False

	while max(v) != 0:
		v = sorted(v, reverse=rev)
		for i in range(K):
			v[i] -= P if v[i] > P else v[i]
		for i in range(K, N):
			v[i] -= Q if v[i] > Q else v[i]
		days += 1
	return days

def get_min_days(v, N, K, P, Q):
	days = 0
	# print(K, P, Q)
	if P > Q:
		rev = True
	else:
		rev = False

	while max(v) != 0:
		v = sorted(v, reverse=rev)
		for i in range(K):
			v[i] -= P if v[i] > P else v[i]
		for i in range(K, N):
			v[i] -= Q if v[i] > Q else v[i]
		days += 1
	return days


print('\n' + '=' * 100 + '\n')
intro = conn.recvuntil('\n\n').decode('utf-8')
print(intro)

print(conn.recvline().decode('utf-8'))
print(conn.recvline().decode('utf-8'))
print(conn.recvline().decode('utf-8'))
print(conn.recvline().decode('utf-8'))
print(conn.recvline().decode('utf-8'))
print(conn.recvline().decode('utf-8'))
print('=' * 100 + '\n')

for i in range(100):
	test = conn.recvline().decode('utf-8').strip()
	print(test)

	N, K = get_vals(conn.recvline().decode('utf-8').split(','))

	v = [0] * (N)
	P, Q = get_vals(conn.recvline().decode('utf-8').split(','))
	v[0], a, c, mod = get_vals(conn.recvline().decode('utf-8').split(','))

	build_v(v, N, a, c, mod)

	min_days = get_min_days(v, N, K, P, Q)
	print(min_days)

	# min_days = get_min_days_2(v, N, K, P, Q)
	# print(min_days)

	conn.sendline(str(min_days))
	print(conn.recvline().decode('utf-8'))
	print(conn.recvline().decode('utf-8'))

# print(conn.recvline().decode('utf-8'))
# print(conn.recvline().decode('utf-8'))

