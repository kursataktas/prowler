from prowler.exceptions.exceptions import ProwlerException


class S3BaseException(ProwlerException):
    """Base class for S3 exceptions."""

    S3_ERROR_CODES = {
        (2500, "S3TestConnectionError"): {
            "message": "Failed to test connection to S3 bucket.",
            "remediation": "Check the S3 bucket name and permissions.",
        }
    }

    def __init__(self, code, file=None, original_exception=None, message=None):
        module = "S3"
        error_info = self.S3_ERROR_CODES.get((code, self.__class__.__name__))
        if message:
            error_info["message"] = message
        super().__init__(
            code=code,
            provider=module,
            file=file,
            original_exception=original_exception,
            error_info=error_info,
        )


class S3TestConnectionError(S3BaseException):
    def __init__(self, file=None, original_exception=None, message=None):
        super().__init__(
            2500, file=file, original_exception=original_exception, message=message
        )
