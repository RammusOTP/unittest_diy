import operator


def expect(value):
    return Expectation(value)


class FailedExpectationError(RuntimeError):
    def __init__(self, message):
        self.message = message


class Expectation:


    def __init__(self, value):
        self.value = value


    def to_equal(self, comparison):
        self._assert(comparison, operator.eq,"to equal")


    def to_not_equal(self, comparison):
        self._assert(comparison, operator.is_not, "to not equal")


    def _assert(self, comparison, op, message):
        if not op(self.value, comparison):
            raise FailedExpectationError(f"expected {self.value} {message} {comparison}")


    def to_include(self, element):
        self._assert(element, operator.contains, "to include")


    def to_not_include(self, element):


        def not_include(list, element):
            return element not in list


        self._assert(element, not_include, "to not include")