# Generated from main/MiniGo.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3D")
        buf.write("\u0289\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3s\n\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3~\n\3\5\3\u0080\n")
        buf.write("\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\5\5\u0094\n\5\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\7\3\7\3\7\5\7\u00a1\n\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\5\7\u00aa\n\7\3\7\3\7\5\7\u00ae\n\7\3\b\3")
        buf.write("\b\3\b\3\b\5\b\u00b4\n\b\3\b\3\b\5\b\u00b8\n\b\3\b\3\b")
        buf.write("\3\t\3\t\3\t\3\t\3\t\5\t\u00c1\n\t\3\n\3\n\3\n\3\13\3")
        buf.write("\13\3\13\3\13\5\13\u00ca\n\13\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\5\f\u00d2\n\f\3\f\3\f\5\f\u00d6\n\f\3\f\3\f\3\r\3\r\3")
        buf.write("\r\3\r\3\r\3\r\5\r\u00e0\n\r\3\r\3\r\5\r\u00e4\n\r\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\20")
        buf.write("\3\20\3\20\3\20\5\20\u00f5\n\20\3\20\3\20\3\20\3\20\3")
        buf.write("\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\5\21\u0104")
        buf.write("\n\21\3\22\3\22\3\22\3\22\3\22\3\22\5\22\u010c\n\22\3")
        buf.write("\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\5\22\u0117")
        buf.write("\n\22\3\22\3\22\3\22\3\22\5\22\u011d\n\22\3\23\3\23\3")
        buf.write("\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\5\24\u012d\n\24\7\24\u012f\n\24\f\24\16\24\u0132")
        buf.write("\13\24\3\25\3\25\3\25\3\25\5\25\u0138\n\25\3\26\3\26\3")
        buf.write("\26\3\26\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\5\30\u014b\n\30\3\30\3\30\3\30\3")
        buf.write("\30\3\30\3\30\5\30\u0153\n\30\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\5\31\u0169\n\31\3\32\3\32\3\32\3")
        buf.write("\32\3\32\3\32\3\33\3\33\3\33\5\33\u0174\n\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\5\35\u0191\n\35\3\36\3\36\3\36\3\36\3")
        buf.write("\36\3\36\3\36\5\36\u019a\n\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3\37\5\37\u01a8\n\37\3")
        buf.write(" \3 \3 \3 \5 \u01ae\n \3 \3 \3!\3!\3!\3!\3!\3!\3!\3!\3")
        buf.write("!\5!\u01bb\n!\3\"\3\"\3\"\3#\3#\3#\3$\3$\3$\3$\3$\3$\3")
        buf.write("$\3$\5$\u01cb\n$\3%\3%\3%\3%\3&\3&\3&\3&\3&\3&\3&\3&\3")
        buf.write("&\3&\3&\3&\5&\u01dd\n&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3")
        buf.write("&\3&\3&\3&\5&\u01ed\n&\5&\u01ef\n&\3\'\3\'\3\'\3\'\3\'")
        buf.write("\3\'\5\'\u01f7\n\'\3(\3(\3(\3(\5(\u01fd\n(\3(\3(\3)\3")
        buf.write(")\3)\3)\3)\3)\3)\3)\3)\3)\5)\u020b\n)\3*\3*\3*\3*\3*\3")
        buf.write("*\7*\u0213\n*\f*\16*\u0216\13*\3+\3+\3+\3+\3+\3+\7+\u021e")
        buf.write("\n+\f+\16+\u0221\13+\3,\3,\3,\3,\3,\3,\7,\u0229\n,\f,")
        buf.write("\16,\u022c\13,\3-\3-\3-\3-\3-\3-\7-\u0234\n-\f-\16-\u0237")
        buf.write("\13-\3.\3.\3.\3.\3.\3.\7.\u023f\n.\f.\16.\u0242\13.\3")
        buf.write("/\3/\3/\5/\u0247\n/\3\60\3\60\3\60\3\60\3\60\3\60\3\60")
        buf.write("\5\60\u0250\n\60\3\60\3\60\3\60\3\60\5\60\u0256\n\60\7")
        buf.write("\60\u0258\n\60\f\60\16\60\u025b\13\60\3\61\3\61\3\61\3")
        buf.write("\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61")
        buf.write("\3\61\3\61\3\61\5\61\u026e\n\61\3\62\3\62\3\62\3\62\3")
        buf.write("\62\3\62\5\62\u0276\n\62\3\62\3\62\3\63\3\63\3\63\3\63")
        buf.write("\5\63\u027e\n\63\3\63\3\63\3\64\3\64\3\64\3\64\3\64\5")
        buf.write("\64\u0287\n\64\3\64\2\t&RTVXZ^\65\2\4\6\b\n\f\16\20\22")
        buf.write("\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPR")
        buf.write("TVXZ\\^`bdf\2\b\5\2\30\30\36\36!%\4\2\66\668;\3\2\32\37")
        buf.write("\3\2)*\3\2+-\4\2((**\2\u02c2\2h\3\2\2\2\4\177\3\2\2\2")
        buf.write("\6\u0081\3\2\2\2\b\u0093\3\2\2\2\n\u0095\3\2\2\2\f\u00ad")
        buf.write("\3\2\2\2\16\u00af\3\2\2\2\20\u00c0\3\2\2\2\22\u00c2\3")
        buf.write("\2\2\2\24\u00c9\3\2\2\2\26\u00cb\3\2\2\2\30\u00d9\3\2")
        buf.write("\2\2\32\u00e5\3\2\2\2\34\u00eb\3\2\2\2\36\u00f0\3\2\2")
        buf.write("\2 \u0103\3\2\2\2\"\u011c\3\2\2\2$\u011e\3\2\2\2&\u0122")
        buf.write("\3\2\2\2(\u0137\3\2\2\2*\u0139\3\2\2\2,\u013d\3\2\2\2")
        buf.write(".\u0141\3\2\2\2\60\u0168\3\2\2\2\62\u016a\3\2\2\2\64\u0170")
        buf.write("\3\2\2\2\66\u017d\3\2\2\28\u0188\3\2\2\2:\u0192\3\2\2")
        buf.write("\2<\u01a7\3\2\2\2>\u01a9\3\2\2\2@\u01ba\3\2\2\2B\u01bc")
        buf.write("\3\2\2\2D\u01bf\3\2\2\2F\u01ca\3\2\2\2H\u01cc\3\2\2\2")
        buf.write("J\u01ee\3\2\2\2L\u01f6\3\2\2\2N\u01f8\3\2\2\2P\u020a\3")
        buf.write("\2\2\2R\u020c\3\2\2\2T\u0217\3\2\2\2V\u0222\3\2\2\2X\u022d")
        buf.write("\3\2\2\2Z\u0238\3\2\2\2\\\u0246\3\2\2\2^\u0248\3\2\2\2")
        buf.write("`\u026d\3\2\2\2b\u026f\3\2\2\2d\u0279\3\2\2\2f\u0286\3")
        buf.write("\2\2\2hi\5\4\3\2ij\7\2\2\3j\3\3\2\2\2ks\5B\"\2ls\5\26")
        buf.write("\f\2ms\5\32\16\2ns\5\36\20\2os\5\6\4\2ps\5\n\6\2qs\5:")
        buf.write("\36\2rk\3\2\2\2rl\3\2\2\2rm\3\2\2\2rn\3\2\2\2ro\3\2\2")
        buf.write("\2rp\3\2\2\2rq\3\2\2\2st\3\2\2\2tu\5\4\3\2u\u0080\3\2")
        buf.write("\2\2v~\5B\"\2w~\5\26\f\2x~\5\32\16\2y~\5\36\20\2z~\5\6")
        buf.write("\4\2{~\5\n\6\2|~\5:\36\2}v\3\2\2\2}w\3\2\2\2}x\3\2\2\2")
        buf.write("}y\3\2\2\2}z\3\2\2\2}{\3\2\2\2}|\3\2\2\2~\u0080\3\2\2")
        buf.write("\2\177r\3\2\2\2\177}\3\2\2\2\u0080\5\3\2\2\2\u0081\u0082")
        buf.write("\7\b\2\2\u0082\u0083\7\66\2\2\u0083\u0084\7\t\2\2\u0084")
        buf.write("\u0085\7\60\2\2\u0085\u0086\5\b\5\2\u0086\u0087\7\61\2")
        buf.write("\2\u0087\u0088\7\64\2\2\u0088\7\3\2\2\2\u0089\u008a\7")
        buf.write("\66\2\2\u008a\u008b\5L\'\2\u008b\u008c\7\64\2\2\u008c")
        buf.write("\u008d\3\2\2\2\u008d\u008e\5\b\5\2\u008e\u0094\3\2\2\2")
        buf.write("\u008f\u0090\7\66\2\2\u0090\u0091\5L\'\2\u0091\u0092\7")
        buf.write("\64\2\2\u0092\u0094\3\2\2\2\u0093\u0089\3\2\2\2\u0093")
        buf.write("\u008f\3\2\2\2\u0094\t\3\2\2\2\u0095\u0096\7\b\2\2\u0096")
        buf.write("\u0097\7\66\2\2\u0097\u0098\7\n\2\2\u0098\u0099\7\60\2")
        buf.write("\2\u0099\u009a\5\f\7\2\u009a\u009b\7\61\2\2\u009b\u009c")
        buf.write("\7\64\2\2\u009c\13\3\2\2\2\u009d\u00a0\5\16\b\2\u009e")
        buf.write("\u00a1\5L\'\2\u009f\u00a1\3\2\2\2\u00a0\u009e\3\2\2\2")
        buf.write("\u00a0\u009f\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2\u00a3\7")
        buf.write("\64\2\2\u00a3\u00a4\3\2\2\2\u00a4\u00a5\5\f\7\2\u00a5")
        buf.write("\u00ae\3\2\2\2\u00a6\u00a9\5\16\b\2\u00a7\u00aa\5L\'\2")
        buf.write("\u00a8\u00aa\3\2\2\2\u00a9\u00a7\3\2\2\2\u00a9\u00a8\3")
        buf.write("\2\2\2\u00aa\u00ab\3\2\2\2\u00ab\u00ac\7\64\2\2\u00ac")
        buf.write("\u00ae\3\2\2\2\u00ad\u009d\3\2\2\2\u00ad\u00a6\3\2\2\2")
        buf.write("\u00ae\r\3\2\2\2\u00af\u00b0\7\66\2\2\u00b0\u00b3\7.\2")
        buf.write("\2\u00b1\u00b4\5\20\t\2\u00b2\u00b4\3\2\2\2\u00b3\u00b1")
        buf.write("\3\2\2\2\u00b3\u00b2\3\2\2\2\u00b4\u00b7\3\2\2\2\u00b5")
        buf.write("\u00b8\5L\'\2\u00b6\u00b8\3\2\2\2\u00b7\u00b5\3\2\2\2")
        buf.write("\u00b7\u00b6\3\2\2\2\u00b8\u00b9\3\2\2\2\u00b9\u00ba\7")
        buf.write("/\2\2\u00ba\17\3\2\2\2\u00bb\u00bc\5\22\n\2\u00bc\u00bd")
        buf.write("\7\65\2\2\u00bd\u00be\5\20\t\2\u00be\u00c1\3\2\2\2\u00bf")
        buf.write("\u00c1\5\22\n\2\u00c0\u00bb\3\2\2\2\u00c0\u00bf\3\2\2")
        buf.write("\2\u00c1\21\3\2\2\2\u00c2\u00c3\5\24\13\2\u00c3\u00c4")
        buf.write("\5L\'\2\u00c4\23\3\2\2\2\u00c5\u00c6\7\66\2\2\u00c6\u00c7")
        buf.write("\7\65\2\2\u00c7\u00ca\5\24\13\2\u00c8\u00ca\7\66\2\2\u00c9")
        buf.write("\u00c5\3\2\2\2\u00c9\u00c8\3\2\2\2\u00ca\25\3\2\2\2\u00cb")
        buf.write("\u00cc\7\20\2\2\u00cc\u00d5\7\66\2\2\u00cd\u00d1\5L\'")
        buf.write("\2\u00ce\u00cf\7 \2\2\u00cf\u00d2\5R*\2\u00d0\u00d2\3")
        buf.write("\2\2\2\u00d1\u00ce\3\2\2\2\u00d1\u00d0\3\2\2\2\u00d2\u00d6")
        buf.write("\3\2\2\2\u00d3\u00d4\7 \2\2\u00d4\u00d6\5R*\2\u00d5\u00cd")
        buf.write("\3\2\2\2\u00d5\u00d3\3\2\2\2\u00d6\u00d7\3\2\2\2\u00d7")
        buf.write("\u00d8\7\64\2\2\u00d8\27\3\2\2\2\u00d9\u00da\7\20\2\2")
        buf.write("\u00da\u00e3\7\66\2\2\u00db\u00df\5L\'\2\u00dc\u00dd\7")
        buf.write(" \2\2\u00dd\u00e0\5R*\2\u00de\u00e0\3\2\2\2\u00df\u00dc")
        buf.write("\3\2\2\2\u00df\u00de\3\2\2\2\u00e0\u00e4\3\2\2\2\u00e1")
        buf.write("\u00e2\7 \2\2\u00e2\u00e4\5R*\2\u00e3\u00db\3\2\2\2\u00e3")
        buf.write("\u00e1\3\2\2\2\u00e4\31\3\2\2\2\u00e5\u00e6\7\17\2\2\u00e6")
        buf.write("\u00e7\7\66\2\2\u00e7\u00e8\7 \2\2\u00e8\u00e9\5R*\2\u00e9")
        buf.write("\u00ea\7\64\2\2\u00ea\33\3\2\2\2\u00eb\u00ec\7\17\2\2")
        buf.write("\u00ec\u00ed\7\66\2\2\u00ed\u00ee\7 \2\2\u00ee\u00ef\5")
        buf.write("R*\2\u00ef\35\3\2\2\2\u00f0\u00f1\7\7\2\2\u00f1\u00f4")
        buf.write("\5> \2\u00f2\u00f5\5L\'\2\u00f3\u00f5\3\2\2\2\u00f4\u00f2")
        buf.write("\3\2\2\2\u00f4\u00f3\3\2\2\2\u00f5\u00f6\3\2\2\2\u00f6")
        buf.write("\u00f7\7\60\2\2\u00f7\u00f8\5\"\22\2\u00f8\u00f9\7\61")
        buf.write("\2\2\u00f9\u00fa\7\64\2\2\u00fa\37\3\2\2\2\u00fb\u00fc")
        buf.write("\7\66\2\2\u00fc\u00fd\5L\'\2\u00fd\u00fe\3\2\2\2\u00fe")
        buf.write("\u00ff\7\65\2\2\u00ff\u0100\5 \21\2\u0100\u0104\3\2\2")
        buf.write("\2\u0101\u0102\7\66\2\2\u0102\u0104\5L\'\2\u0103\u00fb")
        buf.write("\3\2\2\2\u0103\u0101\3\2\2\2\u0104!\3\2\2\2\u0105\u0117")
        buf.write("\5$\23\2\u0106\u0117\5.\30\2\u0107\u010b\7\6\2\2\u0108")
        buf.write("\u010c\5d\63\2\u0109\u010c\5R*\2\u010a\u010c\3\2\2\2\u010b")
        buf.write("\u0108\3\2\2\2\u010b\u0109\3\2\2\2\u010b\u010a\3\2\2\2")
        buf.write("\u010c\u0117\3\2\2\2\u010d\u0117\5\30\r\2\u010e\u0117")
        buf.write("\5\34\17\2\u010f\u0117\5\62\32\2\u0110\u0117\5\64\33\2")
        buf.write("\u0111\u0117\5\66\34\2\u0112\u0117\5d\63\2\u0113\u0117")
        buf.write("\5b\62\2\u0114\u0117\7\22\2\2\u0115\u0117\7\21\2\2\u0116")
        buf.write("\u0105\3\2\2\2\u0116\u0106\3\2\2\2\u0116\u0107\3\2\2\2")
        buf.write("\u0116\u010d\3\2\2\2\u0116\u010e\3\2\2\2\u0116\u010f\3")
        buf.write("\2\2\2\u0116\u0110\3\2\2\2\u0116\u0111\3\2\2\2\u0116\u0112")
        buf.write("\3\2\2\2\u0116\u0113\3\2\2\2\u0116\u0114\3\2\2\2\u0116")
        buf.write("\u0115\3\2\2\2\u0117\u0118\3\2\2\2\u0118\u0119\7\64\2")
        buf.write("\2\u0119\u011a\3\2\2\2\u011a\u011d\5\"\22\2\u011b\u011d")
        buf.write("\3\2\2\2\u011c\u0116\3\2\2\2\u011c\u011b\3\2\2\2\u011d")
        buf.write("#\3\2\2\2\u011e\u011f\5&\24\2\u011f\u0120\t\2\2\2\u0120")
        buf.write("\u0121\5R*\2\u0121%\3\2\2\2\u0122\u0123\b\24\1\2\u0123")
        buf.write("\u0124\7\66\2\2\u0124\u0130\3\2\2\2\u0125\u012c\f\4\2")
        buf.write("\2\u0126\u0127\7\27\2\2\u0127\u012d\7\66\2\2\u0128\u0129")
        buf.write("\7\62\2\2\u0129\u012a\5R*\2\u012a\u012b\7\63\2\2\u012b")
        buf.write("\u012d\3\2\2\2\u012c\u0126\3\2\2\2\u012c\u0128\3\2\2\2")
        buf.write("\u012d\u012f\3\2\2\2\u012e\u0125\3\2\2\2\u012f\u0132\3")
        buf.write("\2\2\2\u0130\u012e\3\2\2\2\u0130\u0131\3\2\2\2\u0131\'")
        buf.write("\3\2\2\2\u0132\u0130\3\2\2\2\u0133\u0134\5*\26\2\u0134")
        buf.write("\u0135\5(\25\2\u0135\u0138\3\2\2\2\u0136\u0138\5*\26\2")
        buf.write("\u0137\u0133\3\2\2\2\u0137\u0136\3\2\2\2\u0138)\3\2\2")
        buf.write("\2\u0139\u013a\7\62\2\2\u013a\u013b\5R*\2\u013b\u013c")
        buf.write("\7\63\2\2\u013c+\3\2\2\2\u013d\u013e\7\66\2\2\u013e\u013f")
        buf.write("\t\2\2\2\u013f\u0140\5R*\2\u0140-\3\2\2\2\u0141\u0142")
        buf.write("\7\3\2\2\u0142\u0143\7.\2\2\u0143\u0144\5R*\2\u0144\u0145")
        buf.write("\7/\2\2\u0145\u0146\7\60\2\2\u0146\u0147\5\"\22\2\u0147")
        buf.write("\u014a\7\61\2\2\u0148\u014b\5\60\31\2\u0149\u014b\3\2")
        buf.write("\2\2\u014a\u0148\3\2\2\2\u014a\u0149\3\2\2\2\u014b\u0152")
        buf.write("\3\2\2\2\u014c\u014d\7\4\2\2\u014d\u014e\7\60\2\2\u014e")
        buf.write("\u014f\5\"\22\2\u014f\u0150\7\61\2\2\u0150\u0153\3\2\2")
        buf.write("\2\u0151\u0153\3\2\2\2\u0152\u014c\3\2\2\2\u0152\u0151")
        buf.write("\3\2\2\2\u0153/\3\2\2\2\u0154\u0155\7\4\2\2\u0155\u0156")
        buf.write("\7\3\2\2\u0156\u0157\7.\2\2\u0157\u0158\5R*\2\u0158\u0159")
        buf.write("\7/\2\2\u0159\u015a\7\60\2\2\u015a\u015b\5\"\22\2\u015b")
        buf.write("\u015c\7\61\2\2\u015c\u015d\3\2\2\2\u015d\u015e\5\60\31")
        buf.write("\2\u015e\u0169\3\2\2\2\u015f\u0160\7\4\2\2\u0160\u0161")
        buf.write("\7\3\2\2\u0161\u0162\7.\2\2\u0162\u0163\5R*\2\u0163\u0164")
        buf.write("\7/\2\2\u0164\u0165\7\60\2\2\u0165\u0166\5\"\22\2\u0166")
        buf.write("\u0167\7\61\2\2\u0167\u0169\3\2\2\2\u0168\u0154\3\2\2")
        buf.write("\2\u0168\u015f\3\2\2\2\u0169\61\3\2\2\2\u016a\u016b\7")
        buf.write("\5\2\2\u016b\u016c\5R*\2\u016c\u016d\7\60\2\2\u016d\u016e")
        buf.write("\5\"\22\2\u016e\u016f\7\61\2\2\u016f\63\3\2\2\2\u0170")
        buf.write("\u0173\7\5\2\2\u0171\u0174\5,\27\2\u0172\u0174\58\35\2")
        buf.write("\u0173\u0171\3\2\2\2\u0173\u0172\3\2\2\2\u0174\u0175\3")
        buf.write("\2\2\2\u0175\u0176\7\64\2\2\u0176\u0177\5R*\2\u0177\u0178")
        buf.write("\7\64\2\2\u0178\u0179\5,\27\2\u0179\u017a\7\60\2\2\u017a")
        buf.write("\u017b\5\"\22\2\u017b\u017c\7\61\2\2\u017c\65\3\2\2\2")
        buf.write("\u017d\u017e\7\5\2\2\u017e\u017f\7\66\2\2\u017f\u0180")
        buf.write("\7\65\2\2\u0180\u0181\7\66\2\2\u0181\u0182\7\30\2\2\u0182")
        buf.write("\u0183\7\23\2\2\u0183\u0184\5R*\2\u0184\u0185\7\60\2\2")
        buf.write("\u0185\u0186\5\"\22\2\u0186\u0187\7\61\2\2\u0187\67\3")
        buf.write("\2\2\2\u0188\u0189\7\20\2\2\u0189\u0190\7\66\2\2\u018a")
        buf.write("\u018b\5L\'\2\u018b\u018c\7 \2\2\u018c\u018d\5R*\2\u018d")
        buf.write("\u0191\3\2\2\2\u018e\u018f\7 \2\2\u018f\u0191\5R*\2\u0190")
        buf.write("\u018a\3\2\2\2\u0190\u018e\3\2\2\2\u01919\3\2\2\2\u0192")
        buf.write("\u0193\7\7\2\2\u0193\u0194\7.\2\2\u0194\u0195\5<\37\2")
        buf.write("\u0195\u0196\7/\2\2\u0196\u0199\5> \2\u0197\u019a\5L\'")
        buf.write("\2\u0198\u019a\3\2\2\2\u0199\u0197\3\2\2\2\u0199\u0198")
        buf.write("\3\2\2\2\u019a\u019b\3\2\2\2\u019b\u019c\7\60\2\2\u019c")
        buf.write("\u019d\5\"\22\2\u019d\u019e\7\61\2\2\u019e\u019f\7\64")
        buf.write("\2\2\u019f;\3\2\2\2\u01a0\u01a1\7\66\2\2\u01a1\u01a2\7")
        buf.write("\66\2\2\u01a2\u01a3\3\2\2\2\u01a3\u01a4\7\65\2\2\u01a4")
        buf.write("\u01a8\5<\37\2\u01a5\u01a6\7\66\2\2\u01a6\u01a8\7\66\2")
        buf.write("\2\u01a7\u01a0\3\2\2\2\u01a7\u01a5\3\2\2\2\u01a8=\3\2")
        buf.write("\2\2\u01a9\u01aa\7\66\2\2\u01aa\u01ad\7.\2\2\u01ab\u01ae")
        buf.write("\5@!\2\u01ac\u01ae\3\2\2\2\u01ad\u01ab\3\2\2\2\u01ad\u01ac")
        buf.write("\3\2\2\2\u01ae\u01af\3\2\2\2\u01af\u01b0\7/\2\2\u01b0")
        buf.write("?\3\2\2\2\u01b1\u01b2\5\24\13\2\u01b2\u01b3\5L\'\2\u01b3")
        buf.write("\u01b4\3\2\2\2\u01b4\u01b5\7\65\2\2\u01b5\u01b6\5@!\2")
        buf.write("\u01b6\u01bb\3\2\2\2\u01b7\u01b8\5\24\13\2\u01b8\u01b9")
        buf.write("\5L\'\2\u01b9\u01bb\3\2\2\2\u01ba\u01b1\3\2\2\2\u01ba")
        buf.write("\u01b7\3\2\2\2\u01bbA\3\2\2\2\u01bc\u01bd\5D#\2\u01bd")
        buf.write("\u01be\5H%\2\u01beC\3\2\2\2\u01bf\u01c0\5F$\2\u01c0\u01c1")
        buf.write("\5L\'\2\u01c1E\3\2\2\2\u01c2\u01c3\7\62\2\2\u01c3\u01c4")
        buf.write("\t\3\2\2\u01c4\u01c5\7\63\2\2\u01c5\u01c6\3\2\2\2\u01c6")
        buf.write("\u01cb\5F$\2\u01c7\u01c8\7\62\2\2\u01c8\u01c9\t\3\2\2")
        buf.write("\u01c9\u01cb\7\63\2\2\u01ca\u01c2\3\2\2\2\u01ca\u01c7")
        buf.write("\3\2\2\2\u01cbG\3\2\2\2\u01cc\u01cd\7\60\2\2\u01cd\u01ce")
        buf.write("\5J&\2\u01ce\u01cf\7\61\2\2\u01cfI\3\2\2\2\u01d0\u01dd")
        buf.write("\7\25\2\2\u01d1\u01dd\7\26\2\2\u01d2\u01dd\7\24\2\2\u01d3")
        buf.write("\u01dd\7\67\2\2\u01d4\u01dd\78\2\2\u01d5\u01dd\79\2\2")
        buf.write("\u01d6\u01dd\7:\2\2\u01d7\u01dd\7;\2\2\u01d8\u01dd\7<")
        buf.write("\2\2\u01d9\u01dd\5N(\2\u01da\u01dd\5H%\2\u01db\u01dd\7")
        buf.write("\66\2\2\u01dc\u01d0\3\2\2\2\u01dc\u01d1\3\2\2\2\u01dc")
        buf.write("\u01d2\3\2\2\2\u01dc\u01d3\3\2\2\2\u01dc\u01d4\3\2\2\2")
        buf.write("\u01dc\u01d5\3\2\2\2\u01dc\u01d6\3\2\2\2\u01dc\u01d7\3")
        buf.write("\2\2\2\u01dc\u01d8\3\2\2\2\u01dc\u01d9\3\2\2\2\u01dc\u01da")
        buf.write("\3\2\2\2\u01dc\u01db\3\2\2\2\u01dd\u01de\3\2\2\2\u01de")
        buf.write("\u01df\7\65\2\2\u01df\u01ef\5J&\2\u01e0\u01ed\7\25\2\2")
        buf.write("\u01e1\u01ed\7\26\2\2\u01e2\u01ed\7\24\2\2\u01e3\u01ed")
        buf.write("\7\67\2\2\u01e4\u01ed\78\2\2\u01e5\u01ed\79\2\2\u01e6")
        buf.write("\u01ed\7:\2\2\u01e7\u01ed\7;\2\2\u01e8\u01ed\7<\2\2\u01e9")
        buf.write("\u01ed\5N(\2\u01ea\u01ed\5H%\2\u01eb\u01ed\7\66\2\2\u01ec")
        buf.write("\u01e0\3\2\2\2\u01ec\u01e1\3\2\2\2\u01ec\u01e2\3\2\2\2")
        buf.write("\u01ec\u01e3\3\2\2\2\u01ec\u01e4\3\2\2\2\u01ec\u01e5\3")
        buf.write("\2\2\2\u01ec\u01e6\3\2\2\2\u01ec\u01e7\3\2\2\2\u01ec\u01e8")
        buf.write("\3\2\2\2\u01ec\u01e9\3\2\2\2\u01ec\u01ea\3\2\2\2\u01ec")
        buf.write("\u01eb\3\2\2\2\u01ed\u01ef\3\2\2\2\u01ee\u01dc\3\2\2\2")
        buf.write("\u01ee\u01ec\3\2\2\2\u01efK\3\2\2\2\u01f0\u01f7\7\66\2")
        buf.write("\2\u01f1\u01f7\7\f\2\2\u01f2\u01f7\7\r\2\2\u01f3\u01f7")
        buf.write("\7\16\2\2\u01f4\u01f7\7\13\2\2\u01f5\u01f7\5D#\2\u01f6")
        buf.write("\u01f0\3\2\2\2\u01f6\u01f1\3\2\2\2\u01f6\u01f2\3\2\2\2")
        buf.write("\u01f6\u01f3\3\2\2\2\u01f6\u01f4\3\2\2\2\u01f6\u01f5\3")
        buf.write("\2\2\2\u01f7M\3\2\2\2\u01f8\u01f9\7\66\2\2\u01f9\u01fc")
        buf.write("\7\60\2\2\u01fa\u01fd\5P)\2\u01fb\u01fd\3\2\2\2\u01fc")
        buf.write("\u01fa\3\2\2\2\u01fc\u01fb\3\2\2\2\u01fd\u01fe\3\2\2\2")
        buf.write("\u01fe\u01ff\7\61\2\2\u01ffO\3\2\2\2\u0200\u0201\7\66")
        buf.write("\2\2\u0201\u0202\7\31\2\2\u0202\u0203\5R*\2\u0203\u0204")
        buf.write("\3\2\2\2\u0204\u0205\7\65\2\2\u0205\u0206\5P)\2\u0206")
        buf.write("\u020b\3\2\2\2\u0207\u0208\7\66\2\2\u0208\u0209\7\31\2")
        buf.write("\2\u0209\u020b\5R*\2\u020a\u0200\3\2\2\2\u020a\u0207\3")
        buf.write("\2\2\2\u020bQ\3\2\2\2\u020c\u020d\b*\1\2\u020d\u020e\5")
        buf.write("T+\2\u020e\u0214\3\2\2\2\u020f\u0210\f\4\2\2\u0210\u0211")
        buf.write("\7\'\2\2\u0211\u0213\5T+\2\u0212\u020f\3\2\2\2\u0213\u0216")
        buf.write("\3\2\2\2\u0214\u0212\3\2\2\2\u0214\u0215\3\2\2\2\u0215")
        buf.write("S\3\2\2\2\u0216\u0214\3\2\2\2\u0217\u0218\b+\1\2\u0218")
        buf.write("\u0219\5V,\2\u0219\u021f\3\2\2\2\u021a\u021b\f\4\2\2\u021b")
        buf.write("\u021c\7&\2\2\u021c\u021e\5V,\2\u021d\u021a\3\2\2\2\u021e")
        buf.write("\u0221\3\2\2\2\u021f\u021d\3\2\2\2\u021f\u0220\3\2\2\2")
        buf.write("\u0220U\3\2\2\2\u0221\u021f\3\2\2\2\u0222\u0223\b,\1\2")
        buf.write("\u0223\u0224\5X-\2\u0224\u022a\3\2\2\2\u0225\u0226\f\4")
        buf.write("\2\2\u0226\u0227\t\4\2\2\u0227\u0229\5X-\2\u0228\u0225")
        buf.write("\3\2\2\2\u0229\u022c\3\2\2\2\u022a\u0228\3\2\2\2\u022a")
        buf.write("\u022b\3\2\2\2\u022bW\3\2\2\2\u022c\u022a\3\2\2\2\u022d")
        buf.write("\u022e\b-\1\2\u022e\u022f\5Z.\2\u022f\u0235\3\2\2\2\u0230")
        buf.write("\u0231\f\4\2\2\u0231\u0232\t\5\2\2\u0232\u0234\5Z.\2\u0233")
        buf.write("\u0230\3\2\2\2\u0234\u0237\3\2\2\2\u0235\u0233\3\2\2\2")
        buf.write("\u0235\u0236\3\2\2\2\u0236Y\3\2\2\2\u0237\u0235\3\2\2")
        buf.write("\2\u0238\u0239\b.\1\2\u0239\u023a\5\\/\2\u023a\u0240\3")
        buf.write("\2\2\2\u023b\u023c\f\4\2\2\u023c\u023d\t\6\2\2\u023d\u023f")
        buf.write("\5\\/\2\u023e\u023b\3\2\2\2\u023f\u0242\3\2\2\2\u0240")
        buf.write("\u023e\3\2\2\2\u0240\u0241\3\2\2\2\u0241[\3\2\2\2\u0242")
        buf.write("\u0240\3\2\2\2\u0243\u0244\t\7\2\2\u0244\u0247\5\\/\2")
        buf.write("\u0245\u0247\5^\60\2\u0246\u0243\3\2\2\2\u0246\u0245\3")
        buf.write("\2\2\2\u0247]\3\2\2\2\u0248\u0249\b\60\1\2\u0249\u024a")
        buf.write("\5`\61\2\u024a\u0259\3\2\2\2\u024b\u0255\f\4\2\2\u024c")
        buf.write("\u024f\7\27\2\2\u024d\u0250\7\66\2\2\u024e\u0250\5d\63")
        buf.write("\2\u024f\u024d\3\2\2\2\u024f\u024e\3\2\2\2\u0250\u0256")
        buf.write("\3\2\2\2\u0251\u0252\7\62\2\2\u0252\u0253\5R*\2\u0253")
        buf.write("\u0254\7\63\2\2\u0254\u0256\3\2\2\2\u0255\u024c\3\2\2")
        buf.write("\2\u0255\u0251\3\2\2\2\u0256\u0258\3\2\2\2\u0257\u024b")
        buf.write("\3\2\2\2\u0258\u025b\3\2\2\2\u0259\u0257\3\2\2\2\u0259")
        buf.write("\u025a\3\2\2\2\u025a_\3\2\2\2\u025b\u0259\3\2\2\2\u025c")
        buf.write("\u026e\7\66\2\2\u025d\u026e\78\2\2\u025e\u026e\79\2\2")
        buf.write("\u025f\u026e\7:\2\2\u0260\u026e\7;\2\2\u0261\u026e\7\67")
        buf.write("\2\2\u0262\u0263\7.\2\2\u0263\u0264\5R*\2\u0264\u0265")
        buf.write("\7/\2\2\u0265\u026e\3\2\2\2\u0266\u026e\5d\63\2\u0267")
        buf.write("\u026e\7<\2\2\u0268\u026e\5N(\2\u0269\u026e\5B\"\2\u026a")
        buf.write("\u026e\7\25\2\2\u026b\u026e\7\26\2\2\u026c\u026e\7\24")
        buf.write("\2\2\u026d\u025c\3\2\2\2\u026d\u025d\3\2\2\2\u026d\u025e")
        buf.write("\3\2\2\2\u026d\u025f\3\2\2\2\u026d\u0260\3\2\2\2\u026d")
        buf.write("\u0261\3\2\2\2\u026d\u0262\3\2\2\2\u026d\u0266\3\2\2\2")
        buf.write("\u026d\u0267\3\2\2\2\u026d\u0268\3\2\2\2\u026d\u0269\3")
        buf.write("\2\2\2\u026d\u026a\3\2\2\2\u026d\u026b\3\2\2\2\u026d\u026c")
        buf.write("\3\2\2\2\u026ea\3\2\2\2\u026f\u0270\5&\24\2\u0270\u0271")
        buf.write("\7\27\2\2\u0271\u0272\7\66\2\2\u0272\u0275\7.\2\2\u0273")
        buf.write("\u0276\5f\64\2\u0274\u0276\3\2\2\2\u0275\u0273\3\2\2\2")
        buf.write("\u0275\u0274\3\2\2\2\u0276\u0277\3\2\2\2\u0277\u0278\7")
        buf.write("/\2\2\u0278c\3\2\2\2\u0279\u027a\7\66\2\2\u027a\u027d")
        buf.write("\7.\2\2\u027b\u027e\5f\64\2\u027c\u027e\3\2\2\2\u027d")
        buf.write("\u027b\3\2\2\2\u027d\u027c\3\2\2\2\u027e\u027f\3\2\2\2")
        buf.write("\u027f\u0280\7/\2\2\u0280e\3\2\2\2\u0281\u0282\5R*\2\u0282")
        buf.write("\u0283\7\65\2\2\u0283\u0284\5f\64\2\u0284\u0287\3\2\2")
        buf.write("\2\u0285\u0287\5R*\2\u0286\u0281\3\2\2\2\u0286\u0285\3")
        buf.write("\2\2\2\u0287g\3\2\2\2\66r}\177\u0093\u00a0\u00a9\u00ad")
        buf.write("\u00b3\u00b7\u00c0\u00c9\u00d1\u00d5\u00df\u00e3\u00f4")
        buf.write("\u0103\u010b\u0116\u011c\u012c\u0130\u0137\u014a\u0152")
        buf.write("\u0168\u0173\u0190\u0199\u01a7\u01ad\u01ba\u01ca\u01dc")
        buf.write("\u01ec\u01ee\u01f6\u01fc\u020a\u0214\u021f\u022a\u0235")
        buf.write("\u0240\u0246\u024f\u0255\u0259\u026d\u0275\u027d\u0286")
        return buf.getvalue()


class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'else'", "'for'", "'return'", 
                     "'func'", "'type'", "'struct'", "'interface'", "'string'", 
                     "'int'", "'float'", "'boolean'", "'const'", "'var'", 
                     "'continue'", "'break'", "'range'", "'nil'", "'true'", 
                     "'false'", "'.'", "':='", "':'", "'<'", "'<='", "'>'", 
                     "'>='", "'=='", "'!='", "'='", "'+='", "'-='", "'*='", 
                     "'/='", "'%='", "'&&'", "'||'", "'!'", "'+'", "'-'", 
                     "'*'", "'/'", "'%'", "'('", "')'", "'{'", "'}'", "'['", 
                     "']'", "';'", "','" ]

    symbolicNames = [ "<INVALID>", "IF", "ELSE", "FOR", "RETURN", "FUNC", 
                      "TYPE", "STRUCT", "INTERFACE", "STRING", "INT", "FLOAT", 
                      "BOOLEAN", "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", 
                      "NIL", "TRUE", "FALSE", "DOT", "COLONASSIGN", "COLON", 
                      "LT", "LE", "GT", "GE", "EQ", "NE", "ASSIGN", "ADD_ASSIGN", 
                      "SUB_ASSIGN", "MUL_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", 
                      "AND", "OR", "NOT", "ADD", "SUB", "MUL", "DIV", "MOD", 
                      "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACKET", 
                      "RBRACKET", "SEMICOLON", "COMMA", "ID", "FLOAT_LIT", 
                      "INT_DEC", "INT_BIN", "INT_OCT", "INT_HEX", "STRING_LIT", 
                      "BOOLEAN_LIT", "NEWLINE", "WS", "COMMENTS", "COMMENTS_LINE", 
                      "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_list_declaration = 1
    RULE_struct_type = 2
    RULE_data_struct = 3
    RULE_interface_type = 4
    RULE_data_inter = 5
    RULE_initialize_inter = 6
    RULE_list_interface = 7
    RULE_data_inter_thamso_list = 8
    RULE_data_inter_thamso = 9
    RULE_global_variable = 10
    RULE_local_variable = 11
    RULE_global_constant = 12
    RULE_local_constant = 13
    RULE_function = 14
    RULE_data_func = 15
    RULE_body_func = 16
    RULE_assignment_func = 17
    RULE_dot = 18
    RULE_list_arr_index = 19
    RULE_arr_index = 20
    RULE_assignment_for = 21
    RULE_if_else = 22
    RULE_else_if = 23
    RULE_for_basic = 24
    RULE_for_icu = 25
    RULE_for_range = 26
    RULE_var_for = 27
    RULE_struct_func = 28
    RULE_method = 29
    RULE_func_call_str = 30
    RULE_func_call_thamso_str = 31
    RULE_array_literal = 32
    RULE_type_array = 33
    RULE_list_type_arr = 34
    RULE_list_expr = 35
    RULE_data_list_expr = 36
    RULE_type_data = 37
    RULE_struct_literal = 38
    RULE_list_elements = 39
    RULE_expr = 40
    RULE_expr1 = 41
    RULE_expr2 = 42
    RULE_expr3 = 43
    RULE_expr4 = 44
    RULE_expr5 = 45
    RULE_expr6 = 46
    RULE_expr7 = 47
    RULE_call_statement = 48
    RULE_func_call = 49
    RULE_func_call_thamso = 50

    ruleNames =  [ "program", "list_declaration", "struct_type", "data_struct", 
                   "interface_type", "data_inter", "initialize_inter", "list_interface", 
                   "data_inter_thamso_list", "data_inter_thamso", "global_variable", 
                   "local_variable", "global_constant", "local_constant", 
                   "function", "data_func", "body_func", "assignment_func", 
                   "dot", "list_arr_index", "arr_index", "assignment_for", 
                   "if_else", "else_if", "for_basic", "for_icu", "for_range", 
                   "var_for", "struct_func", "method", "func_call_str", 
                   "func_call_thamso_str", "array_literal", "type_array", 
                   "list_type_arr", "list_expr", "data_list_expr", "type_data", 
                   "struct_literal", "list_elements", "expr", "expr1", "expr2", 
                   "expr3", "expr4", "expr5", "expr6", "expr7", "call_statement", 
                   "func_call", "func_call_thamso" ]

    EOF = Token.EOF
    IF=1
    ELSE=2
    FOR=3
    RETURN=4
    FUNC=5
    TYPE=6
    STRUCT=7
    INTERFACE=8
    STRING=9
    INT=10
    FLOAT=11
    BOOLEAN=12
    CONST=13
    VAR=14
    CONTINUE=15
    BREAK=16
    RANGE=17
    NIL=18
    TRUE=19
    FALSE=20
    DOT=21
    COLONASSIGN=22
    COLON=23
    LT=24
    LE=25
    GT=26
    GE=27
    EQ=28
    NE=29
    ASSIGN=30
    ADD_ASSIGN=31
    SUB_ASSIGN=32
    MUL_ASSIGN=33
    DIV_ASSIGN=34
    MOD_ASSIGN=35
    AND=36
    OR=37
    NOT=38
    ADD=39
    SUB=40
    MUL=41
    DIV=42
    MOD=43
    LPAREN=44
    RPAREN=45
    LBRACE=46
    RBRACE=47
    LBRACKET=48
    RBRACKET=49
    SEMICOLON=50
    COMMA=51
    ID=52
    FLOAT_LIT=53
    INT_DEC=54
    INT_BIN=55
    INT_OCT=56
    INT_HEX=57
    STRING_LIT=58
    BOOLEAN_LIT=59
    NEWLINE=60
    WS=61
    COMMENTS=62
    COMMENTS_LINE=63
    ERROR_CHAR=64
    UNCLOSE_STRING=65
    ILLEGAL_ESCAPE=66

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_declaration(self):
            return self.getTypedRuleContext(MiniGoParser.List_declarationContext,0)


        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniGoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.list_declaration()
            self.state = 103
            self.match(MiniGoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_declaration(self):
            return self.getTypedRuleContext(MiniGoParser.List_declarationContext,0)


        def array_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Array_literalContext,0)


        def global_variable(self):
            return self.getTypedRuleContext(MiniGoParser.Global_variableContext,0)


        def global_constant(self):
            return self.getTypedRuleContext(MiniGoParser.Global_constantContext,0)


        def function(self):
            return self.getTypedRuleContext(MiniGoParser.FunctionContext,0)


        def struct_type(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_typeContext,0)


        def interface_type(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_typeContext,0)


        def struct_func(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_funcContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_declaration" ):
                return visitor.visitList_declaration(self)
            else:
                return visitor.visitChildren(self)




    def list_declaration(self):

        localctx = MiniGoParser.List_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_list_declaration)
        try:
            self.state = 125
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 112
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 105
                    self.array_literal()
                    pass

                elif la_ == 2:
                    self.state = 106
                    self.global_variable()
                    pass

                elif la_ == 3:
                    self.state = 107
                    self.global_constant()
                    pass

                elif la_ == 4:
                    self.state = 108
                    self.function()
                    pass

                elif la_ == 5:
                    self.state = 109
                    self.struct_type()
                    pass

                elif la_ == 6:
                    self.state = 110
                    self.interface_type()
                    pass

                elif la_ == 7:
                    self.state = 111
                    self.struct_func()
                    pass


                self.state = 114
                self.list_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 123
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                if la_ == 1:
                    self.state = 116
                    self.array_literal()
                    pass

                elif la_ == 2:
                    self.state = 117
                    self.global_variable()
                    pass

                elif la_ == 3:
                    self.state = 118
                    self.global_constant()
                    pass

                elif la_ == 4:
                    self.state = 119
                    self.function()
                    pass

                elif la_ == 5:
                    self.state = 120
                    self.struct_type()
                    pass

                elif la_ == 6:
                    self.state = 121
                    self.interface_type()
                    pass

                elif la_ == 7:
                    self.state = 122
                    self.struct_func()
                    pass


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def STRUCT(self):
            return self.getToken(MiniGoParser.STRUCT, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def data_struct(self):
            return self.getTypedRuleContext(MiniGoParser.Data_structContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_type" ):
                return visitor.visitStruct_type(self)
            else:
                return visitor.visitChildren(self)




    def struct_type(self):

        localctx = MiniGoParser.Struct_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_struct_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.match(MiniGoParser.TYPE)
            self.state = 128
            self.match(MiniGoParser.ID)
            self.state = 129
            self.match(MiniGoParser.STRUCT)
            self.state = 130
            self.match(MiniGoParser.LBRACE)
            self.state = 131
            self.data_struct()
            self.state = 132
            self.match(MiniGoParser.RBRACE)

            self.state = 133
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Data_structContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def data_struct(self):
            return self.getTypedRuleContext(MiniGoParser.Data_structContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def type_data(self):
            return self.getTypedRuleContext(MiniGoParser.Type_dataContext,0)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_data_struct

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitData_struct" ):
                return visitor.visitData_struct(self)
            else:
                return visitor.visitChildren(self)




    def data_struct(self):

        localctx = MiniGoParser.Data_structContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_data_struct)
        try:
            self.state = 145
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 135
                self.match(MiniGoParser.ID)
                self.state = 136
                self.type_data()

                self.state = 137
                self.match(MiniGoParser.SEMICOLON)
                self.state = 139
                self.data_struct()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 141
                self.match(MiniGoParser.ID)
                self.state = 142
                self.type_data()

                self.state = 143
                self.match(MiniGoParser.SEMICOLON)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def INTERFACE(self):
            return self.getToken(MiniGoParser.INTERFACE, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def data_inter(self):
            return self.getTypedRuleContext(MiniGoParser.Data_interContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_type" ):
                return visitor.visitInterface_type(self)
            else:
                return visitor.visitChildren(self)




    def interface_type(self):

        localctx = MiniGoParser.Interface_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_interface_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.match(MiniGoParser.TYPE)
            self.state = 148
            self.match(MiniGoParser.ID)
            self.state = 149
            self.match(MiniGoParser.INTERFACE)
            self.state = 150
            self.match(MiniGoParser.LBRACE)
            self.state = 151
            self.data_inter()
            self.state = 152
            self.match(MiniGoParser.RBRACE)

            self.state = 153
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Data_interContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def data_inter(self):
            return self.getTypedRuleContext(MiniGoParser.Data_interContext,0)


        def initialize_inter(self):
            return self.getTypedRuleContext(MiniGoParser.Initialize_interContext,0)


        def type_data(self):
            return self.getTypedRuleContext(MiniGoParser.Type_dataContext,0)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_data_inter

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitData_inter" ):
                return visitor.visitData_inter(self)
            else:
                return visitor.visitChildren(self)




    def data_inter(self):

        localctx = MiniGoParser.Data_interContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_data_inter)
        try:
            self.state = 171
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 155
                self.initialize_inter()
                self.state = 158
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.LBRACKET, MiniGoParser.ID]:
                    self.state = 156
                    self.type_data()
                    pass
                elif token in [MiniGoParser.SEMICOLON]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 160
                self.match(MiniGoParser.SEMICOLON)
                self.state = 162
                self.data_inter()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 164
                self.initialize_inter()
                self.state = 167
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.LBRACKET, MiniGoParser.ID]:
                    self.state = 165
                    self.type_data()
                    pass
                elif token in [MiniGoParser.SEMICOLON]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 169
                self.match(MiniGoParser.SEMICOLON)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Initialize_interContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def list_interface(self):
            return self.getTypedRuleContext(MiniGoParser.List_interfaceContext,0)


        def type_data(self):
            return self.getTypedRuleContext(MiniGoParser.Type_dataContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_initialize_inter

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitialize_inter" ):
                return visitor.visitInitialize_inter(self)
            else:
                return visitor.visitChildren(self)




    def initialize_inter(self):

        localctx = MiniGoParser.Initialize_interContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_initialize_inter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.match(MiniGoParser.ID)
            self.state = 174
            self.match(MiniGoParser.LPAREN)
            self.state = 177
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 175
                self.list_interface()
                pass

            elif la_ == 2:
                pass


            self.state = 181
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.LBRACKET, MiniGoParser.ID]:
                self.state = 179
                self.type_data()
                pass
            elif token in [MiniGoParser.RPAREN]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 183
            self.match(MiniGoParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_interfaceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def data_inter_thamso_list(self):
            return self.getTypedRuleContext(MiniGoParser.Data_inter_thamso_listContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def list_interface(self):
            return self.getTypedRuleContext(MiniGoParser.List_interfaceContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_interface

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_interface" ):
                return visitor.visitList_interface(self)
            else:
                return visitor.visitChildren(self)




    def list_interface(self):

        localctx = MiniGoParser.List_interfaceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_list_interface)
        try:
            self.state = 190
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 185
                self.data_inter_thamso_list()
                self.state = 186
                self.match(MiniGoParser.COMMA)
                self.state = 187
                self.list_interface()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 189
                self.data_inter_thamso_list()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Data_inter_thamso_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def data_inter_thamso(self):
            return self.getTypedRuleContext(MiniGoParser.Data_inter_thamsoContext,0)


        def type_data(self):
            return self.getTypedRuleContext(MiniGoParser.Type_dataContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_data_inter_thamso_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitData_inter_thamso_list" ):
                return visitor.visitData_inter_thamso_list(self)
            else:
                return visitor.visitChildren(self)




    def data_inter_thamso_list(self):

        localctx = MiniGoParser.Data_inter_thamso_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_data_inter_thamso_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.data_inter_thamso()
            self.state = 193
            self.type_data()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Data_inter_thamsoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def data_inter_thamso(self):
            return self.getTypedRuleContext(MiniGoParser.Data_inter_thamsoContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_data_inter_thamso

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitData_inter_thamso" ):
                return visitor.visitData_inter_thamso(self)
            else:
                return visitor.visitChildren(self)




    def data_inter_thamso(self):

        localctx = MiniGoParser.Data_inter_thamsoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_data_inter_thamso)
        try:
            self.state = 199
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 195
                self.match(MiniGoParser.ID)
                self.state = 196
                self.match(MiniGoParser.COMMA)
                self.state = 197
                self.data_inter_thamso()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 198
                self.match(MiniGoParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Global_variableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def type_data(self):
            return self.getTypedRuleContext(MiniGoParser.Type_dataContext,0)


        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_global_variable

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGlobal_variable" ):
                return visitor.visitGlobal_variable(self)
            else:
                return visitor.visitChildren(self)




    def global_variable(self):

        localctx = MiniGoParser.Global_variableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_global_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self.match(MiniGoParser.VAR)
            self.state = 202
            self.match(MiniGoParser.ID)
            self.state = 211
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.LBRACKET, MiniGoParser.ID]:
                self.state = 203
                self.type_data()
                self.state = 207
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.ASSIGN]:
                    self.state = 204
                    self.match(MiniGoParser.ASSIGN)

                    self.state = 205
                    self.expr(0)
                    pass
                elif token in [MiniGoParser.SEMICOLON]:
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            elif token in [MiniGoParser.ASSIGN]:
                self.state = 209
                self.match(MiniGoParser.ASSIGN)

                self.state = 210
                self.expr(0)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 213
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Local_variableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def type_data(self):
            return self.getTypedRuleContext(MiniGoParser.Type_dataContext,0)


        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_local_variable

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLocal_variable" ):
                return visitor.visitLocal_variable(self)
            else:
                return visitor.visitChildren(self)




    def local_variable(self):

        localctx = MiniGoParser.Local_variableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_local_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            self.match(MiniGoParser.VAR)
            self.state = 216
            self.match(MiniGoParser.ID)
            self.state = 225
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.LBRACKET, MiniGoParser.ID]:
                self.state = 217
                self.type_data()
                self.state = 221
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.ASSIGN]:
                    self.state = 218
                    self.match(MiniGoParser.ASSIGN)

                    self.state = 219
                    self.expr(0)
                    pass
                elif token in [MiniGoParser.SEMICOLON]:
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            elif token in [MiniGoParser.ASSIGN]:
                self.state = 223
                self.match(MiniGoParser.ASSIGN)

                self.state = 224
                self.expr(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Global_constantContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(MiniGoParser.CONST, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_global_constant

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGlobal_constant" ):
                return visitor.visitGlobal_constant(self)
            else:
                return visitor.visitChildren(self)




    def global_constant(self):

        localctx = MiniGoParser.Global_constantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_global_constant)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self.match(MiniGoParser.CONST)
            self.state = 228
            self.match(MiniGoParser.ID)
            self.state = 229
            self.match(MiniGoParser.ASSIGN)

            self.state = 230
            self.expr(0)
            self.state = 231
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Local_constantContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(MiniGoParser.CONST, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_local_constant

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLocal_constant" ):
                return visitor.visitLocal_constant(self)
            else:
                return visitor.visitChildren(self)




    def local_constant(self):

        localctx = MiniGoParser.Local_constantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_local_constant)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.match(MiniGoParser.CONST)
            self.state = 234
            self.match(MiniGoParser.ID)
            self.state = 235
            self.match(MiniGoParser.ASSIGN)

            self.state = 236
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def func_call_str(self):
            return self.getTypedRuleContext(MiniGoParser.Func_call_strContext,0)


        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def body_func(self):
            return self.getTypedRuleContext(MiniGoParser.Body_funcContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def type_data(self):
            return self.getTypedRuleContext(MiniGoParser.Type_dataContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_function

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction" ):
                return visitor.visitFunction(self)
            else:
                return visitor.visitChildren(self)




    def function(self):

        localctx = MiniGoParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.match(MiniGoParser.FUNC)
            self.state = 239
            self.func_call_str()
            self.state = 242
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.LBRACKET, MiniGoParser.ID]:
                self.state = 240
                self.type_data()
                pass
            elif token in [MiniGoParser.LBRACE]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 244
            self.match(MiniGoParser.LBRACE)
            self.state = 245
            self.body_func()
            self.state = 246
            self.match(MiniGoParser.RBRACE)
            self.state = 247
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Data_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def data_func(self):
            return self.getTypedRuleContext(MiniGoParser.Data_funcContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def type_data(self):
            return self.getTypedRuleContext(MiniGoParser.Type_dataContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_data_func

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitData_func" ):
                return visitor.visitData_func(self)
            else:
                return visitor.visitChildren(self)




    def data_func(self):

        localctx = MiniGoParser.Data_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_data_func)
        try:
            self.state = 257
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 249
                self.match(MiniGoParser.ID)
                self.state = 250
                self.type_data()
                self.state = 252
                self.match(MiniGoParser.COMMA)
                self.state = 253
                self.data_func()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 255
                self.match(MiniGoParser.ID)
                self.state = 256
                self.type_data()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Body_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def body_func(self):
            return self.getTypedRuleContext(MiniGoParser.Body_funcContext,0)


        def assignment_func(self):
            return self.getTypedRuleContext(MiniGoParser.Assignment_funcContext,0)


        def if_else(self):
            return self.getTypedRuleContext(MiniGoParser.If_elseContext,0)


        def local_variable(self):
            return self.getTypedRuleContext(MiniGoParser.Local_variableContext,0)


        def local_constant(self):
            return self.getTypedRuleContext(MiniGoParser.Local_constantContext,0)


        def for_basic(self):
            return self.getTypedRuleContext(MiniGoParser.For_basicContext,0)


        def for_icu(self):
            return self.getTypedRuleContext(MiniGoParser.For_icuContext,0)


        def for_range(self):
            return self.getTypedRuleContext(MiniGoParser.For_rangeContext,0)


        def func_call(self):
            return self.getTypedRuleContext(MiniGoParser.Func_callContext,0)


        def call_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Call_statementContext,0)


        def BREAK(self):
            return self.getToken(MiniGoParser.BREAK, 0)

        def CONTINUE(self):
            return self.getToken(MiniGoParser.CONTINUE, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def RETURN(self):
            return self.getToken(MiniGoParser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_body_func

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody_func" ):
                return visitor.visitBody_func(self)
            else:
                return visitor.visitChildren(self)




    def body_func(self):

        localctx = MiniGoParser.Body_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_body_func)
        try:
            self.state = 282
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.IF, MiniGoParser.FOR, MiniGoParser.RETURN, MiniGoParser.CONST, MiniGoParser.VAR, MiniGoParser.CONTINUE, MiniGoParser.BREAK, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 276
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
                if la_ == 1:
                    self.state = 259
                    self.assignment_func()
                    pass

                elif la_ == 2:
                    self.state = 260
                    self.if_else()
                    pass

                elif la_ == 3:
                    self.state = 261
                    self.match(MiniGoParser.RETURN)
                    self.state = 265
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                    if la_ == 1:
                        self.state = 262
                        self.func_call()
                        pass

                    elif la_ == 2:
                        self.state = 263
                        self.expr(0)
                        pass

                    elif la_ == 3:
                        pass


                    pass

                elif la_ == 4:
                    self.state = 267
                    self.local_variable()
                    pass

                elif la_ == 5:
                    self.state = 268
                    self.local_constant()
                    pass

                elif la_ == 6:
                    self.state = 269
                    self.for_basic()
                    pass

                elif la_ == 7:
                    self.state = 270
                    self.for_icu()
                    pass

                elif la_ == 8:
                    self.state = 271
                    self.for_range()
                    pass

                elif la_ == 9:
                    self.state = 272
                    self.func_call()
                    pass

                elif la_ == 10:
                    self.state = 273
                    self.call_statement()
                    pass

                elif la_ == 11:
                    self.state = 274
                    self.match(MiniGoParser.BREAK)
                    pass

                elif la_ == 12:
                    self.state = 275
                    self.match(MiniGoParser.CONTINUE)
                    pass


                self.state = 278
                self.match(MiniGoParser.SEMICOLON)
                self.state = 280
                self.body_func()
                pass
            elif token in [MiniGoParser.RBRACE]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dot(self):
            return self.getTypedRuleContext(MiniGoParser.DotContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def COLONASSIGN(self):
            return self.getToken(MiniGoParser.COLONASSIGN, 0)

        def EQ(self):
            return self.getToken(MiniGoParser.EQ, 0)

        def ADD_ASSIGN(self):
            return self.getToken(MiniGoParser.ADD_ASSIGN, 0)

        def SUB_ASSIGN(self):
            return self.getToken(MiniGoParser.SUB_ASSIGN, 0)

        def MUL_ASSIGN(self):
            return self.getToken(MiniGoParser.MUL_ASSIGN, 0)

        def DIV_ASSIGN(self):
            return self.getToken(MiniGoParser.DIV_ASSIGN, 0)

        def MOD_ASSIGN(self):
            return self.getToken(MiniGoParser.MOD_ASSIGN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assignment_func

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_func" ):
                return visitor.visitAssignment_func(self)
            else:
                return visitor.visitChildren(self)




    def assignment_func(self):

        localctx = MiniGoParser.Assignment_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_assignment_func)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self.dot(0)

            self.state = 285
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.COLONASSIGN) | (1 << MiniGoParser.EQ) | (1 << MiniGoParser.ADD_ASSIGN) | (1 << MiniGoParser.SUB_ASSIGN) | (1 << MiniGoParser.MUL_ASSIGN) | (1 << MiniGoParser.DIV_ASSIGN) | (1 << MiniGoParser.MOD_ASSIGN))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 286
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DotContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def dot(self):
            return self.getTypedRuleContext(MiniGoParser.DotContext,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def LBRACKET(self):
            return self.getToken(MiniGoParser.LBRACKET, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RBRACKET(self):
            return self.getToken(MiniGoParser.RBRACKET, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_dot

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDot" ):
                return visitor.visitDot(self)
            else:
                return visitor.visitChildren(self)



    def dot(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.DotContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_dot, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289
            self.match(MiniGoParser.ID)
            self._ctx.stop = self._input.LT(-1)
            self.state = 302
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.DotContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_dot)
                    self.state = 291
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 298
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [MiniGoParser.DOT]:
                        self.state = 292
                        self.match(MiniGoParser.DOT)
                        self.state = 293
                        self.match(MiniGoParser.ID)
                        pass
                    elif token in [MiniGoParser.LBRACKET]:
                        self.state = 294
                        self.match(MiniGoParser.LBRACKET)
                        self.state = 295
                        self.expr(0)
                        self.state = 296
                        self.match(MiniGoParser.RBRACKET)
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 304
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class List_arr_indexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arr_index(self):
            return self.getTypedRuleContext(MiniGoParser.Arr_indexContext,0)


        def list_arr_index(self):
            return self.getTypedRuleContext(MiniGoParser.List_arr_indexContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_arr_index

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_arr_index" ):
                return visitor.visitList_arr_index(self)
            else:
                return visitor.visitChildren(self)




    def list_arr_index(self):

        localctx = MiniGoParser.List_arr_indexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_list_arr_index)
        try:
            self.state = 309
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 305
                self.arr_index()
                self.state = 306
                self.list_arr_index()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 308
                self.arr_index()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arr_indexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACKET(self):
            return self.getToken(MiniGoParser.LBRACKET, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RBRACKET(self):
            return self.getToken(MiniGoParser.RBRACKET, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_arr_index

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr_index" ):
                return visitor.visitArr_index(self)
            else:
                return visitor.visitChildren(self)




    def arr_index(self):

        localctx = MiniGoParser.Arr_indexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_arr_index)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 311
            self.match(MiniGoParser.LBRACKET)
            self.state = 312
            self.expr(0)
            self.state = 313
            self.match(MiniGoParser.RBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_forContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def COLONASSIGN(self):
            return self.getToken(MiniGoParser.COLONASSIGN, 0)

        def EQ(self):
            return self.getToken(MiniGoParser.EQ, 0)

        def ADD_ASSIGN(self):
            return self.getToken(MiniGoParser.ADD_ASSIGN, 0)

        def SUB_ASSIGN(self):
            return self.getToken(MiniGoParser.SUB_ASSIGN, 0)

        def MUL_ASSIGN(self):
            return self.getToken(MiniGoParser.MUL_ASSIGN, 0)

        def DIV_ASSIGN(self):
            return self.getToken(MiniGoParser.DIV_ASSIGN, 0)

        def MOD_ASSIGN(self):
            return self.getToken(MiniGoParser.MOD_ASSIGN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assignment_for

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_for" ):
                return visitor.visitAssignment_for(self)
            else:
                return visitor.visitChildren(self)




    def assignment_for(self):

        localctx = MiniGoParser.Assignment_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_assignment_for)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 315
            self.match(MiniGoParser.ID)

            self.state = 316
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.COLONASSIGN) | (1 << MiniGoParser.EQ) | (1 << MiniGoParser.ADD_ASSIGN) | (1 << MiniGoParser.SUB_ASSIGN) | (1 << MiniGoParser.MUL_ASSIGN) | (1 << MiniGoParser.DIV_ASSIGN) | (1 << MiniGoParser.MOD_ASSIGN))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 317
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_elseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def LBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.LBRACE)
            else:
                return self.getToken(MiniGoParser.LBRACE, i)

        def body_func(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Body_funcContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Body_funcContext,i)


        def RBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.RBRACE)
            else:
                return self.getToken(MiniGoParser.RBRACE, i)

        def else_if(self):
            return self.getTypedRuleContext(MiniGoParser.Else_ifContext,0)


        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_if_else

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_else" ):
                return visitor.visitIf_else(self)
            else:
                return visitor.visitChildren(self)




    def if_else(self):

        localctx = MiniGoParser.If_elseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_if_else)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            self.match(MiniGoParser.IF)
            self.state = 320
            self.match(MiniGoParser.LPAREN)
            self.state = 321
            self.expr(0)
            self.state = 322
            self.match(MiniGoParser.RPAREN)
            self.state = 323
            self.match(MiniGoParser.LBRACE)
            self.state = 324
            self.body_func()
            self.state = 325
            self.match(MiniGoParser.RBRACE)
            self.state = 328
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 326
                self.else_if()
                pass

            elif la_ == 2:
                pass


            self.state = 336
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ELSE]:
                self.state = 330
                self.match(MiniGoParser.ELSE)
                self.state = 331
                self.match(MiniGoParser.LBRACE)
                self.state = 332
                self.body_func()
                self.state = 333
                self.match(MiniGoParser.RBRACE)
                pass
            elif token in [MiniGoParser.SEMICOLON]:
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_ifContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def else_if(self):
            return self.getTypedRuleContext(MiniGoParser.Else_ifContext,0)


        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def body_func(self):
            return self.getTypedRuleContext(MiniGoParser.Body_funcContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_else_if

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_if" ):
                return visitor.visitElse_if(self)
            else:
                return visitor.visitChildren(self)




    def else_if(self):

        localctx = MiniGoParser.Else_ifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_else_if)
        try:
            self.state = 358
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 338
                self.match(MiniGoParser.ELSE)
                self.state = 339
                self.match(MiniGoParser.IF)
                self.state = 340
                self.match(MiniGoParser.LPAREN)
                self.state = 341
                self.expr(0)
                self.state = 342
                self.match(MiniGoParser.RPAREN)
                self.state = 343
                self.match(MiniGoParser.LBRACE)
                self.state = 344
                self.body_func()
                self.state = 345
                self.match(MiniGoParser.RBRACE)
                self.state = 347
                self.else_if()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 349
                self.match(MiniGoParser.ELSE)
                self.state = 350
                self.match(MiniGoParser.IF)
                self.state = 351
                self.match(MiniGoParser.LPAREN)
                self.state = 352
                self.expr(0)
                self.state = 353
                self.match(MiniGoParser.RPAREN)
                self.state = 354
                self.match(MiniGoParser.LBRACE)
                self.state = 355
                self.body_func()
                self.state = 356
                self.match(MiniGoParser.RBRACE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_basicContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def body_func(self):
            return self.getTypedRuleContext(MiniGoParser.Body_funcContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_for_basic

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_basic" ):
                return visitor.visitFor_basic(self)
            else:
                return visitor.visitChildren(self)




    def for_basic(self):

        localctx = MiniGoParser.For_basicContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_for_basic)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 360
            self.match(MiniGoParser.FOR)
            self.state = 361
            self.expr(0)
            self.state = 362
            self.match(MiniGoParser.LBRACE)
            self.state = 363
            self.body_func()
            self.state = 364
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_icuContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEMICOLON)
            else:
                return self.getToken(MiniGoParser.SEMICOLON, i)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def assignment_for(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Assignment_forContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Assignment_forContext,i)


        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def body_func(self):
            return self.getTypedRuleContext(MiniGoParser.Body_funcContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def var_for(self):
            return self.getTypedRuleContext(MiniGoParser.Var_forContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_icu

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_icu" ):
                return visitor.visitFor_icu(self)
            else:
                return visitor.visitChildren(self)




    def for_icu(self):

        localctx = MiniGoParser.For_icuContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_for_icu)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 366
            self.match(MiniGoParser.FOR)
            self.state = 369
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.state = 367
                self.assignment_for()
                pass
            elif token in [MiniGoParser.VAR]:
                self.state = 368
                self.var_for()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 371
            self.match(MiniGoParser.SEMICOLON)
            self.state = 372
            self.expr(0)
            self.state = 373
            self.match(MiniGoParser.SEMICOLON)
            self.state = 374
            self.assignment_for()
            self.state = 375
            self.match(MiniGoParser.LBRACE)
            self.state = 376
            self.body_func()
            self.state = 377
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_rangeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def COLONASSIGN(self):
            return self.getToken(MiniGoParser.COLONASSIGN, 0)

        def RANGE(self):
            return self.getToken(MiniGoParser.RANGE, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def body_func(self):
            return self.getTypedRuleContext(MiniGoParser.Body_funcContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_for_range

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_range" ):
                return visitor.visitFor_range(self)
            else:
                return visitor.visitChildren(self)




    def for_range(self):

        localctx = MiniGoParser.For_rangeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_for_range)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 379
            self.match(MiniGoParser.FOR)
            self.state = 380
            self.match(MiniGoParser.ID)
            self.state = 381
            self.match(MiniGoParser.COMMA)
            self.state = 382
            self.match(MiniGoParser.ID)
            self.state = 383
            self.match(MiniGoParser.COLONASSIGN)
            self.state = 384
            self.match(MiniGoParser.RANGE)
            self.state = 385
            self.expr(0)
            self.state = 386
            self.match(MiniGoParser.LBRACE)
            self.state = 387
            self.body_func()
            self.state = 388
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_forContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def type_data(self):
            return self.getTypedRuleContext(MiniGoParser.Type_dataContext,0)


        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_var_for

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_for" ):
                return visitor.visitVar_for(self)
            else:
                return visitor.visitChildren(self)




    def var_for(self):

        localctx = MiniGoParser.Var_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_var_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 390
            self.match(MiniGoParser.VAR)
            self.state = 391
            self.match(MiniGoParser.ID)
            self.state = 398
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.LBRACKET, MiniGoParser.ID]:
                self.state = 392
                self.type_data()

                self.state = 393
                self.match(MiniGoParser.ASSIGN)

                self.state = 394
                self.expr(0)
                pass
            elif token in [MiniGoParser.ASSIGN]:
                self.state = 396
                self.match(MiniGoParser.ASSIGN)

                self.state = 397
                self.expr(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def method(self):
            return self.getTypedRuleContext(MiniGoParser.MethodContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def func_call_str(self):
            return self.getTypedRuleContext(MiniGoParser.Func_call_strContext,0)


        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def body_func(self):
            return self.getTypedRuleContext(MiniGoParser.Body_funcContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def type_data(self):
            return self.getTypedRuleContext(MiniGoParser.Type_dataContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_func

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_func" ):
                return visitor.visitStruct_func(self)
            else:
                return visitor.visitChildren(self)




    def struct_func(self):

        localctx = MiniGoParser.Struct_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_struct_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 400
            self.match(MiniGoParser.FUNC)
            self.state = 401
            self.match(MiniGoParser.LPAREN)
            self.state = 402
            self.method()
            self.state = 403
            self.match(MiniGoParser.RPAREN)
            self.state = 404
            self.func_call_str()
            self.state = 407
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.LBRACKET, MiniGoParser.ID]:
                self.state = 405
                self.type_data()
                pass
            elif token in [MiniGoParser.LBRACE]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 409
            self.match(MiniGoParser.LBRACE)
            self.state = 410
            self.body_func()
            self.state = 411
            self.match(MiniGoParser.RBRACE)
            self.state = 412
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def method(self):
            return self.getTypedRuleContext(MiniGoParser.MethodContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod" ):
                return visitor.visitMethod(self)
            else:
                return visitor.visitChildren(self)




    def method(self):

        localctx = MiniGoParser.MethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_method)
        try:
            self.state = 421
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 414
                self.match(MiniGoParser.ID)
                self.state = 415
                self.match(MiniGoParser.ID)
                self.state = 417
                self.match(MiniGoParser.COMMA)
                self.state = 418
                self.method()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 419
                self.match(MiniGoParser.ID)
                self.state = 420
                self.match(MiniGoParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_call_strContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def func_call_thamso_str(self):
            return self.getTypedRuleContext(MiniGoParser.Func_call_thamso_strContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_func_call_str

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call_str" ):
                return visitor.visitFunc_call_str(self)
            else:
                return visitor.visitChildren(self)




    def func_call_str(self):

        localctx = MiniGoParser.Func_call_strContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_func_call_str)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 423
            self.match(MiniGoParser.ID)
            self.state = 424
            self.match(MiniGoParser.LPAREN)
            self.state = 427
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.state = 425
                self.func_call_thamso_str()
                pass
            elif token in [MiniGoParser.RPAREN]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 429
            self.match(MiniGoParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_call_thamso_strContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def func_call_thamso_str(self):
            return self.getTypedRuleContext(MiniGoParser.Func_call_thamso_strContext,0)


        def data_inter_thamso(self):
            return self.getTypedRuleContext(MiniGoParser.Data_inter_thamsoContext,0)


        def type_data(self):
            return self.getTypedRuleContext(MiniGoParser.Type_dataContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_func_call_thamso_str

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call_thamso_str" ):
                return visitor.visitFunc_call_thamso_str(self)
            else:
                return visitor.visitChildren(self)




    def func_call_thamso_str(self):

        localctx = MiniGoParser.Func_call_thamso_strContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_func_call_thamso_str)
        try:
            self.state = 440
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 431
                self.data_inter_thamso()
                self.state = 432
                self.type_data()
                self.state = 434
                self.match(MiniGoParser.COMMA)
                self.state = 435
                self.func_call_thamso_str()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 437
                self.data_inter_thamso()
                self.state = 438
                self.type_data()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_array(self):
            return self.getTypedRuleContext(MiniGoParser.Type_arrayContext,0)


        def list_expr(self):
            return self.getTypedRuleContext(MiniGoParser.List_exprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_literal" ):
                return visitor.visitArray_literal(self)
            else:
                return visitor.visitChildren(self)




    def array_literal(self):

        localctx = MiniGoParser.Array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_array_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 442
            self.type_array()
            self.state = 443
            self.list_expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_arrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_type_arr(self):
            return self.getTypedRuleContext(MiniGoParser.List_type_arrContext,0)


        def type_data(self):
            return self.getTypedRuleContext(MiniGoParser.Type_dataContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_type_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_array" ):
                return visitor.visitType_array(self)
            else:
                return visitor.visitChildren(self)




    def type_array(self):

        localctx = MiniGoParser.Type_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_type_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 445
            self.list_type_arr()

            self.state = 446
            self.type_data()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_type_arrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_type_arr(self):
            return self.getTypedRuleContext(MiniGoParser.List_type_arrContext,0)


        def LBRACKET(self):
            return self.getToken(MiniGoParser.LBRACKET, 0)

        def RBRACKET(self):
            return self.getToken(MiniGoParser.RBRACKET, 0)

        def INT_DEC(self):
            return self.getToken(MiniGoParser.INT_DEC, 0)

        def INT_BIN(self):
            return self.getToken(MiniGoParser.INT_BIN, 0)

        def INT_OCT(self):
            return self.getToken(MiniGoParser.INT_OCT, 0)

        def INT_HEX(self):
            return self.getToken(MiniGoParser.INT_HEX, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_list_type_arr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_type_arr" ):
                return visitor.visitList_type_arr(self)
            else:
                return visitor.visitChildren(self)




    def list_type_arr(self):

        localctx = MiniGoParser.List_type_arrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_list_type_arr)
        self._la = 0 # Token type
        try:
            self.state = 456
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 448
                self.match(MiniGoParser.LBRACKET)
                self.state = 449
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.ID) | (1 << MiniGoParser.INT_DEC) | (1 << MiniGoParser.INT_BIN) | (1 << MiniGoParser.INT_OCT) | (1 << MiniGoParser.INT_HEX))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 450
                self.match(MiniGoParser.RBRACKET)
                self.state = 452
                self.list_type_arr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 453
                self.match(MiniGoParser.LBRACKET)
                self.state = 454
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.ID) | (1 << MiniGoParser.INT_DEC) | (1 << MiniGoParser.INT_BIN) | (1 << MiniGoParser.INT_OCT) | (1 << MiniGoParser.INT_HEX))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 455
                self.match(MiniGoParser.RBRACKET)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def data_list_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Data_list_exprContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_list_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_expr" ):
                return visitor.visitList_expr(self)
            else:
                return visitor.visitChildren(self)




    def list_expr(self):

        localctx = MiniGoParser.List_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_list_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 458
            self.match(MiniGoParser.LBRACE)
            self.state = 459
            self.data_list_expr()
            self.state = 460
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Data_list_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def data_list_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Data_list_exprContext,0)


        def TRUE(self):
            return self.getToken(MiniGoParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(MiniGoParser.FALSE, 0)

        def NIL(self):
            return self.getToken(MiniGoParser.NIL, 0)

        def FLOAT_LIT(self):
            return self.getToken(MiniGoParser.FLOAT_LIT, 0)

        def INT_DEC(self):
            return self.getToken(MiniGoParser.INT_DEC, 0)

        def INT_BIN(self):
            return self.getToken(MiniGoParser.INT_BIN, 0)

        def INT_OCT(self):
            return self.getToken(MiniGoParser.INT_OCT, 0)

        def INT_HEX(self):
            return self.getToken(MiniGoParser.INT_HEX, 0)

        def STRING_LIT(self):
            return self.getToken(MiniGoParser.STRING_LIT, 0)

        def struct_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_literalContext,0)


        def list_expr(self):
            return self.getTypedRuleContext(MiniGoParser.List_exprContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_data_list_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitData_list_expr" ):
                return visitor.visitData_list_expr(self)
            else:
                return visitor.visitChildren(self)




    def data_list_expr(self):

        localctx = MiniGoParser.Data_list_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_data_list_expr)
        try:
            self.state = 492
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 474
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
                if la_ == 1:
                    self.state = 462
                    self.match(MiniGoParser.TRUE)
                    pass

                elif la_ == 2:
                    self.state = 463
                    self.match(MiniGoParser.FALSE)
                    pass

                elif la_ == 3:
                    self.state = 464
                    self.match(MiniGoParser.NIL)
                    pass

                elif la_ == 4:
                    self.state = 465
                    self.match(MiniGoParser.FLOAT_LIT)
                    pass

                elif la_ == 5:
                    self.state = 466
                    self.match(MiniGoParser.INT_DEC)
                    pass

                elif la_ == 6:
                    self.state = 467
                    self.match(MiniGoParser.INT_BIN)
                    pass

                elif la_ == 7:
                    self.state = 468
                    self.match(MiniGoParser.INT_OCT)
                    pass

                elif la_ == 8:
                    self.state = 469
                    self.match(MiniGoParser.INT_HEX)
                    pass

                elif la_ == 9:
                    self.state = 470
                    self.match(MiniGoParser.STRING_LIT)
                    pass

                elif la_ == 10:
                    self.state = 471
                    self.struct_literal()
                    pass

                elif la_ == 11:
                    self.state = 472
                    self.list_expr()
                    pass

                elif la_ == 12:
                    self.state = 473
                    self.match(MiniGoParser.ID)
                    pass


                self.state = 476
                self.match(MiniGoParser.COMMA)
                self.state = 477
                self.data_list_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 490
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
                if la_ == 1:
                    self.state = 478
                    self.match(MiniGoParser.TRUE)
                    pass

                elif la_ == 2:
                    self.state = 479
                    self.match(MiniGoParser.FALSE)
                    pass

                elif la_ == 3:
                    self.state = 480
                    self.match(MiniGoParser.NIL)
                    pass

                elif la_ == 4:
                    self.state = 481
                    self.match(MiniGoParser.FLOAT_LIT)
                    pass

                elif la_ == 5:
                    self.state = 482
                    self.match(MiniGoParser.INT_DEC)
                    pass

                elif la_ == 6:
                    self.state = 483
                    self.match(MiniGoParser.INT_BIN)
                    pass

                elif la_ == 7:
                    self.state = 484
                    self.match(MiniGoParser.INT_OCT)
                    pass

                elif la_ == 8:
                    self.state = 485
                    self.match(MiniGoParser.INT_HEX)
                    pass

                elif la_ == 9:
                    self.state = 486
                    self.match(MiniGoParser.STRING_LIT)
                    pass

                elif la_ == 10:
                    self.state = 487
                    self.struct_literal()
                    pass

                elif la_ == 11:
                    self.state = 488
                    self.list_expr()
                    pass

                elif la_ == 12:
                    self.state = 489
                    self.match(MiniGoParser.ID)
                    pass


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_dataContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def INT(self):
            return self.getToken(MiniGoParser.INT, 0)

        def FLOAT(self):
            return self.getToken(MiniGoParser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(MiniGoParser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(MiniGoParser.STRING, 0)

        def type_array(self):
            return self.getTypedRuleContext(MiniGoParser.Type_arrayContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_type_data

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_data" ):
                return visitor.visitType_data(self)
            else:
                return visitor.visitChildren(self)




    def type_data(self):

        localctx = MiniGoParser.Type_dataContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_type_data)
        try:
            self.state = 500
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 494
                self.match(MiniGoParser.ID)
                pass
            elif token in [MiniGoParser.INT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 495
                self.match(MiniGoParser.INT)
                pass
            elif token in [MiniGoParser.FLOAT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 496
                self.match(MiniGoParser.FLOAT)
                pass
            elif token in [MiniGoParser.BOOLEAN]:
                self.enterOuterAlt(localctx, 4)
                self.state = 497
                self.match(MiniGoParser.BOOLEAN)
                pass
            elif token in [MiniGoParser.STRING]:
                self.enterOuterAlt(localctx, 5)
                self.state = 498
                self.match(MiniGoParser.STRING)
                pass
            elif token in [MiniGoParser.LBRACKET]:
                self.enterOuterAlt(localctx, 6)
                self.state = 499
                self.type_array()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def list_elements(self):
            return self.getTypedRuleContext(MiniGoParser.List_elementsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_literal" ):
                return visitor.visitStruct_literal(self)
            else:
                return visitor.visitChildren(self)




    def struct_literal(self):

        localctx = MiniGoParser.Struct_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_struct_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 502
            self.match(MiniGoParser.ID)
            self.state = 503
            self.match(MiniGoParser.LBRACE)
            self.state = 506
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.state = 504
                self.list_elements()
                pass
            elif token in [MiniGoParser.RBRACE]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 508
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_elementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def list_elements(self):
            return self.getTypedRuleContext(MiniGoParser.List_elementsContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def COLON(self):
            return self.getToken(MiniGoParser.COLON, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_elements

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_elements" ):
                return visitor.visitList_elements(self)
            else:
                return visitor.visitChildren(self)




    def list_elements(self):

        localctx = MiniGoParser.List_elementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_list_elements)
        try:
            self.state = 520
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 510
                self.match(MiniGoParser.ID)
                self.state = 511
                self.match(MiniGoParser.COLON)
                self.state = 512
                self.expr(0)
                self.state = 514
                self.match(MiniGoParser.COMMA)
                self.state = 515
                self.list_elements()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 517
                self.match(MiniGoParser.ID)
                self.state = 518
                self.match(MiniGoParser.COLON)
                self.state = 519
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self):
            return self.getTypedRuleContext(MiniGoParser.Expr1Context,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def OR(self):
            return self.getToken(MiniGoParser.OR, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 80
        self.enterRecursionRule(localctx, 80, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 523
            self.expr1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 530
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,39,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 525
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 526
                    self.match(MiniGoParser.OR)
                    self.state = 527
                    self.expr1(0) 
                self.state = 532
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,39,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self):
            return self.getTypedRuleContext(MiniGoParser.Expr2Context,0)


        def expr1(self):
            return self.getTypedRuleContext(MiniGoParser.Expr1Context,0)


        def AND(self):
            return self.getToken(MiniGoParser.AND, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)



    def expr1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 82
        self.enterRecursionRule(localctx, 82, self.RULE_expr1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 534
            self.expr2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 541
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,40,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                    self.state = 536
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 537
                    self.match(MiniGoParser.AND)
                    self.state = 538
                    self.expr2(0) 
                self.state = 543
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,40,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(MiniGoParser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(MiniGoParser.Expr2Context,0)


        def LT(self):
            return self.getToken(MiniGoParser.LT, 0)

        def LE(self):
            return self.getToken(MiniGoParser.LE, 0)

        def GT(self):
            return self.getToken(MiniGoParser.GT, 0)

        def GE(self):
            return self.getToken(MiniGoParser.GE, 0)

        def EQ(self):
            return self.getToken(MiniGoParser.EQ, 0)

        def NE(self):
            return self.getToken(MiniGoParser.NE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 84
        self.enterRecursionRule(localctx, 84, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 545
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 552
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,41,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 547
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 548
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.LT) | (1 << MiniGoParser.LE) | (1 << MiniGoParser.GT) | (1 << MiniGoParser.GE) | (1 << MiniGoParser.EQ) | (1 << MiniGoParser.NE))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 549
                    self.expr3(0) 
                self.state = 554
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,41,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(MiniGoParser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(MiniGoParser.Expr3Context,0)


        def ADD(self):
            return self.getToken(MiniGoParser.ADD, 0)

        def SUB(self):
            return self.getToken(MiniGoParser.SUB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 86
        self.enterRecursionRule(localctx, 86, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 556
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 563
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,42,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 558
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 559
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.ADD or _la==MiniGoParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 560
                    self.expr4(0) 
                self.state = 565
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,42,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(MiniGoParser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(MiniGoParser.Expr4Context,0)


        def MUL(self):
            return self.getToken(MiniGoParser.MUL, 0)

        def DIV(self):
            return self.getToken(MiniGoParser.DIV, 0)

        def MOD(self):
            return self.getToken(MiniGoParser.MOD, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr4" ):
                return visitor.visitExpr4(self)
            else:
                return visitor.visitChildren(self)



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 88
        self.enterRecursionRule(localctx, 88, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 567
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 574
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,43,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 569
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 570
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 571
                    self.expr5() 
                self.state = 576
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,43,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(MiniGoParser.Expr5Context,0)


        def NOT(self):
            return self.getToken(MiniGoParser.NOT, 0)

        def SUB(self):
            return self.getToken(MiniGoParser.SUB, 0)

        def expr6(self):
            return self.getTypedRuleContext(MiniGoParser.Expr6Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr5" ):
                return visitor.visitExpr5(self)
            else:
                return visitor.visitChildren(self)




    def expr5(self):

        localctx = MiniGoParser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_expr5)
        self._la = 0 # Token type
        try:
            self.state = 580
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NOT, MiniGoParser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 577
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.NOT or _la==MiniGoParser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 578
                self.expr5()
                pass
            elif token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.LPAREN, MiniGoParser.LBRACKET, MiniGoParser.ID, MiniGoParser.FLOAT_LIT, MiniGoParser.INT_DEC, MiniGoParser.INT_BIN, MiniGoParser.INT_OCT, MiniGoParser.INT_HEX, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 579
                self.expr6(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr7(self):
            return self.getTypedRuleContext(MiniGoParser.Expr7Context,0)


        def expr6(self):
            return self.getTypedRuleContext(MiniGoParser.Expr6Context,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def LBRACKET(self):
            return self.getToken(MiniGoParser.LBRACKET, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RBRACKET(self):
            return self.getToken(MiniGoParser.RBRACKET, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def func_call(self):
            return self.getTypedRuleContext(MiniGoParser.Func_callContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr6" ):
                return visitor.visitExpr6(self)
            else:
                return visitor.visitChildren(self)



    def expr6(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr6Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 92
        self.enterRecursionRule(localctx, 92, self.RULE_expr6, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 583
            self.expr7()
            self._ctx.stop = self._input.LT(-1)
            self.state = 599
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,47,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr6Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                    self.state = 585
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 595
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [MiniGoParser.DOT]:
                        self.state = 586
                        self.match(MiniGoParser.DOT)
                        self.state = 589
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
                        if la_ == 1:
                            self.state = 587
                            self.match(MiniGoParser.ID)
                            pass

                        elif la_ == 2:
                            self.state = 588
                            self.func_call()
                            pass


                        pass
                    elif token in [MiniGoParser.LBRACKET]:
                        self.state = 591
                        self.match(MiniGoParser.LBRACKET)
                        self.state = 592
                        self.expr(0)
                        self.state = 593
                        self.match(MiniGoParser.RBRACKET)
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 601
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,47,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def INT_DEC(self):
            return self.getToken(MiniGoParser.INT_DEC, 0)

        def INT_BIN(self):
            return self.getToken(MiniGoParser.INT_BIN, 0)

        def INT_OCT(self):
            return self.getToken(MiniGoParser.INT_OCT, 0)

        def INT_HEX(self):
            return self.getToken(MiniGoParser.INT_HEX, 0)

        def FLOAT_LIT(self):
            return self.getToken(MiniGoParser.FLOAT_LIT, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def func_call(self):
            return self.getTypedRuleContext(MiniGoParser.Func_callContext,0)


        def STRING_LIT(self):
            return self.getToken(MiniGoParser.STRING_LIT, 0)

        def struct_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_literalContext,0)


        def array_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Array_literalContext,0)


        def TRUE(self):
            return self.getToken(MiniGoParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(MiniGoParser.FALSE, 0)

        def NIL(self):
            return self.getToken(MiniGoParser.NIL, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr7" ):
                return visitor.visitExpr7(self)
            else:
                return visitor.visitChildren(self)




    def expr7(self):

        localctx = MiniGoParser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_expr7)
        try:
            self.state = 619
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 602
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 603
                self.match(MiniGoParser.INT_DEC)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 604
                self.match(MiniGoParser.INT_BIN)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 605
                self.match(MiniGoParser.INT_OCT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 606
                self.match(MiniGoParser.INT_HEX)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 607
                self.match(MiniGoParser.FLOAT_LIT)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 608
                self.match(MiniGoParser.LPAREN)
                self.state = 609
                self.expr(0)
                self.state = 610
                self.match(MiniGoParser.RPAREN)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 612
                self.func_call()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 613
                self.match(MiniGoParser.STRING_LIT)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 614
                self.struct_literal()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 615
                self.array_literal()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 616
                self.match(MiniGoParser.TRUE)
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 617
                self.match(MiniGoParser.FALSE)
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 618
                self.match(MiniGoParser.NIL)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dot(self):
            return self.getTypedRuleContext(MiniGoParser.DotContext,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def func_call_thamso(self):
            return self.getTypedRuleContext(MiniGoParser.Func_call_thamsoContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_call_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_statement" ):
                return visitor.visitCall_statement(self)
            else:
                return visitor.visitChildren(self)




    def call_statement(self):

        localctx = MiniGoParser.Call_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_call_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 621
            self.dot(0)
            self.state = 622
            self.match(MiniGoParser.DOT)
            self.state = 623
            self.match(MiniGoParser.ID)
            self.state = 624
            self.match(MiniGoParser.LPAREN)
            self.state = 627
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.NOT, MiniGoParser.SUB, MiniGoParser.LPAREN, MiniGoParser.LBRACKET, MiniGoParser.ID, MiniGoParser.FLOAT_LIT, MiniGoParser.INT_DEC, MiniGoParser.INT_BIN, MiniGoParser.INT_OCT, MiniGoParser.INT_HEX, MiniGoParser.STRING_LIT]:
                self.state = 625
                self.func_call_thamso()
                pass
            elif token in [MiniGoParser.RPAREN]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 629
            self.match(MiniGoParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def func_call_thamso(self):
            return self.getTypedRuleContext(MiniGoParser.Func_call_thamsoContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_func_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call" ):
                return visitor.visitFunc_call(self)
            else:
                return visitor.visitChildren(self)




    def func_call(self):

        localctx = MiniGoParser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_func_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 631
            self.match(MiniGoParser.ID)
            self.state = 632
            self.match(MiniGoParser.LPAREN)
            self.state = 635
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.NOT, MiniGoParser.SUB, MiniGoParser.LPAREN, MiniGoParser.LBRACKET, MiniGoParser.ID, MiniGoParser.FLOAT_LIT, MiniGoParser.INT_DEC, MiniGoParser.INT_BIN, MiniGoParser.INT_OCT, MiniGoParser.INT_HEX, MiniGoParser.STRING_LIT]:
                self.state = 633
                self.func_call_thamso()
                pass
            elif token in [MiniGoParser.RPAREN]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 637
            self.match(MiniGoParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_call_thamsoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def func_call_thamso(self):
            return self.getTypedRuleContext(MiniGoParser.Func_call_thamsoContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_func_call_thamso

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call_thamso" ):
                return visitor.visitFunc_call_thamso(self)
            else:
                return visitor.visitChildren(self)




    def func_call_thamso(self):

        localctx = MiniGoParser.Func_call_thamsoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_func_call_thamso)
        try:
            self.state = 644
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 639
                self.expr(0)
                self.state = 640
                self.match(MiniGoParser.COMMA)
                self.state = 641
                self.func_call_thamso()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 643
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[18] = self.dot_sempred
        self._predicates[40] = self.expr_sempred
        self._predicates[41] = self.expr1_sempred
        self._predicates[42] = self.expr2_sempred
        self._predicates[43] = self.expr3_sempred
        self._predicates[44] = self.expr4_sempred
        self._predicates[46] = self.expr6_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def dot_sempred(self, localctx:DotContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr1_sempred(self, localctx:Expr1Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         

    def expr6_sempred(self, localctx:Expr6Context, predIndex:int):
            if predIndex == 6:
                return self.precpred(self._ctx, 2)
         




