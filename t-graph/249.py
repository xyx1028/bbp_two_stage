import matplotlib.pyplot as plt

# 算法名称列表
algorithm_names = [
    "MB-WFD", "FFD", "BFD", "1-67-IC-BFD–MB-WFD", "1-67-IC-BFD–MB-FFD", "1-75-IC-BFD–MB-FFD",
    "1-75-IC-BFD–MB-WFD", "1-75-MB-WFD–MB-FFD", "1-100-MB-WFD–MB-FFD", "2-50-MB-FFD–MB-WFD",
    "2-50-MB-FFD–IC-BFD", "2-67-MB-WFD–IC-FFD", "2-67-MB-FFD–IC-FFD", "2-75-MB-FFD–BC",
    "2-50-MB-FFD–BC", "1-67-MB-FFD–BC", "1-75-IC-FFD-IC-BFD", "2-50-IC-FFD-IC-BFD", "2-67-IC-FFD-IC-BFD"
]

# 从文件中读取数据
dynamic_data = {
    'algorithm': algorithm_names,
    'deviation': [10.71, 10.71, 10.71, 10.71, 10.71, 10.71, 10.71, 10.71, 10.71, 11.14, 10.71, 10.71, 10.71, 10.71, 10.71, 10.71, 10.71, 10.71, 10.71],
    'time': [0.001365, 0.001093, 0.001268, 0.001401, 0.001192, 0.001195, 0.001311, 0.002275, 0.002191, 0.001191, 0.001266, 0.002101, 0.001292, 0.001192, 0.001266, 0.001117, 0.001341, 0.001639, 0.001443]
}

fixed_data = {
    'algorithm': algorithm_names,
    'deviation': [10.71, 10.71, 10.71, 10.71, 10.71, 10.71, 10.71, 10.71, 10.71, 11.14, 10.71, 10.71, 10.71, 10.71, 10.71, 10.71, 10.71, 10.71, 10.71],
    'time': [0.001365, 0.001093, 0.001268, 0.001401, 0.001192, 0.001195, 0.001311, 0.002275, 0.002191, 0.001191, 0.001266, 0.002101, 0.001292, 0.001192, 0.001266, 0.001117, 0.001341, 0.001639, 0.001443]
}

plt.figure(figsize=(12, 6))

# 绘制deviation对比图
plt.subplot(1, 2, 1)
plt.plot(algorithm_names, dynamic_data['deviation'], marker='o', label='Dynamic Threshold')
plt.plot(algorithm_names, fixed_data['deviation'], marker='s', label='Fixed Threshold')
plt.xticks(rotation=90)
plt.xlabel('Algorithm')
plt.ylabel('Deviation (%)')
plt.title('Deviation Comparison for 249 Items in Dataset T')
plt.legend()

# 绘制time对比图
plt.subplot(1, 2, 2)
plt.plot(algorithm_names, dynamic_data['time'], marker='o', label='Dynamic Threshold')
plt.plot(algorithm_names, fixed_data['time'], marker='s', label='Fixed Threshold')
plt.xticks(rotation=90)
plt.xlabel('Algorithm')
plt.ylabel('Time (sec)')
plt.title('Time Comparison for 249 Items in Dataset T')
plt.legend()

plt.tight_layout()
plt.show()

