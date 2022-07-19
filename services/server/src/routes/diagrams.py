from fastapi import APIRouter
from typing import List, Tuple
from fastapi import Body
from src.crud.diagrams import get_diagrams

from src.schemas.diagram import DiagramRule
from src.schemas.diagram import DiagramData

router = APIRouter()


@router.post("/diagrams", response_model=List[DiagramData],
             description="Передаём правила для фильтров на диаграмму,\
             \n получаем данные для диаграм")
async def get_diagrams_data(
        rules: List[DiagramRule] = Body(
            None,
            description="Задаём фильтры для диаграм",
        )
    ):
    return await get_diagrams(list(set(rules)))

# @router.delete(
#     "/user/{user_id}",
#     response_model=Status,
#     responses={404: {"model": HTTPNotFoundError}},
#     dependencies=[Depends(get_current_user)],
# )
# async def delete_user(
#     user_id: int, current_user: UserOutSchema = Depends(get_current_user)
# ) -> Status:
#     return await crud.delete_user(user_id, current_user)
