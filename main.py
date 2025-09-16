from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from validations.funcionario_requests import NovoFuncionario
from controllers.funcionario_controller import FuncionarioController
from starlette import status
import json

app = FastAPI()

escreve_arquivo = open("employees_dataset.json", "a", encoding='utf-8')
le_arquivo = open("employees_dataset.json", "r", encoding='utf-8')
dados = json.load(le_arquivo)
opcoes = ["sex", "country", "role"]

@app.get("/")
def redirect_docs():
    return RedirectResponse("/docs")

@app.post("/employees")
def rota_adiciona_funcionario(request: NovoFuncionario):
    return FuncionarioController.cria_funcionario(request, escreve_arquivo)

@app.get("/top-countries")
def rota_retorna_melhores_paises():
    return FuncionarioController.retorna_melhores_paises(dados)

@app.get("/salary-avg/{by}")
def rota_retorna_media_salarial(by: str):
    if by in opcoes:
        return FuncionarioController.retorna_media_salarial(by, dados)
    else:
        return HTTPException(detail="Grupo escolhido não é válido. Opções: 'sex', 'country', 'role'", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

@app.get("/overload-employees")
def rota_retorna_usuarios_quantidade_projetos():
    return FuncionarioController.retorna_usuarios_mais_projetos(dados)

@app.get("/employees-by-roles")
def rota_retorna_cargos_quantidade_funcionarios():
    return FuncionarioController.retorna_funcionarios_por_cargo(dados)