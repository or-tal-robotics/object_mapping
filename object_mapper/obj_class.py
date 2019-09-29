#!/usr/bin/env python

# Libraries:
import numpy as np

# Updating the Probabilities of every object with consideration for the old ones:
def Updated_Probabilities_and_Cls(old_probability,new_probability,viewed_number,new_cls):
    old_weight = (viewed_number - 1)/viewed_number
    new_weight = 1 - old_weight

    if len(old_probability) == 0:
        updated_prob = np.array(new_probability)
    elif len(new_probability) == 0:
        updated_prob = np.array(old_probability)
    else:
        updated_prob = old_weight * np.array(old_probability) + new_weight * np.array(new_probability)
        new_cls = np.argmax(updated_prob)+1
    return updated_prob, new_cls

# Calculating the distance between two points:
def _distance(pt_1, pt_2):
    pt_1 = np.array((pt_1[0,0], pt_1[0,1]))
    pt_2 = np.array((pt_2[0], pt_2[1]))
    return np.linalg.norm(pt_1-pt_2)

def closest_node(node, nodes):
    i = 0
    j = 0
    dist = 9999999
    for n in nodes:
        if _distance(node, n) <= dist:
            dist = _distance(node, n)
            j = i
        i += 1
    return [dist , j]

def Search_Radius(r,a,b):
    return np.amax([r,a,b])

class Object_Map_cls():


    def __init__(self,x_center=0,y_center=0,r=0,a=0,b=0,angle=0,cls_num=0,prob_distribution=[],viewed_number=0):

        self.x_center = x_center
        self.y_center = y_center
        self.r = r
        self.a = a
        self.b = b
        self.angle = angle
        self.cls_num = cls_num
        self.prob_distribution = prob_distribution
        self.viewed_number = viewed_number

