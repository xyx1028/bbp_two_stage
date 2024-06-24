import matplotlib.pyplot as plt
import numpy as np

# 算法名称
algorithm_names = [
    "MB-WFD", "FFD", "BFD", "1-67-IC-BFD–MB-WFD", "1-67-IC-BFD–MB-FFD", "1-75-IC-BFD–MB-FFD",
    "1-75-IC-BFD–MB-WFD", "1-75-MB-WFD–MB-FFD", "1-100-MB-WFD–MB-FFD", "2-50-MB-FFD–MB-WFD",
    "2-50-MB-FFD–IC-BFD", "2-67-MB-WFD–IC-FFD", "2-67-MB-FFD–IC-FFD", "2-75-MB-FFD–BC",
    "2-50-MB-FFD–BC", "1-67-MB-FFD–BC", "1-75-IC-FFD-IC-BFD", "2-50-IC-FFD-IC-BFD", "2-67-IC-FFD-IC-BFD"
]


# 从文件中读取数据
dynamic_data = {
    'algorithm': algorithm_names,
    'deviation': [11.02, 11.02, 11.02, 11.02, 11.02, 11.02, 11.02, 11.02, 11.02, 12.24, 11.02, 11.02, 11.02, 11.02, 11.02, 11.02, 11.02, 11.02, 11.02],
    'time': [0.004640, 0.004420, 0.004470, 0.004651, 0.005265, 0.004655, 0.004586, 0.005578, 0.004930, 0.004935, 0.004570, 0.005294, 0.004884, 0.004793, 0.004214, 0.004770, 0.004769, 0.004942, 0.005141]
}

fixed_data = {
    'algorithm': algorithm_names,
    'deviation': [11.02, 11.02, 11.02, 11.05, 11.02, 11.02, 11.02, 11.02, 11.02, 11.02, 11.02, 11.02, 11.02, 11.02, 11.02, 11.02, 11.02, 11.02, 11.02],
    'time': [0.004640, 0.004420, 0.004470, 0.004651, 0.005265, 0.004655, 0.004586, 0.005578, 0.004930, 0.004935, 0.004570, 0.005294, 0.004884, 0.004793, 0.004214, 0.004770, 0.004769, 0.004942, 0.005141]
}


plt.figure(figsize=(12, 6))

# 绘制deviation对比图
plt.subplot(1, 2, 1)
plt.plot(algorithm_names, dynamic_data['deviation'], marker='o', label='Dynamic Threshold')
plt.plot(algorithm_names, fixed_data['deviation'], marker='s', label='Fixed Threshold')
plt.xticks(rotation=90)
plt.xlabel('Algorithm')
plt.ylabel('Deviation (%)')
plt.title('Deviation Comparison for 501 Items in Dataset T')
plt.legend()

# 绘制time对比图
plt.subplot(1, 2, 2)
plt.plot(algorithm_names, dynamic_data['time'], marker='o', label='Dynamic Threshold')
plt.plot(algorithm_names, fixed_data['time'], marker='s', label='Fixed Threshold')
plt.xticks(rotation=90)
plt.xlabel('Algorithm')
plt.ylabel('Time (sec)')
plt.title('Time Comparison for 501 Items in Dataset T')
plt.legend()

plt.tight_layout()
plt.show()

