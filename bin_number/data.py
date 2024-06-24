import random
import csv

def generate_data(size, item_size_range, num_sets):
    return [[random.randint(item_size_range[0], item_size_range[1]) for _ in range(size)] for _ in range(num_sets)]

def save_to_csv(datasets, class_label):
    for size, data in datasets.items():
        filename = f"{class_label}_{size}.csv"
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for items in data:
                writer.writerow(items)  # 写入每个实例的物品大小列表

sizes_u = [120, 250, 500, 1000]  # 为类别 u 指定不同的实例大小
sizes_t = [60, 120, 249, 501]  # 为类别 t 指定不同的实例大小
item_size_range_u = (20, 100)  # 类别 u 的物品大小范围
item_size_range_t = (250, 500)  # 类别 t 的物品大小范围
num_sets = 20  # 每个子集的实例数

datasets_u = {size: generate_data(size, item_size_range_u, num_sets) for size in sizes_u}
datasets_t = {size: generate_data(size, item_size_range_t, num_sets) for size in sizes_t}

save_to_csv(datasets_u, 'class_u')
save_to_csv(datasets_t, 'class_t')
