import argparse

parser = argparse.ArgumentParser(description="easy file sharing")
parser.add_argument("-p", "--push", type=str, help='filepath')

args = parser.parse_args()

if args.push:
    print(f"pushing file: {args.push}")
else:
    print('no file path')
