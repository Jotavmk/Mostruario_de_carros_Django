# Deploy no Vercel - JV Carros

## 📋 Pré-requisitos

1. Conta no Vercel (gratuita)
2. Projeto no GitHub/GitLab
3. Python 3.11+

## 🚀 Passos para Deploy

### 1. Preparar o Projeto

Certifique-se de que todos os arquivos estão commitados:

```bash
git add .
git commit -m "Configuração para Vercel"
git push
```

### 2. Conectar ao Vercel

1. Acesse [vercel.com](https://vercel.com)
2. Faça login com sua conta GitHub
3. Clique em "New Project"
4. Importe seu repositório
5. Configure as seguintes variáveis de ambiente:

### 3. Variáveis de Ambiente

No painel do Vercel, adicione estas variáveis:

```
DEBUG=False
SECRET_KEY=sua-chave-secreta-aqui
```

### 4. Configurações do Projeto

O projeto já está configurado com:

- ✅ `vercel.json` - Configuração do Vercel
- ✅ `requirements.txt` - Dependências Python
- ✅ `runtime.txt` - Versão do Python
- ✅ `api/index.py` - Endpoint para Vercel
- ✅ `build_files.sh` - Script de build
- ✅ Configurações de produção no `settings.py`

### 5. Deploy

1. Clique em "Deploy" no Vercel
2. Aguarde o build (pode demorar alguns minutos)
3. Acesse o link fornecido

## 🔧 Solução de Problemas

### Erro 404
- Verifique se o `vercel.json` está correto
- Confirme se o `api/index.py` existe
- Verifique se o `wsgi.py` está configurado

### Erro de Dependências
- Verifique se o `requirements.txt` está atualizado
- Confirme se a versão do Python está correta

### Erro de Arquivos Estáticos
- Execute `python manage.py collectstatic` localmente
- Verifique se o WhiteNoise está configurado

## 📁 Estrutura para Vercel

```
Loja_de_carros_django/
├── vercel.json              # Configuração do Vercel
├── requirements.txt          # Dependências Python
├── runtime.txt              # Versão do Python
├── api/
│   └── index.py            # Endpoint para Vercel
├── loja_carros/
│   ├── settings.py         # Configurações Django
│   └── wsgi.py            # WSGI para Vercel
└── build_files.sh          # Script de build
```

## 🌐 URLs Importantes

- **Site**: https://seu-projeto.vercel.app
- **Admin**: https://seu-projeto.vercel.app/admin/

## ⚠️ Limitações do Vercel

1. **Banco de Dados**: SQLite não funciona no Vercel (stateless)
2. **Upload de Arquivos**: Não persistente
3. **Sessões**: Não persistentes

## 🔄 Próximos Passos

Para um projeto completo em produção, considere:

1. **Banco de Dados**: PostgreSQL (Railway, Supabase)
2. **Upload de Arquivos**: AWS S3, Cloudinary
3. **Sessões**: Redis
4. **Email**: SendGrid, Mailgun

## 📞 Suporte

Se encontrar problemas:

1. Verifique os logs no Vercel
2. Teste localmente com `DEBUG=False`
3. Verifique se todas as dependências estão no `requirements.txt` 