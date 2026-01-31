import sys
# se debe instalar matplotlib py -m install matplotlib  - pip install matplotlib desde consola
import matplotlib
# matplotlib.use('Agg')
import pandas as pd
import matplotlib.pyplot as plt
#  pd.options.display.max_rows=1000
df=pd.read_csv('data.csv')
df.plot()
plt.show()

plt.savefig(sys.stdout.buffer)
sys.stdout.flush