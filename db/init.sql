-- 자산(asset) 테이블
CREATE TABLE IF NOT EXISTS asset (
	id			UUID PRIMARY KEY,
	status		INTEGER NOT NULL,
	type		TEXT NOT NULL,
	category	INTEGER NOT NULL,
	os			INTEGER NOT NULL,
	hostname	VARCHAR(255) NOT NULL,
	ip			INET NOT NULL
);

-- 분류(category) 테이블
CREATE TABLE category (
	code		SERIAL PRIMARY KEY,
	name		TEXT NOT NULL
)

-- 운영체제(OS) 테이블
CREATE TABLE os (
	code		SERIAL PRIMARY KEY,
	name		TEXT NOT NULL
);

-- 분류(category) 데이터 삽입
INSERT INTO category (code, name) VALUES
(1, 'server'),
(2, 'network'),
(3, 'security'),
(4, 'storage');

-- os 테스트 데이터 삽입
INSERT INTO os (code, name) VALUES
(1, 'windosws'),
(2, 'linux'),
(3, 'secuos'),
(4, 'bsd');

-- asset 테스트 데이터 삽입
INSERT INTO asset (id, status, type, category, os, hostname, ip) VALUES
('d95cd69a-c55a-4d78-abb3-e49aa937c8a5', 1, 'vm', 1, 1, 'ad-test', '192.168.6.108'),
('ef3816af-1be1-473c-8648-2cc375449450', 1, 'vm', 1, 2, 'dns', '192.168.5.55'),
('6b75c4a3-2eb6-40b4-a6cd-6cc0926581ba', 0, 'vm', 1, 2, 'ubuntu-test', '192.168.6.86'),
('b48d7409-6caa-4552-91df-93aece819547', 0, 'vm', 1, 2, 'cyj-test', '192.168.6.53'),
('fca729dd-2a86-4d37-9f68-d88d04d7db40', 1, 'pm', 3, 3, 'fw01', '192.168.12.2'),
('95ecb45b-afcf-499a-bea3-3fadf50247e1', 1, 'pm', 3, 3, 'fw02', '192.168.12.3'),
('903753a0-5bc1-4b86-bd55-be8a2ac96a5d', 1, 'vm', 1, 4, 'fileserver', '192.168.6.109'),
('d62803fe-af2b-4f5b-a818-4efb437dcbd0', 0, 'pm', 1, 1, 'gw-web', '175.124.141.235'),
('11dd6fed-6a86-444e-abf0-27a66c9d708b', 0, 'pm', 1, 1, 'gw-db', '175.124.141.236');

