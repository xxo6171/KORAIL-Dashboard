from dataclasses import dataclass
import numpy as np

@dataclass
class Model:
    _date: str
    _data: np.array

    @property
    def date(self) -> str:
        return self._date

    @property
    def data(self) -> np.array:
        return self._data

    @data.setter
    def data(self, value: np.array):
        self._data = value