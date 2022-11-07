#!/usr/bin/env python3
import pytest

from src.monopoly.properties import BaseProperty
from src.monopoly import settings


class TestBaseProperty:
    @pytest.fixture
    def my_property(self):
        return BaseProperty

    def test_property_starts_with_no_onwer(self, my_property):
        assert my_property.owner is None


class TestBasePropertyProbabilities:
    sample_size = 100_000

    @pytest.fixture
    def trials(self):
        trials = []
        for _ in range(self.sample_size):
            p = BaseProperty()
            trials.append((p.price, p.rent))
        return trials

    def test_property_price_generation_with_probability(self, trials):
        actual_avg = sum([p for p, r in trials]) / self.sample_size
        assert actual_avg - 1 < 275 < actual_avg + 1

    def test_property_rent_generation_with_probability(self, trials):
        actual_avg = sum([r for p, r in trials]) / self.sample_size
        assert actual_avg - 1 < 125 < actual_avg + 1

    def test_property_price_range(self, trials):
        assert min([p for p, r in trials]) >= settings.MIN_PRICE
        assert max([p for p, r in trials]) <= settings.MAX_PRICE
