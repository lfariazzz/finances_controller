from fastapi import APIRouter

auth_router = APIRouter(prefix="/auth", tags=["Auth"])

@auth_router.get("/")
async def autenticar():
    return{"Mensagem":"Você entrou na rota de autenticação"}