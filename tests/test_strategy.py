#!/usr/bin/env python3
import pytest
import random

from src.monopoly.strategies import (
    ImpulsiveStrategy,
    DemandingStrategy,
    CarefulStrategy,
    RandomStrategy,
)


class TestImpulsiveStrategy:
    @pytest.fixture
    def strategy(self):
        return ImpulsiveStrategy()

    def test_impulsive_strategy(self, strategy):
        assert strategy.valid_purchase(0, 0, 0)

    @pytest.mark.parametrize(
        "player_cash, property_square_price, property_square_rent",
        [
            (0, 0, 0),
            (2, 1, 0),
            (1, 1, 0),
        ],
    )
    def test_impulsive_strategy_buys_any(
        self, strategy, player_cash, property_square_price, property_square_rent
    ):
        assert strategy.valid_purchase(
            player_cash, property_square_price, property_square_rent
        )


class TestDemandingStrategy:
    @pytest.fixture
    def strategy(self):
        return DemandingStrategy(50)

    def test_demanding_strategy_buys_property_with_rent_above_50(self, strategy):
        assert strategy.valid_purchase(0, 0, 51)

    def test_demanding_strategy_does_not_buy_property_with_rent_equals_50(
        self, strategy
    ):
        assert not strategy.valid_purchase(0, 0, 50)

    def test_demanding_strategy_does_not_buy_property_with_rent_bellow_50(
        self, strategy
    ):
        assert not strategy.valid_purchase(0, 0, 49)


class TestCarefulStrategy:
    @pytest.fixture
    def strategy(self):
        return CarefulStrategy(80)

    def test_careful_strategy_79_cash_left(self, strategy):
        assert not strategy.valid_purchase(79, 0, 0)

    def test_careful_strategy_80_cash_left(self, strategy):
        assert strategy.valid_purchase(80, 0, 0)

    def test_careful_strategy_80_cash_left(self, strategy):
        assert strategy.valid_purchase(81, 0, 0)


class TestRandomStrategy:
    @pytest.fixture
    def strategy(self):
        random.seed()
        return RandomStrategy(0.5)

    def test_random_strategy_with_seed(self, strategy):
        random.seed(0)  # yelds 0.8444218515250481
        s = strategy.valid_purchase(0, 0, 0)
        random.seed()
        assert s

    def test_random_strategy_with_probability(self, strategy):
        sample_size = 1_000_000
        trials = [strategy.valid_purchase(0, 0, 0) for _ in range(sample_size)]
        avg = sum(trials) / sample_size
        assert avg - 0.01 < 0.5 < avg + 0.01
