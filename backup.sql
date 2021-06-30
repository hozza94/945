BEGIN TRANSACTION;
CREATE TABLE "member" (
	"id"	integer,
	"name"	char(10),
	"age"	integer,
	"sex"	char(1),
	"birthDay"	char(12),
	"contact"	char(13),
	"address"	text,
	"job"	varchar(50),
	"email"	varchar(50),
	"baptism"	bool,
	"baptismDay"	char(10),
	"marriage"	bool,
	"prevChurch"	varchar(30),
	"guider"	char(10),
	"guiderContact"	char(13),
	PRIMARY KEY("id")
);
INSERT INTO "member" VALUES(1,'구자호',29,'M','1994.01.05','010-2471-3412','경기도 수원시 영통구 동수원로 432, 3동 1408호','취업준비생','hozza94@gmail.com',1,'0000.00.00',0,'수원순복음교회','박유여','010-7106-8754');
COMMIT;
