from lumibot.brokers import Alpaca
from lumibot.backtesting import YahooDataBacktesting
from lumibot.strategies.strategy import Strategy
from lumibot.traders import Trader
from datetime import datetime
"""from lumibot.brokers import Alpaca: Dòng này nhập lớp Alpaca từ mô-đun brokers của thư viện lumibot. Trong ngữ cảnh này, Alpaca có thể là một lớp hoặc đối tượng được sử dụng để tương tác với API của Alpaca, một dịch vụ giao dịch chứng khoán trực tuyến.
from lumibot.backtesting import YahooDataBacktesting: Dòng này nhập lớp YahooDataBacktesting từ mô-đun backtesting của thư viện lumibot. Trong ngữ cảnh này, YahooDataBacktesting có thể là một lớp hoặc đối tượng được sử dụng để thực hiện việc backtesting (kiểm thử lịch sử) các chiến lược giao dịch với dữ liệu từ dịch vụ Yahoo Finance.
from lumibot.strategies.strategy import Strategy: Dòng này nhập lớp Strategy từ mô-đun strategy của thư viện lumibot. Trong ngữ cảnh này, Strategy có thể là một lớp hoặc đối tượng được sử dụng để định nghĩa các chiến lược giao dịch cho các hệ thống giao dịch tự động.

from lumibot.traders import Trader: Dòng này nhập lớp Trader từ mô-đun traders của thư viện lumibot. Trong ngữ cảnh này, Trader có thể là một lớp hoặc đối tượng được sử dụng để thực hiện các giao dịch trên các sàn giao dịch chứng khoán.

from datetime import datetime: Dòng này nhập hàm datetime từ mô-đun datetime trong Python. Trong ngữ cảnh này, datetime được sử dụng để làm việc với các đối tượng ngày và giờ.

Các dòng mã này có vẻ là nhập các thành phần cần thiết từ thư viện lumibot để thực hiện các hoạt động liên quan đến giao dịch chứng khoán, backtesting và quản lý chiến lược giao dịch."""

API_KEY = "PKONLN2EMM048DUF66R7"
API_SECRET = "C3IhBQoodbigtjkgFCqmQmUhvySwKhs8hJjTsw4E"
BASE_URL = "https://paper-api.alpaca.markets"

ALPACA_CREDS = {
    "API_KEY": API_KEY,
    "API_SECRET": API_SECRET,
    "PAPER": True
} 

class MLTrader(Strategy): ##tạo thành xương sống cho bot giao dịch##
    def initialize(self, symbol:str="SPY"):
        self.symbol = symbol
        self.sleeptime = "24H"
        self.last_trade = None

        ##bên B
    def position_sizing(self):
        cash = self.get_cash()
        last_price = self.get_last_price (self.symbol)



    def on_trading_iteration(self):##phương thức lập giao dịch##
        if self.last_trade == None:
            order = self.create_order(
                self.symbol,
                10,
                "buy",
                type="market"
            )
            self.submit_order(order)
            self.last_trade = "buy"

## Tạo ngày bắt đầu và ngày kết thúc##
start_date = datetime(2023,12,15)
end_date = datetime(2023,12,31)

broker = Alpaca(ALPACA_CREDS)
strategy = MLTrader(name='mlstart', broker = broker, parameters={"symbol":"SPY"})
strategy.backtest(
    YahooDataBacktesting,
    start_date,
    end_date,
   parameters={"symbol":"SPY"}
)