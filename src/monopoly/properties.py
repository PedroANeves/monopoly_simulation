#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Union
from dataclasses import dataclass, field

from src.monopoly.players import BasePlayer
from src.monopoly import settings

import random


def generate_price():
    random.seed()
    return random.randint(settings.MIN_PRICE, settings.MAX_PRICE)


def generate_rent():
    random.seed()
    return random.randint(settings.MIN_RENT, settings.MAX_RENT)


@dataclass
class BaseProperty:
    price: int = field(default_factory=generate_price)
    rent: int = field(default_factory=generate_rent)
    owner: Union[BasePlayer, None] = None
