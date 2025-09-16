import uuid
from fastapi.responses import JSONResponse
from fastapi import HTTPException
from starlette import status
from validations.funcionario_requests import NovoFuncionario
import pandas as pd
import json

class FuncionarioController:
    def cria_funcionario(request: NovoFuncionario, escreve_arquivo):
        try:
            lista_projetos = []
            for projeto in request.projetos:
                lista_projetos.append({
                    "name": projeto.name
                })
            
                id = str(uuid.uuid4())
                json.dump({
                    "id": id,
                    "name": request.nome,
                    "sex": request.sexo,
                    "role": request.cargo,
                    "salary": request.salario,
                    "country": request.pais,
                    "projects": lista_projetos
                }, escreve_arquivo)

            return JSONResponse(content={"id": id}, status_code=status.HTTP_200_OK)
        except Exception as e:
            return HTTPException(detail=f"Erro ao criar usuário: {e}", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def retorna_melhores_paises(dados):
        try:
            arquivo = pd.DataFrame(dados)
            filtro = arquivo.groupby("country")["salary"].mean().sort_values(ascending=False)[:5].to_dict()
            return JSONResponse(content=filtro, status_code=status.HTTP_200_OK)
        except Exception as e:
            return HTTPException(detail=f"Erro ao filtrar salários: {e}", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def retorna_media_salarial(filtro, dados):
        try:
            arquivo = pd.DataFrame(dados)
            filtro = arquivo.groupby(filtro)["salary"].mean().sort_values(ascending=False).to_dict()
            return JSONResponse(content=filtro, status_code=status.HTTP_200_OK)
        except Exception as e:
            return HTTPException(detail=f"Erro ao filtrar salários: {e}", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def retorna_usuarios_mais_projetos(dados):
        try:
            arquivo = pd.DataFrame(dados)
            arquivo["projects_count"] = arquivo["projects"].apply(len)
            filtro = arquivo.sort_values("projects_count", ascending=False).head(31)
            resultado = filtro.set_index("name")["projects_count"].to_dict()
            return JSONResponse(content=resultado, status_code=status.HTTP_200_OK)
        except Exception as e:
            return HTTPException(detail=f"Erro ao filtrar usuários: {e}", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def retorna_funcionarios_por_cargo(dados):
        try:
            arquivo = pd.DataFrame(dados)
            resultado = []
            quantidade = arquivo["role"].value_counts()
            for i,n in quantidade.items():
                resultado.append({"role": i, "quantity": n})
            return JSONResponse(content=resultado, status_code=status.HTTP_200_OK)
        except Exception as e:
            return HTTPException(detail=f"Erro ao filtrar cargos: {e}", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)