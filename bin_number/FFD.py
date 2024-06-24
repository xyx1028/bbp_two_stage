import pandas as pd
import numpy as np
import time

# 载入数据集
def load_data(file_path):
    data = pd.read_csv(file_path, header=None)
    return data.applymap(int).values.tolist()

# 单阶段算法 FFD
def ffd(items, bin_capacity):
    bins = []
    items_sorted = sorted(items, reverse=True)  # 物品按大小降序排序

    for item in items_sorted:
        placed = False
        for bin in bins:
            if sum(bin) + item <= bin_capacity:
                bin.append(item)
                placed = True
                break
        if not placed:
            bins.append([item])

    return bins

# 运行实验
def run_experiment(file_path, bin_capacity=150):
    datasets = load_data(file_path)
    all_times = []
    all_deviation_percents = []

    for items in datasets:
        start_time = time.time()
        
        bins = ffd(items, bin_capacity)
        
        end_time = time.time()
        time_spent = end_time - start_time
        total_capacity = sum(items)
        lower_bound = np.ceil(total_capacity / bin_capacity)  # 计算KLB

        kalgebra = len(bins)  # KALG是算法所需的箱子数
        deviation_percent = ((kalgebra - lower_bound) / lower_bound) * 100 if lower_bound != 0 else 0

        all_deviation_percents.append(deviation_percent)
        all_times.append(time_spent)

    average_time_spent = np.mean(all_times)  # 计算所有处理时间的平均值
    average_deviation_percents = np.mean(all_deviation_percents)  # 计算所有偏差百分比的平均值
    return average_deviation_percents, average_time_spent

# 运行实验
file_path = 'class_u_120.csv'  # 确保路径正确
average_deviation_percents, average_time_spent = run_experiment(file_path)
print("--------------------------------------------------------------------------------")
print(f"Total average time spent: {average_time_spent} seconds")
print(f"Total average deviation: {average_deviation_percents}%")
print("--------------------------------------------------------------------------------")
