from flask import Blueprint, jsonify, request
from services.songs import SongsService
from schemas.song_schema import SongDTO, CreateSongDTO, UpdateSongDTO


song_blueprint = Blueprint('songs', __name__, url_prefix='/songs')


@song_blueprint.get("/")
def get_all_songs():
    """Отримати список усіх пісень"""
    songs = SongsService.get_all_songs()
    response = [SongDTO.model_validate(song).model_dump() for song in songs]
    return jsonify(response), 200


@song_blueprint.get("/<int:song_id>")
def get_song(song_id: int):
    """Отримати пісню за ID"""
    song = SongsService.get_song_by_id(song_id)
    response = SongDTO.model_validate(song).model_dump()
    return jsonify(response), 200


@song_blueprint.post("/")
def create_song():
    body = CreateSongDTO.model_validate(request.get_json())
    song = SongsService.create_song(
        title=body.title,
        duration=body.duration,
        genre=body.genre
    )
    response = SongDTO.model_validate(song).model_dump()
    return jsonify(response), 201


@song_blueprint.put("/<int:song_id>")
def update_song(song_id: int):
    """Оновити пісню за ID"""
    body = UpdateSongDTO.model_validate(request.get_json())
    updated_song = SongsService.update_song(
        song_id=song_id,
        title=body.title,
        duration=body.duration,
        genre=body.genre
    )
    response = SongDTO.model_validate(updated_song).model_dump()
    return jsonify(response), 200


@song_blueprint.delete("/<int:song_id>")
def delete_song(song_id: int):
    song = SongsService.get_song_by_id(song_id)
    SongsService.delete_song(song_id)
    return jsonify({"detail": "Song deleted successfully"}), 200
