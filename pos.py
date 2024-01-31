#  Proof of stack
import hashlib
import time


class Block:
    def __init__(self, data, previous_hash):
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.generate_hash()

    # Calculate the SHA256 hash of the block
    def generate_hash(self):
        block_contents = str(self.timestamp) + str(self.data) + str(self.previous_hash)
        block_hash = hashlib.sha256(block_contents.encode()).hexdigest()
        return block_hash


class BlockChain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    @staticmethod
    def create_genesis_block():
        return Block("Genesis Block", "0")

    def get_last_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_last_block().hash
        new_block.hash = new_block.generate_hash()
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.hash != current_block.generate_hash():
                return False
            if previous_block.hash != previous_block.generate_hash():
                return False
        return True


if __name__ == '__main__':
    blockchain = BlockChain()
    print('Mining block 1...')
    block_1 = Block("Transaction 1", "")
    blockchain.add_block(block_1)
    print(block_1.previous_hash)
    print(block_1.hash)

    print('Mining block 2...')
    block_2 = Block("Transaction 2", "")
    blockchain.add_block(block_2)
    print(block_2.previous_hash)
    print(block_2.hash)

    print('Mining block 3...')
    block_3 = Block("Transaction 3", "")
    blockchain.add_block(block_3)
    print(block_3.previous_hash)
    print(block_3.hash)

    print("Is blockchain valid? {}".format(blockchain.is_chain_valid()))