import sys
import numpy as np


def encrypt(msg, key, size, rot_func):
    msg = [c for c in msg]
    cph = [[''] * size for _ in range(size)]
    c = 0
    for s in range(4):
        for i in range(size):
            for j in range(size):
                if key[i][j]:
                    cph[i][j] = msg[c]
                    c += 1
        key = rot_func(key)
    return matrix_to_message(cph)


def decrypt(cph, key, size, rot_func):
    cph = np.array([c for c in cph]).reshape((size, size)).tolist()
    msg = []
    for s in range(4):
        for i in range(size):
            for j in range(size):
                if key[i][j]:
                    msg.append(cph[i][j])
        key = rot_func(key)
    return matrix_to_message(msg)


# Rotate counter clock wise
def rotate(grid):
    return [list(r) for r in reversed(list(zip(*grid)))]


# Rotate clock wise
def unrotate(grid):
    return [list(r) for r in zip(*grid[::-1])]


def holes_to_matrix(holes, size):
    grid = [False] * size * size
    for h in holes:
        grid[h] = True
    return np.array(grid).reshape((size, size)).tolist()


def pad_crop_message(msg, size):
    msg = [c for c in msg]
    if len(msg) < size * size:
        msg.extend(['X'] * (size * size - len(msg)))
    elif len(msg) > size * size:
        msg = msg[:size * size]
    return ''.join(msg)


def matrix_to_message(msg):
    return ''.join(np.array(msg).flatten().tolist())


if __name__ == '__main__':
    print("Size:")
    size = int(sys.stdin.readline().strip())
    if size < 2:
        print("Invalid Size")
        exit()

    print("Rotation (0 - clockwise, 1 - counterclockwise):")
    rotation = int(sys.stdin.readline().strip())
    if rotation != 0 and rotation != 1:
        print("Invalid Rotation")
        exit()

    print("Mode (0 - encrypt, 1 - decrypt):")
    mode = int(sys.stdin.readline().strip())
    if rotation != 0 and rotation != 1:
        print("Invalid Mode")
        exit()

    print("Holes (number per hole, ordered left to right and up to down, split by space):")
    holes = list(set([int(n) for n in sys.stdin.readline().strip().split()]))
    holes.sort()
    if len(holes) == 0 or len(holes) > size * size or holes[0] < 0 or holes[-1] >= size * size:
        print("Invalid Holes")
        exit()

    key = holes_to_matrix(holes, size)

    print("Message:")
    msg = sys.stdin.readline().strip().replace(' ', '').upper()
    msg = pad_crop_message(msg, size)

    if mode == 0:
        print(encrypt(msg, key, size, rotate))
    else:
        print(decrypt(msg, key, size, rotate))
