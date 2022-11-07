#!/usr/bin/env python3

from abc import ABC, abstractmethod
from dataclasses import dataclass

import random


class BaseStrategy(ABC):
    @abstractmethod
    def valid_purchase(self, player_cash, property_square_price, property_square_rent):
        ...


class ImpulsiveStrategy(BaseStrategy):
    """
    O jogador impulsivo compra qualquer propriedade sobre a qual ele parar.
    """

    def valid_purchase(self, player_cash, property_square_price, property_square_rent):
        return True


@dataclass
class DemandingStrategy(BaseStrategy):
    """
    O jogador exigente compra qualquer propriedade, desde que o valor do
    aluguel dela seja maior do que 50.
    """

    target_min_rent: int = 50

    def valid_purchase(self, player_cash, property_square_price, property_square_rent):
        return property_square_rent > self.target_min_rent


@dataclass
class CarefulStrategy(BaseStrategy):
    """
    O jogador cauteloso compra qualquer propriedade desde que ele tenha uma
    reserva de 80 saldo sobrando depois de realizada a compra.
    """

    target_min_cash: int = 80

    def valid_purchase(self, player_cash, property_square_price, property_square_rent):
        return player_cash - property_square_price >= self.target_min_cash


@dataclass
class RandomStrategy(BaseStrategy):
    """
    O jogador aleatório compra a propriedade que ele parar em cima com
    probabilidade de 50%.
    """

    target_chance: int = 0.5

    def _calculate_chance(self):
        return random.random()

    def valid_purchase(self, player_cash, property_square_price, property_square_rent):
        calculated_chance = self._calculate_chance()
        return calculated_chance > self.target_chance
