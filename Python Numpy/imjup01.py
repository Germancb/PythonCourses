import pandas as pd
datos = pd.Series([100, 200, 300], index= ["Juan", "Pedro", "Luis"])
datos.plot(ylabel="Ahorro", kind="pie")
