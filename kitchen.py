import json


class Kitchen:
    def __init__(self, staff: set):
        self.staff = staff

    def get_order(self, raw_order: str):
        with open(f'{raw_order}.txt', 'w') as order_file:
            order_file.write(self.parse_order(f'{raw_order}.json'))

    def buy_products(self):
        pass

    def make_dish(self):
        pass

    def get_json_order(self, filename) -> dict:
        with open(filename, 'r') as f:
            abcd = json.load(f)
            return abcd

    def parse_order(self, filename: str) -> str:
        raw_order = self.get_json_order(filename)
        order = ""
        for key, value in raw_order.items():
            order = f"{key}: {', '.join(value)}"
        return order




