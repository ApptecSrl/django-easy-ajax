from django.utils.module_loading import import_string


class Selector(object):

    def __init__(self, module_path=None, id=None):
        if (module_path is not None) and (id is not None):
            func = import_string(module_path)
            self.execute = func

    def execute(self, id=None):
        raise NotImplementedError
