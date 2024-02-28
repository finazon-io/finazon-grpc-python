# Finazon Python gRPC Client

This is the official Python library for Finazon, offering access to:
- Lists of datasets, publishers, markets, and tickers.
- Market data: ticker snapshots, time series, trades, and technical indicators.
- Data from specific datasets such as Benzinga, Binance, Crypto, Forex, SEC, and SIP.

🔑 **API key** is essential. If you haven't got one yet, [sign up here](https://finazon.io/).

## Requirements
Ensure you have Python 3.8 or later. 

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Finazon Python gRPC Client library:
```shell
pip install finazon-grpc-python
```
Or use [poetry](https://python-poetry.org/) package manager to add Finazon Python gRPC Client library to your project:
```shell
poetry add finazon-grpc-python
```

🔗 View the package on [PyPI](https://pypi.org/project/finazon-grpc-python/).

## Updating to last version
Using pip:
```shell
pip install -U finazon-grpc-python
```
Using poetry:
```shell
poetry add finazon-grpc-python@latest
```

## Quick start

### 1. Create project virtual environment (venv)
```shell
mkdir hello-finazon && cd hello-finazon
python3 -m venv .venv
```

Activate venv (Linux/MacOS)
```shell
source .venv/bin/activate
```

Activate venv (Windows cmd.exe)
```shell
<full_path_to_project>\.venv\Scripts\activate.bat
```

More information about Python virtual environments can be found [here](https://docs.python.org/3/library/venv.html )

### 2. Install package
```shell
pip install finazon-grpc-python
```

### 3. Create `time_series.py` script
```python
from finazon_grpc_python.time_series_service import TimeSeriesService, GetTimeSeriesRequest
from finazon_grpc_python.common.errors import FinazonGrpcRequestError


service = TimeSeriesService('your_api_key')

try:
    request = GetTimeSeriesRequest(ticker='AAPL', dataset='sip_non_pro', interval='1h')
    response = service.get_time_series(request)
    print('Last 1h candle for AAPL:\n')
    print(response.result[0])
except FinazonGrpcRequestError as e:
    print(f'Received error, code: {e.code}, message: {e.message}')

```

### 4. Input your API key
Replace `'your_api_key'` with your actual key.

### 5. Run script
```bash
python3 time_series.py
```
📝 Expected output:
```
Last 1h candle for AAPL:

timestamp: 1709071200
open: 183.03
close: 182.985
high: 183.05
low: 182.93
volume: 32163
```

👀 Check the full example and other examples [here](https://github.com/finazon-io/finazon-grpc-python/tree/main/finazon_grpc_python/examples)


## RPC support

The following table outlines the supported rpc calls:
<!--rpc_table_boundary-->
| Service              | rpc                       | Description                                        |
|----------------------|---------------------------|----------------------------------------------------|
| ApiUsageService      | get_api_usage             | Get a list of products with quota limit/usage      |
| BenzingaService      | get_dividents_calendar    | Returns the dividends calendar from Benzinga       |
| BenzingaService      | get_earnings_calendar     | Returns the earnings calendar from Benzinga        |
| BenzingaService      | get_news                  | Returns the news articles from Benzinga            |
| BenzingaService      | get_ipo                   | Returns IPO data from Benzinga                     |
| BinanceService       | get_time_series           | Get time series data without technical indicators  |
| CryptoService        | get_time_series           | Get time series data for any given ticker          |
| DatasetsService      | get_datasets              | Get a list of all datasets available at Finazon    |
| ExchangeService      | get_markets_crypto        | Returns a list of supported crypto markets         |
| ExchangeService      | get_markets_stocks        | Returns a list of supported stock markets          |
| ForexService         | get_time_series           | Get time series data for any given ticker          |
| PublisherService     | get_publishers            | Get a list of all publishers available at Finazon  |
| SecService           | get_filings               | Real-time and historical access to all forms, filings, and exhibits directly from the SEC's EDGAR system |
| SipService           | get_trades                | Returns detailed information on trades executed through the Securities Information Processor (SIP) |
| SipService           | get_market_center         | Returns a list of market centers                   |
| SnapshotService      | get_snapshot              | This endpoint returns a combination of different data points, such as daily performance, last quote, last trade, minute data, and previous day performance |
| TickersService       | find_tickers_stocks       | This API call returns an array of stocks tickers available at Finazon Data API. This list is updated daily |
| TickersService       | find_tickers_crypto       | This API call returns an array of crypto tickers available at Finazon Data API. This list is updated daily |
| TickersService       | find_tickers_forex        | This API call returns an array of forex tickers available at Finazon Data API. This list is updated daily |
| TickersService       | find_ticker_us            | This API call returns an array of US tickers available at Finazon Data API. This list is updated daily |
| TimeSeriesService    | get_time_series           | Get time series data without technical indicators  |
| TimeSeriesService    | get_time_series_atr       | Get time series data for ATR technical indicator   |
| TimeSeriesService    | get_time_series_b_bands   | Get time series data for BBands technical indicator |
| TimeSeriesService    | get_time_series_ichimoku  | Get time series data for Ichimoku technical indicator |
| TimeSeriesService    | get_time_series_ma        | Get time series data for Ma technical indicator    |
| TimeSeriesService    | get_time_series_macd      | Get time series data for Macd technical indicator  |
| TimeSeriesService    | get_time_series_obv       | Get time series data for Obv technical indicator   |
| TimeSeriesService    | get_time_series_rsi       | Get time series data for Rsi technical indicator   |
| TimeSeriesService    | get_time_series_sar       | Get time series data for Sar technical indicator   |
| TimeSeriesService    | get_time_series_stoch     | Get time series data for Stoch technical indicator |
| TradeService         | get_trades                | Returns general information on executed trades     |
<!--rpc_table_boundary-->
Here's how you can import `service` and `request` objects:

```python
from finazon_grpc_python.service_name_service import ServiceNameService, RpcNameRequest

# ...

service = ServiceNameService('your_api_key')
response = service.rpc_name(RpcNameRequest())
```

## Documentation
Delve deeper with our [official documentation](https://finazon.io/docs).

## Examples
Explore practical scenarios in the [examples](https://github.com/finazon-io/finazon-grpc-python/tree/main/examples) directory.

## Support
- 🌐 Visit our [contact page](https://finazon.io/contact-sales).
- 🛠 Or our [support center](https://support.finazon.io/en/).

## Stay updated
- Follow us on [𝕏](https://twitter.com/finazon_io).
- Join our community on [Discord](https://discord.gg/D5u4ZpB7w7).
- Follow us on [LinkedIn](https://www.linkedin.com/company/finazon).

## Contributing
1. Fork and clone: `$ git clone https://github.com/finazon-io/finazon-grpc-python.git`.
2. Branch out: `$ cd finazon-grpc-python && git checkout -b my-feature`.
3. Commit changes and test.
4. Push your branch and open a pull request with a comprehensive description.

For more guidance on contributing, see the [GitHub Docs](https://docs.github.com/en/get-started/quickstart/contributing-to-projects) on GitHub.

## License

This project is licensed under the MIT License. See the `LICENSE.txt` file in this repository for more details.
