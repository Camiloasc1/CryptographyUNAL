import sys
import os
import base64
import homework6.elgamal as elgamal


def encrypt(msg, key):
    return elgamal.encrypt(key, msg)


def decrypt(cph, key):
    return elgamal.decrypt(key, cph)


def read_file(path):
    with open(path, mode='rb') as file:
        data = file.read()
    return data


def write_file(path, data):
    with open(path, mode='wb') as file:
        file.write(data)


if __name__ == '__main__':
    print("Key length: ", end='', flush=True)
    key_length = int(sys.stdin.readline().strip())
    key_length = key_length if key_length else 256
    if key_length <= 1:
        print("Invalid ElGamal key length.")
        exit()

    print("Confidence: ", end='', flush=True)
    Confidence = int(sys.stdin.readline().strip())
    Confidence = Confidence if Confidence else 32
    if key_length <= 1:
        print("Invalid ElGamal Confidence.")
        exit()

    print("Input file: ", end='', flush=True)
    in_img = sys.stdin.readline().strip()
    in_img = in_img if in_img else "in.png"

    print("Output file: ", end='', flush=True)
    out_img = sys.stdin.readline().strip()
    out_img = out_img if out_img else "out.png"

    print("Generating keys...")
    keys = elgamal.generate_keys(key_length, Confidence)
    priv = keys['privateKey']
    pub = keys['publicKey']

    msg = read_file(in_img)
    cph = encrypt(msg, pub)
    cph64 = base64.standard_b64encode(cph)
    print("Base64:", cph64)
    cph = base64.standard_b64decode(cph64)
    write_file(out_img, decrypt(cph, priv))
    os.system("xdg-open " + out_img)  # open file
