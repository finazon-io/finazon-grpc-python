import operator
import textwrap

from google.protobuf.json_format import MessageToDict


def add_null_obj_values(obj, columns) -> dict:
    for col in columns:
        if col not in obj:
            obj[col] = None
    return obj


def convert_collection_to_pandas(val):
    """
    Converts list/dict to DataFrame

    :param val: list or dict
    :rtype: pandas.DataFrame
    """
    try:
        import pandas
    except ImportError:
        raise ImportError(
            textwrap.dedent(
                """
                    No module named 'pandas'. You can install it with follow command:

                    > pip install finazon-grpc-python[pandas] 

                    or 

                    > pip install pandas
                """
            ).strip()
        )

    if isinstance(val, (list, tuple)):
        if len(val) == 0:
            return pandas.DataFrame()
        else:
            columns_beg = tuple(val[0].keys())
            columns_end = tuple(val[-1].keys())
            get_row = operator.itemgetter(*columns_end)
            data = [get_row(add_null_obj_values(obj, columns_end)) if
                    columns_beg != columns_end else
                    get_row(obj) for obj in val]
            return pandas.DataFrame(data, columns=columns_end)
    elif isinstance(val, dict):
        try:
            return pandas.DataFrame.from_dict(val, orient='index', dtype='float')
        except ValueError:
            return pandas.DataFrame.from_dict(
                {'data_key': val}, orient='index', dtype='object'
            )
    else:
        raise ValueError('Expected list, tuple or dict, but {} found'.format(type(val)))


def convert_response_to_dict(response) -> dict:
    return MessageToDict(response)


def convert_response_to_pandas(response):
    """
    :rtype: pandas.DataFrame
    """
    d = convert_response_to_dict(response)
    return convert_collection_to_pandas(d['result'] if d and 'result' in d else [])
