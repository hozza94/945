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
INSERT INTO "member" VALUES(1,'����ȣ',29,'M','1994.01.05','010-2471-3412','��⵵ ������ ���뱸 �������� 432, 3�� 1408ȣ','����غ��','hozza94@gmail.com',1,'0000.00.00',0,'������������ȸ','������','010-7106-8754');
COMMIT;
