from typing import Union, Iterator
import psycopg2
import pandas as pd
from pandas import DataFrame
from src.exceptions import DBConnectException


class Postgresql:
    def __init__(self, **kwargs):
        try:
            self._db = psycopg2.connect(**kwargs)
        except Exception:
            raise DBConnectException()

    def query(self, sql: str) -> Union[DataFrame, Iterator[DataFrame]]:
        return pd.read_sql_query(sql, self._db)

    def close(self):
        self._db.close()
