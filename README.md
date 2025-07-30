# JV Carros - Mostruário de Veículos

Mostruário de veículos feito em Django.

## Funcionalidades

- ✅ Sistema de login e registro de usuários
- ✅ Listagem de carros com filtros
- ✅ Detalhes completos dos carros
- ✅ Sistema de compra de carros
- ✅ Histórico de compras do usuário
- ✅ Perfil do usuário
- ✅ Interface responsiva e moderna
- ✅ CSS separado em arquivo próprio
- ✅ Banco de dados SQLite
- ✅ Relacionamento 1 para N

## Tecnologias Utilizadas

- **Backend**: Django 5.2.4
- **Banco de Dados**: SQLite
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Ícones**: Font Awesome
- **Imagens**: Pillow (PIL)

## Estrutura do Projeto

```
Loja_de_carros_django/
├── loja_carros/          # Configurações do projeto
├── vendas/               # App principal
│   ├── models.py         # Modelos Carro e Compra
│   ├── views.py          # Views do sistema
│   ├── urls.py           # URLs do app
│   ├── forms.py          # Formulários
│   └── admin.py          # Configuração do admin
├── templates/            # Templates HTML
│   ├── base.html         # Template base
│   ├── home.html         # Página inicial
│   ├── login.html        # Login
│   ├── register.html     # Registro
│   ├── carros_list.html  # Lista de carros
│   ├── carro_detail.html # Detalhes do carro
│   ├── comprar_carro.html # Confirmação de compra
│   ├── minhas_compras.html # Histórico de compras
│   └── perfil.html       # Perfil do usuário
├── static/               # Arquivos estáticos
│   └── css/
│       └── style.css     # CSS personalizado
├── media/                # Upload de imagens
└── db.sqlite3           # Banco de dados
```

## Instalação e Configuração

### 1. Clone o repositório
```bash
git clone <url-do-repositorio>
cd Loja_de_carros_django
```

### 2. Instale as dependências
```bash
pip install Django Pillow
```

### 3. Execute as migrações
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Crie um superusuário (opcional)
```bash
python manage.py createsuperuser
```

### 5. Popule o banco com dados de exemplo
```bash
python populate_cars.py
```

### 6. Execute o servidor
```bash
python manage.py runserver
```

### 7. Acesse o sistema
- **Site principal**: http://127.0.0.1:8000/
- **Admin**: http://127.0.0.1:8000/admin/

## Modelos de Dados

### Carro
- `marca`: Marca do carro (choices)
- `modelo`: Modelo do carro
- `ano`: Ano de fabricação
- `preco`: Preço do carro
- `quilometragem`: Quilometragem atual
- `combustivel`: Tipo de combustível (choices)
- `cor`: Cor do carro
- `descricao`: Descrição detalhada
- `imagem`: Imagem do carro (opcional)
- `disponivel`: Status de disponibilidade
- `data_cadastro`: Data de cadastro

### Compra
- `comprador`: Usuário que comprou (ForeignKey)
- `carro`: Carro comprado (ForeignKey)
- `data_compra`: Data da compra
- `preco_pago`: Preço pago na compra

## Funcionalidades do Sistema

### Para Visitantes
- Visualizar carros disponíveis
- Ver detalhes dos carros
- Fazer login ou registro

### Para Usuários Logados
- Todas as funcionalidades de visitantes
- Comprar carros
- Ver histórico de compras
- Acessar perfil pessoal

### Para Administradores
- Gerenciar carros via admin
- Visualizar todas as compras
- Adicionar/editar carros

## Filtros Disponíveis

- **Busca por texto**: Marca, modelo ou descrição
- **Filtro por marca**: Todas as marcas disponíveis
- **Filtro por preço**: Preço mínimo e máximo
- **Ordenação**: Por data de cadastro (mais recentes primeiro)

## Design e Interface

- **Responsivo**: Funciona em desktop, tablet e mobile
- **Moderno**: Design limpo e profissional
- **Intuitivo**: Navegação fácil e clara
- **CSS Separado**: Arquivo `static/css/style.css` com estilos personalizados

## Segurança

- Autenticação de usuários
- Proteção CSRF
- Validação de formulários
- Controle de acesso às páginas

## Próximas Melhorias

- [ ] Sistema de avaliações
- [ ] Chat entre comprador e vendedor
- [ ] Sistema de pagamento
- [ ] Notificações por email
- [ ] Upload múltiplo de imagens
- [ ] Sistema de favoritos
- [ ] Relatórios de vendas

## Contribuição

Sinta-se à vontade para contribuir com melhorias, correções de bugs ou novas funcionalidades!

## Licença

Este projeto está sob a licença MIT. 