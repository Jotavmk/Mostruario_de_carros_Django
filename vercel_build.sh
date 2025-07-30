#!/bin/bash
# vercel_build.sh
echo "Instalando dependências..."
pip install -r requirements.txt

echo "Coletando arquivos estáticos..."
python manage.py collectstatic --noinput --clear

echo "Executando migrações..."
python manage.py migrate --noinput

echo "Build concluído!" 