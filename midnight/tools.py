import importlib


def get_class_from_string(cls):
    module_name, class_name = cls.rsplit(".", 1)
    module = importlib.import_module(module_name)
    return getattr(module, class_name)
