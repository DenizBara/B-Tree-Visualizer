from tkinter import *
from .draw_heap import draw_heap

class HeapCanvas:
  canvas = None

  def __init__(self, master, root):
    self.canvas = Canvas(root, bg="#fff")
    self.canvas.pack(fill=BOTH, expand=1)

  def draw(self, heap):
    self.canvas.delete('all')
    draw_heap(heap, self.canvas)
