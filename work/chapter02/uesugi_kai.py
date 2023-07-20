# 上杉暗号の改良
import uesugi_table as table

# 列名と行名を定義
COLS = "いろはにほへと"
ROWS = "ちりぬるをわか"

# 暗号化
def encrypt(src):
    # 1文字ずつ変換
    result = ""
    for ch in src:
        # 辞書内にその文字があるか
        if ch in table.CONV_DIC:
            ch = table.CONV_DIC[ch]  # 文字を置換
            # 列名と行名に変換
            ch = COLS[int(ch[0]) - 1] + ROWS[int(ch[1]) - 1]
        result += ch
    return result


# 復号化
def decrypt(src):
    # 1文字ずつ変換
    result = ""
    n1 = -1
    for ch in src:
        if ch in COLS:
            n1 = COLS.index(ch)
        elif ch in ROWS:
            n2 = ROWS.index(ch)
            if (0 <= n1 <= 6) and (0 <= n2 <= 6):
                result += table.CONV_TABLE[n1][n2]
            n1 = -1
        else:
            result += ch
            n1 = -1
    return result


if __name__ == "__main__":
    enc = encrypt("しろくま")
    dec = decrypt(enc)
    print("暗号化: ", enc)
    print("復号化: ", dec)
