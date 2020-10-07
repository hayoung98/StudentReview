# coding: utf-8
from matplotlib_venn import venn2
from matplotlib import pyplot as plt


# Venn2
set_a = set([1,False,True,False])
set_b = set([True,False,False,False])

venn2(subsets=[set_a, set_b],
      set_labels=['Set_A', 'Set_B'],
      set_colors=['red', 'blue'])

plt.show()