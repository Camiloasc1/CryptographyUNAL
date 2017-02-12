import sys
import string
import numpy as np
from numpy.linalg import inv, det

int_to_alpha_map = list(string.ascii_uppercase)
alpha_to_int_map = dict([(c, i) for i, c in enumerate(int_to_alpha_map)])


def alpha_to_int(msg):
    out = list()
    for c in msg:
        out.append(alpha_to_int_map[c])
    return out


def int_to_alpha(msg):
    out = list()
    for i in msg:
        out.append(int_to_alpha_map[i])
    return ''.join(out)


def encrypt(msg, key, block_size):
    if len(msg) % 2 == 1:
        msg += 'X'
    msg = alpha_to_int(msg)
    key = np.array(key).reshape((block_size, block_size))
    cph = []
    for c in zip(msg[::2], msg[1::2]):
        c = np.array(c)
        cph.extend((c.dot(key) % 26).tolist())
    return int_to_alpha(cph)


def decrypt(cph, key, block_size):
    if len(cph) % 2 == 1:
        cph += 'X'
    cph = alpha_to_int(cph)
    key = np.array(key).reshape((block_size, block_size))
    _, x, _ = EEA(np.rint(det(key)).astype(int), 26)  # The modular inverse of det(k) % 26
    key = np.rint(inv(key) * det(key) * x).astype(int)  # Multiply by det(k) in order get the adj(k)
    msg = []
    for c in zip(cph[::2], cph[1::2]):
        c = np.array(c)
        msg.extend((c.dot(key) % 26).tolist())
    return int_to_alpha(msg)


def EEA(a, b):
    if b == 0:
        return a, 1, 0
    g, x, y = EEA(b, a % b)
    return g, y, x - a // b * y


def is_valid_key(key):
    # from math import gcd

    d = np.rint(det(np.array(key).reshape((2, 2)))).astype(int)
    # return not (d == 0 or gcd(d, 26) != 1)  # this makes the key invalid for Hill cipher
    return not (d == 0 or d % 2 == 0 or d % 13 == 0)  # this makes the key invalid for Hill cipher


if __name__ == '__main__':
    msg = sys.stdin.readline().strip().upper()
    key = [int(n) for n in sys.stdin.readline().split()]
    if is_valid_key(key):
        print("Encrypted: '" + encrypt(msg, key, 2) + "'")
        print("Decrypted: '" + decrypt(msg, key, 2) + "'")
    else:
        print("Invalid key")
