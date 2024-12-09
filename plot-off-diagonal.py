####Zhunyun Tang---2024/08/31(Utilizing chatgpt)####
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib.colors as mcolors
import os
from matplotlib.ticker import FuncFormatter

font_path = '/usr/share/fonts/Times-New-Roman/timesbd.ttf'
prop = fm.FontProperties(fname=font_path)
fm.fontManager.addfont(font_path)
plt.rcParams['font.family'] = prop.get_name()
plt.rcParams['mathtext.fontset'] = 'stix'  # Use 'stix' fontset which includes a wide range of symbols.
plt.rcParams['mathtext.rm'] = prop.get_name()  # Roman (regular) font for math
plt.rcParams['mathtext.it'] = prop.get_name()  # Italic font for math
plt.rcParams['mathtext.bf'] = prop.get_name()  # Bold font for math

print("Please select a direction:")
print("x-direction (enter 5), y-direction (enter 6), z-direction (enter 7)")
z_column = int(input("Please enter a number:"))
if z_column not in [5, 6, 7]:
    raise ValueError("Invalid input, must be 5, 6 or 7")

input_file = 'ThConductivityCohMode_fre'
output_file = 'ThConductivityCohMode_fre2'

data = np.loadtxt(input_file)

data[:, [3, 4]] = data[:, [4, 3]]
np.savetxt(output_file, data, fmt='%.5E')

data1 = np.loadtxt('ThConductivityCohMode_fre')
data2 = np.loadtxt('ThConductivityCohMode_fre2')

pi_factor = 2 * np.pi
data1[:, [3, 4]] /= pi_factor
data2[:, [3, 4]] /= pi_factor
combined_data = np.vstack([data1, data2])
np.savetxt('ThConductivityCohMode_fre-full', combined_data, fmt='%.5E')

data = np.loadtxt('ThConductivityCohMode_fre-full')
x = data[:, 3]  # 第四列
y = data[:, 4]  # 第五列
z = data[:, z_column]  # 

cmap = plt.get_cmap('rainbow')
cmap = cmap(np.linspace(0.15, 1.0, 256))  # 
cmap = mcolors.LinearSegmentedColormap.from_list('rainbow_partial', cmap)

norm = mcolors.LogNorm(vmin=1e-10, vmax=1e-6)

plt.figure(figsize=(20/2.54, 15/2.54))  # 设置图像大小宽20cm，高15cm
plt.scatter(x, y, c=z, cmap=cmap, norm=norm, s=1)  # 

cbar = plt.colorbar()
cbar.ax.set_xlabel('(W/mK)', labelpad=12, fontsize=20)
cbar.ax.xaxis.set_label_position('top')
cbar.ax.tick_params(labelsize=20)
formatter = FuncFormatter(lambda x, _: f'{x:.1f}')
plt.gca().xaxis.set_major_formatter(formatter)
plt.gca().yaxis.set_major_formatter(formatter)

plt.xlabel(r'$\omega_{\mathbf{q}j}$ (THz)', fontsize=22)  
plt.ylabel(r'$\omega_{\mathbf{q}j^\prime}$ (THz)', fontsize=22) 
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)

plt.tight_layout()
plt.savefig('ThConductivityCohMode_fre_density_plot.png', format='png', dpi=600)

#plt.show()
os.remove('ThConductivityCohMode_fre2')
os.remove('ThConductivityCohMode_fre-full')