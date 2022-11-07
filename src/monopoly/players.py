#!/usr/bin/env python3

from abc import ABC, abstractmethod
from dataclasses import dataclass

from src.monopoly.strategies import BaseStrategy


@dataclass
class BasePlayer(ABC):
    strategy: BaseStrategy
    cash = 300

    @property
    def in_race(self):
        return self.cash > 0

    def can_buy(self, property_price: int):
        if self.in_race:
            return self.cash >= property_price
        else:
            raise RuntimeError("Player has not cash therefore is not in the race.")

    def should_buy(self, property_square):
        if self.can_buy(property_square.price):
            return self.strategy.valid_purchase(
                self.cash, property_square.price, property_square.rent
            )
