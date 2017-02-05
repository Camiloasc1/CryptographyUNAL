# One-Time-Pad modulo 26
import string

int_to_alpha_map = list(string.ascii_uppercase)
assert len(int_to_alpha_map) == 26
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


def code(msg, key):
    msg = alpha_to_int(msg)
    key = alpha_to_int(key)
    for i in range(len(msg)):
        msg[i] = (msg[i] + key[i]) % 26
    return int_to_alpha(msg)


def decode(msg, key):
    msg = alpha_to_int(msg)
    key = alpha_to_int(key)
    for i in range(len(msg)):
        msg[i] = (msg[i] - key[i]) % 26
    return int_to_alpha(msg)


def keyof(msg, cph):
    return decode(cph, msg)


assert code('TODAY', 'XVHEU') == 'QJKES'
assert decode('QJKES', 'XVHEU') == 'TODAY'
assert keyof('TODAY', 'QJKES') == 'XVHEU'

if __name__ == '__main__':
    print(code('HELLO', 'JFZTE'))
    print(keyof('APPLE', 'QJKES'))
    print(keyof('GLASS', 'QJKES'))
    print(keyof('READY', 'QJKES'))
    print(keyof('MONTH', 'QJKES'))
    print(decode('QJKES', 'JFZTE'))  # Not for sure, can be any other pair of plaintext-key combination
