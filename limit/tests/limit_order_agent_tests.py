# import unittest

# class LimitOrderAgentTest(unittest.TestCase):

#     def test_something(self):
#         self.fail("not implemented")

execution_client = ExecutionClient()
agent = LimitOrderAgent(execution_client)

# Add an order to buy 1000 shares of IBM if the price drops to $100
agent.add_order('buy', 'IBM', 1000, 100)

# Simulate price updates
price_updates = [
    ('IBM', 105),
    ('IBM', 102),
    ('IBM', 100),
    ('IBM', 98)
]

for product_id, market_price in price_updates:
    agent.price_tick(product_id, market_price)
