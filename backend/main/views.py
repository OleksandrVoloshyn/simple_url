from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .services import get_or_create_short_url, get_url_for_redirect, get_top_urls


class MainView(APIView):
    """get or create simple url"""

    def post(self, *args, **kwargs):
        front = self.request.META['HTTP_ORIGIN']
        url_base = self.request.data.get('url')
        url_result = get_or_create_short_url(url_base, front)
        return Response({'url_result': url_result}, status.HTTP_200_OK)


class GetTopURLSView(APIView):
    """get top clickable urls by QueryParams 'top' """

    def get(self, *args, **kwargs):
        top_list = get_top_urls(self.request.query_params.get('top'))
        return Response({'top_list': top_list}, status.HTTP_200_OK)


class RedirectView(APIView):
    """get base url from simple one if not exist return False"""

    def get(self, *args, **kwargs):
        res = get_url_for_redirect(kwargs.get('data'))
        return Response({'result': res}, status.HTTP_200_OK)
