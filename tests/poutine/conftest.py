import pytest


def pytest_collection_modifyitems(items):
    for item in items:
        if "init" not in item.keywords:
            item.add_marker(pytest.mark.init(rng_seed=123))