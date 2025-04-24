import numpy as np
import math
import pygame

def vector_like(values : list | np.ndarray):
    if type(values) is list : 
        if len(values) == 4 : return np.array(values)
        elif len(values) == 3 : return np.array(values + [1])
    elif type(values) is np.ndarray :
        if len(values) == 4 : return values
        elif len(values) == 3 : return np.append(values, [1])
    else : raise TypeError("Expected list or array") 

def translate(pos):
    return np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [pos[0],pos[1],pos[2],1]
    ])
    
def rot_x(a):
    return np.array([
        [1, 0, 0, 0],
        [0, math.cos(a), math.sin(a), 0],
        [0, -math.sin(a), math.cos(a), 0],
        [0, 0, 0, 1]
    ])
    
def rot_y(b):
    return np.array([
        [math.cos(b), 0, -math.sin(b), 0],
        [0, 1, 0, 0],
        [math.sin(b), 0, math.cos(b), 0],
        [0, 0, 0, 1]
    ])
    
def rot_z(g):
    return np.array([
        [math.cos(g), math.sin(g), 0, 0],
        [-math.sin(g), math.cos(g), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])
    
def rot_w(o, t):
    w = np.array([
        [0, -o[2], o[1], 0],
        [o[2], 0, -o[0], 0],
        [-o[1], o[0], 0, 0],
        [0, 0, 0, 1]
    ])
    return np.identity(4)+w*math.sin(t)+w**2*(1 - math.cos(t))
    
def scale(s):
    return np.array([
        [s[0], 0, 0, 0],
        [0, s[1], 0, 0],
        [0, 0, s[2], 0],
        [0, 0, 0, 1]
    ])