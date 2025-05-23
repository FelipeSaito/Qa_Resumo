# Teste de Software é o processo de verificar se um sistema funciona conforme o esperado. Existem diferentes tipos: teste unitário (valida funções isoladas),
# teste de integração (verifica se componentes interagem corretamente), teste de sistema (testa o sistema completo), teste de aceitação (confirma que atende
# às necessidades do usuário) e teste de regressão (garante que mudanças não causem novos erros). Todos são essenciais para garantir a qualidade e confiabilidade do software.

def multiplicar(a, b):
    return a * b

def test_multiplicar():
    assert multiplicar(2, 3) == 6
    assert multiplicar(-1, 5) == -5
    assert multiplicar(0, 10) == 0
    print("Teste Unitário passou!")

test_multiplicar()

def autenticar(usuario, senha):
    return usuario == "user" and senha == "pass"

def acessar_painel(usuario, senha):
    if autenticar(usuario, senha):
        return "Painel acessado"
    return "Acesso negado"

def test_acessar_painel():
    assert acessar_painel("user", "pass") == "Painel acessado"
    assert acessar_painel("user", "errado") == "Acesso negado"
    print("Teste de Integração passou!")

test_acessar_painel()

class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def total_livros(self):
        return len(self.livros)

def test_biblioteca():
    biblio = Biblioteca()
    biblio.adicionar_livro("Livro A")
    biblio.adicionar_livro("Livro B")
    assert biblio.total_livros() == 2
    print("Teste de Sistema passou!")

test_biblioteca()

def test_aceitacao():
    resultado = acessar_painel("user", "pass")
    assert resultado == "Painel acessado"
    print("Teste de Aceitação passou!")

test_aceitacao()

def test_regressao():
    assert multiplicar(4, 5) == 20
    print("Teste de Regressão passou!")

test_regressao()
