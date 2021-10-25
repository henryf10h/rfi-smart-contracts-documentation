import pytest
import os
from dotenv import load_dotenv
from brownie import Contract, network, accounts
import json
#Arrange
#Act
#Assert
#Cleanup
load_dotenv()
network.connect('polygon-test')
print(network.show_active())
address = '0x05dEf9395C27FFE7404A73bdBDb5a65b059ad3FC'
ABI = json.load(open("./tests/abi.py","r"))
c = Contract.from_abi("RFIT",address,ABI)
A = accounts.add('2503dbc77c120f2ed279663a3aed3d0f461a8e478471ef9804e93c8685dd4e81')
print(A)
B = accounts.add('fc77c63111af8a027126fe702aeefe631315506088834f5da81c9d315cc9d0b8')
print(B)
print(c.transfer(B,50000 * 10**9,{"from":A}))
