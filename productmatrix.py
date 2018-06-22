from numpy import *
m=matrix(arange(12).reshape(3,4))
m_col=m.prod(0)
m_row=m.prod(1)
print("product of row and column are =\n",m_row,"\n",m_col)
