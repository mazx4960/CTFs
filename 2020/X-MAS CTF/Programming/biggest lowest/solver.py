from pwn import *

url = 'challs.xmas.htsp.ro'
port = 6051

conn = remote(url, port)

def solve(arr, k1, k2):
	size = max(arr) + 1
	s = [0] * size
	for num in arr:
		s[num] += 1

	ans1 = []
	count = k1
	for i in range(size):
		if s[i] > 0 and count > s[i]:
			count -= s[i]
			ans1 += [str(i)] * s[i]
		elif s[i] > 0 and count <= s[i]:
			ans1 += [str(i)] * count
			break

	ans2 = []
	count = k2
	for i in range(size - 1, 0, -1):
		if s[i] > 0 and count > s[i]:
			count -= s[i]
			ans2 += [str(i)] * s[i]
		elif s[i] > 0 and count <= s[i]:
			ans2 += [str(i)] * count
			break
		else:
			continue

	
	return ', '.join(ans1) + '; ' + ', '.join(ans2)

intro = conn.recvuntil('\n\n').decode('utf-8')
print(intro)
for i in range(50):
	test = conn.recvline().strip()
	print(test)

	chall = str(conn.recvline())
	chall = chall[chall.index('[') + 1:chall.index(']')].split(',')
	chall = list(map(lambda x: int(x), chall))
	k1 = int(str(conn.recvline().strip()).split('=')[1][:-1])
	k2 = int(str(conn.recvline().strip()).split('=')[1][:-1])
	print(chall, k1, k2)
	# print(solve(chall, k1, k2))
	conn.sendline(solve(chall, k1, k2))
	conn.recvline()


print(conn.recvline())
print(conn.recvline())
