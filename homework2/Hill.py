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
    key = np.rint(inv(key) * det(key)).astype(int)  # Multiply by det(k) in order to be sure there are integers
    msg = []
    for c in zip(cph[::2], cph[1::2]):
        c = np.array(c)
        msg.extend((c.dot(key) % 26).tolist())
    return int_to_alpha(msg)


if __name__ == '__main__':
    msg = sys.stdin.readline().strip()
    key = [int(n) for n in sys.stdin.readline().split()]
    print("Encrypted: '" + encrypt(msg, key, 2) + "'")
    print("Decrypted: '" + decrypt(msg, key, 2) + "'")
