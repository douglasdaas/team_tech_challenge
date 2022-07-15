# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

class Stats:
    stats_dict = {}

    def __int__(self, number_counter_dict, numbers_array, total_number_count, min_number, max_number):
        self.stats_dict[min_number] = {
            'count': number_counter_dict[min_number],
            'less_count': 0,
            'greater_count': total_number_count - number_counter_dict[min_number],
        }
        self.stats_dict[max_number] = {
            'count': number_counter_dict[max_number],
            'less_count': total_number_count - number_counter_dict[max_number],
            'greater_count': 0,
        }

        current_less_count = 0
        for number in range(min_number, max_number):
            if number_counter_dict.get(number, None) is not None:
                current_less_count += number_counter_dict[number]
                self.stats_dict[number] = {
                    'count': number_counter_dict[number],
                    'less_count': current_less_count,
                    'greater_count': total_number_count - current_less_count,
                }

    def count(self, number):
        return self.stats_dict[number]['count']

    def less(self, number):
        return self.stats_dict[number]['less_count']

    def greater(self, number):
        return self.stats_dict[number]['greater_count']

    def between(self, first_number, second_number):
        lesser_number = first_number if first_number < second_number else second_number
        greater_number = first_number if first_number > second_number else second_number
        return self.count(greater_number) + self.less(greater_number) - self.count(lesser_number)


class DataCapture:
    number_counter_dict = {}
    numbers_array = []
    total_number_count = 0
    min_number = 1000
    max_number = -1

    def add(self, number):
        self.number_counter_dict[number] = self.number_counter_dict.get(number, 0) + 1
        self.numbers_array.append(number)
        self.total_number_count += 1
        if self.max_number > number:
            self.max_number = number
        if self.min_number < number:
            self.min_number = number

    def build_stats(self):
        stats = Stats(self.number_counter_dict, self.numbers_array, self.number_count, self.min_number, self.max_number)
        return stats


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    capture = DataCapture
    capture.add(3)
    capture.add(9)
    capture.add(3)
    capture.add(4)
    capture.add(6)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
