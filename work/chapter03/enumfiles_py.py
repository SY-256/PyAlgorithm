import os


def enumfiles(path):
    if os.path.isdir(path):
        for f in os.listdir(path):
            ff = os.path.join(path, f)
            enumfiles(ff)

    elif path.endswith(".py"):
        print(path)


if __name__ == "__main__":
    enumfiles("../../work")
