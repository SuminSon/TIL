class TrieNode:
    def __init__(self,key, data=None):
        self.key = key
        self.data = data
        self.children = {}

class Trie:
    def __init__(self):
        self.head = TrieNode(None)

    def insert(self,string):
        cur_node = self.head
        for char in string:
            if char not in cur_node.children:
                cur_node.children[char] = TrieNode(char)
            cur_node = cur_node.children[char]
        cur_node.data = string

    def search(self, string):
        cur_node = self.head

        for char in string:
            if char in cur_node.children:
                cur_node = cur_node.children[char]
            else:
                return False

        if cur_node.data:
            return True
        else:
            return False

    def starts_with(self, prefix):
        cur_node = self.head
        words = []

        for p in prefix:
            if p in cur_node.children:
                cur_node = cur_node.children[p]
            else:
                return None

        cur_node = [cur_node]
        next_node = []
        while True:
            for node in cur_node:
                if node.data:
                    words.append(node.data)
                next_node.extend(list(node.children.values()))
            if len(next_node) != 0:
                cur_node = next_node
                next_node = []
            else:
                break
        return words