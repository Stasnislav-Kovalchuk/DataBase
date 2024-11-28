import datetime

from sqlalchemy import text

from models.session import SessionLocal
from models.song import Song


class ProcedureDao:
    def __init__(self, session):
       self.session = session

    def call_insert_user(self, name, email,):
       sql = text("CALL `InsertUser`(:name, :email)")
       self.session.execute(sql, {
           'name': name,
           'email': email,
       })
       self.session.commit()

    def call_create_playlist(self, name, user_id):
       sql = text("CALL `Playlist`(:name, :user_id)")
       self.session.execute(sql, {
              'name': name,
              'user_id': user_id,
       })
       self.session.commit()

    def call_create_noname_songs(self, start_id: int, number_of_songs: int):
        """
        Викликає збережену процедуру для створення кількох пісень
        """
        sql = text("CALL CreateNonameSongs(:start_id, :number_of_songs)")
        self.session.execute(sql, {
            'start_id': start_id,
            'number_of_songs': number_of_songs
        })
        self.session.commit()

    def call_get_avg_playlist_duration(self):
        try:
            sql = text("CALL GetAvgPlaylistDuration()")
            result = self.session.execute(sql).fetchone()
            print(f"Result: {result}")
            return result[0] if result else None
        except Exception as e:
            print(f"Error: {e}")
            raise




