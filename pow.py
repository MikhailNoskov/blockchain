import hashlib
import time


class Block:
    def __init__(self, data, previous_hash):
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.generate_hash()

    # Calculate the SHA256 hash of the block
    def generate_hash(self):
        block_contents = str(self.timestamp) + str(self.data) + str(self.previous_hash) + str(self.nonce)
        return hashlib.sha256(block_contents.encode()).hexdigest()

    # Proof of work algorithm
    def mine_block(self, difficulty):
        while self.hash[:difficulty] != '0' * difficulty:
            self.nonce += 1
            self.hash = self.generate_hash()
        print('Mined successfully')


# Define the blockchain structure
class BlockChain:
    def __init__(self, difficulty=2):
        self.chain = [self.create_genesis_block()]
        self.difficulty = difficulty

    # Create the first (genesis) block
    @staticmethod
    def create_genesis_block():
        return Block("Genesis Block", "0")

    # Get the last block in the blockchain
    def get_last_block(self):
        return self.chain[-1]

    # Add a new block to the blockchain
    def add_block(self, new_block):
        new_block.previous_hash = self.get_last_block().hash
        new_block.mine_block(self.difficulty)
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

    print('Mining block 2...')
    block_2 = Block("Transaction 2", "")
    blockchain.add_block(block_2)

    print('Mining block 3...')
    block_3 = Block("Transaction 3", "")
    blockchain.add_block(block_3)

    # Tamper with blockchain
    blockchain.chain[1].data = "Tampered transaction"

    print("Is blockchain valid after tampering? {}".format(blockchain.is_chain_valid()))
