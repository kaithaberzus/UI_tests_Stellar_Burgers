class Helper:

    # Добавление нуля перед номером заказа
    def add_zero_before_number(self,number):
        num = str(f'0{number}')
        return num

    # Добавление решетки к нулю перед номером заказа
    def add_reshotka_before_zero(self, number):
        num = str(f'#{self.add_zero_before_number(number)}')
        return num