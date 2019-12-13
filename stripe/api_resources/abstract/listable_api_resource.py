from __future__ import absolute_import, division, print_function

from stripe import api_requestor, util
from stripe.api_resources.abstract.api_resource import APIResource
from stripe.http_client import AsyncClient


class ListableAPIResource(APIResource):
    @classmethod
    def auto_paging_iter(cls, *args, **params):
        return cls.list(*args, **params).auto_paging_iter()
    @classmethod
    async def async_auto_paging_iter(cls, *args, **params):
        return cls.async_list(*args, **params).async_auto_paging_iter()

    @classmethod
    def list(
        cls, api_key=None, stripe_version=None, stripe_account=None, **params
    ):
        requestor = api_requestor.APIRequestor(
            api_key,
            api_base=cls.api_base(),
            api_version=stripe_version,
            account=stripe_account,
        )
        url = cls.class_url()
        response, api_key = requestor.request("get", url, params)
        stripe_object = util.convert_to_stripe_object(
            response, api_key, stripe_version, stripe_account
        )
        stripe_object._retrieve_params = params
        return stripe_object

    @classmethod
    async def async_list(
        cls, api_key=None, stripe_version=None, stripe_account=None, **params
    ):
        requestor = api_requestor.APIRequestor(
            api_key,
            api_base=cls.api_base(),
            api_version=stripe_version,
            account=stripe_account,
        )
        url = cls.class_url()
        response, api_key = await requestor.async_request("get", url, params)
        stripe_object = util.convert_to_stripe_object(
            response, api_key, stripe_version, stripe_account
        )
        stripe_object._retrieve_params = params
        return stripe_object
