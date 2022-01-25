""" 
This file includes http and tiktok exceptions

## Reference

https://ads.tiktok.com/marketing_api/docs?id=1701890984602626
"""


class BaseError(Exception):
    def __init__(self, message, response, *args, **kwargs):
        super().__init__(message, *args, **kwargs)
        self.response = response


class BadRequestError(BaseError):
    pass


class UnauthorizedError(BaseError):
    pass


class ForbiddenError(BaseError):
    pass


class NotFoundError(BaseError):
    pass


class GoneError(BaseError):
    pass


class UnsupportedMediaTypeError(BaseError):
    pass


class UnprocessableEntityError(BaseError):
    pass


class TooManyRequestsError(BaseError):
    pass


class InternalServerError(BaseError):
    pass


class NotImplementedError(BaseError):
    pass


class ServiceUnavailableError(BaseError):
    pass


class UnknownError(BaseError):
    pass


class UncategorizedError(BaseError):
    pass


class InvalidParameterError(BaseError):
    pass


class FilterFieldError(BaseError):
    pass


class UnsupportedInterfaceError(BaseError):
    pass


class SystemError(BaseError):
    pass


class AppIdSecretMismatchError(BaseError):
    pass


class ExpiredAccessTokenError(BaseError):
    pass


class InvalidAccessTokenError(BaseError):
    pass


class EmptyAccessTokenError(BaseError):
    pass


class AuthorizationTypeError(BaseError):
    pass


class AuthorizationCodeError(BaseError):
    pass


class MaxSuccessfulCallsExceededError(BaseError):
    pass


class AppNotFoundError(BaseError):
    pass


class AdvertiserCompanyMismatchError(BaseError):
    pass


class AdvertiserNotFoundError(BaseError):
    pass


class AdvertiserRoleError(BaseError):
    pass


class FileSignatureError(BaseError):
    pass


class VideoIsTranscodingError(BaseError):
    pass


class FetchImageTimeoutError(BaseError):
    pass


class IllegalImageContentError(BaseError):
    pass


class FileNotFoundError(BaseError):
    pass


class EmptyFileError(BaseError):
    pass


class ExceptionFactory:
    mapping = {
        400: BadRequestError,
        401: UnauthorizedError,
        403: ForbiddenError,
        404: NotFoundError,
        410: GoneError,
        415: UnsupportedMediaTypeError,
        422: UnprocessableEntityError,
        429: TooManyRequestsError,
        500: InternalServerError,
        501: NotImplementedError,
        503: ServiceUnavailableError,
        40001: InvalidParameterError,
        40002: ForbiddenError,
        40003: FilterFieldError,
        40008: UnsupportedInterfaceError,
        40100: TooManyRequestsError,
        40101: AppIdSecretMismatchError,
        40102: ExpiredAccessTokenError,
        # 40103: ExpiredRefreshTokenError,
        40104: EmptyAccessTokenError,
        40105: InvalidAccessTokenError,
        # 40107: InvalidRefreshTokenError,
        40108: AuthorizationTypeError,
        40110: AuthorizationCodeError,
        40111: MaxSuccessfulCallsExceededError,
        40113: AppNotFoundError,
        40115: AdvertiserCompanyMismatchError,
        40118: ForbiddenError,
        40300: AdvertiserNotFoundError,
        40301: AdvertiserRoleError,
        40700: UncategorizedError,
        40900: FileSignatureError,
        40901: VideoIsTranscodingError,
        40902: FetchImageTimeoutError,
        40904: IllegalImageContentError,
        40905: FileNotFoundError,
        40906: EmptyFileError,
        50000: SystemError,
    }

    def get_exception(self, code, message, response):
        exception = self.mapping.get(code, UnknownError)
        return exception(message, response)
