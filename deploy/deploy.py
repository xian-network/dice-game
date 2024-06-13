from xian_py.wallet import Wallet
from xian_py.xian import Xian

# Assuming the contract code is in a file named 'contract_code.py' in the same directory
with open('./contracts/con_uberdice.py', 'r') as file:
    code = file.read()

# Give your contract a name to be submitted as, must start with `con_`
contract_name = 'con_my_cool_contract'

wallet = Wallet(
    '<wallet_address>')
xian = Xian('https://testnet.xian.org', wallet=wallet)

# Constructor arguments // do not include in `submit_contract` if the seed() function has no arguments in your contract.
arguments = {
    'some_arg': '12345'
}

# Deploy contract to network and pass arguments to it
submit = xian.submit_contract(
    contract_name,
    code,
    # args=arguments
)

print(f'success: {submit["success"]}')
print(f'tx_hash: {submit["tx_hash"]}')
print(f'view tx in explorer: https://explorer.xian.org/tx/{submit["tx_hash"]}')
