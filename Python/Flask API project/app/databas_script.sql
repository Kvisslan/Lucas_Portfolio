DROP TABLE IF EXISTS Authorsinfo;
DROP TABLE IF EXISTS Reviews;

CREATE TABLE Authorsinfo (
    author_id INTEGER PRIMARY KEY AUTOINCREMENT,
    titel varchar(150),
    authorname varchar(150),
    shortsummary varchar(150),
    genre varchar(100)
);

CREATE TABLE Reviews(
    review_id INTEGER PRIMARY KEY AUTOINCREMENT,
    score INTEGER,
    username varchar(50),
    reviewsummary varchar(100),
    author_id INTEGER,
    FOREIGN KEY (author_id) REFERENCES Authorsinfo(author_id)
);

INSERT INTO Authorsinfo (titel, authorname, shortsummary, genre)
VALUES
('Mitt i natten', 'Kristin Hannah', 'En gripande berättelse om systrarnas kamp i andra världskrigets Frankrike.', 'Historisk skönlitteratur'),
('Den tysta flickan', 'Alex Michaelides', 'En psykologisk thriller om en kvinna med selektivt mutism och en mörk hemlighet.', 'Thriller'),
('Ögonen i skogen', 'Karsten Dümmel', 'En spännande fantasy där världens öden vävs samman genom magiska ögon.', 'Fantasy'),
('Mörkrets hjärta', 'Joseph Conrad', 'En resa uppför Kongofloden avslöjar mänsklighetens mörkaste sidor.', 'Klassiker'),
('Stjärnklart', 'Kim Stanley Robinson', 'En episk science fiction-saga om kolonisationen av Mars och mänsklighetens överlevnad.', 'Science fiction'),
('Försvinnande', 'Gillian Flynn', 'En psykologisk thriller där en kvinna plötsligt försvinner och hennes man blir huvudmisstänkt.', 'Thriller'),
('Hundra år av ensamhet', 'Gabriel García Márquez', 'En familjesaga om Buendía-klanen och den magiska staden Macondo.', 'Magisk realism'),
('Den fantastiska historien om Benjamin Button', 'F. Scott Fitzgerald', 'En kortroman om en man som åldras baklänges och de konsekvenser det medför.', 'Novell'),
('Vindens skugga', 'Carlos Ruiz Zafón', 'En mystisk berättelse om en bokhandel, förbannelser och försvunna författare.', 'Mystik'),
('Flickan på tåget', 'Paula Hawkins', 'En psykologisk thriller där en kvinna blir indragen i en försvinningsgåta från ett pendeltåg.', 'Thriller'),
('Dödssynden', 'Liane Moriarty', 'I en småstad avslöjar skvaller och hemligheter under en skolföreställning.', 'Roman'),
('1984', 'George Orwell', 'En dystopisk framtidsskildring där övervakning och kontroll når nya nivåer.', 'Dystopi'),
('Jane Eyre', 'Charlotte Brontë', 'En klassisk kärlekshistoria och bildningsroman om den föräldralösa Jane Eyre.', 'Klassiker'),
('Den store Gatsby', 'F. Scott Fitzgerald', 'En berättelse om kärlek, rikedom och förlust under jazzålderns glans.', 'Roman'),
('De sju systrarna', 'Lucinda Riley', 'En gripande historia om sju adopterade systrar och deras sökande efter sina rötter.', 'Historisk skönlitteratur');

INSERT INTO Reviews (score, username, reviewsummary, author_id)
VALUES
( 4, 'StarlightDreamer','Bra', 2),
( 5, 'QuantumJester','Kul läsning', 1),
( 3, 'VelvetPenguin','Över förväntan', 9),
( 2, 'LunaPhoenix','Tur att den var billig', 10),
( 5, 'JazzedNavigator','Bästa jag läst', 1),
( 4, 'PixelVoyager','Bra starka karaktärer', 11),
( 4, 'MysticHawk','Gillar!', 2),
( 3, 'CyberSphinx','Bra skriven men många men', 12),
( 2, 'NeonNomad','Läste första och var tvungen att läsa den andra.', 13),
( 5, 'SolarFlareGazer','ÄLSKAR!', 1),
( 2, 'CrimsonWhisperer','Ok', 2),
( 1, 'TechnoWombat','Inte min favorit.', 8),
( 2, 'CelestialSorcerer','Läst bättre', 7),
( 3, 'MidnightMarauder','Inte min genre', 2),
( 3, 'EchoNebula','Kul ibland', 3),
( 1, 'CosmicPenguin','Nej', 4),
( 5, 'QuantumQuasar','Wow!', 1),
( 5, 'EnigmaExplorer','Finner inga ord.', 1),
( 4, 'DazzlePanda','Lika bra som mitt användarnamn!', 5),
( 3, 'ElectraHarmony','Okej söndagsläsning.', 6);