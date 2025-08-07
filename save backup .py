# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 16:43:38 2024

@author: kaikisen
"""

import shutil
import os
from datetime import datetime

def read_paths_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        source_path = lines[0].strip()
        destination_directory = lines[1].strip()
        return source_path, destination_directory

def copy_and_rename(source_path, destination_directory):
    # 获取当前时间，并格式化为MM-DD-HH-MM-SS
    timestamp = datetime.now().strftime('%m-%d-%H%M-%S')

    # 创建目标文件夹路径
    destination_name = os.path.basename(source_path)
    if os.path.isfile(source_path):
        # 如果是文件，重命名为 <文件名>_<时间戳>
        destination_file = os.path.join(destination_directory, f"{os.path.splitext(destination_name)[0]}_{timestamp}{os.path.splitext(destination_name)[1]}")
        shutil.copy2(source_path, destination_file)
        print(f"文件已成功复制并重命名为: {destination_file}")
    elif os.path.isdir(source_path):
        # 如果是文件夹，重命名为 <时间戳>
        destination_folder = os.path.join(destination_directory, timestamp)
        shutil.copytree(source_path, destination_folder)
        print(f"文件夹已成功复制并重命名为: {destination_folder}")
    else:
        print("源路径不是文件或文件夹")

# 从txt文件中读取路径，第一行源地址第二行目标地址
file_path = r'C:/Users/用户名/Desktop/savepath.txt'  # 外部文本文档路径
source_path, destination_directory = read_paths_from_file(file_path)

copy_and_rename(source_path, destination_directory)
