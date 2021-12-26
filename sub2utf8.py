import os
from argparse import ArgumentParser

from chardet import detect


def get_encoding_type(file):
    """Get file encoding type"""
    with open(file, "rb") as f:
        rawdata = f.read()
    return detect(rawdata)["encoding"]


def convert_file(srcfile):
    """Convert file encoding to utf8"""
    from_codec = get_encoding_type(srcfile)
    trgfile = srcfile + ".temp"
    try:
        with open(srcfile, "r", encoding=from_codec) as f, open(
            trgfile, "w", encoding="utf-8"
        ) as e:
            text = f.read()
            e.write(text)

        os.remove(srcfile)
        os.rename(trgfile, srcfile)
    except UnicodeDecodeError:
        print("Decode Error")
    except UnicodeEncodeError:
        print("Encode Error")


def main():
    ap = ArgumentParser()
    ap.add_argument("-f", "--file", required=True, help="File name")
    ap.description = "\n".join(
        [
            "Hi!",
            "This program will convert any file to utf8. You can even use it for Bulgarian subtitles.",
            "Just please provide a file name (-f) and go!",
        ]
    )
    args = vars(ap.parse_args())
    if not os.path.exists(args["file"]):
        raise FileNotFoundError(
            "The file you provided doesn't exist. Please provide a valid file path. :)"
        )
    convert_file(args["file"])


if __name__ == "__main__":
    main()
