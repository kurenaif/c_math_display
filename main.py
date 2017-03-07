import matplotlib.pyplot as plt
from yacc import parser


x,y = 0.5,0.5

while True:
    s = input('> ')
    result = parser.parse(s)
    plt.tick_params(axis='x', which='both', top='off', bottom='off', labelbottom='off')
    plt.tick_params(axis='y', which='both', left='off', right='off', labelleft='off')
    plt.text(x,y,"$"+result+"$", horizontalalignment='center', fontsize=30)
    plt.show()
