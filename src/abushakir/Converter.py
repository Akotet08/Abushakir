import Calander_Exceptions as exceptions
import Constants

class Converter:
    def divide(self, numinator, denominator):
        result = [0]* 2
        result[0] = numinator // denominator
        result[1] = numinator % denominator
        return result
        
    def convert_1_10_ToGeez(self, num):
        if num < 1:
            raise exceptions.EthiopicNumberException("Zero (0) and Negative numbers doesn't exsit in Ethiopic numerals ")
        else:
            return Constants.Constants().geezNumbers[num]
        
    def convert_11_100_ToGeez(self, num):
        if num == 100:
            return Constants.Constants().geezNumbers[num]
        result = self.divide(num, 10)
        if result[1] != 0:
            return Constants.Constants().geezNumbers[result[0] * 10] + Constants.Constants().geezNumbers[result[1]]
        return Constants.Constants().geezNumbers[result[0] * 10]

    def convert_101_1000_ToGeez(self, num):
        result = self.divide(num, 100)
        if num == 1000:
            return Constants.Constants().geezNumbers[1000]
        if result[1] != 0:
            if result[1] < 11:
                return Constants.Constants().geezNumbers[result[0]] + Constants.Constants().geezNumbers[100] + self.convert_1_10_ToGeez(result[1])
            else:
                return Constants.Constants().geezNumbers[result[0]] + Constants.Constants().geezNumbers[100] + self.convert_11_100_ToGeez(result[1])
        return Constants.Constants().geezNumbers[result[0]] + Constants.Constants().geezNumbers[100]
    def convertToGeez(self, num):
        result = "empty"
        if num < 1:
            raise exceptions.EthiopicNumberException("Zero (0) and Negative numbers doesn't exsit in Ethiopic numerals ")
        elif num >= 1 and num < 11:
            result = self.convert_1_10_ToGeez(num)
        elif num >10 and num < 101:
            result = self.convert_11_100_ToGeez(num)
        elif num >100 and num < 1001:
            result = self.convert_101_1000_ToGeez(num)
        elif num >1001 and num < 10001:
            result = self.divide(num, 1000)
            if num == 10000:
                result = Constants.Constants().geezNumbers[10000]
            elif result[1] != 0:
                if result[1] < 11:
                    result = Constants.Constants().geezNumbers[result[0] * 10] + Constants.Constants().geezNumbers[100] + self.convert_1_10_ToGeez(result[1])
                elif result[1] < 101:
                    result = Constants.Constants().geezNumbers[result[0] * 10] + Constants.Constants().geezNumbers[100] + self.convert_11_100_ToGeez(result[1])
                else: 
                    result = Constants.Constants().geezNumbers[result[0] * 10] + Constants.Constants().geezNumbers[100] + self.convert_101_1000_ToGeez(result[1])
            else:
                result = Constants.Constants().geezNumbers[result[0] * 10] + Constants.Constants().geezNumbers[100]
        return result
