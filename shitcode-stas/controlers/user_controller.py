from flask import Blueprint, jsonify, request
from services.users import UserService
from schemas.user_schema import CreateUserDTO
from schemas.mixed import RUserDTO

user_blueprint = Blueprint('users', __name__, url_prefix='/users')

@user_blueprint.get("/")
def get_all_users():
    users = UserService.get_all_users()
    response = [RUserDTO.model_validate(user).model_dump() for user in users]
    return jsonify(response)

@user_blueprint.get("/<int:id>")
def get_user(id: int):
    user = UserService.get_user_by_id(id=id)
    response = RUserDTO.model_validate(user).model_dump()
    return jsonify(response)

@user_blueprint.post("/")
def create_user():
    body = CreateUserDTO.model_validate(request.get_json())
    user = UserService.create_user(
        name=body.name,
        email=body.email
    )
    response = RUserDTO.model_validate(user).model_dump()
    return jsonify(response), 201
