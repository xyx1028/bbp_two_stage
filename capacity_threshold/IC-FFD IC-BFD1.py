import pandas as pd
import numpy as np
import time

# 载入数据集
def load_data(file_path):
    data = pd.read_csv(file_path, header=None)
    return data.applymap(int).values.tolist()

# 动态阈值装箱算法，结合IC-FFD和IC-BFD策略
def dynamic_packing_algorithm(items, bin_capacity, threshold_percent):
    bins = []
    items_sorted = sorted(items, reverse=True)
    threshold = bin_capacity * threshold_percent
    stage = "first"  # 初始阶段

    for item in items_sorted:
        if stage == "first":
            # 第一阶段装箱策略：首次适应下降
            placed = False
            for bin in bins:
                if sum(bin) + item <= bin_capacity:
                    # 检查是否将要超过阈值，如果是则切换到第二阶段，不放入物品
                    if sum(bin) >= threshold:
                        stage = "second"
                        placed = True
                        break
                    bin.append(item) 
                    placed = True
                    break
            if not placed:
                bins.append([item])
        if stage == "second":
            # 第二阶段装箱策略：最佳适应下降
            best_bin = None
            min_space_left = float('inf')
            for bin in bins:
                space_left = bin_capacity - sum(bin)
                if space_left >= item and space_left < min_space_left:
                    best_bin = bin
                    min_space_left = space_left
            if best_bin:
                best_bin.append(item)
            else:
                # 如果第二阶段无法放入任何已有的箱子中，则添加新箱子，并切换回第一阶段
                bins.append([item])
                stage = "first"

    return bins

def run_experiment(file_path, bin_capacity, threshold_percent):
    datasets = load_data(file_path)
    all_deviation_percents = []
    all_times = []

    for items in datasets:
        start_time = time.time()
        bins = dynamic_packing_algorithm(items, bin_capacity, threshold_percent)
        time_spent = time.time() - start_time

        total_capacity = sum(items)
        lower_bound = np.ceil(total_capacity / bin_capacity)
        kalgebra = len(bins)
        deviation_percent = ((kalgebra - lower_bound) / lower_bound) * 100 if lower_bound != 0 else 0

        all_times.append(time_spent)
        all_deviation_percents.append(deviation_percent)

    average_time_spent = np.mean(all_times)
    average_deviation_percent = np.mean(all_deviation_percents)

    return average_deviation_percent, average_time_spent

# 设置参数并运行实验
bin_capacity = 1000  # 箱子容量
threshold_percent = 0.67  # 阈值百分比
file_path = 'class_t_60.csv'
average_deviation_percent, average_time_spent = run_experiment(file_path, bin_capacity, threshold_percent)
print(f"Average Deviation Percent: {average_deviation_percent}%")
print(f"Average Time Spent: {average_time_spent} seconds")