import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#finance classes
class Stock:
        def __init__(self, name, price, dividend):
            self.name = name
            self.price = price
            self.dividend = dividend
        def yield_dividend(self):
            return self.dividend / self.price

apple_stock = Stock('Apple', 120, 0.82)
google_stock = Stock('Google', 150, 0.82)
facebook_stock = Stock('Facebook', 130, 0.82)

print("Apple stock yield dividend: ", apple_stock.yield_dividend())

class Portfolio:
        def __init__(self, name):
            self.name = name
            self.instruments = []
                  
        def add_instrument(self, stock):
            self.instruments.append([stock.name, stock.price, stock.dividend])
        
        def total_value(self):
            test = 0
            for i in range(len(self.instruments)):
                test += self.instruments[i][1]
            return test

portfolio_1 = Portfolio('Portfolio_1')
portfolio_1.add_instrument(apple_stock)
portfolio_1.add_instrument(google_stock)
portfolio_1.add_instrument(facebook_stock)

print("Portfolio instruments: ", portfolio_1.instruments)
print("Portfolio total value: ", portfolio_1.total_value())

class CurrencyConverter:
        def __init__(self):
            self.conversion_rate = {}
                  
        def add_rate(self, pair, rate):
            self.conversion_rate[pair] = rate
            
        def convert(self, amount, source_currency, target_currency):
            return amount * self.conversion_rate[source_currency + "/" + target_currency]
    
currency_converter_1 = CurrencyConverter()
currency_converter_1.add_rate("EUR/USD", 1.05)
currency_converter_1.add_rate("USD/EUR", 0.95)
print("100 euros to usd: ", currency_converter_1.convert(100, "EUR", "USD"))

#2-assets portfolio returns and volatilities

asset_A = [0.1, 0.2]
asset_B = [0.15, 0.3]

weights_A = np.array([i/10 for i in range(11)])

weights_B = 1 - weights_A

returns = asset_B[0]*weights_B + asset_A[0]*weights_A

covA_B = 0.5

vola = (weights_B**2 * asset_B[1]**2 + weights_A**2 * asset_A[1]**2 + 2 * weights_A * weights_B * asset_A[1] * asset_B[1] * covA_B)**0.5
print("returns :", returns)
print("volatilities :", vola)

#finance plots
stock_prices_1 = [105, 103, 106, 109, 108, 107, 110, 112, 111, 113]
stock_prices_2 = [107, 108, 107, 107, 106, 108, 109, 108, 109, 110]

fig, ax1 = plt.subplots()
ax1.set_xlabel('Days')
ax1.set_ylabel('stock price 1', color='red')
ax1.plot(stock_prices_1, color='red', ls="solid")
ax1.tick_params(axis='y', labelcolor='red')

ax2 = ax1.twinx()
ax2.set_ylabel('stock price 2', color='blue')
ax2.plot(stock_prices_2, color='blue', ls="dotted")
ax2.tick_params(axis='y', labelcolor='blue')

plt.title('Stock Prices Over 10 Days')

plt.show()

returns = [0.05, -0.02, 0.03, -0.01, 0.02, 0.03, -0.03, 0.01, 0.04, -0.01]
sns.histplot(returns, bins=5)
plt.title("Distribution of Stock Returns")
plt.show()
