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
import logging
import grpc
from finazon_grpc_python.time_series_pb2_grpc import TimeSeriesServiceStub
from finazon_grpc_python.time_series_pb2 import GetTimeSeriesRequest, GetTimeSeriesResponse


api_url = 'grpc-latest.finazon.io:443'
api_token = 'your_api_key'

# Setup gRPC credentials
call_credentials = grpc.access_token_call_credentials(api_token)
channel_credentials = grpc.ssl_channel_credentials()
credentials = grpc.composite_channel_credentials(channel_credentials, call_credentials)

try:
    # Open gRPC channel and call method
    with grpc.secure_channel(api_url, credentials=credentials) as channel:
        stub = TimeSeriesServiceStub(channel)
        request = GetTimeSeriesRequest(ticker="AAPL", dataset="sip_non_pro")
        response: GetTimeSeriesResponse = stub.GetTimeSeries(request)

        # Iterate over time series response result
        for item in response.result:
            print(item)
# Catch gRPC exceptions
except grpc.RpcError as e:
    if e.code() == grpc.StatusCode.UNAUTHENTICATED:
        logging.error('Invalid API key was provided')
    else:
        logging.error(f'gRPC exception: {e}')

```

### 4. Input your API key
Replace `'your_api_key'` with your actual key.

### 5. Run script
```bash
python3 time_series.py
```
📝 Expected output:
```
timestamp: 1698955140
open: 177.57
close: 177.57
high: 177.78
low: 177.55
volume: 8330379

timestamp: 1698955080
open: 177.58
close: 177.572
high: 177.605
low: 177.5317
volume: 398134

timestamp: 1698955020
open: 177.67
close: 177.58
high: 177.69
low: 177.56
volume: 439780

...
```

👀 Check the full example and other examples [here](https://github.com/finazon-io/finazon-grpc-python/tree/main/examples)


## RPC support

The following table outlines the supported rpc calls:
<!--rpc_table_boundary-->
| Service              | rpc                       | Description                                        |
|----------------------|---------------------------|----------------------------------------------------|
| ApiUsageService      | GetApiUsage               | Get a list of products with quota limit/usage      |
| BenzingaService      | GetDividentsCalendar      | Returns the dividends calendar from Benzinga       |
| BenzingaService      | GetEarningsCalendar       | Returns the earnings calendar from Benzinga        |
| BenzingaService      | GetNews                   | Returns the news articles from Benzinga            |
| BenzingaService      | GetIPO                    | Returns IPO data from Benzinga                     |
| BinanceService       | GetTimeSeries             | Get time series data without technical indicators  |
| CryptoService        | GetTimeSeries             | Get time series data for any given ticker          |
| DatasetsService      | GetDatasets               | Get a list of all datasets available at Finazon    |
| ExchangeService      | GetMarketsCrypto          | Returns a list of supported crypto markets         |
| ExchangeService      | GetMarketsStocks          | Returns a list of supported stock markets          |
| ForexService         | GetTimeSeries             | Get time series data for any given ticker          |
| PublisherService     | GetPublishers             | Get a list of all publishers available at Finazon  |
| SecService           | GetFilings                | Real-time and historical access to all forms, filings, and exhibits directly from the SEC's EDGAR system |
| SipService           | GetTrades                 | Returns detailed information on trades executed through the Securities Information Processor (SIP) |
| SipService           | GetMarketCenter           | Returns a list of market centers                   |
| SnapshotService      | GetSnapshot               | This endpoint returns a combination of different data points, such as daily performance, last quote, last trade, minute data, and previous day performance |
| TickersService       | FindTickersStocks         | This API call returns an array of stocks tickers available at Finazon Data API. This list is updated daily |
| TickersService       | FindTickersCrypto         | This API call returns an array of crypto tickers available at Finazon Data API. This list is updated daily |
| TickersService       | FindTickersForex          | This API call returns an array of forex tickers available at Finazon Data API. This list is updated daily |
| TickersService       | FindTickerUS              | This API call returns an array of US tickers available at Finazon Data API. This list is updated daily |
| TimeSeriesService    | GetTimeSeries             | Get time series data without technical indicators  |
| TimeSeriesService    | GetTimeSeriesAtr          | Get time series data for ATR technical indicator   |
| TimeSeriesService    | GetTimeSeriesBBands       | Get time series data for BBands technical indicator |
| TimeSeriesService    | GetTimeSeriesIchimoku     | Get time series data for Ichimoku technical indicator |
| TimeSeriesService    | GetTimeSeriesMa           | Get time series data for Ma technical indicator    |
| TimeSeriesService    | GetTimeSeriesMacd         | Get time series data for Macd technical indicator  |
| TimeSeriesService    | GetTimeSeriesObv          | Get time series data for Obv technical indicator   |
| TimeSeriesService    | GetTimeSeriesRsi          | Get time series data for Rsi technical indicator   |
| TimeSeriesService    | GetTimeSeriesSar          | Get time series data for Sar technical indicator   |
| TimeSeriesService    | GetTimeSeriesStoch        | Get time series data for Stoch technical indicator |
| TradeService         | GetTrades                 | Returns general information on executed trades     |
<!--rpc_table_boundary-->
Here's how you can import `stub` and `request` objects:

```python
from finazon_grpc_python.service_name_pb2_grpc import ServiceNameServiceStub
from finazon_grpc_python.service_name_pb2 import RpcNameRequest, RpcNameResponse

# ...

stub = ServiceNameStub(channel)
response = stub.RpcName(RpcNameRequest())
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
