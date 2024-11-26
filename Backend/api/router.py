class SecondaryDatabaseRouter:
    """
    Router para asignar modelos específicos a la base de datos secundaria (secondary_db).
    """

    def db_for_read(self, model, **hints):
        if model._meta.db_table in ['facturas', 'api_facturas']:
            return 'secondary_db'
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.db_table in ['facturas', 'api_facturas']:
            return 'secondary_db'
        return 'default'

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        # Tablas específicas para secondary_db
        if db == 'secondary_db':
            return model_name in ['factura', 'apifactura']

        # Todas las demás tablas deben ir a primary_db
        if db == 'default':
            return model_name not in ['factura', 'apifactura']

        return False
