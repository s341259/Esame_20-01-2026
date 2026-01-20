from database.DB_connect import DBConnect
from model.artist import Artist
from model.track import Track

class DAO:

    @staticmethod
    def get_artists_min_albums(min_albums):

        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """select artisti_album.id, artisti_album.name
                    from (select a.id, a.name, count(al.id) as n_album
                            from artist a,
                                album al
                            where a.id = al.artist_id
                            group by a.id) as artisti_album
                    where artisti_album.n_album  >= %s"""
        cursor.execute(query,(min_albums,))
        for row in cursor:
            artist = Artist(id=row['id'], name=row['name'], genre=set())
            result.append(artist)
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_track(min_albums):

        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """select t.id, t.genre_id, a1.id as artistid 
                    from track t,
                        album al,
                        (select artisti_album.id, artisti_album.name
                                        from (select a.id, a.name, count(al.id) as n_album
                                                from artist a,
                                                    album al
                                                where a.id = al.artist_id
                                                group by a.id) as artisti_album
                                        where artisti_album.n_album  >= %s) as a1
                    where t.album_id = al.id and a1.id = al.artist_id """
        cursor.execute(query, (min_albums,))
        for row in cursor:
            tracks = Track(id=row['id'],genre_id=row["genre_id"],artistid=row['artistid'])
            result.append(tracks)
        cursor.close()
        conn.close()
        return result
