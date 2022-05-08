# CLI (command-line interface)
from argparse import ArgumentParser

args = ArgumentParser()

args.add_argument("name", type=str)
args.add_argument("age", type=int, nargs='?', default=0)
# args.parse_args("-f", "--test")
# args.parse_args("-f", "--test", type=int, nargs='?', default=0)

args = vars(args.parse_args())
print(args)


name = args['name']
age = args['age']

print(f"Hello {name}! My value is {age}")
