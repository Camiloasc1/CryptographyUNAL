import sys
import os
import base64
import homework5.pyaes as pyaes


def encrypt(msg, key):
    return pyaes.AESModeOfOperationCTR(key).encrypt(msg)


def decrypt(cph, key):
    return pyaes.AESModeOfOperationCTR(key).decrypt(cph)


def read_file(path):
    with open(path, mode='rb') as file:
        data = file.read()
    return data


def write_file(path, data):
    with open(path, mode='wb') as file:
        file.write(data)


if __name__ == '__main__':
    print("Key: ", end='', flush=True)
    key = sys.stdin.readline().strip().encode()
    if len(key) != 16 and len(key) != 24 and len(key) != 32:
        print("Invalid AES key size. Key must be 128, 192 or 256.")
        exit()

    print("Input file: ", end='', flush=True)
    in_img = sys.stdin.readline().strip()
    in_img = in_img if in_img else "in.png"

    print("Output file: ", end='', flush=True)
    out_img = sys.stdin.readline().strip()
    out_img = out_img if out_img else "out.png"

    msg = read_file(in_img)
    cph = encrypt(msg, key)
    cph64 = base64.standard_b64encode(cph)
    print("Base64:", cph64)
    cph = base64.standard_b64decode(cph64)
    write_file(out_img, decrypt(cph, key))
    os.system("xdg-open " + out_img)  # open file
