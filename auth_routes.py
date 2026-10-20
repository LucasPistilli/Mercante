from fastapi import APIRouter

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.post("/usuarios/")
async def cadastro():
    return {"Mensagem"}

@auth_router.post("/login/")
async def login():
    return {"Logado"}

@auth_router.get("/usuarios/me/")
async def retorno_dados():
    return {"Mensagem" : "Você acessou a rota de autentificação"}

@auth_router.put("/usuarios/me/")
async def atualizar_dados():
    return {"Dados atualizados"}