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

from trieve_py_client.models.search_cluster_response import SearchClusterResponse

class TestSearchClusterResponse(unittest.TestCase):
    """SearchClusterResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SearchClusterResponse:
        """Test SearchClusterResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SearchClusterResponse`
        """
        model = SearchClusterResponse()
        if include_optional:
            return SearchClusterResponse(
                clusters = [
                    trieve_py_client.models.search_cluster_topics.SearchClusterTopics(
                        avg_score = 1.337, 
                        created_at = '', 
                        dataset_id = '', 
                        density = 56, 
                        id = '', 
                        topic = '', )
                    ]
            )
        else:
            return SearchClusterResponse(
                clusters = [
                    trieve_py_client.models.search_cluster_topics.SearchClusterTopics(
                        avg_score = 1.337, 
                        created_at = '', 
                        dataset_id = '', 
                        density = 56, 
                        id = '', 
                        topic = '', )
                    ],
        )
        """

    def testSearchClusterResponse(self):
        """Test SearchClusterResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
