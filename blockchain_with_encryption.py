import hashlib
import json
from time import time


class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data = dict()
        data['index'] = self.index
        data['timestamp'] = self.timestamp
        data['data'] = self.data
        data['previous_hash'] = self.previous_hash
        block_string = json.dumps(data, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()


class BlockChain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    @staticmethod
    def create_genesis_block():
        return Block(0, time(), "Genesis block", "0")

    def add_block(self, data):
        previous_block = self.chain[-1]
        new_block = Block(previous_block.index + 1, time(), data, previous_block.hash)
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True


blockchain = BlockChain()

blockchain.add_block("Transaction 1")
blockchain.add_block("Transaction 2")
blockchain.add_block("Transaction 3")

print("Blockchain is valid: ", blockchain.is_chain_valid())

blockchain.chain[1].data = "Tampered Transaction"
print("Blockchain is valid: ", blockchain.is_chain_valid())
