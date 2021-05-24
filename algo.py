import pygame
import sys
# import random
import math
import os
from collections import deque
from tkinter import messagebox
from tkinter import Tk

grid = []
queue, visited = deque(), []
pathway = []

width, height = 1000, 1000
window = (width, height)

pygame.init()
screen = pygame.display.set_mode(window)
pygame.display.set_caption("Dijkstra's Visualizer")
clock = pygame.time.Clock()

# def visualizer():


# visualizer()
