create table Users (
	id INTEGER PRIMARY KEY,
	email VARCHAR(64),
	password VARCHAR(64),
	name VARCHAR(64),
    img_color_url VARCHAR(128),
    img_color_bw VARCHAR(128),
    role Integer,
    status Integer
);

create table Events (
	id INTEGER PRIMARY KEY,
	event_user_id INTEGER,
	creator_user_id INTEGER
	description VARCHAR(128),
	add_time DATETIME,
	start_time DATETIME,
	completed_time DATETIME
);