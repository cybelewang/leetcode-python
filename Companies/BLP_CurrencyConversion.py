"""
给不同银行做汇率交换的记录，求一个汇率在不同银行做交换的平均值。 给了Sample:
bank1, EURRMB, 1.11
bank1, EURRMB, 1.12
bank2,  EURRMB, 1.14
bank2, , UDSRMB, 7.3
同一种外汇交易在一个银行只用保存最近一次的数值，所以在sample data里getcurrency EURRMB的结果应该是 (1.12 + 1.14) / 2 = 1.13
"""
class Currency:
    def __init__(self):
        self.bankCurrency = {} # key is the concatenation of bank and currency, value is the currency value
        self.currency = {} # key is currency, value is a list [total count, total value]

    def add(self, bank, currency, value):
        """
        add currency value of a bank to system
        if the value already exists, overwrite the existing one
        """
        encode = bank + '#' + currency
        diff = value
        if encode in self.bankCurrency:
            # update existing bank and currency, only add diff to maps
            diff = value - self.bankCurrency[encode]
            count, total = self.currency[currency]
            total += diff
            self.currency[currency] = [count, total]
        else:
            # add non-existing bank and currency, add value to maps
            count, total = self.currency.get(currency, [0, 0.0])
            count += 1
            total += value
            self.currency[currency] = [count, total]
        self.bankCurrency[encode] = value

    def getCurrency(self, currency):
        if currency not in self.currency:
            raise NameError("Currency {} doesn't exist")
        count, total = self.currency[currency]
        return total/count


cur = Currency()
cur.add("bank1", "EURRMB", 1.11)
cur.add("bank2", "EURRMB", 1.14)
cur.add("bank2", "UDSRMB", 7.3)
print(cur.bankCurrency)
print(cur.currency)
print(cur.getCurrency("EURRMB"))
cur.add("bank1", "EURRMB", 1.12)
print(cur.getCurrency("EURRMB"))