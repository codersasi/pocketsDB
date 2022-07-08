# Generated from grammar/pockets.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .pocketsParser import pocketsParser
else:
    from pocketsParser import pocketsParser

# This class defines a complete listener for a parse tree produced by pocketsParser.
class pocketsListener(ParseTreeListener):

    # Enter a parse tree produced by pocketsParser#pocket.
    def enterPocket(self, ctx:pocketsParser.PocketContext):
        pass

    # Exit a parse tree produced by pocketsParser#pocket.
    def exitPocket(self, ctx:pocketsParser.PocketContext):
        pass


    # Enter a parse tree produced by pocketsParser#statement.
    def enterStatement(self, ctx:pocketsParser.StatementContext):
        pass

    # Exit a parse tree produced by pocketsParser#statement.
    def exitStatement(self, ctx:pocketsParser.StatementContext):
        pass


    # Enter a parse tree produced by pocketsParser#create.
    def enterCreate(self, ctx:pocketsParser.CreateContext):
        pass

    # Exit a parse tree produced by pocketsParser#create.
    def exitCreate(self, ctx:pocketsParser.CreateContext):
        pass


    # Enter a parse tree produced by pocketsParser#insert.
    def enterInsert(self, ctx:pocketsParser.InsertContext):
        pass

    # Exit a parse tree produced by pocketsParser#insert.
    def exitInsert(self, ctx:pocketsParser.InsertContext):
        pass


    # Enter a parse tree produced by pocketsParser#delete.
    def enterDelete(self, ctx:pocketsParser.DeleteContext):
        pass

    # Exit a parse tree produced by pocketsParser#delete.
    def exitDelete(self, ctx:pocketsParser.DeleteContext):
        pass


    # Enter a parse tree produced by pocketsParser#select.
    def enterSelect(self, ctx:pocketsParser.SelectContext):
        pass

    # Exit a parse tree produced by pocketsParser#select.
    def exitSelect(self, ctx:pocketsParser.SelectContext):
        pass


    # Enter a parse tree produced by pocketsParser#columnNames.
    def enterColumnNames(self, ctx:pocketsParser.ColumnNamesContext):
        pass

    # Exit a parse tree produced by pocketsParser#columnNames.
    def exitColumnNames(self, ctx:pocketsParser.ColumnNamesContext):
        pass


    # Enter a parse tree produced by pocketsParser#values.
    def enterValues(self, ctx:pocketsParser.ValuesContext):
        pass

    # Exit a parse tree produced by pocketsParser#values.
    def exitValues(self, ctx:pocketsParser.ValuesContext):
        pass


    # Enter a parse tree produced by pocketsParser#constants.
    def enterConstants(self, ctx:pocketsParser.ConstantsContext):
        pass

    # Exit a parse tree produced by pocketsParser#constants.
    def exitConstants(self, ctx:pocketsParser.ConstantsContext):
        pass


    # Enter a parse tree produced by pocketsParser#expressionList.
    def enterExpressionList(self, ctx:pocketsParser.ExpressionListContext):
        pass

    # Exit a parse tree produced by pocketsParser#expressionList.
    def exitExpressionList(self, ctx:pocketsParser.ExpressionListContext):
        pass


    # Enter a parse tree produced by pocketsParser#booleanExpression.
    def enterBooleanExpression(self, ctx:pocketsParser.BooleanExpressionContext):
        pass

    # Exit a parse tree produced by pocketsParser#booleanExpression.
    def exitBooleanExpression(self, ctx:pocketsParser.BooleanExpressionContext):
        pass


    # Enter a parse tree produced by pocketsParser#compare.
    def enterCompare(self, ctx:pocketsParser.CompareContext):
        pass

    # Exit a parse tree produced by pocketsParser#compare.
    def exitCompare(self, ctx:pocketsParser.CompareContext):
        pass


    # Enter a parse tree produced by pocketsParser#expression.
    def enterExpression(self, ctx:pocketsParser.ExpressionContext):
        pass

    # Exit a parse tree produced by pocketsParser#expression.
    def exitExpression(self, ctx:pocketsParser.ExpressionContext):
        pass


    # Enter a parse tree produced by pocketsParser#identifier.
    def enterIdentifier(self, ctx:pocketsParser.IdentifierContext):
        pass

    # Exit a parse tree produced by pocketsParser#identifier.
    def exitIdentifier(self, ctx:pocketsParser.IdentifierContext):
        pass


    # Enter a parse tree produced by pocketsParser#constant.
    def enterConstant(self, ctx:pocketsParser.ConstantContext):
        pass

    # Exit a parse tree produced by pocketsParser#constant.
    def exitConstant(self, ctx:pocketsParser.ConstantContext):
        pass


    # Enter a parse tree produced by pocketsParser#fileIdentifier.
    def enterFileIdentifier(self, ctx:pocketsParser.FileIdentifierContext):
        pass

    # Exit a parse tree produced by pocketsParser#fileIdentifier.
    def exitFileIdentifier(self, ctx:pocketsParser.FileIdentifierContext):
        pass



del pocketsParser