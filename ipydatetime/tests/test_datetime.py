#!/usr/bin/env python
# coding: utf-8

# Copyright (c) Vidar Tonaas Fauske.
# Distributed under the terms of the Modified BSD License.

import pytest

import datetime

from traitlets import TraitError

from ..datetime_widget import DatetimePicker


def test_time_creation_blank():
    w = DatetimePicker()
    assert w.value is None


def test_time_creation_value():
    t = datetime.datetime.today()
    w = DatetimePicker(value=t)
    assert w.value is t


def test_time_validate_value_none():
    t = datetime.datetime(2002, 2, 20, 13, 37, 42, 7)
    t_min = datetime.datetime(1442, 1, 1)
    t_max = datetime.datetime(2056, 1, 1)
    w = DatetimePicker(value=t, min=t_min, max=t_max)
    w.value = None
    assert w.value is None


def test_time_validate_value_vs_min():
    t = datetime.datetime(2002, 2, 20, 13, 37, 42, 7)
    t_min = datetime.datetime(2019, 1, 1)
    t_max = datetime.datetime(2056, 1, 1)
    w = DatetimePicker(min=t_min, max=t_max)
    w.value = t
    assert w.value.year == 2019


def test_time_validate_value_vs_max():
    t = datetime.datetime(2002, 2, 20, 13, 37, 42, 7)
    t_min = datetime.datetime(1664, 1, 1)
    t_max = datetime.datetime(1994, 1, 1)
    w = DatetimePicker(min=t_min, max=t_max)
    w.value = t
    assert w.value.year == 1994


def test_time_validate_min_vs_value():
    t = datetime.datetime(2002, 2, 20, 13, 37, 42, 7)
    t_min = datetime.datetime(2019, 1, 1)
    t_max = datetime.datetime(2056, 1, 1)
    w = DatetimePicker(value=t, max=t_max)
    w.min = t_min
    assert w.value.year == 2019


def test_time_validate_min_vs_max():
    t = datetime.datetime(2002, 2, 20, 13, 37, 42, 7)
    t_min = datetime.datetime(2112, 1, 1)
    t_max = datetime.datetime(2056, 1, 1)
    w = DatetimePicker(value=t, max=t_max)
    with pytest.raises(TraitError):
        w.min = t_min


def test_time_validate_max_vs_value():
    t = datetime.datetime(2002, 2, 20, 13, 37, 42, 7)
    t_min = datetime.datetime(1664, 1, 1)
    t_max = datetime.datetime(1994, 1, 1)
    w = DatetimePicker(value=t, min=t_min)
    w.max = t_max
    assert w.value.year == 1994


def test_time_validate_max_vs_min():
    t = datetime.datetime(2002, 2, 20, 13, 37, 42, 7)
    t_min = datetime.datetime(1664, 1, 1)
    t_max = datetime.datetime(1337, 1, 1)
    w = DatetimePicker(value=t, min=t_min)
    with pytest.raises(TraitError):
        w.max = t_max
