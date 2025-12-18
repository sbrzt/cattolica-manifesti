# main.py

from src.process import extract_paradata


def main():
    print(extract_paradata("data/process/17_BNS3593/17_BNS3593_imp.xmp", "data/process/17_BNS3593/17_BNS3593_proc.xmp"))



if __name__ == "__main__":
    main()
