class AuthRouter:
    def db_for_read(self, model, **hints):
        """Controla la base de datos para lecturas de autenticación."""
        if model._meta.app_label == 'auth' or model._meta.app_label == 'contenttypes':
            return 'default'
        return None

    def db_for_write(self, model, **hints):
        """Controla la base de datos para escrituras de autenticación."""
        if model._meta.app_label == 'auth' or model._meta.app_label == 'contenttypes':
            return 'default'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Controla qué base de datos permite migraciones para autenticación."""
        if app_label in ['auth', 'contenttypes', 'admin', 'sessions']:
            return db == 'default'
        return None
