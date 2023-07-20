# 上杉暗号の暗号化と復号化
import kansuji
import uesugi_table as table

# 平文から上杉暗号に変換
def encrypt(src):
    # 1文字ずつ変換
    result = ""
    for c in src:
        # 辞書内にその文字があるか
        if c in table.CONV_DIC:
            c = table.CONV_DIC[c]  # あればその文字に変換
        result += c
    return kansuji.to_kansuji(result)  # 漢数字に変換


# 上杉暗号から平文に変換
def decrypt(src):
    result = ""
    row, col = -1, -1
    src = kansuji.to_romaji(src)
    # 1文字ずつ変換
    for c in src:
        "1から7までの数字以外か？"
        if c not in "1234567":
            result += c
            continue
        # 数値の1文字目の場合
        if row == -1:
            row = int(c) - 1
            continue
        # 数値の2文字目の場合
        col = int(c) - 1
        # テーブルの文字を参照
        result += table.CONV_TABLE[row][col]
        row = -1
    return result


# pytest
def test_uesugi_encrypt():
    assert encrypt("しろくま") == "六七一二四七五二"
    assert decrypt("六七一二四七五二") == "しろくま"
    assert encrypt("おこのみやき") == "四六五五四五六六五一六三"
    assert decrypt("四六五五四五六六五一六三") == "おこのみやき"


if __name__ == "__main__":
    enc = encrypt("おもてなし")
    dec = decrypt(enc)
    print("暗号化: ", enc)
    print("復号化: ", dec)
