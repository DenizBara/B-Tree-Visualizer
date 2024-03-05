import uuid
from node import *
import time
from animation_speed import ANIMATION_SPEED

class BinomialTree:
  def __init__(self, root=None, initial_key=None):
    self.id = uuid.uuid4()
    if root:
      self.root = root
    elif initial_key != None:
      self.root = Node(initial_key, 0)

  def union(self, tree):
    if tree.root.degree != self.root.degree:
      raise Exception("Can't union trees with different degrees")

    if self.root.key <= tree.root.key:
      self.root.children.append(tree.root)
      self.root.degree += 1
      return self

    tree.root.degree += 1
    tree.root.children.append(self.root)
    return tree

  def is_empty(self):
    return self.root == None

  def clear(self):
    self.root = None

  def size(self):
    return pow(2, self.root.degree)

  # ca sa urcam elementul pana la root in binomial tree (elementul cel mai mic din tree e radacina)
  # toate nodurile sunt >= 0, astfel setam nodul curent la -1
  def set_key_negative(self, key, curr_node, heap_canvas, heap, master, parent=None):
    if curr_node.key == key:
      curr_node.key = -1
      time.sleep(ANIMATION_SPEED)
      heap_canvas.draw(heap)
      master.update()
      if parent is not None:
        parent.key, curr_node.key = curr_node.key, parent.key
        time.sleep(ANIMATION_SPEED)
        heap_canvas.draw(heap)
        master.update()
      return

    for child in curr_node.children:
      self.set_key_negative(key, child, heap_canvas, heap, master, curr_node)
      if curr_node.key == -1:
        if parent is not None:
          time.sleep(ANIMATION_SPEED)
          heap_canvas.draw(heap)
          master.update()
          parent.key, curr_node.key = curr_node.key, parent.key
        break

