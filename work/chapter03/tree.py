import os, sys

# インデントに使用する記号
INDENT_PIN_C = "|----"
INDENT_PIN_E = "└----"
INDENT_BLANK = "    "
INDENT_LEVEL = "|   "
# 再帰的にファイル一覧を表示する関数
def enumfiles(path, indent="", level=0, is_late=False):
    # ファイル（ディレクトリ）の先頭に表示する記号を選択
    pin = INDENT_PIN_E if is_late else INDENT_PIN_C
    pin = "" if level == 0 else pin
    if os.path.isdir(path):
        # ディレクトリの場合
        print(indent + pin + os.path.basename(path))
        # インデント記号を用意
        indent += INDENT_BLANK if is_late else INDENT_LEVEL
        indent = "" if level == 0 else indent
        # ディレクトリ以下のファイル一覧を取得して繰り返す
        subdirs = list(sorted(os.listdir(path)))
        for i, f in enumerate(subdirs):
            ff = os.path.join(path, f)
            is_late = (len(subdirs) - 1) == i  # 最後の要素か
            enumfiles(ff, indent, level + 1, is_late)  # 再帰

    else:
        print(indent + pin + os.path.basename(path))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("USAGE: tree.py (path)")
        quit()
    enumfiles(sys.argv[1])
