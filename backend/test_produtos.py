import pytest
import requests
import os

BASE_URL = os.getenv('API_BASE_URL', 'http://localhost:8000/api/produtos')

@pytest.fixture(scope='module')
def auth_token():
    # Substitua este trecho pela sua lógica de autenticação, se necessário.
    # Ex: fazer uma requisição para a sua rota de login e retornar o token.
    return "e488d81a16bade8bd64fa436bdfd94537a07c064"

def test_listar_produtos():
    response = requests.get(BASE_URL)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_criar_produto(auth_token):
    produto_novo = {
        "nome": "Arroz Branco",
        "categoria": "Alimento",
        "preco": 2.49
    }
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = requests.post(BASE_URL, json=produto_novo, headers=headers)
    assert response.status_code == 201
    assert "id" in response.json()
    assert response.json()["nome"] == produto_novo["nome"]

@pytest.mark.parametrize("produto_id, expected_status", [
    (1, 200),
    (9999, 404),
])
def test_buscar_produto_por_id(produto_id, expected_status):
    response = requests.get(f"{BASE_URL}/{produto_id}")
    assert response.status_code == expected_status
    if expected_status == 200:
        assert "nome" in response.json()

def test_atualizar_produto_existente(auth_token):
    # Primeiro, crie um produto para depois atualizá-lo.
    produto_para_atualizar = {
        "nome": "Feijão Cavalo",
        "categoria": "Alimento",
        "preco": 3.96
    }
    headers = {"Authorization": f"Bearer {auth_token}"}
    response_post = requests.post(BASE_URL, json=produto_para_atualizar, headers=headers)
    assert response_post.status_code == 201
    produto_id = response_post.json()["id"]

    # Agora, atualize o produto.
    dados_atualizados = {
        "nome": "Macarrão tipo semola",
        "preco": 3.99
    }
    response_put = requests.put(f"{BASE_URL}/{produto_id}", json=dados_atualizados, headers=headers)
    assert response_put.status_code == 200
    assert response_put.json()["nome"] == dados_atualizados["nome"]

def test_deletar_produto(auth_token):
    # Primeiro, crie um produto para depois deletá-lo.
    produto_para_deletar = {
        "nome": "Costela de Porco",
        "categoria": "Alimento",
        "preco": 150.00
    }
    headers = {"Authorization": f"Bearer {auth_token}"}
    response_post = requests.post(BASE_URL, json=produto_para_deletar, headers=headers)
    assert response_post.status_code == 201
    produto_id = response_post.json()["id"]

    # Agora, delete o produto.
    response_delete = requests.delete(f"{BASE_URL}/{produto_id}", headers=headers)
    assert response_delete.status_code == 204

    # Verifique se o produto foi realmente deletado.
    response_get = requests.get(f"{BASE_URL}/{produto_id}")
    assert response_get.status_code == 404
