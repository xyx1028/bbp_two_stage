import matplotlib.pyplot as plt

# 算法名称列表
algorithm_names = [
    "MB-WFD", "FFD", "BFD", "1-67-IC-BFD–MB-WFD", "1-67-IC-BFD–MB-FFD", "1-75-IC-BFD–MB-FFD",
    "1-75-IC-BFD–MB-WFD", "1-75-MB-WFD–MB-FFD", "1-100-MB-WFD–MB-FFD", "2-50-MB-FFD–MB-WFD",
    "2-50-MB-FFD–IC-BFD", "2-67-MB-WFD–IC-FFD", "2-67-MB-FFD–IC-FFD", "2-75-MB-FFD–BC",
    "2-50-MB-FFD–BC", "1-67-MB-FFD–BC", "1-75-IC-FFD-IC-BFD", "2-50-IC-FFD-IC-BFD", "2-67-IC-FFD-IC-BFD"
]

# 读取数据
dynamic_data = {
    'algorithm': algorithm_names,
    'deviation': [1.90, 1.60, 1.60, 1.90, 1.60, 1.60, 1.90, 1.60, 1.60, 2.55, 1.60, 1.60, 1.60, 1.60, 1.60, 1.60, 1.60, 1.60, 1.60],
    'time': [0.001120, 0.000993, 0.001450, 0.001340, 0.001053, 0.001024, 0.001515, 0.001039, 0.001445, 0.001158, 0.001117, 0.001600, 0.001142, 0.001142, 0.001142, 0.001067, 0.001415, 0.001143, 0.001118]
}

fixed_data = {
    'algorithm': algorithm_names,
    'deviation': [1.90, 1.60, 1.60, 1.90, 1.60, 1.60, 2.00, 1.60, 3.01, 1.60, 1.60, 1.90, 1.60, 1.60, 1.60, 1.60, 1.60, 1.60, 1.60],
    'time': [0.001120, 0.000993, 0.001450, 0.001340, 0.001053, 0.001024, 0.001515, 0.001039, 0.001445, 0.001158, 0.001117, 0.001600, 0.001142, 0.001142, 0.001142, 0.001067, 0.001415, 0.001143, 0.001118]
}

# 创建折线图
plt.figure(figsize=(12, 6))

# 绘制deviation对比图
plt.subplot(1, 2, 1)
plt.plot(algorithm_names, dynamic_data['deviation'], marker='o', label='Dynamic Threshold')
plt.plot(algorithm_names, fixed_data['deviation'], marker='s', label='Fixed Threshold')
plt.xticks(rotation=90)
plt.xlabel('Algorithm')
plt.ylabel('Deviation (%)')
plt.title('Deviation Comparison for 250 Items in Dataset U')
plt.legend()

# 绘制time对比图
plt.subplot(1, 2, 2)
plt.plot(algorithm_names, dynamic_data['time'], marker='o', label='Dynamic Threshold')
plt.plot(algorithm_names, fixed_data['time'], marker='s', label='Fixed Threshold')
plt.xticks(rotation=90)
plt.xlabel('Algorithm')
plt.ylabel('Time (sec)')
plt.title('Time Comparison for 250 Items in Dataset U')
plt.legend()

plt.tight_layout()
plt.show()
