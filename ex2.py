class Lemonade:
    def __init__(self, add=None):
        self.add = add

    def show_info(self):
        if self.add is None:
            return f'Обычная газировка'
        else:
            return f'Газировка с {self.add}'


i = Lemonade()
print(i.show_info())