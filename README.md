## XOR in python

![Screenshot](help.png)

## Table of contents
* [Exemples](#Examples)
* [Requirements](#requirements)

## Examples

Crypt : 

```
# Linux
$ python3 xor_cipher.py -c key message message2
$ python3 xor_cipher.py --crypt key message message2

# Windows
$ py xor_cipher.py -c key message message2
$ py xor_cipher.py --crypt key message message2
````
Result :

![alt text](https://image.noelshack.com/fichiers/2020/16/1/1586780992-capture.png)

Decrypt : 

```
# Linux
$ python3 xor_cipher.py -d key 00000110 00000000 00001010 00011000 00000100 00011110 00001110 01000101 00010100 00001110 00010110 00001010 00001010 00000010 00011100 01011001
$ python3 xor_cipher.py --decrypt 00000110 00000000 00001010 00011000 00000100 00011110 00001110 01000101 00010100 00001110 00010110 00001010 00001010 00000010 00011100 01011001

# Windows
$ py xor_cipher.py -d key 00000110 00000000 00001010 00011000 00000100 00011110 00001110 01000101 00010100 00001110 00010110 00001010 00001010 00000010 00011100 01011001
$ py xor_cipher.py --decrypt key 00000110 00000000 00001010 00011000 00000100 00011110 00001110 01000101 00010100 00001110 00010110 00001010 00001010 00000010 00011100 01011001
````
Result :

![alt text](https://image.noelshack.com/fichiers/2020/16/1/1586781660-capture.png)

## Requirements

- sys
- os
- platform
- itertools
- base64
- binascii
