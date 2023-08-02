import os


def enumfiles(path):
    for pathname, dirnames, filenames in os.walk(path):
        for f in filenames:
            ff = os.path.join(pathname, f)
            print(ff)


if __name__ == "__main__":
    enumfiles("../../work")
