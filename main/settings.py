from django.conf import settings
import os

settings.ADMIN_EMAIL = 'admin@example.com'

settings.MAIL_FROM = 'admin@example.com'

settings.STATICFILES_DIRS += (
        os.path.join(settings.BASE_DIR, "main", "static"),
)
