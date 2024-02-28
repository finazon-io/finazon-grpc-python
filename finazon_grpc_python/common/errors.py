
class FinazonGrpcError(Exception):
    pass


class FinazonGrpcRequestError(FinazonGrpcError):
    def __init__(self, message: str, method: str, code: str):
        self.message = message
        self.method = method
        self.code = code

    def __reduce__(self):
        return FinazonGrpcRequestError, (self.message, self.method, self.code)


class FinazonGrpcUnauthorizedError(FinazonGrpcRequestError):
    pass


class FinazonGrpcPermissionDeniedError(FinazonGrpcRequestError):
    pass