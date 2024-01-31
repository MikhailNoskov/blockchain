import hashlib


class Block:
    def __init__(self, data, previous_hash):
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    # Calculate the SHA256 hash of the block
    def calculate_hash(self):
        hash_string = str(self.data) + str(self.previous_hash) + str(self.nonce)
        return hashlib.sha256(hash_string.encode()).hexdigest()

    # Proof of work algorithm
    def mine_block(self, difficulty):
        while self.hash[:difficulty] != '0' * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()
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


if __name__ == '__main__':
    # Test the blockchain
    blockchain = BlockChain(5)
    blockchain.add_block(Block("Block 1", ""))
    blockchain.add_block(Block("Block 2", ""))
    blockchain.add_block(Block("Block 3", ""))
    blockchain.add_block(Block("Block 4", ""))
    blockchain.add_block(Block("Block 5", ""))
    blockchain.add_block(Block("Block 6", ""))

    # Print the blockchain
    for block in blockchain.chain:
        print("Block data: ", block.data)
        print("Block hash: ", block.hash, block.nonce, block.previous_hash)
