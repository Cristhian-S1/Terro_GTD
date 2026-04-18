"""
Tabla 1 - Identificadores y Fechas
Columnas: IYEAR, IMONTH, EXTENDED
Gráfico: Línea - Evolución de ataques por año y ataques extendidos
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import warnings
warnings.filterwarnings('ignore')

df = pd.read_excel('../GTD_5156.xlsx', usecols=['IYEAR', 'IMONTH', 'IDAY', 'EXTENDED'])

# Ataques por año (total)
ataques_anio = df.groupby('IYEAR').size().reset_index(name='total')

# Ataques extendidos por año
extendidos = df[df['EXTENDED'] == 1].groupby('IYEAR').size().reset_index(name='extendidos')

merged = ataques_anio.merge(extendidos, on='IYEAR', how='left').fillna(0)
merged['pct_extendidos'] = (merged['extendidos'] / merged['total'] * 100).round(2)

fig, ax = plt.subplots(figsize=(14, 6))
fig.suptitle('Tabla 1 — Evolución Temporal de Ataques Terroristas', fontsize=15, fontweight='bold', y=0.98)

# Panel superior: total de ataques por año
ax.plot(merged['IYEAR'], merged['total'], color='#2196F3', linewidth=2.2, marker='o', markersize=5)
ax.fill_between(merged['IYEAR'], merged['total'], alpha=0.15, color='#2196F3')
ax.set_ylabel('Total de ataques', fontsize=11)
ax.set_xlabel('Año', fontsize=11)
ax.set_title('Total de incidentes por año', fontsize=12)
ax.yaxis.set_major_locator(ticker.MaxNLocator(integer=True))
ax.grid(axis='y', linestyle='--', alpha=0.5)
for x, y in zip(merged['IYEAR'], merged['total']):
    ax.annotate(str(y), (x, y), textcoords='offset points', xytext=(0, 6), ha='center', fontsize=8)

plt.tight_layout()
plt.savefig('tabla1_fechas_linea.png', dpi=150, bbox_inches='tight')
plt.show()
print("Guardado: tabla1_fechas_linea.png")
