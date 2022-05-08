# CLI (command-line interface)
from argparse import ArgumentParser

args = ArgumentParser()

args.add_argument("first_arg")

args = args.parse_args()

print(args)

