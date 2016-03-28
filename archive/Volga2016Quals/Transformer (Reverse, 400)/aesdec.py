#!/usr/bin/python
from Crypto.Cipher import AES
key=''.join([chr((int('3C4FCF098815F7ABA6D2AE2816157E2B',16)>>i*8)&0xff) for i in xrange(0,16)])
aes=AES.new(key,AES.MODE_ECB)
with open('flag.transformed','rb') as f:
    ciphertext=f.read()
print aes.decrypt(ciphertext)
