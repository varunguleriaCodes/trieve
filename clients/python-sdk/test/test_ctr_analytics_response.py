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

from trieve_py_client.models.ctr_analytics_response import CTRAnalyticsResponse

class TestCTRAnalyticsResponse(unittest.TestCase):
    """CTRAnalyticsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CTRAnalyticsResponse:
        """Test CTRAnalyticsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CTRAnalyticsResponse`
        """
        model = CTRAnalyticsResponse()
        if include_optional:
            return CTRAnalyticsResponse(
                avg_position_of_click = 1.337,
                percent_searches_with_clicks = 1.337,
                percent_searches_without_clicks = 1.337,
                searches_with_clicks = 56,
                queries = [
                    trieve_py_client.models.search_queries_with_clicks_ctr_response.SearchQueriesWithClicksCTRResponse(
                        clicked_chunks = [
                            {"chunk_html":"<p>Hello, world!</p>","created_at":"2021-01-01 00:00:00.000","dataset_id":"e3e3e3e3-e3e3-e3e3-e3e3-e3e3e3e3e3e3","id":"e3e3e3e3-e3e3-e3e3-e3e3-e3e3e3e3e3e3","link":"https://trieve.ai","metadata":{"key":"value"},"tag_set":"[tag1,tag2]","time_stamp":"2021-01-01 00:00:00.000","tracking_id":"e3e3e3e3-e3e3-e3e3-e3e3-e3e3e3e3e3e3","updated_at":"2021-01-01 00:00:00.000","weight":0.5}
                            ], 
                        created_at = '', 
                        positions = [
                            56
                            ], 
                        query = '', )
                    ],
                percent_recommendations_with_clicks = 1.337,
                percent_recommendations_without_clicks = 1.337,
                recommendations_with_clicks = 56,
                recommendations = [
                    trieve_py_client.models.recommendations_with_clicks_ctr_response.RecommendationsWithClicksCTRResponse(
                        clicked_chunks = [
                            {"chunk_html":"<p>Hello, world!</p>","created_at":"2021-01-01 00:00:00.000","dataset_id":"e3e3e3e3-e3e3-e3e3-e3e3-e3e3e3e3e3e3","id":"e3e3e3e3-e3e3-e3e3-e3e3-e3e3e3e3e3e3","link":"https://trieve.ai","metadata":{"key":"value"},"tag_set":"[tag1,tag2]","time_stamp":"2021-01-01 00:00:00.000","tracking_id":"e3e3e3e3-e3e3-e3e3-e3e3-e3e3e3e3e3e3","updated_at":"2021-01-01 00:00:00.000","weight":0.5}
                            ], 
                        created_at = '', 
                        negative_ids = [
                            ''
                            ], 
                        negative_tracking_ids = [
                            ''
                            ], 
                        positions = [
                            56
                            ], 
                        positive_ids = [
                            ''
                            ], 
                        positive_tracking_ids = [
                            ''
                            ], )
                    ]
            )
        else:
            return CTRAnalyticsResponse(
                avg_position_of_click = 1.337,
                percent_searches_with_clicks = 1.337,
                percent_searches_without_clicks = 1.337,
                searches_with_clicks = 56,
                queries = [
                    trieve_py_client.models.search_queries_with_clicks_ctr_response.SearchQueriesWithClicksCTRResponse(
                        clicked_chunks = [
                            {"chunk_html":"<p>Hello, world!</p>","created_at":"2021-01-01 00:00:00.000","dataset_id":"e3e3e3e3-e3e3-e3e3-e3e3-e3e3e3e3e3e3","id":"e3e3e3e3-e3e3-e3e3-e3e3-e3e3e3e3e3e3","link":"https://trieve.ai","metadata":{"key":"value"},"tag_set":"[tag1,tag2]","time_stamp":"2021-01-01 00:00:00.000","tracking_id":"e3e3e3e3-e3e3-e3e3-e3e3-e3e3e3e3e3e3","updated_at":"2021-01-01 00:00:00.000","weight":0.5}
                            ], 
                        created_at = '', 
                        positions = [
                            56
                            ], 
                        query = '', )
                    ],
                percent_recommendations_with_clicks = 1.337,
                percent_recommendations_without_clicks = 1.337,
                recommendations_with_clicks = 56,
                recommendations = [
                    trieve_py_client.models.recommendations_with_clicks_ctr_response.RecommendationsWithClicksCTRResponse(
                        clicked_chunks = [
                            {"chunk_html":"<p>Hello, world!</p>","created_at":"2021-01-01 00:00:00.000","dataset_id":"e3e3e3e3-e3e3-e3e3-e3e3-e3e3e3e3e3e3","id":"e3e3e3e3-e3e3-e3e3-e3e3-e3e3e3e3e3e3","link":"https://trieve.ai","metadata":{"key":"value"},"tag_set":"[tag1,tag2]","time_stamp":"2021-01-01 00:00:00.000","tracking_id":"e3e3e3e3-e3e3-e3e3-e3e3-e3e3e3e3e3e3","updated_at":"2021-01-01 00:00:00.000","weight":0.5}
                            ], 
                        created_at = '', 
                        negative_ids = [
                            ''
                            ], 
                        negative_tracking_ids = [
                            ''
                            ], 
                        positions = [
                            56
                            ], 
                        positive_ids = [
                            ''
                            ], 
                        positive_tracking_ids = [
                            ''
                            ], )
                    ],
        )
        """

    def testCTRAnalyticsResponse(self):
        """Test CTRAnalyticsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
