# 漢数字とローマ数字の相互変換を行う
# 変換テーブル
KANSUJI = list("零一二三四五六七八九")
ROMAJI = list("0123456789")

# 変換テーブルを辞書に変換
KANSUJI_DIC = {key: str(no) for no, key in enumerate(KANSUJI)}

# 漢数字に変換
def to_kansuji(src):
    result = ""
    # 文字列srcを1文ずつ変換
    for c in src:
        if c in ROMAJI:
            c = KANSUJI[int(c)]
        result += c
    return result


# ローマ数字に変換
def to_romaji(src):
    result = ""
    # 文字列srcを1文字ずつ変換
    for c in src:
        if c in KANSUJI_DIC:
            c = KANSUJI_DIC[c]
        result += c
    return result


# pytestで関数をテスト
def test_kansuji():
    assert to_kansuji("345") == "三四五"
    assert to_romaji("三四五") == "345"
