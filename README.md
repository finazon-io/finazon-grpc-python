# finazon-grpc-python
Finazon gRPC client library for Python

## Requirements
Python >= 3.8

## Installation

Via pip
```shell
pip install finazon-grpc-python
```
Via poetry
```shell
poetry add finazon-grpc-python
```

## Usage example
See [examples](https://github.com/finazon-io/finazon-grpc-python/tree/main/examples)

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
| DatasetsService      | GetDatasets               | Get a list of all datasets available at Finazon    |
| ExchangeService      | GetMarketsCrypto          | Returns a list of supported crypto markets         |
| ExchangeService      | GetMarketsStocks          | Returns a list of supported stock markets          |
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

## License

This project is licensed under the MIT License. See the `LICENSE.txt` file in this repository for more details.
