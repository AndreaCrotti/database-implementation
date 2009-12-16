CREATE TABLE lives(person_name PRIMARY KEY, city, street);
CREATE TABLE works(person_name PRIMARY KEY, company_name, salary);
CREATE TABLE located(company_name PRIMARY KEY, city);
CREATE TABLE boss(person_name PRIMARY KEY, manager_name);

insert into lives values(1, 'mantova', 'pippo');
insert into lives values(2, 'brescia', 'pippo');
insert into lives values(3, 'topolina', 'abc');

insert into works values(1, 'MyComp', 100);
insert into works values(2, 'BigComp', 200);

insert into located values('MyComp', 'brescia');
insert into located values('BigComp', 'verona');

insert into boss values(1, 'capo');
insert into boss values(2, 'altrocapo');
