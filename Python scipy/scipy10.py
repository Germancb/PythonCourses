from scipy import stats
goles =[2, 15, 3, 8, 0, 11]
asistencias = [4, 7, 8, 6, 1, 13]
print(stats.spearmanr(goles, asistencias)[0])

