"""
Tabla 5 - Armamento
Columnas: WEAPTYPE1_TXT, WEAPSUBTYPE1_TXT, WEAPTYPE2_TXT
Gráfico: Barras horizontales - Tipos y subtipos de armas más usadas
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import warnings
warnings.filterwarnings('ignore')

cols = ['WEAPTYPE1_TXT', 'WEAPSUBTYPE1_TXT', 'WEAPTYPE2_TXT']
df = pd.read_excel('../GTD_5156.xlsx', usecols=cols)
df['WEAPTYPE1_TXT'] = df['WEAPTYPE1_TXT'].fillna('Desconocido')
df['WEAPSUBTYPE1_TXT'] = df['WEAPSUBTYPE1_TXT'].fillna('No especificado')

# Conteo de tipo de arma principal
tipo_conteo = df['WEAPTYPE1_TXT'].value_counts()

# Top subtipos del arma más usada
arma_principal = tipo_conteo.index[0]
sub_conteo = df[df['WEAPTYPE1_TXT'] == arma_principal]['WEAPSUBTYPE1_TXT'].value_counts().head(8)

fig, ax = plt.subplots(figsize=(10, 8))
fig.suptitle('Tabla 5 — Armamento Utilizado en Ataques Terroristas', fontsize=15, fontweight='bold')

# Tipos de arma principal
colores_tipo = cm.RdYlBu_r(np.linspace(0.15, 0.85, len(tipo_conteo)))
bars = ax.barh(tipo_conteo.index[::-1], tipo_conteo.values[::-1],
               color=colores_tipo, edgecolor='white', linewidth=0.5)
ax.set_xlabel('Número de incidentes', fontsize=11)
ax.set_title('Frecuencia por tipo de arma principal', fontsize=12)
ax.grid(axis='x', linestyle='--', alpha=0.4)
for bar, val in zip(bars, tipo_conteo.values[::-1]):
    ax.text(bar.get_width() + 5, bar.get_y() + bar.get_height()/2,
            f'{val:,}', va='center', fontsize=9)
ax.set_xlim(0, tipo_conteo.max() * 1.15)

plt.tight_layout()
plt.savefig('tabla5_armas_barras.png', dpi=150, bbox_inches='tight')
plt.show()
print("Guardado: tabla5_armas_barras.png")
