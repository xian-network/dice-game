import unittest
from contracting.client import ContractingClient
import random
import string


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.c = ContractingClient()
        self.c.flush()

        with open('../contracts/currency.py') as f:
            code = f.read()
            self.c.submit(code, name='currency',
                          constructor_args={'vk': 'boi'})

        self.currency = self.c.get_contract('currency')

        with open('../contracts/con_uberdice.py') as f:
            code = f.read()
            self.c.submit(code, name='con_uberdice', signer='boi')

        self.uberdice = self.c.get_contract('con_uberdice')

    def test_roll_loss(self):
        self.currency.transfer(amount=1000, to='con_uberdice', signer='boi')
        self.currency.approve(amount=50, to='con_uberdice', signer='boi')
        self.uberdice.roll(bet_size=50, token_contract='currency', roll_type='under',roll_target=10, signer='boi',environment={
	        'block_height': 5,
	        'block_hash': 'loser'
	    }) # Environment makes the roll a predictable 83, which is over 10 so it's a loss.
        self.assertEqual(self.currency.balance_of(account='con_uberdice'), 1050) # Lose, so house gets 50.

    def test_roll_win(self):
        self.currency.transfer(amount=1000, to='con_uberdice', signer='boi')
        self.currency.approve(amount=50, to='con_uberdice', signer='boi')
        (self.uberdice.roll(bet_size=50, token_contract='currency', roll_type='over',roll_target=80, signer='boi',environment={
            'block_height': 5,
            'block_hash': 'loser'
        })) # Environment makes the roll a predictable 83, which is over 80 so it's a win.
        self.assertEqual(int(self.currency.balance_of(account='con_uberdice')),819) # Win, so house loses the multiplier of 50.

    def test_roll_win_cant_cover(self):
        self.currency.transfer(amount=200, to='con_uberdice', signer='boi')
        self.currency.approve(amount=50, to='con_uberdice', signer='boi')
        with self.assertRaises(AssertionError):
            self.uberdice.roll(bet_size=50, token_contract='currency', roll_type='over',roll_target=82, signer='boi',environment={
                'block_height': 5,
                'block_hash': 'loser'
            })

    def test_change_owner(self):
        self.uberdice.change_owner(new_owner='new_owner', signer='boi')
        self.assertEqual(self.uberdice.game['owner'], 'new_owner')

    def test_change_allowed_tokens(self):
        self.uberdice.change_allowed_tokens(tokens=['currency', 'other_token'], signer='boi')
        self.assertEqual(self.uberdice.game['allowed_tokens'], ['currency', 'other_token'])
        with self.assertRaises(AssertionError):
            self.uberdice.roll(bet_size=50, token_contract='not_allowed', roll_type='over', roll_target=50, signer='boi',environment={
                'block_height': 5,
                'block_hash': 'loser'
            })

    def test_change_max_token_bet(self):
        self.uberdice.change_max_token_bet(token_contract='currency', max_bet=100, signer='boi')
        self.assertEqual(self.uberdice.game['max_token_bet', 'currency'], 100)
        
        with self.assertRaises(AssertionError):
            self.uberdice.roll(bet_size=101, token_contract='currency', roll_type='over', roll_target=50, signer='boi',environment={
                'block_height': 5,
                'block_hash': 'loser'
            })

    def test_change_house_edge(self):
        self.uberdice.change_house_edge(new_edge=0.05, signer='boi')
        self.assertEqual(self.uberdice.game['house_edge'], 0.05)


if __name__ == '__main__':
    unittest.main()