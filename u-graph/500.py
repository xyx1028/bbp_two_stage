import matplotlib.pyplot as plt

# 算法名称
algorithm_names = [
    "MB-WFD", "FFD", "BFD", "1-67-IC-BFD–MB-WFD", "1-67-IC-BFD–MB-FFD", "1-75-IC-BFD–MB-FFD",
    "1-75-IC-BFD–MB-WFD", "1-75-MB-WFD–MB-FFD", "1-100-MB-WFD–MB-FFD", "2-50-MB-FFD–MB-WFD",
    "2-50-MB-FFD–IC-BFD", "2-67-MB-WFD–IC-FFD", "2-67-MB-FFD–IC-FFD", "2-75-MB-FFD–BC",
    "2-50-MB-FFD–BC", "1-67-MB-FFD–BC", "1-75-IC-FFD-IC-BFD", "2-50-IC-FFD-IC-BFD", "2-67-IC-FFD-IC-BFD"
]

# 动态阈值调整数据
dynamic_data = {
    'algorithm': algorithm_names,
    'deviation': [1.46, 1.22, 1.22, 1.46, 1.22, 1.22, 1.79, 1.27, 1.27, 1.79, 1.22, 1.44, 1.22, 1.22, 1.22, 1.22, 1.22, 1.22, 1.22],
    'time': [0.004819, 0.003501, 0.005105, 0.006046, 0.004163, 0.003875, 0.005141, 0.004633, 0.005193, 0.004249, 0.004128, 0.005250, 0.004570, 0.003874, 0.003874, 0.003611, 0.004694, 0.004347, 0.004247]
}

# 固定阈值数据
fixed_data = {
    'algorithm': algorithm_names,
    'deviation': [1.46, 1.22, 1.22, 1.46, 1.22, 1.22, 1.51, 1.22, 1.66, 1.22, 1.22, 1.46, 1.22, 1.22, 1.22, 1.22, 1.22, 1.22, 1.22],
    'time': [0.004819, 0.003501, 0.005105, 0.006046, 0.004163, 0.003875, 0.005141, 0.004633, 0.005193, 0.004249, 0.004128, 0.005250, 0.004570, 0.003874, 0.003874, 0.003611, 0.004694, 0.004347, 0.004247]
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
plt.title('Deviation Comparison for 500 Items in Dataset U')
plt.legend()

# 绘制time对比图
plt.subplot(1, 2, 2)
plt.plot(algorithm_names, dynamic_data['time'], marker='o', label='Dynamic Threshold')
plt.plot(algorithm_names, fixed_data['time'], marker='s', label='Fixed Threshold')
plt.xticks(rotation=90)
plt.xlabel('Algorithm')
plt.ylabel('Time (sec)')
plt.title('Time Comparison for 500 Items in Dataset U')
plt.legend()

plt.tight_layout()
plt.show()
