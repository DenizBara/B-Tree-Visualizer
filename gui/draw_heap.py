from .draw_tree import draw_tree
from .constants import tree_draw_horizontal_offset

def draw_heap(heap, canvas):
  prev_root = None
  prev_root_pos = {}
  for i in range(0, len(heap.trees)):
    root_pos = { 'y': 10, 'x': None }
    if not prev_root:
      root_pos['x'] = 30
    else:
      root_pos['x'] = prev_root_pos['x'] + tree_draw_horizontal_offset * (prev_root.degree + 1)
      
    curr_root = heap.trees[i].root
    prev_root_pos = root_pos
    prev_root = curr_root
    draw_tree(curr_root, 0, root_pos, 0, canvas)
  