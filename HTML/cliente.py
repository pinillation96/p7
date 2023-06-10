from antlr4 import *
from antlr.HTMLParserListener import HTMLParserListener
from antlr.HTMLLexer import HTMLLexer
from antlr.HTMLParser import HTMLParser
import sys


class TreePrinter(HTMLParserListener):

  def enterATag(self, ctx:HTMLParser.ATagContext):
        for i in range(len(ctx.htmlAttribute())):
            if ctx.htmlAttribute(i).TAG_NAME().getText() == 'href':
                print(ctx.htmlAttribute(i).ATTVALUE_VALUE().getText())

"""     def enterName(self, ctx:HTMLParser.NameContext):
        #print(ctx.TAG_NAME(0).getText())
        pass """

"""     def enterHtmlAttribute(self, ctx:HTMLParser.HtmlAttributeContext):
        if ctx.TAG_NAME().getText() == "style":
            print(ctx.ATTVALUE_VALUE().getText()) """

def main(argv):
    parser = HTMLParser(CommonTokenStream(HTMLLexer(FileStream("test.html"))))
    tree = parser.htmlDocument()

    print(tree)

    walker = ParseTreeWalker()
    walker.walk(TreePrinter(), tree)


if __name__ == '__main__':
    main("test.html")
