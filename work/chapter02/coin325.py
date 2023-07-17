# コインの組み合わせ
for c1 in range(0, 12 + 1):
    for c5 in range(0, 9 + 1):
        for c10 in range(0, 30 + 1):
            # 合計金額を計算
            total = (c10 * 10) + (c5 * 5) + c1
            # 金額に合致する場合は画面に出力
            if total == 325:
                print(f"10円*{c10} + 5円*{c5} + 1円*{c1}")
