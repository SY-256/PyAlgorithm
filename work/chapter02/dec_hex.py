# 10進数と16進数の相互変換
# 10進数を16進数に変換する関数
def dec_to_hex(n):
    label = "0123456789ABCDEF"
    result = ""
    if n == 0:
        return "0"
    while n > 0:
        m = n % 16
        n = n // 16
        result = label[m] + result  # 今回の桁を文字列で追加
    return result


# 16進数を10進数に変換する関数
def hex_to_dex(hex_str):
    result = 0
    for c in hex_str:
        result *= 16
        v = 0
        if c in "0123456789":
            v = ord(c) - ord("0")
        elif c in "ABCDEF":
            v = ord(c) - ord("A") + 10
        elif c in "abcdef":
            v = ord(c) - ord("a") + 10
        result += v
    return result


# テスト
def test_dec_hex():
    assert dec_to_hex(255) == "FF"
    assert dec_to_hex(256) == "100"
    assert dec_to_hex(0) == "0"

    assert hex_to_dex("FF") == 255
    assert hex_to_dex("100") == 256
    assert hex_to_dex("F") == 15


if __name__ == "__main__":
    print("dex_to_hex(255) => ", dec_to_hex(255))
    print('hex_to_dex("FF") => ', hex_to_dex("FF"))
