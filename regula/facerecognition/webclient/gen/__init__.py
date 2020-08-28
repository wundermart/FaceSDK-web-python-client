# coding: utf-8

# flake8: noqa

"""
    Regula Face Recognition Web API

    Regula Face Recognition Web API  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

__version__ = "1.0.0"

# import apis into sdk package
from regula.facerecognition.webclient.gen.api.matching_api import MatchingApi

# import ApiClient
from regula.facerecognition.webclient.gen.api_client import ApiClient
from regula.facerecognition.webclient.gen.configuration import Configuration
from regula.facerecognition.webclient.gen.exceptions import OpenApiException
from regula.facerecognition.webclient.gen.exceptions import ApiTypeError
from regula.facerecognition.webclient.gen.exceptions import ApiValueError
from regula.facerecognition.webclient.gen.exceptions import ApiKeyError
from regula.facerecognition.webclient.gen.exceptions import ApiAttributeError
from regula.facerecognition.webclient.gen.exceptions import ApiException
# import models into sdk package
from regula.facerecognition.webclient.gen.models.compare_request import CompareRequest
from regula.facerecognition.webclient.gen.models.compare_request_fields import CompareRequestFields
from regula.facerecognition.webclient.gen.models.compare_response import CompareResponse
from regula.facerecognition.webclient.gen.models.compare_response_fields import CompareResponseFields
from regula.facerecognition.webclient.gen.models.image_source import ImageSource
from regula.facerecognition.webclient.gen.models.operation_log import OperationLog
