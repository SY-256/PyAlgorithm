# 10進数->8進数変換
def dec_to_oct(n):
    label = "01234567"
    result = ""
    if n == 0:
        return "0"
    while n > 0:
        m = n & 0b111
        n = n >> 3
        result = label[m] + result
    return result


# 8進数->10進数変換
def oct_to_dec(oct_str):
    result = 0
    for c in oct_str:
        result *= 8
        if c in "01234567":
            v = ord(c) - ord("0")
        result += v
    return result


def test_dec_to_oct():
    assert dec_to_oct(8) == "10"
    assert dec_to_oct(7) == "7"
    assert dec_to_oct(15) == "17"
    assert dec_to_oct(10) == "12"
    assert dec_to_oct(16) == "20"

    assert oct_to_dec("10") == 8
    assert oct_to_dec("7") == 7
    assert oct_to_dec("17") == 15
    assert oct_to_dec("20") == 16
    assert oct_to_dec("12") == 10
