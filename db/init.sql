-- 자산(asset) 테이블
CREATE TABLE IF NOT EXISTS asset (
	id			UUID PRIMARY KEY DEFAULT gen_random_uuid(),
	status		INTEGER NOT NULL,
	type		TEXT NOT NULL,
	category	INTEGER NOT NULL,
	subcategory	INTEGER NOT NULL,
	os			INTEGER NOT NULL,
	hostname	VARCHAR(255) NOT NULL,
	ip			INET NOT NULL
);

-- 분류(category) 테이블
CREATE TABLE category (
	code		SERIAL PRIMARY KEY,
	name		TEXT NOT NULL
);

-- 세분류(subcategory) 테이블
CREATE TABLE subcategory (
	code		SERIAL PRIMARY KEY,
	name		TEXT NOT NULL
);

-- 운영체제(OS) 테이블
CREATE TABLE os (
	code		SERIAL PRIMARY KEY,
	name		TEXT NOT NULL
);

-- 계정(account) 테이블
CREATE TABLE account (
    id 			UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    username 	VARCHAR(255) NOT NULL,
    password 	TEXT NOT NULL,
    asset_id 	UUID NOT NULL,
    create_at 	TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    update_at 	TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    CONSTRAINT fk_asset FOREIGN KEY (asset_id) REFERENCES asset (id) ON DELETE CASCADE
);

-- 분류(category) 데이터 삽입
INSERT INTO category (code, name) VALUES
(1, 'server'),
(2, 'network'),
(3, 'security'),
(4, 'storage');

-- 세분류(subcategory) 데이터 삽입
INSERT INTO subcategory (code, name) VALUES
(1, 'app_server'),
(2, 'sec_server'),
(3, 'l4_switch'),
(4, 'l3_switch'),
(5, 'l2_switch'),
(6, 'hub'),
(7, 'ap'),
(8, 'wlan_controller'),
(9, 'firewall'),
(10, 'vpn'),
(11, 'proxy'),
(12, 'nac');

-- os 테스트 데이터 삽입
INSERT INTO os (code, name) VALUES
(1, 'windosws'),
(2, 'linux'),
(3, 'secuos'),
(4, 'bsd'),
(5, 'ios');

-- asset 테스트 데이터 삽입
INSERT INTO asset (status, type, category, subcategory, os, hostname, ip) VALUES
(1, 'vm', 1, 1, 1, 'ad-test', '192.168.6.108'),
(1, 'vm', 1, 1, 2, 'dns', '192.168.5.55'),
(0, 'vm', 1, 1, 2, 'ubuntu-test', '192.168.6.86'),
(0, 'vm', 1, 1, 2, 'cyj-test', '192.168.6.53'),
(1, 'pm', 1, 2, 1, 'nasca&escort', '192.168.5.108'),
(1, 'vm', 1, 2, 2, 'v3', '192.168.5.120'),
(1, 'pm', 3, 9, 3, 'fw01', '192.168.12.2'),
(1, 'pm', 3, 9, 3, 'fw02', '192.168.12.3'),
(1, 'pm', 2, 4, 5, 'bb01', '172.10.70.2'),
(1, 'pm', 2, 4, 5, 'bb02', '172.10.70.3'),
(1, 'vm', 1, 1, 4, 'fileserver', '192.168.6.109'),
(0, 'pm', 1, 1, 1, 'gw-web', '175.124.141.235'),
(0, 'pm', 1, 1, 1, 'gw-db', '175.124.141.236');

