"""
Tabla 6 - Objetivos
Columnas: TARGTYPE1_TXT, REGION_TXT, NATLTY1_TXT
Gráfico: Heatmap - Frecuencia de tipos de objetivo por región geográfica
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import warnings
warnings.filterwarnings('ignore')

cols = ['TARGTYPE1_TXT', 'REGION_TXT', 'NATLTY1_TXT']
df = pd.read_excel('../GTD_5156.xlsx', usecols=cols)
df = df.dropna(subset=['TARGTYPE1_TXT', 'REGION_TXT'])

# Top 10 tipos de objetivo
top_targ = df['TARGTYPE1_TXT'].value_counts().head(10).index
df_f = df[df['TARGTYPE1_TXT'].isin(top_targ)]

# Tabla cruzada
pivot = df_f.pivot_table(index='TARGTYPE1_TXT', columns='REGION_TXT', aggfunc='size', fill_value=0)

# Normalizar por fila (% dentro de cada tipo de objetivo)
pivot_pct = pivot.div(pivot.sum(axis=1), axis=0) * 100

fig, ax = plt.subplots(figsize=(12, 7))
fig.suptitle('Tabla 6 — Tipos de Objetivo vs Región Geográfica', fontsize=15, fontweight='bold')

# Heatmap de conteos absolutos
im1 = ax.imshow(pivot.values, cmap='YlOrRd', aspect='auto')
ax.set_xticks(range(len(pivot.columns)))
ax.set_xticklabels([c[:18] for c in pivot.columns], rotation=45, ha='right', fontsize=8)
ax.set_yticks(range(len(pivot.index)))
ax.set_yticklabels(pivot.index, fontsize=9)
ax.set_title('Conteo absoluto de ataques', fontsize=12)
plt.colorbar(im1, ax=ax, shrink=0.8, label='Nº incidentes')

for i in range(len(pivot.index)):
    for j in range(len(pivot.columns)):
        val = pivot.values[i, j]
        color = 'white' if val > pivot.values.max() * 0.6 else 'black'
        ax.text(j, i, str(val), ha='center', va='center', fontsize=7, color=color)

plt.tight_layout()
plt.savefig('tabla6_objetivos_heatmap.png', dpi=150, bbox_inches='tight')
plt.show()
print("Guardado: tabla6_objetivos_heatmap.png")
