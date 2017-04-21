import importlib

config = {}


def load(phase):
    res = importlib.import_module('cfg.' + phase)
    config.update(res.config)
    return config

