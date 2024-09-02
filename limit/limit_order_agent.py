from trading_framework.execution_client import ExecutionClient
from trading_framework.price_listener import PriceListener


class LimitOrderAgent(PriceListener):

    def __init__(self, execution_client: ExecutionClient) -> None:
        """
                :param execution_client: can be used to buy or sell - see ExecutionClient protocol definition
        """
        self.execution_client = execution_client
        self.orders = []
        super().__init__()


    def add_order(self, action, product_id, amount, limit_price):
        
        order = {
            'action': action,
            'product_id': product_id,
            'amount': amount,
            'limit_price': limit_price
        }
        self.orders.append(order)

    def on_price_tick(self, product_id: str, price: float):
        for order in self.orders:
            if order['product_id'] == product_id:
                if order['action'] == 'buy' and market_price <= order['limit_price']:
                    # Execute the buy order
                    self.execution_client.execute_order(order['product_id'], order['amount'], 'buy')
                    self.orders.remove(order)
                elif order['action'] == 'sell' and market_price >= order['limit_price']:
                    # Execute the sell order
                    self.execution_client.execute_order(order['product_id'], order['amount'], 'sell')
                    self.orders.remove(order)

# Example usage:
# execution_client = YourExecutionClient()  # Replace with actual execution client
# agent = LimitOrderAgent(execution_client)
# agent.add_order('buy', 'IBM', 1000, 100)
