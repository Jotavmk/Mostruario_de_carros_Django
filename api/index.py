import os
import sys
from pathlib import Path

# Adiciona o diretório do projeto ao path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# Configura as variáveis de ambiente
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'loja_carros.settings')

# Importa a aplicação Django
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# Para Vercel
app = application 