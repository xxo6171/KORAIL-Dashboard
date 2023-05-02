from dataclasses import dataclass
import numpy as np


@dataclass
class Model:
    _date: str
    _data: np.array
    _objectId: np.uint8 = None

    @property
    def date(self) -> str:
        return self._date

    @property
    def data(self) -> np.array:
        return self._data

    @property
    def objectId(self) -> np.uint8:
        return self._objectId

    @objectId.setter
    def objectId(self, object_id: np.uint8) -> None:
        self._objectId = object_id
