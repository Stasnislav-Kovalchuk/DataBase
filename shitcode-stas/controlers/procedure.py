from flask import Blueprint, request, jsonify
from models.session import SessionLocal
from schemas.procedure import ProcedureDao
from services.procedure import ProcedureService


procedure_bp = Blueprint('procedure_bp', __name__)
procedure_dao = ProcedureDao(SessionLocal())
procedure_service = ProcedureService(procedure_dao)


@procedure_bp.route('/insert_user', methods=['POST'])
def insert_parcel():
   data = request.json
   procedure_service.insert_user(
       data['name'], data['email']
   )
   return jsonify({'message': 'User inserted successfully'}), 201

@procedure_bp.route('/create_playlist', methods=['POST'])
def create_playlist():
    data = request.json
    procedure_service.create_playlist(
         data['name'], data['user_id']
    )
    return jsonify({'message': 'playlist created successfully'}), 201

@procedure_bp.route('/create_noname_songs', methods=['POST'])
def create_noname_songs():
    """
    Обробляє POST-запит для створення кількох noname пісень.
    Очікує JSON-дані:
    {
        "start_id": <початковий ID>,
        "number_of_songs": <кількість пісень>
    }
    """
    data = request.json
    procedure_service.create_noname_songs(
        start_id=data['start_id'],
        number_of_songs=data['number_of_songs']
    )
    return jsonify({
        'message': f'{data["number_of_songs"]} Noname songs created successfully'
    }), 201


@procedure_bp.route('/get_avg_playlist_duration', methods=['GET'])
def get_avg_playlist_duration():
    """
    Обробляє GET-запит для отримання середньої тривалості пісень у плейлистах.
    """
    try:
        avg_duration = procedure_service.get_avg_playlist_duration()
        return jsonify({'average_duration': avg_duration}), 200
    except Exception as e:
        return jsonify({'тут короче біда': str(e)}), 500




# @procedure_bp.route('/insert_user_courier', methods=['POST'])
# def insert_user_courier():
#    data = request.json
#    procedure_service.insert_user_courier(
#        data['user_name'], data['user_surname'], data['courier_name'], data['courier_surname']
#    )
#    return jsonify({'message': 'User courier inserted successfully'}), 201
#
#
# @procedure_bp.route('/insert_noname_parcel_rows', methods=['POST'])
# def insert_noname_parcel_rows():
#    procedure_service.insert_noname_parcel_rows()
#    return jsonify({'message': 'Noname parcel rows inserted successfully'}), 201
#
#
# @procedure_bp.route('/get_min_parcel_weight', methods=['GET'])
# def get_min_parcel_weight():
#    min_weight = procedure_service.get_min_parcel_weight()
#    return jsonify({'min_weight': min_weight}), 200
#
#
# @procedure_bp.route('/create_random_parcel_tables', methods=['POST'])
# def create_random_parcel_tables():
#    procedure_service.create_random_parcel_tables()
#    return jsonify({'message': 'Random parcel tables created successfully'}), 201