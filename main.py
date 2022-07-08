import pathlib
from argparse import ArgumentParser
from parser.sql_parser import SQLParser


def process_args():
    args_parser = ArgumentParser(description='Database File Base Path')
    args_parser.add_argument('--base-dir', dest='base_dir', type=pathlib.Path, help='Base Directory for Files')
    return args_parser.parse_args()


def take_input(params):
    base_dir: pathlib.Path = params.base_dir
    sql = ""
    parser = SQLParser(base_dir.absolute())
    while True:
        line = input("$ ").strip()
        sql += line
        if line == 'exit':
            break
        elif line[-1] == ';':
            try:
                parser.parse(sql)
            except FileNotFoundError as e:
                print(f"File Not found at {e}")
            except RuntimeError as e:
                print(f"Error {e} while executing")
            except Exception as e:
                print(f"Error while parsing {e}")
            else:
                sql = ""


if __name__ == '__main__':
    args = process_args()
    take_input(args)
