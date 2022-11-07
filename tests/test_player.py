#!/usr/bin/env python3
import pytest

from src.monopoly.players import BasePlayer

from src.monopoly.strategies import ImpulsiveStrategy


class TestBasePlayer:
    @pytest.fixture
    def player(self):
        return BasePlayer(strategy=ImpulsiveStrategy)

    def test_base_player_starts_with_300_cash(self, player):
        assert player.cash == 300

    def test_player_starts_in_race(self, player):
        assert player.in_race

    def test_simple_player(self, player):
        assert player

    def test_player_can_buy(self, player):
        assert player.can_buy(100)

    def test_player_with_less_than_zero_cash_is_not_on_race(self, player):
        player.cash = 0
        assert not player.in_race

    def test_player_not_in_race_cant_check_a_purchase(self, player):
        player.cash = 0
        with pytest.raises(RuntimeError):
            player.can_buy(1)
