# Biggest Lowest

> Points: 37 [50]

## Description

> The goal of the challenge is simple. Given an array, k1 and k2, find the first k1 smallest elements as well as the k2 largest elements. Note that the elements in the array are not unique.

## Solution

The goal of the challenge is simple. Given an array, k1 and k2, find the first k1 smallest elements as well as the k2 largest elements. Note that the elements in the array are not unique.

The naive solution would be just to sort the array and do array slicing to yield the largest and smallest few elements. However, even in the best case, that would only be an O(nlogn) solution. Meet count sort. The idea is simple, loop through the array once to gather a count of each element in the array then loop through the already count array iteratively to get the smallest and largest few elements. O(n) solution.

```
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
```

## Flag
`X-MAS{th15_i5_4_h34p_pr0bl3m_bu7_17'5_n0t_4_pwn_ch41l}`