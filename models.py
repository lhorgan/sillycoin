import hashlib

class Coin: # in this impl, also a block
    def __init__(self, prev_coin_hash, merkle_tree):
        self.prve_coin_hash = prev_coin_hash
        self.merkle_tree = merkle_tree

class Transaction:
    def __init__(self, sender, reciper, coin):
        self.sender = sender
        self.reciper = reciper
        self.coin = coin

class MerkleTree:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def build_merkle_tree(self, leaves):
        if len(leaves) % 2 != 0:
            leaves.append(None)

        if len(leaves) == 2:
            self.left = leaves[0]
            self.right = leaves[1]
            self.val = hash([self.get_val(leaves[0]), self.get_val(leaves[1])])
        else:
            new_leaves = []
            for i in range(0, len(leaves), 2):
                sub_tree = MerkleTree(hash([self.get_val(leaves[i]), self.get_val(leaves[i + 1])]), leaves[i], leaves[i + 1])
                new_leaves.append(sub_tree)

            self.build_merkle_tree(new_leaves)

    def get_val(self, item):
        try:
            return item.val
        except AttributeError:
            return item

def hash(items):
    concat = ""
    for item in items:
        if item is not None:
            concat += item
    return hashlib.sha256(concat).hexdigest()
