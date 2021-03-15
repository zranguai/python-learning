# 用python解决打标签时将xml文件的标签名打错
# 问题描述:再进行达标签时将magnetic_tile的标签名错误的打成了magnetic_title，又不想一张一张的修改
"""
通过解析xml文件，批量修改xml文件里的标签名称，改变xml文件的标签
"""
import os.path
import glob
import xml.etree.ElementTree as ET
path = r'E:\xml\errorxml'    # 文件夹路径
for xml_file in glob.glob(path + '/*.xml'):
####### 返回解析树
    # print(xml_file)
    tree = ET.parse(xml_file)
    root = tree.getroot()
    # print(root.findall('object')[0].find('name').text)    # 打印测试是否是自己要的标签名
    if root.findall('object')[0].find('name').text == 'magnetic_title':    # 判断是不是错误的标签
        root.findall('object')[0].find('name').text = 'magnetic_tile'    # 将错误的标签进行修改
        print(root.findall('object')[0].find('name').text)    # 打印测试
        tree.write(xml_file)    # 将改好的文件重新写入
