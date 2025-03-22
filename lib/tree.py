class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    # Start the recursive search from the root
    return self._depth_first_search(self.root, id)

  def _depth_first_search(self, node, id):
    # If node is None, return None (base case or empty tree)
    if node is None:
      return None
    
    # Check if the current node's id matches the target id
    if node['id'] == id:
      return node
    
    # Recursively search each child
    for child in node['children']:
      result = self._depth_first_search(child, id)
      if result is not None:  # If a match is found in any subtree, return it
        return result
    
    # If no match is found in this subtree, return None
    return None