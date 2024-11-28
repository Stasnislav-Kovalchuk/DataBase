from flask import Blueprint, jsonify, request
from services.playlists import PlaylistsService
from schemas.playlist_schema import CreatePlaylistDTO, AddSongDTO
from schemas.mixed import RPlaylistDTO

playlist_blueprint = Blueprint('playlists', __name__, url_prefix='/playlists')


@playlist_blueprint.get("/")
def get_all_playlists():
    playlists = PlaylistsService.get_all_playlists()
    response = [RPlaylistDTO.model_validate(playlist).model_dump() for playlist in playlists]
    return jsonify(response)


@playlist_blueprint.get("/<int:id>")
def get_playlist(id: int):
    playlist = PlaylistsService.get_playlist_by_id(id=id)
    response = RPlaylistDTO.model_validate(playlist).model_dump()
    return jsonify(response)


@playlist_blueprint.post("/")
def create_playlist():
    body = CreatePlaylistDTO.model_validate(request.get_json())
    playlist = PlaylistsService.create_playlist(
        name=body.name,
        user_id=body.user_id
    )
    response = RPlaylistDTO.model_validate(playlist).model_dump()
    return jsonify(response), 201


@playlist_blueprint.post("/<int:id>/songs")
def add_song(id: int):
    body = AddSongDTO.model_validate(request.get_json())
    playlist = PlaylistsService.add_song_to_playlist(
        playlist_id=id,
        song_id=body.song_id
    )
    response = RPlaylistDTO.model_validate(playlist).model_dump()
    return jsonify(response), 201


@playlist_blueprint.delete("/<int:playlist_id>/songs/<int:song_id>")
def remove_song(playlist_id: int, song_id: int):
    playlist = PlaylistsService.remove_song_from_playlist(
        playlist_id=playlist_id,
        song_id=song_id
    )
    response = RPlaylistDTO.model_validate(playlist).model_dump()
    return jsonify(response), 201
