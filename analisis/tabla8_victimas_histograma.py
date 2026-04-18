"""
Tabla 8 - Víctimas y Daños
Columnas: NKILL, NWOUND, NKILLTER, PROPVALUE, ISHOSTKID, NHOSTKID, RANSOM
Gráfico: Histograma - Distribución de víctimas mortales y heridos + análisis de daños
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import warnings
warnings.filterwarnings('ignore')

cols = ['PROPVALUE', 'ISHOSTKID', 'NHOSTKID', 'RANSOM', 'PROPERTY']
df = pd.read_excel('../GTD_5156.xlsx', usecols=cols)

fig = plt.figure(figsize=(16, 6))
gs = gridspec.GridSpec(1, 2, figure=fig, wspace=0.35)
fig.suptitle('Tabla 8 — Víctimas, Daños Materiales y Secuestros', fontsize=15, fontweight='bold')

# Panel 3: Daños a la propiedad (torta)
ax3 = fig.add_subplot(gs[0, 0])
prop_counts = df['PROPERTY'].value_counts()
labels_prop = {1: 'Sí, hubo daños', 0: 'Sin daños', -9: 'Desconocido', 2: 'Dudoso'}
prop_labels = [labels_prop.get(k, str(k)) for k in prop_counts.index]
colores_prop = ['#E53935', '#43A047', '#9E9E9E', '#FDD835']
ax3.pie(prop_counts.values, labels=prop_labels, autopct='%1.1f%%',
        colors=colores_prop[:len(prop_counts)],
        startangle=90, wedgeprops=dict(linewidth=1.5, edgecolor='white'))
ax3.set_title('Daños a la propiedad\n(campo PROPERTY)', fontsize=11)

# Panel 4: Secuestros y rescate
ax4 = fig.add_subplot(gs[0, 1])
hostkid_si = (df['ISHOSTKID'] == 1).sum()
hostkid_no = (df['ISHOSTKID'] == 0).sum()
ransom_si = df[df['ISHOSTKID'] == 1]['RANSOM'].apply(lambda x: 1 if x == 1 else 0).sum()

stats_labels = ['Total incidentes\nc/secuestro', 'Incidentes\nsin secuestro', 'Secuestros con\npetición de rescate']
stats_vals = [hostkid_si, hostkid_no, ransom_si]
bar_colors = ['#E53935', '#43A047', '#FDD835']
bars = ax4.bar(stats_labels, stats_vals, color=bar_colors, edgecolor='white', linewidth=0.7)
for bar in bars:
    ax4.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 5,
             f'{bar.get_height():,}', ha='center', va='bottom', fontsize=10, fontweight='bold')
ax4.set_ylabel('Número de incidentes', fontsize=10)
ax4.set_title('Secuestros y rescates\n(campos ISHOSTKID, RANSOM)', fontsize=11)
ax4.grid(axis='y', linestyle='--', alpha=0.4)

plt.savefig('tabla8_victimas_histograma.png', dpi=150, bbox_inches='tight')
plt.show()
print("Guardado: tabla8_victimas_histograma.png")
