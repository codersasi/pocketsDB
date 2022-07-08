import pathlib

from argparse import ArgumentParser

from antlr4 import InputStream, ParseTreeWalker
from antlr4.CommonTokenStream import CommonTokenStream

from pockets.grammar.pocketsLexer import pocketsLexer
from pockets.grammar.pocketsParser import pocketsParser
from pockets.grammar.pocketsListener import pocketsListener


class SQLParser(pocketsListener):
    def __init__(self, base_path):
        self.tokens = None

    def parse_sql(self, sql: str):
        print(f"Parsing SQL: {sql}")
        data = InputStream(sql)
        lexer = pocketsLexer(data)
        stream = CommonTokenStream(lexer)
        self.tokens = stream
        parser = pocketsParser(stream)
        tree = parser.pocket()
        walker = ParseTreeWalker()
        walker.walk(self, tree)

    def exitCreate(self, ctx:pocketsParser.CreateContext):
        print(f"Inside the create method {self.tokens.getText(ctx.start, ctx.stop)}")

    def exitInsert(self, ctx:pocketsParser.InsertContext):
        print(f"Inside the insert method {self.tokens.getText(ctx.start, ctx.stop)}")

    def exitSelect(self, ctx:pocketsParser.SelectContext):
        print(f"Inside the select method {self.tokens.getText(ctx.start, ctx.stop)}")

    def exitDelete(self, ctx:pocketsParser.DeleteContext):
        print(f"Inside the delete method {self.tokens.getText(ctx.start, ctx.stop)}")


if __name__ == "__main__":
    args_parser = ArgumentParser(description='Database File Base Path')
    args_parser.add_argument('--base-dir', dest='base_dir', type=pathlib.Path, help='Base Directory for Files')
    args = args_parser.parse_args()

    parser = SQLParser(args.base_dir)
    parser.parse_sql("create file demo.csv (id, name, desc, city);")
