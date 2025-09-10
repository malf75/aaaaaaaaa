import uuid
from fastapi.responses import JSONResponse
from fastapi import HTTPException
from starlette import status
import json

class FuncionarioController:
    def cria_funcionario(nome: str, sexo: str, cargo: str, salario: int, pais: str, projetos: list):
        try:
            lista_projetos = []
            for projeto in projetos:
                lista_projetos.append({
                    "name": projeto.name
                })
            with open("employees_dataset.json", "a", encoding='utf-8') as arquivo_json:
                id = str(uuid.uuid4())
                json.dump({
                    "id": id,
                    "name": nome,
                    "sex": sexo,
                    "role": cargo,
                    "salary": salario,
                    "country": pais,
                    "projects": lista_projetos
                }, arquivo_json)

            return JSONResponse(content={"id": id}, status_code=status.HTTP_200_OK)
        except Exception as e:
            return HTTPException(detail=f"Erro ao criar usuário: {e}", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def retorna_melhores_paises():
        try:
            return JSONResponse(content="aaaaaaaaaaaaaaa", status_code=200)
        except Exception as e:
            return HTTPException(detail=f"Erro ao criar usuário: {e}", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)