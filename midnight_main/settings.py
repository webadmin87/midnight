from django.conf import settings
import os

settings.STATICFILES_DIRS += (
        os.path.join(settings.BASE_DIR, "midnight_main", "static"),
)

# Settings
#
# MIDNIGHT_MAIN_ADMIN_EMAIL = 'admin@example.com'
# MIDNIGHT_MAIN_MAIL_FROM = 'admin@example.com'
# MIDNIGHT_MAIN_PAGE_TPL_CHOICES = models.Page.PAGE_TPL_CHOICES

