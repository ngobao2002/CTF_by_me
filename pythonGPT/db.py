import sqlite3

# Kết nối đến cơ sở dữ liệu (tạo mới nếu chưa tồn tại)
conn = sqlite3.connect('nba_players.sqlite')
cursor = conn.cursor()

# Tạo bảng cho cầu thủ nếu chưa tồn tại
cursor.execute('''
CREATE TABLE IF NOT EXISTS players (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    team TEXT NOT NULL,
    position TEXT NOT NULL,
    points_per_game REAL,
    assists_per_game REAL,
    rebounds_per_game REAL
)
''')

# Tạo bảng cho thử thách bình thường nếu chưa tồn tại
cursor.execute('''
CREATE TABLE IF NOT EXISTS level (
    level INTEGER PRIMARY KEY,
    challenge TEXT NOT NULL,
    query TEXT NOT NULL
)
''')

# Tạo bảng cho thử thách admin nếu chưa tồn tại
cursor.execute('''
CREATE TABLE IF NOT EXISTS admin_level (
    level INTEGER PRIMARY KEY,
    challenge TEXT NOT NULL,
    query TEXT NOT NULL
)
''')

# Thêm dữ liệu vào bảng cầu thủ
players = [
    ('LeBron James', 'Los Angeles Lakers', 'Forward', 27.0, 7.4, 7.4),
    ('Stephen Curry', 'Golden State Warriors', 'Guard', 29.4, 6.2, 5.5),
    ('Kevin Durant', 'Phoenix Suns', 'Forward', 27.0, 5.6, 7.1),
    ('Giannis Antetokounmpo', 'Milwaukee Bucks', 'Forward', 29.9, 5.8, 11.4),
    ('Joel Embiid', 'Philadelphia 76ers', 'Center', 33.0, 4.2, 10.2),
    # ... Thêm dữ liệu cho đến 100 cầu thủ
]

cursor.executemany('''
INSERT INTO players (name, team, position, points_per_game, assists_per_game, rebounds_per_game)
VALUES (?, ?, ?, ?, ?, ?)
''', players)

# Thêm thử thách vào bảng level
levels = [
    (1, 'Retrieve all players with more than 20 points per game', 'SELECT * FROM players WHERE points_per_game > 20;'),
    (2, 'Find players from the Los Angeles Lakers', 'SELECT * FROM players WHERE team = "Los Angeles Lakers";'),
    (3, 'Get players with rebounds greater than 8', 'SELECT name FROM players WHERE rebounds_per_game > 8;'),
    (4, 'List players with average assists more than 5', 'SELECT name FROM players WHERE assists_per_game > 5;'),
    (5, 'Retrieve players with highest points per game', 'SELECT name FROM players ORDER BY points_per_game DESC LIMIT 1;')
]

cursor.executemany('''
INSERT INTO level (level, challenge, query)
VALUES (?, ?, ?)
''', levels)

# Thêm thử thách admin vào bảng admin_level
admin_levels = [
    (6, 'Retrieve the hidden CTF flag', 'SELECT "FLAG{CTF_SQL_INJECTION}" AS flag;')
]

cursor.executemany('''
INSERT INTO admin_level (level, challenge, query)
VALUES (?, ?, ?)
''', admin_levels)

# Lưu và đóng kết nối
conn.commit()
conn.close()

print("Database 'nba_players.sqlite' has been updated with admin-level challenges.")
