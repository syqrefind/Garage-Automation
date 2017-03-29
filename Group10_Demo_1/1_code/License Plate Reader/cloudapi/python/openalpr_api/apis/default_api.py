# coding: utf-8

"""
DefaultApi.py
Copyright 2015 SmartBear Software

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

from __future__ import absolute_import

import sys
import os

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class DefaultApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def recognize_post(self, secret_key, tasks, image, **kwargs):
        """
        
        Send an image for OpenALPR to analyze and provide metadata back

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.recognize_post(secret_key, tasks, image, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str secret_key: The secret key used to authenticate your account.  You can view your \nsecret key by visiting \nhttps://cloud.openalpr.com/ (required)
        :param list[str] tasks: Tasks to execute.  You can choose to detect the license plate, \nas well as additional metadata about the vehicle.  Each additional \noption costs an API credit. (required)
        :param file image: The image file that you wish to analyze\nAt least one value for image, image_bytes, or image_url must be provided (required)
        :param str image_bytes: The image file that you wish to analyze encoded in base64\nAt least one value for image, image_bytes, or image_url must be provided
        :param str image_url: A URL to an image that you wish to analyze\nAt least one value for image, image_bytes, or image_url must be provided
        :param str country: Defines the training data used by OpenALPR.  \"us\" analyzes \nNorth-American style plates.  \"eu\" analyzes European-style plates.\n\nThis field is required if using the \"plate\" task\n\nYou may use multiple datasets by using commas between the country \ncodes.  For example, 'au,auwide' would analyze using both the \nAustralian plate styles.  A full list of supported country codes \ncan be found here\nhttps://github.com/openalpr/openalpr/tree/master/runtime_data/config
        :param str state: Corresponds to a US state or EU country code used by OpenALPR pattern \nrecognition.  For example, using \"md\" matches US plates against the \nMaryland plate patterns.  Using \"fr\" matches European plates against \nthe French plate patterns.
        :param int return_image: If set to 1, the image you uploaded will be encoded in base64 and \nsent back along with the response
        :param int topn: The number of results you would like to be returned for plate \ncandidates and vehicle classifications
        :param str prewarp: Prewarp configuration is used to calibrate the analyses for the \nangle of a particular camera.  More information is available here\nhttp://doc.openalpr.com/accuracy_improvements.html#calibration
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['secret_key', 'tasks', 'image', 'image_bytes', 'image_url', 'country', 'state', 'return_image', 'topn', 'prewarp']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method recognize_post" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'secret_key' is set
        if ('secret_key' not in params) or (params['secret_key'] is None):
            raise ValueError("Missing the required parameter `secret_key` when calling `recognize_post`")
        # verify the required parameter 'tasks' is set
        if ('tasks' not in params) or (params['tasks'] is None):
            raise ValueError("Missing the required parameter `tasks` when calling `recognize_post`")
        # verify the required parameter 'image' is set
        if ('image' not in params) or (params['image'] is None):
            raise ValueError("Missing the required parameter `image` when calling `recognize_post`")

        resource_path = '/recognize'.replace('{format}', 'json')
        method = 'POST'

        path_params = {}

        query_params = {}
        if 'secret_key' in params:
            query_params['secret_key'] = params['secret_key']
        if 'tasks' in params:
            query_params['tasks'] = params['tasks']
        if 'image_url' in params:
            query_params['image_url'] = params['image_url']
        if 'country' in params:
            query_params['country'] = params['country']
        if 'state' in params:
            query_params['state'] = params['state']
        if 'return_image' in params:
            query_params['return_image'] = params['return_image']
        if 'topn' in params:
            query_params['topn'] = params['topn']
        if 'prewarp' in params:
            query_params['prewarp'] = params['prewarp']

        header_params = {}

        form_params = {}
        files = {}
        if 'image' in params:
            files['image'] = params['image']

        body_params = None

        if 'image_bytes' in params:
            form_params['image_bytes'] = params['image_bytes']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['multipart/form-data'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, method,
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=files,
                                            response_type='InlineResponse200',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response
