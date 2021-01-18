# Ransomware

> Points: 50 [500]

## Description

> A python ransomware

## Solution

1. decompile the python bytecode using uncompyle6
2. decrypt the .enc file using AES
3. binwalk the decrypted png file
4. The flag is the second image

## Flag
`flag{345y_l4_h4iy44444444}`