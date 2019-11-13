from rest_framework import viewsets, status
from seguridad.message_config import MESSAGES
import copy


class MainAppViewSetMixin(viewsets.ModelViewSet):
    """ Esta clase es un mixin de la clase ModelVieSet """

    # def list(self, request, *args, **kwargs):
    #     pass
    #
    # def retrieve(self, request, *args, **kwargs):
    #     pass

    def create(self, request, *args, **kwargs):
        response = super(MainAppViewSetMixin, self).create(request, *args, **kwargs)
        return self.build_reesponse(response)

    def destroy(self, request, *args, **kwargs):
        response = super(MainAppViewSetMixin, self).destroy(request, *args, **kwargs)
        return self.build_reesponse(response)

    def partial_update(self, request, *args, **kwargs):
        response = super(MainAppViewSetMixin, self).partial_update(request, *args, **kwargs)
        return self.build_reesponse(response)

    def update(self, request, *args, **kwargs):
        response = super(MainAppViewSetMixin, self).update(request, *args, **kwargs)
        return self.build_reesponse(response)

    def build_reesponse(self, response):
        """Retorna dado un objeto response otro response con el mensaje obtenido a partir de
        message_config"""
        id_message = self.get_serializer().Meta.model.__name__
        data = copy.copy(response.data)
        del response.data
        response.data = {'data': data}
        if id_message in MESSAGES and response.status_code in MESSAGES[id_message]:
            response.data['message'] = MESSAGES[id_message][response.status_code]['message']
            if 'description' in MESSAGES[id_message][response.status_code]:
                response.data['description'] = MESSAGES[id_message][response.status_code][
                    'description']
        else:
            response.data['message'] = id_message
            if 'description' in MESSAGES['GLOBAL'][response.status_code]:
                response.data['description'] = MESSAGES['GLOBAL'][response.status_code][
                    'description']
        return response
