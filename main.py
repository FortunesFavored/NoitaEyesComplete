import sys
sys.dont_write_bytecode = True

from worldEyes import worldEyes as WE
from sourceEyes import sourceEyes as SE

y = SE.SourceEyes()
print(y.rawMsg1, '\n')
x = WE.WorldEyes()

print(x.getNumericMsg(x.msg1), '\n')
print(x.getInvertedNumericMsg(x.msg1))