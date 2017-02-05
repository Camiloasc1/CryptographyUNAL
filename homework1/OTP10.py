# One-Time-Pad modulo 10
mod10_map = [
    (0, 'A'), (1, 'T'), (2, ''), (3, 'O'), (4, 'N'), (5, 'E'), (6, ''), (7, 'S'), (8, 'I'), (9, 'R'),
    (20, 'B'), (21, 'C'), (22, 'D'), (23, 'F'), (24, 'G'), (25, 'H'), (26, 'J'), (27, 'K'), (28, 'L'), (29, 'M'),
    (60, 'P'), (61, 'Q'), (62, 'U'), (63, 'V'), (64, 'W'), (65, 'X'), (66, 'Y'), (67, 'Z'), (68, '.'), (69, ' ')]

int_to_alpha_map = dict(mod10_map)
alpha_to_int_map = dict([(v, k) for k, v in int_to_alpha_map.items()])


def flatten(msg):
    return [int(c) for c in ''.join(str(i) for i in msg)]


def bulk(msg):
    out = []
    i = 0
    while i < len(msg):
        if msg[i] == 2 or msg[i] == 6:
            out.append(int(str(msg[i]) + str(msg[i + 1])))
            i += 1
        else:
            out.append(msg[i])
        i += 1
    return out


def alpha_to_int(msg):
    out = list()
    for c in msg:
        out.append(alpha_to_int_map[c])
    return flatten(out)


def int_to_alpha(msg):
    msg = bulk(msg)
    out = list()
    for i in msg:
        out.append(int_to_alpha_map[i])
    return ''.join(out)


def code(msg, key):
    for i in range(len(msg)):
        msg[i] = (msg[i] - key[i]) % 10
    return msg


def decode(msg, key):
    for i in range(len(msg)):
        msg[i] = (msg[i] + key[i]) % 10
    return msg


def keyof(msg, cph):
    return decode(cph, msg)


if __name__ == '__main__':
    txt = [int(i) for i in list('66475 19274 92028 78494 24146 68542 17507 39398 32348 59378 70636'.replace(' ', ''))]
    key = [int(i) for i in list('66153 77185 10800 54937 48159 83271 12892 07132 34987 53954 23074'.replace(' ', ''))]
    print(txt)
    print(key)
    msg = decode(txt, key)
    print(msg)
    print(int_to_alpha(msg))
    for c, i in zip(int_to_alpha(msg), bulk(msg)):
        print(c, i)
