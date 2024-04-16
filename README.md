# Finazon Python gRPC Client

This is the official Python library for Finazon, offering access to:
- Lists of datasets, publishers, markets, and tickers.
- Market data: ticker snapshots, time series, trades, and technical indicators.
- Data from specific datasets such as Benzinga, Binance, Crypto, Forex, SEC, and SIP.

🔑 **API key** is essential. If you haven't got one yet, [sign up here](https://finazon.io/).

## Requirements
Ensure you have Python 3.9 or later.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Finazon Python gRPC Client library:
```shell
pip install finazon-grpc-python
```
Installation with Pandas support:
```bash
pip install finazon-grpc-python[pandas]
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
    request = GetTimeSeriesRequest(ticker='AAPL', dataset='sip_non_pro', interval='1h', page_size=10)
    response = service.get_time_series(request)
    print('Last OHLCV data\n')
    for item in response.result:
        print(f'{item.timestamp} - {item.open}, {item.high}, {item.low}, {item.close}, {item.volume}')
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
Last OHLCV data

1709323200 - 179.9312, 179.97, 179.415, 179.695, 7701993.0
1709319600 - 179.315, 180.22, 179.31, 180.005, 6668926.0
1709316000 - 178.515, 179.39, 178.33, 179.32, 6103415.0
1709312400 - 177.83, 179.07, 177.38, 178.524, 7184233.0
1709308800 - 178.1857, 178.47, 177.72, 177.935, 7477704.0
1709305200 - 179.7, 179.71, 177.67, 178.295, 13846621.0
1709301600 - 180.2, 180.53, 179.06, 179.245, 6952951.0
1709236800 - 180.225, 181.11, 179.57, 180.93, 12124375.0
1709233200 - 180.115, 180.49, 179.86, 180.2, 5406568.0
1709229600 - 180.15, 180.8, 179.68, 180.085, 5891427.0
```

## More examples

### Get time-series data for AAPL and convert it to Pandas dataframe

Don't forget to install the package with Pandas support
```bash
pip install finazon-grpc-python[pandas]
```
```python
from finazon_grpc_python.time_series_service import TimeSeriesService, GetTimeSeriesRequest
from finazon_grpc_python.common.errors import FinazonGrpcRequestError
from finazon_grpc_python.common.utils import convert_response_to_pandas


service = TimeSeriesService('your_api_key')

try:
    request = GetTimeSeriesRequest(ticker='AAPL', dataset='us_stocks_essential', interval='1h', page_size=50)
    response = service.get_time_series(request)
    df = convert_response_to_pandas(response)
    print(df.describe())
except FinazonGrpcRequestError as e:
    print(f'Received error, code: {e.code}, message: {e.message}')
```

### Get Moving average with period 100 (MA 100) for AAPL

```python
from finazon_grpc_python.time_series_service import TimeSeriesService, GetTimeSeriesMaRequest, GetTimeSeriesRequest
from finazon_grpc_python.common.errors import FinazonGrpcRequestError


service = TimeSeriesService('your_api_key')

try:
    request = GetTimeSeriesMaRequest(
        time_series=GetTimeSeriesRequest(ticker='AAPL', interval='1h', dataset='sip_non_pro', page_size=10),
        time_period=100,
    )
    response = service.get_time_series_ma(request)
    print(response.result)
except FinazonGrpcRequestError as e:
    print(f'Received error, code: {e.code}, message: {e.message}')
```

👀 Check the full example and other examples [here](https://github.com/finazon-io/finazon-grpc-python/tree/main/finazon_grpc_python/examples)

## RPC support

The following table outlines the supported rpc calls:
|Service                |rpc                        |Description                                                                                                                                                      |
|-----------------------|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ApiUsageService       | getApiUsage               | Get a list of products with quota limit/usage                                                                                                                   |
| BenzingaService       | getDividentsCalendar      | Returns the dividends calendar from Benzinga                                                                                                                    |
| BenzingaService       | getEarningsCalendar       | Returns the earnings calendar from Benzinga                                                                                                                     |
| BenzingaService       | getNews                   | Returns the news articles from Benzinga                                                                                                                         |
| BenzingaService       | getIPO                    | Returns IPO data from Benzinga                                                                                                                                  |
| BinanceService        | getTimeSeries             | Get time series data without technical indicators                                                                                                               |
| CryptoService         | getTimeSeries             | Get time series data for any given ticker                                                                                                                       |
| DatasetsService       | getDatasets               | Get a list of all datasets available at Finazon.                                                                                                                |
| ExchangeService       | getMarketsCrypto          | Returns a list of supported crypto markets                                                                                                                      |
| ExchangeService       | getMarketsStocks          | Returns a list of supported stock markets                                                                                                                       |
| ForexService          | getTimeSeries             | Get time series data for any given ticker                                                                                                                       |
| PublisherService      | getPublishers             | Get a list of all publishers available at Finazon.                                                                                                              |
| SecService            | getFilings                | Real-time and historical access to all forms, filings, and exhibits directly from the SEC's EDGAR system.                                                       |
| SipService            | getTrades                 | Returns detailed information on trades executed through the Securities Information Processor (SIP)                                                              |
| SipService            | getMarketCenter           | Returns a list of market centers                                                                                                                                |
| SnapshotService       | getSnapshot               | This endpoint returns a combination of different data points, such as daily performance, last quote, last trade, minute data, and previous day performance.     |
| TickersService        | findTickersStocks         | This API call returns an array of stocks tickers available at Finazon Data API. This list is updated daily.                                                     |
| TickersService        | findTickersCrypto         | This API call returns an array of crypto tickers available at Finazon Data API. This list is updated daily.                                                     |
| TickersService        | findTickersForex          | This API call returns an array of forex tickers available at Finazon Data API. This list is updated daily.                                                      |
| TickersService        | findTickersUS             | This API call returns an array of US tickers available at Finazon Data API. This list is updated daily.                                                         |
| TimeSeriesService     | getTimeSeries             | Get time series data without technical indicators                                                                                                               |
| TimeSeriesService     | getTimeSeriesAtr          | Get time series data for ATR technical indicator.                                                                                                               |
| TimeSeriesService     | getTimeSeriesBBands       | Get time series data for BBands technical indicator.                                                                                                            |
| TimeSeriesService     | getTimeSeriesIchimoku     | Get time series data for Ichimoku technical indicator.                                                                                                          |
| TimeSeriesService     | getTimeSeriesMa           | Get time series data for Ma technical indicator.                                                                                                                |
| TimeSeriesService     | getTimeSeriesMacd         | Get time series data for Macd technical indicator.                                                                                                              |
| TimeSeriesService     | getTimeSeriesObv          | Get time series data for Obv technical indicator.                                                                                                               |
| TimeSeriesService     | getTimeSeriesRsi          | Get time series data for Rsi technical indicator.                                                                                                               |
| TimeSeriesService     | getTimeSeriesSar          | Get time series data for Sar technical indicator.                                                                                                               |
| TimeSeriesService     | getTimeSeriesStoch        | Get time series data for Stoch technical indicator.                                                                                                             |
| TradeService          | getTrades                 | Returns general information on executed trades                                                                                                                  |

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
Explore practical scenarios in the [examples](https://github.com/finazon-io/finazon-grpc-python/tree/main/finazon_grpc_python/examples) directory.

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