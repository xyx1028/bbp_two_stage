import pandas as pd
import matplotlib.pyplot as plt

# 算法的名字
algorithm_names = [
    "MB-WFD", "FFD", "BFD", "1-67-IC-BFD–MB-WFD", "1-67-IC-BFD–MB-FFD",
    "1-75-IC-BFD–MB-FFD", "1-75-IC-BFD–MB-WFD", "1-75-MB-WFD–MB-FFD", "1-100-MB-WFD–MB-FFD",
    "2-50-MB-FFD–MB-WFD", "2-50-MB-FFD–IC-BFD", "2-67-MB-WFD–IC-FFD", "2-67-MB-FFD–IC-FFD",
    "2-75-MB-FFD–BC", "2-50-MB-FFD–BC", "1-67-MB-FFD–BC", "1-75-IC-FFD-IC-BFD",
    "2-50-IC-FFD-IC-BFD", "2-67-IC-FFD-IC-BFD"
]

# 动态阈值的实验数据
dynamic_data = {
    'algorithm': algorithm_names,
    'deviation': [2.69, 2.08, 2.08, 2.69, 2.08, 2.08, 2.69, 2.08, 2.08, 2.69, 2.08, 2.08, 2.08, 2.08, 2.08, 2.08, 2.08, 2.08, 2.08],
    'time': [0.000322, 0.000223, 0.000298, 0.000446, 0.000329, 0.000302, 0.000442, 0.000446, 0.000369, 0.000322, 0.000298, 0.000425, 0.000298, 0.000347, 0.000297, 0.000270, 0.000347, 0.000347, 0.000322]
}

# 固定阈值的实验数据
fixed_data = {
    'algorithm': algorithm_names,
    'deviation': [2.69, 2.08, 2.08, 2.90, 2.08, 2.08, 3.01, 2.08, 6.22, 2.08, 2.08, 2.69, 2.08, 2.08, 2.08, 2.08, 2.08, 2.08, 2.08],
    'time': [0.000322, 0.000223, 0.000298, 0.000446, 0.000329, 0.000302, 0.000442, 0.000446, 0.000369, 0.000322, 0.000298, 0.000425, 0.000298, 0.000347, 0.000297, 0.000270, 0.000347, 0.000347, 0.000322]
}

# 创建 DataFrame
dynamic_df = pd.DataFrame(dynamic_data)
fixed_df = pd.DataFrame(fixed_data)

# 创建折线图
plt.figure(figsize=(12, 6))

# 绘制deviation对比图
plt.subplot(1, 2, 1)
plt.plot(algorithm_names, dynamic_data['deviation'], marker='o', label='Dynamic Threshold')
plt.plot(algorithm_names, fixed_data['deviation'], marker='s', label='Fixed Threshold')
plt.xticks(rotation=90)
plt.xlabel('Algorithm')
plt.ylabel('Deviation (%)')
plt.title('Deviation Comparison for 120 Items in Dataset U')
plt.legend()

# 绘制time对比图
plt.subplot(1, 2, 2)
plt.plot(algorithm_names, dynamic_data['time'], marker='o', label='Dynamic Threshold')
plt.plot(algorithm_names, fixed_data['time'], marker='s', label='Fixed Threshold')
plt.xticks(rotation=90)
plt.xlabel('Algorithm')
plt.ylabel('Time (sec)')
plt.title('Time Comparison for 120 Items in Dataset U')
plt.legend()

plt.tight_layout()
plt.show()