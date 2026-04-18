"""
Tabla 9 - Información Adicional e Internacional
Columnas: INT_LOG, INT_IDEO, INT_MISC, INT_ANY, DBSOURCE, REGION_TXT
Gráfico: Heatmap - Dimensiones internacionales por región
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

cols = ['INT_LOG', 'INT_IDEO', 'INT_MISC', 'INT_ANY', 'DBSOURCE', 'REGION_TXT']
df = pd.read_excel('../GTD_5156.xlsx', usecols=cols)
df = df.dropna(subset=['REGION_TXT'])

int_cols = ['INT_LOG', 'INT_IDEO', 'INT_MISC', 'INT_ANY']
labels_int = {
    'INT_LOG': 'Logístico\nInternacional',
    'INT_IDEO': 'Ideológico\nInternacional',
    'INT_MISC': 'Miscelánea\nInternacional',
    'INT_ANY': 'Cualquier\nDimensión',
}

# Calcular % de incidentes con dimensión internacional (==1) por región
pivot = pd.DataFrame()
for col in int_cols:
    pct = df[df[col] == 1].groupby('REGION_TXT').size() / df.groupby('REGION_TXT').size() * 100
    pivot[labels_int[col]] = pct

pivot = pivot.fillna(0)
pivot = pivot.sort_values('Cualquier\nDimensión', ascending=False)

fig, ax3 = plt.subplots(figsize=(10, 6))
fig.suptitle('Tabla 9 — Dimensiones Internacionales de Ataques Terroristas', fontsize=15, fontweight='bold')

# Gráfico de barras: distribución por fuente (DBSOURCE)
db_counts = df['DBSOURCE'].value_counts().head(8)
colores_db = plt.cm.Set2(np.linspace(0, 1, len(db_counts)))
ax3.barh(db_counts.index[::-1], db_counts.values[::-1], color=colores_db, edgecolor='white')
for i, (idx, val) in enumerate(zip(db_counts.index[::-1], db_counts.values[::-1])):
    ax3.text(val + 1, i, f'{val:,}', va='center', fontsize=9)
ax3.set_xlabel('Número de incidentes', fontsize=10)
ax3.set_title('Fuente de datos (DBSOURCE)\nTop 6', fontsize=11)
ax3.set_xlim(0, db_counts.max() * 1.18)
ax3.grid(axis='x', linestyle='--', alpha=0.4)

plt.savefig('tabla9_internacional_heatmap.png', dpi=150, bbox_inches='tight')
plt.show()
print("Guardado: tabla9_internacional_heatmap.png")
