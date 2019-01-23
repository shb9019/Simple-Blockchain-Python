#!/usr/bin/env python3
from blockchain import Blockchain
import pprint

pp = pprint.PrettyPrinter(indent=2)
blockchain = Blockchain()

def mine(miner):
    # We run the proof of work algorithm to get the next proof...
    last_block = blockchain.last_block
    last_proof = last_block['proof']
    proof = blockchain.proof_of_work(last_proof)

    blockchain.new_transaction(
        sender = "0",
        recipient = miner,
        amount = 1,
    )

    previous_hash = blockchain.hash(last_block)
    block = blockchain.new_block(proof, previous_hash)

    response = {
        'message': "New Block Forged",
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
    }
    pp.pprint(response)
    print('\n')

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

pp.pprint(blockchain.chain)
print('\n')

mine('A')

pp.pprint(blockchain.chain)
print('\n')
