class Phone:
    number = "123"
    _calls = 0

    def input_number(self, number):
        self.number = number

    def output(self):
        return self._calls

    def add_call(self):
        self._calls += 1


one = Phone()
two = Phone()
three = Phone()

one.input_number("+432123")
two.input_number("+4567823")
three.input_number("+987230")

one.add_call()
one.add_call()

two.add_call()
two.add_call()
two.add_call()

three.add_call()
three.add_call()
three.add_call()
three.add_call()


def num_of_calls(phones: list[Phone]) -> int:
    return sum([phone.output() for phone in phones])


print(num_of_calls([one, two, three]))
