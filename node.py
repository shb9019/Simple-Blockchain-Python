#!/usr/bin/env python3
from blockchain import Blockchain

blockchain = Blockchain()

blockchain.new_transaction(
    sender = 'A',
    recipient = 'B',
    amount = 10,
)

blockchain.new_transaction(
    sender = 'B',
    recipient = 'C',
    amount = 10,
)

print(blockchain.chain)
