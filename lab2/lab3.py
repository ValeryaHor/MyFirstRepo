class Order:
    orders_quantity = 0

    def __init__(self):
        self.items = {}
        Order.orders_quantity += 1

    def add_item(self, item, price):

        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Цена должна быть неотрицательным числом")

        self.items[item] = price
        return self.items

    def remove_item(self, item):

        if item not in self.items:
            print(f"Товар '{item}' не найден в заказе")
            return self.items

        confirmation = input(f"Вы уверены, что хотите удалить товар '{item}'? (да/нет): ")

        if confirmation.lower() in ['да', 'yes', 'y', 'д']:
            del self.items[item]
            print(f"Товар '{item}' удален из заказа")
        else:
            print(f"Удаление товара '{item}' отменено")

        return self.items

    def get_total(self):
        return sum(self.items.values())

    def __str__(self):
        if not self.items:
            return "Заказ пуст"

        items_str = "\n".join([f"  - {item}: {price} руб." for item, price in self.items.items()])
        return f"Заказ (всего товаров: {len(self.items)}):\n{items_str}\nОбщая стоимость: {self.get_total()} руб."

    def __del__(self):
        Order.orders_quantity -= 1
