from binomial_tree import BinomialTree
import time
from animation_speed import ANIMATION_SPEED

class BinomialHeap:
  def __init__(self):
    self.trees = []

  def add_elem(self, key, heap_canvas, master):
    tree = BinomialTree(initial_key=key)
    self.trees.insert(0, tree)
    time.sleep(ANIMATION_SPEED)
    heap_canvas.draw(self)
    master.update()
    self._fix_heap(heap_canvas, master)

  def union(self, heap_canvas, heap, master):
    self.trees.extend(heap.trees)
    self._fix_heap(heap_canvas, master)
  
  def get_min_tree(self):
    if not len(self.trees):
      return None

    return min(self.trees, key = lambda tree: tree.root.key)

  def remove_min_node(self, heap_canvas, master, ok=False):
    min_tree = self.get_min_tree()
    if not min_tree:
      return
    if ok:
      if min_tree.root.key != -1:
        return

    time.sleep(ANIMATION_SPEED)
    heap_canvas.draw(self)
    self.trees.remove(min_tree)
    master.update()
    for root_child in min_tree.root.children:
      new_tree = BinomialTree(root=root_child)
      self.trees.append(new_tree)

    time.sleep(ANIMATION_SPEED)
    heap_canvas.draw(self)
    self._fix_heap(heap_canvas, master) 
  
  def is_empty(self):
    return self.size() == 0

  def size(self):
    return len(self.trees)

  def clear(self):
    self.trees = []

  def _fix_heap(self, heap_canvas, master):
    trees = self.trees
    trees.sort(key = lambda tree: tree.root.degree)
    was_merge = True

    while was_merge:
      was_merge = False
      for i in range(0, len(trees) - 1):
        if i >= len(self.trees) - 1:
          break
        
        if trees[i].root.degree == trees[i+1].root.degree:
          time.sleep(ANIMATION_SPEED)
          heap_canvas.draw(self)
          master.update()
          was_merge = True
          trees[i] = trees[i].union(trees[i+1])
          trees.pop(i+1)
          time.sleep(ANIMATION_SPEED)
          heap_canvas.draw(self)
          master.update()

  def remove_node(self, key, heap_canvas, master):
    for tree in self.trees:
      tree.set_key_negative(key, tree.root, heap_canvas, self, master)
    self.remove_min_node(heap_canvas, master, True)
    self._fix_heap(heap_canvas, master)

