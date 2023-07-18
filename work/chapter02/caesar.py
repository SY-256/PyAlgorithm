# シザー暗号
def test_encrypt_caesar():
    assert encrypt("CAT", 3) == "FDW"
    assert encrypt("LOVE", 3) == "ORYH"
    assert decrypt("FDW", 3) == "CAT"


def encrypt(src, key_no):
    result = ""
    # 1文字ずつ処理
    for c in src:
        # 大文字ならkey_no分ずらす
        if "A" <= c <= "Z":
            ci = ord(c)  # 文字コードに変換
            base = ord("A")  # 'A'の文字コード取得
            ci = (ci - base + key_no) % 26 + base
            c = chr(ci)  # 文字コードを文字に変換
        # 変換結果を追加
        result += c
    return result


def decrypt(src, key_no):
    return encrypt(src, key_no * -1)
