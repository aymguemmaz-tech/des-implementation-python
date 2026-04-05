from __future__ import annotations

from typing import List


# =========================
# DES TABLES
# =========================

IP = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7,
]

FP = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25,
]

E = [
    32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1,
]

P = [
    16, 7, 20, 21,
    29, 12, 28, 17,
    1, 15, 23, 26,
    5, 18, 31, 10,
    2, 8, 24, 14,
    32, 27, 3, 9,
    19, 13, 30, 6,
    22, 11, 4, 25,
]

PC1 = [
    57, 49, 41, 33, 25, 17, 9,
    1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27,
    19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29,
    21, 13, 5, 28, 20, 12, 4,
]

PC2 = [
    14, 17, 11, 24, 1, 5,
    3, 28, 15, 6, 21, 10,
    23, 19, 12, 4, 26, 8,
    16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53,
    46, 42, 50, 36, 29, 32,
]

SHIFTS = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

S_BOXES = [
    [  # S1
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
    ],
    [  # S2
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
    ],
    [  # S3
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
    ],
    [  # S4
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
    ],
    [  # S5
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
    ],
    [  # S6
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
    ],
    [  # S7
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
    ],
    [  # S8
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
    ],
]


# =========================
# HELPER FUNCTIONS
# =========================

def permute(block: int, table: List[int], in_bits: int) -> int:
    """
    Apply a bit permutation table to block.
    Table positions are 1-indexed from the leftmost bit.
    """
    result = 0
    for position in table:
        bit = (block >> (in_bits - position)) & 1
        result = (result << 1) | bit
    return result


def left_rotate28(value: int, shift: int) -> int:
    """Rotate a 28-bit integer left."""
    value &= 0x0FFFFFFF
    return ((value << shift) & 0x0FFFFFFF) | (value >> (28 - shift))


def sbox_substitution(block48: int) -> int:
    """
    Apply the 8 DES S-boxes to a 48-bit block.
    Returns a 32-bit integer.
    """
    result = 0
    for i in range(8):
        six_bits = (block48 >> (42 - 6 * i)) & 0x3F
        row = ((six_bits & 0x20) >> 4) | (six_bits & 0x01)
        col = (six_bits >> 1) & 0x0F
        val = S_BOXES[i][row][col]
        result = (result << 4) | val
    return result


def feistel(right32: int, subkey48: int) -> int:
    """
    DES round function F(R, K):
    1) expansion 32->48
    2) XOR with subkey
    3) S-box substitution 48->32
    4) permutation P
    """
    expanded = permute(right32, E, 32)
    mixed = expanded ^ subkey48
    substituted = sbox_substitution(mixed)
    return permute(substituted, P, 32)


def generate_subkeys(key64: int) -> List[int]:
    """
    Generate the 16 DES 48-bit round keys from a 64-bit key.
    DES ignores 8 parity bits through PC-1.
    """
    key56 = permute(key64, PC1, 64)
    c = (key56 >> 28) & 0x0FFFFFFF
    d = key56 & 0x0FFFFFFF

    subkeys: List[int] = []
    for shift in SHIFTS:
        c = left_rotate28(c, shift)
        d = left_rotate28(d, shift)
        cd = (c << 28) | d
        subkeys.append(permute(cd, PC2, 56))
    return subkeys


# =========================
# BLOCK ENCRYPT / DECRYPT
# =========================

def des_encrypt_block(block64: int, key64: int) -> int:
    """
    Encrypt one 64-bit block with DES.
    """
    subkeys = generate_subkeys(key64)

    permuted = permute(block64, IP, 64)
    left = (permuted >> 32) & 0xFFFFFFFF
    right = permuted & 0xFFFFFFFF

    for subkey in subkeys:
        new_left = right
        new_right = left ^ feistel(right, subkey)
        left, right = new_left, new_right

    # Final swap before FP
    preoutput = (right << 32) | left
    return permute(preoutput, FP, 64)


def des_decrypt_block(block64: int, key64: int) -> int:
    """
    Decrypt one 64-bit block with DES.
    """
    subkeys = generate_subkeys(key64)[::-1]

    permuted = permute(block64, IP, 64)
    left = (permuted >> 32) & 0xFFFFFFFF
    right = permuted & 0xFFFFFFFF

    for subkey in subkeys:
        new_left = right
        new_right = left ^ feistel(right, subkey)
        left, right = new_left, new_right

    preoutput = (right << 32) | left
    return permute(preoutput, FP, 64)


# =========================
# BYTE CONVERSION HELPERS
# =========================

def bytes_to_int(block: bytes) -> int:
    if len(block) != 8:
        raise ValueError("DES block must be exactly 8 bytes.")
    return int.from_bytes(block, byteorder="big")


def int_to_bytes(value: int) -> bytes:
    return value.to_bytes(8, byteorder="big")


def xor_bytes(a: bytes, b: bytes) -> bytes:
    return bytes(x ^ y for x, y in zip(a, b))


# =========================
# PADDING
# =========================

def pkcs5_pad(data: bytes) -> bytes:
    pad_len = 8 - (len(data) % 8)
    if pad_len == 0:
        pad_len = 8
    return data + bytes([pad_len] * pad_len)


def pkcs5_unpad(data: bytes) -> bytes:
    if not data or len(data) % 8 != 0:
        raise ValueError("Invalid padded data length.")
    pad_len = data[-1]
    if pad_len < 1 or pad_len > 8:
        raise ValueError("Invalid padding.")
    if data[-pad_len:] != bytes([pad_len] * pad_len):
        raise ValueError("Invalid padding bytes.")
    return data[:-pad_len]


# =========================
# ECB MODE
# =========================

def des_encrypt_ecb(data: bytes, key: bytes) -> bytes:
    """
    Encrypt bytes using DES in ECB mode.
    """
    if len(key) != 8:
        raise ValueError("DES key must be exactly 8 bytes.")

    key64 = bytes_to_int(key)
    padded = pkcs5_pad(data)
    out = bytearray()

    for i in range(0, len(padded), 8):
        block = padded[i:i + 8]
        cipher_block = des_encrypt_block(bytes_to_int(block), key64)
        out.extend(int_to_bytes(cipher_block))

    return bytes(out)


def des_decrypt_ecb(data: bytes, key: bytes) -> bytes:
    """
    Decrypt bytes using DES in ECB mode.
    """
    if len(key) != 8:
        raise ValueError("DES key must be exactly 8 bytes.")
    if len(data) % 8 != 0:
        raise ValueError("Ciphertext length must be a multiple of 8 bytes.")

    key64 = bytes_to_int(key)
    out = bytearray()

    for i in range(0, len(data), 8):
        block = data[i:i + 8]
        plain_block = des_decrypt_block(bytes_to_int(block), key64)
        out.extend(int_to_bytes(plain_block))

    return pkcs5_unpad(bytes(out))


# =========================
# OPTIONAL CBC MODE
# =========================

def des_encrypt_cbc(data: bytes, key: bytes, iv: bytes) -> bytes:
    if len(key) != 8:
        raise ValueError("DES key must be exactly 8 bytes.")
    if len(iv) != 8:
        raise ValueError("DES IV must be exactly 8 bytes.")

    key64 = bytes_to_int(key)
    padded = pkcs5_pad(data)
    out = bytearray()
    prev = iv

    for i in range(0, len(padded), 8):
        block = padded[i:i + 8]
        xored = xor_bytes(block, prev)
        cipher_block = int_to_bytes(des_encrypt_block(bytes_to_int(xored), key64))
        out.extend(cipher_block)
        prev = cipher_block

    return bytes(out)


def des_decrypt_cbc(data: bytes, key: bytes, iv: bytes) -> bytes:
    if len(key) != 8:
        raise ValueError("DES key must be exactly 8 bytes.")
    if len(iv) != 8:
        raise ValueError("DES IV must be exactly 8 bytes.")
    if len(data) % 8 != 0:
        raise ValueError("Ciphertext length must be a multiple of 8 bytes.")

    key64 = bytes_to_int(key)
    out = bytearray()
    prev = iv

    for i in range(0, len(data), 8):
        block = data[i:i + 8]
        decrypted = int_to_bytes(des_decrypt_block(bytes_to_int(block), key64))
        plain_block = xor_bytes(decrypted, prev)
        out.extend(plain_block)
        prev = block

    return pkcs5_unpad(bytes(out))


# =========================
# DEMO / TESTS
# =========================

def main() -> None:
    # Official-style classic DES test vector
    key_hex = "133457799BBCDFF1"
    pt_hex = "0123456789ABCDEF"
    expected_ct_hex = "85E813540F0AB405"

    key = bytes.fromhex(key_hex)
    pt = bytes.fromhex(pt_hex)

    ct_int = des_encrypt_block(bytes_to_int(pt), bytes_to_int(key))
    ct_hex = int_to_bytes(ct_int).hex().upper()

    print("=== Single-block DES test ===")
    print("Key       :", key_hex)
    print("Plaintext :", pt_hex)
    print("Ciphertext:", ct_hex)
    print("Expected  :", expected_ct_hex)
    print("Match     :", ct_hex == expected_ct_hex)

    recovered = int_to_bytes(des_decrypt_block(ct_int, bytes_to_int(key))).hex().upper()
    print("Recovered :", recovered)
    print()

    # ECB example
    message = b"Lorem ipsum dolor sit amet"
    ecb_cipher = des_encrypt_ecb(message, key)
    ecb_plain = des_decrypt_ecb(ecb_cipher, key)

    print("=== ECB example ===")
    print("Message   :", message)
    print("Cipher hex:", ecb_cipher.hex())
    print("Recovered :", ecb_plain)
    print()

    # CBC example
    iv = bytes.fromhex("1234567890ABCDEF")
    cbc_cipher = des_encrypt_cbc(message, key, iv)
    cbc_plain = des_decrypt_cbc(cbc_cipher, key, iv)

    print("=== CBC example ===")
    print("IV        :", iv.hex().upper())
    print("Cipher hex:", cbc_cipher.hex())
    print("Recovered :", cbc_plain)


if __name__ == "__main__":
    main()