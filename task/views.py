from .services import Utils
from django.http import JsonResponse
from rest_framework.views import APIView

class CreateUniqueIdentifier(APIView):

    def get(self, request, namespace):
        ip = self._get_ip_(request)
        namespace = "{unique_id}".format(unique_id=Utils(namespace,ip)._unique_id())
        return JsonResponse({"namespace": namespace}, status=201)

    def _get_ip_(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
