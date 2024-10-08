# coding: utf-8

"""
    Trieve API

    Trieve OpenAPI Specification. This document describes all of the operations available through the Trieve API.

    The version of the OpenAPI document: 0.11.8
    Contact: developers@trieve.ai
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from trieve_py_client.models.chunk_metadata_types import ChunkMetadataTypes

class TestChunkMetadataTypes(unittest.TestCase):
    """ChunkMetadataTypes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ChunkMetadataTypes:
        """Test ChunkMetadataTypes
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ChunkMetadataTypes`
        """
        model = ChunkMetadataTypes()
        if include_optional:
            return ChunkMetadataTypes(
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                dataset_id = '',
                id = '',
                image_urls = [
                    ''
                    ],
                link = '',
                location = trieve_py_client.models.geo_info.GeoInfo(
                    lat = null, 
                    lon = null, ),
                metadata = None,
                num_value = 1.337,
                tag_set = '',
                time_stamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                tracking_id = '',
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                weight = 1.337,
                chunk_html = ''
            )
        else:
            return ChunkMetadataTypes(
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                dataset_id = '',
                id = '',
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                weight = 1.337,
        )
        """

    def testChunkMetadataTypes(self):
        """Test ChunkMetadataTypes"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
