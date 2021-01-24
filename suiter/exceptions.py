
class Error(Exception):
    """Base class for other exceptions"""
    pass

class LimitExceededError(Error):
    """Raised when the maximum limit has been exceeded"""
    pass

# class ValueTooSmallError(Error):
#     """Raised when the input value is too small"""
#     pass

# class ValueTooLargeError(Error):
#     """Raised when the input value is too large"""
#     pass