# 🛍️ LojaMaster — Sistema de Gestão Comercial

**LojaMaster** é o sistema definitivo para quem quer levar sua loja para o próximo nível. Gerencie produtos, categorias, fornecedores, clientes, vendas e muito mais — tudo num ambiente elegante e eficiente.  

## 🚀 Funcionalidades Principais

- 📦 **Gestão de Produtos e Categorias**
- 🧾 **Controle de Estoque**
- 🤝 **Cadastro de Fornecedores e Clientes**
- 💰 **Controle de Vendas e Pagamentos**
- 🔐 **Sistema de Login por Usuário**
- 📈 **Relatórios e Visualização com Gráficos**

---

## 🛠️ Tecnologias Utilizadas

- PHP (com PDO ou Laravel)
- MySQL
- HTML5 + CSS3
- JavaScript (com Chart.js)
- PHPMailer (envio de e-mails)
- PDF Generator (dompdf ou SnappyPDF)

---

## 📚 Instalação

```bash
# Clone o projeto
git clone https://github.com/seu-usuario/lojamaster.git

# Acesse a pasta
cd lojamaster

# Instale as dependências (se estiver usando Laravel)
composer install

# Configure o .env
cp .env.example .env

# Gere a chave
php artisan key:generate

# Crie as tabelas
php artisan migrate
