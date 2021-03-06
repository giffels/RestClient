from RestClient.RequestHandling.HTTPRequest import HTTPRequest

import pycurl

class RestApi(object):
    def __init__(self, auth=None, proxy=None, additional_curl_options=None, use_shared_handle=False):
        self._curl = pycurl.Curl()
        self._curl_options = {}

        if use_shared_handle:
            ###use shared SSL Session ID caches when operating multi-threaded
            shared_curl = pycurl.CurlShare()
            shared_curl.setopt(pycurl.SH_SHARE, pycurl.LOCK_DATA_SSL_SESSION)
            self._curl.setopt(pycurl.SHARE, shared_curl)

        if additional_curl_options:
            self._curl_options.update(additional_curl_options)

        if auth:
            self._curl_options.update(auth.configure_auth())
        if proxy:
            self._curl_options.update(proxy.configure_proxy())

    def __del__(self):
        self._curl.close()

    def get(self, url, api, params={}, data=None, request_headers={}):
        http_request = HTTPRequest(method='GET', url=url, api=api, params=params, data=data,
                                   request_headers=request_headers,
                                   curl_options=self._curl_options)
        return http_request(self._curl)

    def post(self, url, api, params={}, data="", request_headers={}):
        http_request = HTTPRequest(method='POST', url=url, api=api, params=params, data=data,
                                   request_headers=request_headers,
                                   curl_options=self._curl_options)
        return http_request(self._curl)

    def put(self, url, api, params={}, data="", request_headers={}):
        http_request = HTTPRequest(method='PUT', url=url, api=api, params=params, data=data,
                                   request_headers=request_headers,
                                   curl_options=self._curl_options)
        return http_request(self._curl)

    def delete(self, url, api, params={}, data=None, request_headers={}):
        http_request = HTTPRequest(method='DELETE', url=url, api=api, params=params, data=data,
                                   request_headers=request_headers,
                                   curl_options=self._curl_options)
        return http_request(self._curl)
