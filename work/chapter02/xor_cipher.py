import binascii

# 暗号化
def encrypt(src, key):
    result = bytearray()
    # 文字列をバイト配列に変換
    src_bytes = src.encode()
    key_bytes = key.encode()
    # 1バイトずつXORする
    for i, b in enumerate(src_bytes):
        key_b = key_bytes[i % len(key_bytes)]
        xor_v = b ^ key_b  # XOR
        result.append(xor_v)
    # bytearrayをHEX文字列に変換
    result_s = binascii.b2a_hex(result).decode("utf-8")
    return result_s


# 復号化
def decrypt(src, key):
    result = bytearray()
    # HEX文字列をバイト列に変換
    src_b = binascii.a2b_hex(src)
    key_bytes = key.encode()
    # 1バイトずつXORする
    for i, b in enumerate(src_b):
        key_b = key_bytes[i % len(key_bytes)]
        xor_v = b ^ key_b
        result.append(xor_v)
    # bytearrayを文字列に戻す
    result_s = result.decode("utf-8")
    return result_s


# テスト
def test_encrypt_xor_cipher():
    assert encrypt("world", "abc") == "160d110d06"
    assert decrypt("160d110d06", "abc") == "world"


if __name__ == "__main__":
    enc = encrypt("hello", "abc")
    dec = decrypt(enc, "abc")
    print("暗号化: ", enc)
    print("復号化: ", dec)
