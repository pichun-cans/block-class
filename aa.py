import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data, nonce=0):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.index}{self.previous_hash}{self.timestamp}{self.data}{self.nonce}".encode()
        return hashlib.sha256(block_string).hexdigest()

    def __repr__(self):
        return (f"Block(Index: {self.index}, "
                f"Previous Hash: '{self.previous_hash}', "
                f"Timestamp: {self.timestamp}, "
                f"Data: '{self.data}', "
                f"Nonce: {self.nonce}, "
                f"Hash: '{self.hash}')")

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        # Membuat blok genesis
        genesis_block = Block(0, "0", time.time(), "Genesis Block")
        self.chain.append(genesis_block)

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, data):
        previous_block = self.get_latest_block()
        index = previous_block.index + 1
        timestamp = time.time()
        new_block = Block(index, previous_block.hash, timestamp, data)
        self.chain.append(new_block)

    def print_chain(self):
        for block in self.chain:
            print(block)

# Contoh penggunaan
if __name__ == "__main__":
    # Membuat blockchain baru
    blockchain = Blockchain()

    # Menambahkan beberapa blok
    blockchain.add_block("Block 1 Data")
    blockchain.add_block("Block 2 Data")
    blockchain.add_block("Block 3 Data")

    # Mencetak rantai blok
    blockchain.print_chain()
