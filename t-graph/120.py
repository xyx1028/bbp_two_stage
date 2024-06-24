import matplotlib.pyplot as plt

# 算法名称列表
algorithm_names = [
    "MB-WFD", "FFD", "BFD", "1-67-IC-BFD–MB-WFD", "1-67-IC-BFD–MB-FFD", "1-75-IC-BFD–MB-FFD",
    "1-75-IC-BFD–MB-WFD", "1-75-MB-WFD–MB-FFD", "1-100-MB-WFD–MB-FFD", "2-50-MB-FFD–MB-WFD",
    "2-50-MB-FFD–IC-BFD", "2-67-MB-WFD–IC-FFD", "2-67-MB-FFD–IC-FFD", "2-75-MB-FFD–BC",
    "2-50-MB-FFD–BC", "1-67-MB-FFD–BC", "1-75-IC-FFD-IC-BFD", "2-50-IC-FFD-IC-BFD", "2-67-IC-FFD-IC-BFD"
]

# 固定阈值的数据
fixed_data = {
    'deviation': [10.75, 10.75, 10.75, 10.43, 10.75, 10.75, 10.75, 10.75, 10.75, 10.75, 10.75, 10.75, 10.75, 10.75, 10.75, 10.75, 10.75, 10.75, 10.75],
    'time': [0.000322, 0.000273, 0.000297, 0.000350, 0.000322, 0.000369, 0.000373, 0.0000347, 0.000398, 0.000400, 0.000347, 0.000372, 0.000347, 0.000322, 0.000297, 0.000297, 0.000322, 0.000347, 0.000348]
}

# 动态阈值的数据
dynamic_data = {
    'deviation': [10.75, 10.75, 10.75, 10.75, 10.75, 10.75, 10.75, 10.75, 10.75, 10.75, 10.75, 10.75, 10.75, 10.75, 10.75, 10.75, 10.75, 10.75, 10.75],
    'time': [0.000322, 0.000273, 0.000297, 0.000350, 0.000322, 0.000369, 0.000373, 0.0000347, 0.000398, 0.000400, 0.000347, 0.000372, 0.000347, 0.000322, 0.000297, 0.000297, 0.000322, 0.000347, 0.000348]
}

plt.figure(figsize=(12, 6))

# 绘制deviation对比图
plt.subplot(1, 2, 1)
plt.plot(algorithm_names, dynamic_data['deviation'], marker='o', label='Dynamic Threshold')
plt.plot(algorithm_names, fixed_data['deviation'], marker='s', label='Fixed Threshold')
plt.xticks(rotation=90)
plt.xlabel('Algorithm')
plt.ylabel('Deviation (%)')
plt.title('Deviation Comparison for 120 Items in Dataset T')
plt.legend()

# 绘制time对比图
plt.subplot(1, 2, 2)
plt.plot(algorithm_names, dynamic_data['time'], marker='o', label='Dynamic Threshold')
plt.plot(algorithm_names, fixed_data['time'], marker='s', label='Fixed Threshold')
plt.xticks(rotation=90)
plt.xlabel('Algorithm')
plt.ylabel('Time (sec)')
plt.title('Time Comparison for 120 Items in Dataset T')
plt.legend()

plt.tight_layout()
plt.show()
