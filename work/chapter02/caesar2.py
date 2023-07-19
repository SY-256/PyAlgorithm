def encrypt(src, key_no):
    result = ""
    for c in src:
        if "A" <= c <= "Z":
            ci = ord(c)
            base = ord("A")
            ci = (ci - base + key_no) % 26 + base
            c = chr(ci)
        elif "a" <= c <= "z":
            ci = ord(c)
            base = ord("a")
            ci = (ci - base + key_no) % 26 + base
            c = chr(ci)
        result += c
    return result


def decrypt(src, key_no):
    return encrypt(src, -1 * key_no)


def test_encrypt_caesar():
    assert encrypt("cat", 3) == "fdw"
    assert encrypt("love", 3) == "oryh"
    assert decrypt("FDW", 3) == "CAT"
