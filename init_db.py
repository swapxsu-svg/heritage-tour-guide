import sqlite3

conn = sqlite3.connect("database.db")

c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS monuments (

    id          INTEGER PRIMARY KEY AUTOINCREMENT,

    name        TEXT,
    hi_name     TEXT,

    lat         REAL,
    lon         REAL,

    color       TEXT,

    image_url   TEXT,

    -- English content
    history      TEXT,
    secondary    TEXT,
    visitor      TEXT,
    experience   TEXT,
    nearby       TEXT,
    condition    TEXT,
    translation  TEXT,

    -- Hindi content
    hi_history      TEXT,
    hi_secondary    TEXT,
    hi_visitor      TEXT,
    hi_experience   TEXT,
    hi_nearby       TEXT,
    hi_condition    TEXT,
    hi_translation  TEXT

)
""")

conn.commit()

conn.close()

print("monuments table created successfully")