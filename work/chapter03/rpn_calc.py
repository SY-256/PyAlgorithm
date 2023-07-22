# 逆ポーランド記法の計算
def calc_rpn(src):
    # スタックを用意
    stack = []
    # 文字列をトークンに分類
    tokens = src.split(" ")
    # トークンを1つずつ処理
    for t in tokens:
        # 演算子か
        if t in "+-*/%":
            b = stack.pop()  # スタックから末尾を下す
            a = stack.pop()  # スタックから末尾を下す
            if t == "+":
                stack.append(a + b)
            elif t == "-":
                stack.append(a - b)
            elif t == "*":
                stack.append(a * b)
            elif t == "/":
                stack.append(a / b)
            elif t == "%":
                stack.append(a % b)
        # 数値の場合
        else:
            stack.append(float(t))
    # スタックに残った値が答え
    return stack.pop()


# 逆ポーランド記法のテスト
def test_rpn():
    assert calc_rpn("2 3 +") == 5
    assert calc_rpn("2 3 * 4 +") == 10
    assert calc_rpn("2 5 3 * +") == 17
    assert calc_rpn("100 2 /") == 50
    assert calc_rpn("30 25 -") == 5
