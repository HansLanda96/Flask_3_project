import sqlite3


def connection():
    conn = sqlite3.connect('music.sqlite3')
    conn.row_factory = sqlite3.Row
    return conn


def best_selling(sale):
    conn = connection()
    tracks = conn.execute('SELECT t.Name AS Name, SUM(ii.UnitPrice) AS Summary \
                           FROM invoice_items AS ii \
                           JOIN tracks AS t ON ii.TrackId = t.TrackId \
                           GROUP BY ii.TrackId \
                           ORDER BY Summary \
                           DESC LIMIT (?);', (sale,)).fetchall()
    conn.close()
    return tracks
