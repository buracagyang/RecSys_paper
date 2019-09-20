# -*- coding: utf-8 -*-
# @Time     : 2019/9/19 14:58
# @Author   : buracagyang
# @File     : GenerateReadmeFile.py
# @Software : PyCharm

"""
Describe:

"""

import os
import urllib.parse

__author__ = 'buracagyang'

catalog_flag = 0
github_root = "https://github.com/buracagyang/RecSys_paper/blob/master/"

with open('./README.md', 'r', encoding='utf-8') as input_file:
    all_lines = input_file.readlines()

out_file = open('./README.md', 'w', encoding='utf-8')
for line in all_lines:
    if catalog_flag != 1:
        out_file.write(line)
    if line.startswith("##"):
        catalog_flag = 1

dir_list = os.listdir("./")
for one_dir in dir_list:
    if os.path.isdir(one_dir) and not one_dir.startswith('.'):
        out_file.write("\n### " + one_dir + "\n")
        sub_files_list = os.listdir(one_dir)
        for one_file in sub_files_list:
            if not os.path.isdir(one_file) and not one_file.startswith('.'):
                f_link = github_root + urllib.parse.quote(one_dir.strip()) + "/" + urllib.parse.quote(one_file.strip())
                out_line = "* [{file_name}]({link}) <br/>\n".format(file_name=one_file.split('.')[0], link=f_link)
                out_file.write(out_line)

out_file.close()
