from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from validations.funcionario_requests import NovoFuncionario
from controllers.funcionario_controller import FuncionarioController

app = FastAPI()

@app.get("/")
def redirect_docs():
    return RedirectResponse("/docs")

@app.post("/employees")
def rota_adiciona_funcionario(request: NovoFuncionario):
    return FuncionarioController.cria_funcionario(request.name, request.sex, request.role, request.salary, request.country, request.projects)

@app.get("/top-countries")
def rota_retorna_melhores_paises():
    return FuncionarioController.retorna_melhores_paises()

@app.get(f"/salary-avg?by")
def rota_retorna_media_salarial():
    pass

@app.get("/overload-employees")
def rota_retorna_usuarios_quantidade_projetos():
    pass

@app.get("/employees-by-roles")
def rota_retorna_cargos_quantidade_funcionarios():
    pass