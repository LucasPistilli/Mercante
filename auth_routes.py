from fastapi import APIRouter

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/usuarios/me/")
async def autentic():
    return {"Mensagem" : "Você acessou a rota de autentificação"}