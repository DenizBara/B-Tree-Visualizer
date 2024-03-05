import uuid

class Node:
  def __init__(self, key, degree):
    self.id = uuid.uuid4()
    self.key = key
    self.children = []
    self.degree = degree

