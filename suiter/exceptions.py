class Error(Exception):
    """Base class for other exceptions"""
    pass

class LimitExceededError(Error):
    """ Raised when some limit is exceeded """
    def __init__(self, module, method, message):
        self.module = module
        self.method = method
        self.message = message

class TemplateError(Error):
    """ Raised when there is something wrong with a template """
    def __init__(self, module, method, message):
        self.module = module
        self.method = method
        self.message = message

class OpenFileError(Error):
    """ Raised when something is wrong with opening some file """
    def __init__(self, module, method, message):
        self.module = module
        self.method = method
        self.message = message  