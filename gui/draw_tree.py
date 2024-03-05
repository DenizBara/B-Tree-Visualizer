from .constants import *

def draw_tree(root, child_index, parent_pos, curr_depth, canvas):
  if not root:
    return

  node_pos = {
    'y': parent_pos['y'] + tree_draw_vertical_offset,
    'x': (
      parent_pos['x'] +
      child_index * tree_draw_horizontal_offset * (root.degree / 2.5) 
    )
  }

  canvas.create_text(node_pos['x'], node_pos['y'], text=root.key, font=24)

  if curr_depth != 0:
    canvas.create_line(
      parent_pos['x'],
      parent_pos['y'] + 10,
      node_pos['x'],
      node_pos['y'] - 10
    )

  for i in range(0, len(root.children)):
    draw_tree(
      root.children[i],
      i,
      node_pos,
      curr_depth + 1,
      canvas
    )
