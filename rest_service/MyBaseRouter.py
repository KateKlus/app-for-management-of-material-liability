class MyBaseRouter(object):
    def db_for_read(self, model, **kwargs):
        if model._meta.app_label == 'rest_service':
            return 'MO_base'

        if model._meta.app_label == 'glpi':
            return 'glpi1'

        if model._meta.app_label == 'clientapp':
            return 'glpi1'
        return None