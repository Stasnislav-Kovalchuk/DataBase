from schemas.procedure import ProcedureDao


class ProcedureService:
    def __init__(self, procedure_dao: ProcedureDao):
       self.procedure_dao = procedure_dao

    def insert_user(self, name, email):
       self.procedure_dao.call_insert_user(name, email)

    def create_playlist(self, name, user_id):
        self.procedure_dao.call_create_playlist(name, user_id)

    def create_noname_songs(self, start_id: int, number_of_songs: int):
        self.procedure_dao.call_create_noname_songs(start_id, number_of_songs)

    def get_avg_playlist_duration(self):
        return self.procedure_dao.call_get_avg_playlist_duration()

