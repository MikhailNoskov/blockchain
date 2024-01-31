import  hashlib
import datetime


class Block:
    def __init__(self, block_number, transactions, previous_hash, gas_limit, gas_used, miner):
        self.block_number = block_number
        self.timestamp = datetime.datetime.now()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.gas_limit = gas_limit
        self.gas_used = gas_used
        self.miner = miner
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        date_string = (
            str(self.block_number)
            + str(self.timestamp)
            + str(self.transactions)
            + str(self.previous_hash)
            + str(self.gas_limit)
            + str(self.gas_used)
            + str(self.miner)
        )
        return hashlib.sha256(date_string.encode('utf-8')).hexdigest()


class BlockChain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    @staticmethod
    def create_genesis_block():
        return Block(0, 'Genesis block', '0', 0, 0, 'Genesis miner')

    def add_block(self, new_block: Block):
        new_block.previous_hash = self.chain[-1].hash
        self.chain.append(new_block)

    @staticmethod
    def print_block(block: Block):
        for attr_name, value in block.__dict__.items():
            print(f"{' '.join(attr_name.split('_')).title().lstrip()}: {value}")
        print()

    def traverse_chain(self):
        for block in self.chain:
            self.print_block(block)


if __name__ == '__main__':
    blockchain = BlockChain()
    blockchain.add_block(Block(1, "Transaction 1", "", 1000000, 500000, "Miner 1"))
    blockchain.add_block(Block(2, "Transaction 2", "", 2000000, 1500000, "Miner 2"))
    blockchain.add_block(Block(3, "Transaction 3", "", 3000000, 2500000, "Miner 3"))
    blockchain.traverse_chain()
