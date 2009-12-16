CREATE table VIP(id INTEGER, PRIMARY KEY(id));
CREATE table EMPLOYEE(id INTEGER, PRIMARY KEY(id));
CREATE table MALE(id INTEGER, PRIMARY KEY(id));

insert into MALE VALUES (1);
insert into EMPLOYEE VALUES (1);
insert into EMPLOYEE VALUES (2);

select MALE.id
from EMPLOYEE, MALE
where VIP.id=MALE.id or EMPLOYEE.id=Male.id;