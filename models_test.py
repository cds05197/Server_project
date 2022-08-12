import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from django.contrib.auth.models import User
from Board.models import Board

for i in range(100):
  p = Board(title='Test_Board_{}'.format(i), content='Board Test Content', author=User.objects.get(id=1))
  p.save()

  
  
  
  
  
