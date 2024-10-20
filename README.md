# Calculadora em Python

Uma calculadora simples em Python para o trabalho da disciplina Entrega Contínua e DevOps (ECD11), que suporta operações básicas como adição, subtração, multiplicação e divisão.

## Estrutura do Projeto

calculadora-python/ 

├── src/ # Código fonte 

│ └── calculadora.py # Implementação da calculadora 

├── tests/ # Testes automatizados 

│ └── test_calculadora.py # Testes para a calculadora 

├── requirements.txt # Dependências 

├── Procfile                 # Indica como executar a aplicação no Heroku

├── .gitignore # Arquivos a serem ignorados 

└── README.md 

# Documentação do projeto

## Boas Práticas Utilizadas

1. **Organização do Código**: O código-fonte foi organizado em diretórios claros (`src` e `tests`), separando a lógica da aplicação dos testes automatizados. Isso facilita a manutenção e a navegação no projeto.

2. **Modularização**: As operações da calculadora estão encapsuladas em um único arquivo (`calculadora.py`), permitindo fácil extensão e adição de novas funcionalidades no futuro.

3. **Documentação do Código**: Docstrings foram usadas nas funções da calculadora para explicar seus propósitos, parâmetros e retornos, facilitando a compreensão do código.

4. **Controle de Versionamento**: O projeto utiliza Git para controle de versão, permitindo rastrear alterações e colaborar com outros desenvolvedores.

5. **Convenções de Commits**: Mensagens de commit seguem uma estrutura clara, utilizando tipos como `feat`, `fix`, e `docs` para categorizar as alterações.

6. **Estrutura de Branches**: A estrutura de branches foi utilizada para desenvolvimento de novas funcionalidades e correções de bugs, permitindo trabalho paralelo e revisão de código.

7. **Testes Automatizados**: O uso do pytest garante que as funcionalidades da calculadora sejam testadas automaticamente, garantindo a integridade do código após alterações.

8. **CI/CD**: Um pipeline de Integração Contínua (CI) foi configurado (porém não foi feito teste, devido a necessidade de pagamento do Heroku) para executar testes automaticamente em cada commit, garantindo que apenas código validado seja mesclado à branch principal.

## Documentação do Projeto

### Como Executar

1. Clone o repositório.
2. Instale as dependências: `pip install -r requirements.txt`.
3. Execute a calculadora: `python src/calculadora.py`.

### Como Rodar os Testes

1. Certifique-se de ter o pytest instalado.
2. Execute os testes: `pytest tests/`.
