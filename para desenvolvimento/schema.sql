DROP TABLE IF EXISTS Pessoa;
CREATE TABLE Pessoa (
  id integer primary key autoincrement,
  nome string not null,
  sobrenome string not null
);