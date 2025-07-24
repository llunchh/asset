-- 자산(asset) 테이블
CREATE TABLE IF NOT EXISTS asset (
	id			UUID PRIMARY KEY,
	status		INTEGER NOT NULL,
	type		TEXT NOT NULL,
	category	TEXT NOT NULL,
	os			INTEGER NOT NULL,
	hostname	VARCHAR(255) NOT NULL,
	ip			INET NOT NULL
);

-- 운영체제(OS) 테이블
CREATE TABLE os (
	code		SERIAL PRIMARY KEY,
	name		TEXT NOT NULL
);
