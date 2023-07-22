import math, sys

# 逆ポーランド記法で使う関数を辞書で定義
RPN_FUNCTOINS = {
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
}
# 演算子を辞書で定義
RPN_OPERATORS = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
    "%": lambda a, b: a % b,
}
# 定義を辞書で定義
RPN_CONSTANTS = {"pi": math.pi}

# 逆ポーランド記法
def calc_rpn(src):
    stack = []
    tokens = src.split(" ")
    for t in tokens:
        if t in RPN_FUNCTOINS:
            a = stack.pop()
            stack.append(RPN_FUNCTOINS[t](a))  # 関数もオブジェクトとして使用できる
        elif t in RPN_OPERATORS:
            b = stack.pop()
            a = stack.pop()
            stack.append(RPN_OPERATORS[t](a, b))
        elif t in RPN_CONSTANTS:
            stack.append(RPN_CONSTANTS[t])
        else:
            stack.append(float(t))
    return stack.pop()


# テスト
def test_rpn():
    assert calc_rpn("0 sin") == 0
    assert calc_rpn("pi 2 / sin") == math.sin(math.pi / 2)
    assert calc_rpn("pi 3 / cos") == math.cos(math.pi / 3)


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print('[USAGE] rpn_func.py "expr"')
        quit()
    print(calc_rpn(sys.argv[1]))
