import os

# 全ファイル列挙
def enumfiles(path):
    if os.path.isdir(path):
        # ディレクトリの場合
        for f in os.listdir(path):
            ff = os.path.join(path, f)
            enumfiles(ff)  # 再帰処理
    else:
        # ファイルの場合
        print(path)


if __name__ == "__main__":
    # 指定のディレクトリを全列挙
    enumfiles("../../work")
