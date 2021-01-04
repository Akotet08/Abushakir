class Calendar_Exception(Exception):
    def __init__(self, string):
        super().__init__(string)

class BealNameException(Calendar_Exception):
    def __init__(self, string):
        super().__init__(string)

class MonthNumberException(Calendar_Exception):
    def __init__(self, string):
        super().__init__(string)

class WeekNumberException(Calendar_Exception):
    def __init__(self, string):
        super().__init__(string)

class EthiopicNumberException(Calendar_Exception):
    def __init__(self, string):
        super().__init__(string)    