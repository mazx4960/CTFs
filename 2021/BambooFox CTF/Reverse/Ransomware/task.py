# uncompyle6 version 3.7.2
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)]
# Embedded file name: task.py
# Compiled at: 2021-01-14 22:13:24
# Size of source mod 2**32: 420 bytes
# (lambda data, key, iv: 
# 	if len(data) != 0:
# 		(lambda key, iv, data, AES: 
# 			open('flag.enc', 'wb').write(AES.new(key, AES.MODE_CBC, iv).encrypt(lambda x: x + b'\x00' * (16 - len(x) % 16)(data)))
# 		)(data[key:key + 16], data[iv:iv + 16], open('flag.png', 'rb').read(), __import__('Crypto.Cipher.AES').Cipher.AES) # Avoid dead code: lambda fn: __import__('os').remove(fn)('task.py'))(__import__('requests').get('https://ctf.bamboofox.tw/rules').text.encode(), 99, 153)
# okay decompiling task.pyc

data = __import__('requests').get('https://ctf.bamboofox.tw/rules').text.encode()
key = 99
iv = 153

key = data[key:key + 16]
iv = data[iv:iv + 16]
data = open('flag.enc', 'rb').read()
AES = __import__('Cryptodome.Cipher.AES').Cipher.AES

open('flag.png', 'wb').write(AES.new(key, AES.MODE_CBC, iv).decrypt(data + b'\x00' * (16 - len(data) % 16)))