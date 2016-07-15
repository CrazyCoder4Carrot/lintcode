"""
Your Trie object will be instantiated and called as such:
trie = Trie()
trie.insert("lintcode")
trie.search("lint") will return false
trie.startsWith("lint") will return true
"""
class TrieNode:
  def __init__(self):
    # Initialize your data structure here.
    self.dic = {}
class Trie:
  def __init__(self):
    self.root = TrieNode()

  # @param {string} word
  # @return {void}
  # Inserts a word into the trie.
  def insert(self, word):
    d = self.root.dic
    for val in word:
      if val not in d:
        d[val] = {}
      d = d[val]
    d["#"] = "#"
  # @pa""ram {string} word
  # @return {boolean}
  # Returns if the word is in the trie.
  def search(self, word):
    d = self.root.dic.copy()
    for val in word:
      if val not in d:
        return False
      d = d[val]
    return "#" in d
  # @param {string} prefix
  # @return {boolean}
  # Returns if there is any word in the trie
  # that starts with the given prefix.
  def startsWith(self, prefix):
    d = self.root.dic.copy()
    for val in prefix:
      if val not in d:
        return False
      d = d[val]
    return True