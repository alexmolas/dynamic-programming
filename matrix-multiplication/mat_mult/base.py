import abc
from typing import Tuple


class MatrixChainMultiplication(abc.ABC):
    @abc.abstractmethod
    def get_min_cost(self, dims: Tuple[int]) -> int:
        ...

    @abc.abstractmethod
    def get_best_order(self, dims: Tuple[int]) -> str:
        ...

