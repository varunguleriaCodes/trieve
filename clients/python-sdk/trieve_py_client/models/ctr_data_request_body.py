# coding: utf-8

"""
    Trieve API

    Trieve OpenAPI Specification. This document describes all of the operations available through the Trieve API.

    The version of the OpenAPI document: 0.11.8
    Contact: developers@trieve.ai
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from trieve_py_client.models.ctr_type import CTRType
from typing import Optional, Set
from typing_extensions import Self

class CTRDataRequestBody(BaseModel):
    """
    CTRDataRequestBody
    """ # noqa: E501
    clicked_chunk_id: Optional[StrictStr] = Field(default=None, description="The ID of chunk that was clicked")
    clicked_chunk_tracking_id: Optional[StrictStr] = Field(default=None, description="The tracking ID of the chunk that was clicked")
    ctr_type: CTRType
    metadata: Optional[Any] = Field(default=None, description="Any metadata you want to include with the event i.e. action, user_id, etc.")
    position: StrictInt = Field(description="The position of the clicked chunk")
    request_id: StrictStr = Field(description="The request id for the CTR data")
    __properties: ClassVar[List[str]] = ["clicked_chunk_id", "clicked_chunk_tracking_id", "ctr_type", "metadata", "position", "request_id"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of CTRDataRequestBody from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if clicked_chunk_id (nullable) is None
        # and model_fields_set contains the field
        if self.clicked_chunk_id is None and "clicked_chunk_id" in self.model_fields_set:
            _dict['clicked_chunk_id'] = None

        # set to None if clicked_chunk_tracking_id (nullable) is None
        # and model_fields_set contains the field
        if self.clicked_chunk_tracking_id is None and "clicked_chunk_tracking_id" in self.model_fields_set:
            _dict['clicked_chunk_tracking_id'] = None

        # set to None if metadata (nullable) is None
        # and model_fields_set contains the field
        if self.metadata is None and "metadata" in self.model_fields_set:
            _dict['metadata'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CTRDataRequestBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "clicked_chunk_id": obj.get("clicked_chunk_id"),
            "clicked_chunk_tracking_id": obj.get("clicked_chunk_tracking_id"),
            "ctr_type": obj.get("ctr_type"),
            "metadata": obj.get("metadata"),
            "position": obj.get("position"),
            "request_id": obj.get("request_id")
        })
        return _obj

