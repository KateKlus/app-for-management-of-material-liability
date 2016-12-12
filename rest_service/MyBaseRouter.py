class MyBaseRouter(object):
    def db_for_read(self, model, **kwargs):
        if model._meta.app_label == 'rest_service':
            return 'my_base'

        if model._meta.app_label == 'glpi':
            return 'glpi'
        return None