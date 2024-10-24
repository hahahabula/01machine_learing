# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 20:17:20 2024

@author: 10856
"""

# # 信息增益的计算
# import pandas as pd
# import math


# class Node:
#     def __init__(self, node_coni, left=None, right=None, parent=None, depth=0, isvisit=False):
#         self.node_coni = node_coni  # node_coni[0]:结点特征名 node_coni[1]:结点特征取值 node_coni[2]:结点包含的样本点
#         self.left = left  
#         self.right = right  
#         self.parent = parent
#         self.depth = depth  
#         self.isvisit = isvisit



# class decision_tree:
#     def __init__(self,  node_coni):
#         self.root = self._build_tree(node_coni, depth=0)
        
#     def _build_tree(self, node_coni, depth=0):
#         if self.caulate_H_D(node_coni[2]) == 0:
#             node_coni[0] = ""
#             return Node(node_coni, depth=depth+1)
#         node_coni_0 = self.select_max_en(node_coni[2])
#         node_coni_2 = node_coni[2]
#         root_node = Node(
#             node_coni = [node_coni_0, node_coni[1], node_coni_2],
#             depth = depth
#             )
#         value = df[node_coni_0].unique()
#         root_node.left = self._build_tree(
#             node_coni=[None, value[0], node_coni[2][node_coni[2][node_coni_0]==value[0]]],
#             depth = depth + 1
#             )
#         if root_node.left is not None:
#             root_node.left.parent = root_node
            
#         root_node.right = self._build_tree(
#             node_coni=[None, value[1], node_coni[2][node_coni[2][node_coni_0]==value[1]]],
#             depth = depth + 1
#             )
#         if root_node.left is not None:
#             root_node.left.parent = root_node
#         return root_node

        
#     def select_max_en(self, df):
#         max_en_name = ""
#         max_en = -1
#         for i in df.columns[1:-1]:
#             en_iter = self.caulate_H_D_A(i, df)
#             if en_iter > max_en:
#                 max_en = en_iter
#                 max_en_name = i
#         return max_en_name
        
#     def caulate_H_D(self, df):
#         # 接收一个数据框，计算数据集D的信息熵依据类别进行分类
#         C = df["类别"].value_counts()
#         return sum([-i/C.sum()*math.log(i/C.sum(),2) for i in C])
    
#     def caulate_H_D_A(self, A, df):
#         A_1 = df[A].value_counts()
#         table_1 = pd.crosstab(df["类别"], df[A])
#         H_A_1 = {}
#         for i in table_1:
#             H_result = 0
#             for _, j in table_1.iterrows():
#                 D_c = table_1[i].sum()
#                 a = j[i]/D_c
#                 if a == 0:
#                     H_result = 0
#                 else:
#                     H_result += -a*math.log(a,2)
#             H_A_1[i] = H_result
#         return sum([A_1[i]/A_1.sum()*H_A_1[i] for i in A_1.index])
#   def caulate_H_A_gain(self, A, df):
#        return calcaulate_H_D(df) - caulate_H_D_A(A, df)

# csv_file = "D:\桌面\决策树数据.csv"
# df = pd.read_csv(csv_file)
# dt = decision_tree([None,None,df])





    
    
    
    
    
