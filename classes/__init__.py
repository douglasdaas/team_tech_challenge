def validate_number(number):
    try:
        if (type(number) is not str) and (type(number) is not int):
            raise ValueError
        number = int(number)
        if not 0 <= number <= 999:
            raise ValueError
        return int(number)
    except ValueError:
        raise ValueError(f'"{number}" is not an integer between 0 and 999')


class DataCapture:
    number_counter_dict = None
    total_number_count = 0
    max_number = 0
    min_number = 999

    def add(self, number):
        number = validate_number(number)

        if self.number_counter_dict is None:
            self.number_counter_dict = {}

        self.number_counter_dict[number] = self.number_counter_dict.get(number, 0) + 1
        self.total_number_count += 1
        if self.max_number < number:
            self.max_number = number
        if self.min_number > number:
            self.min_number = number

    def build_stats(self):
        return Stats(self.number_counter_dict, self.total_number_count, self.min_number, self.max_number)


class Stats:
    def __init__(self, number_counter_dict, total_number_count, min_number, max_number):
        self.number_counter_dict = number_counter_dict
        self.total_number_count = total_number_count
        self.min_number = min_number
        self.max_number = max_number
        self.stats_dict = {}

        current_less_count = 0
        for number in range(self.min_number, self.max_number + 1):
            self.stats_dict[number] = {
                'count': self.number_counter_dict.get(number, 0),
                'less_count': current_less_count,
                'greater_count': self.total_number_count - current_less_count - self.number_counter_dict.get(number, 0),
            }
            current_less_count += self.number_counter_dict.get(number, 0)

    def count(self, number):
        if number < self.min_number or number > self.max_number:
            return 0
        return self.stats_dict[number]['count']

    def less(self, number):
        if number < self.min_number:
            return 0
        if number > self.max_number:
            return self.total_number_count
        return self.stats_dict[number]['less_count']

    def greater(self, number):
        if number < self.min_number:
            return self.total_number_count
        if number > self.max_number:
            return 0
        return self.stats_dict[number]['greater_count']

    def between(self, first_number, second_number):
        greater_number = first_number if first_number > second_number else second_number
        return self.count(greater_number) + self.less(greater_number)
