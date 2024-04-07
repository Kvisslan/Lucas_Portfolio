# Denna readme innehåller en beskrivning av projektet samt hur man använder applikationen.
Personalregister av Lucas Arvidsson AIDEV23S.

Projektet är byggt så att "Personalregister/app.py" är det som startar själva programmet/servern.
Personalregister/website/__init__.py innehåller det som initierar själva Flaskappen och skapar databasen.
Personalregister/website/models.py är där jag har valt att lagra alla mina "blueprints" för hur databaserna ska se ut. i models.py ingår det även funktioner för att seeda data till databasen om det är så att den är tom.
Personalregister/website/routes.py innehåller alla rutter/routes som finns på hemsidan. Det är rutter för att kunna hantera olika HTTP förfrågningar som GET och POST. Det finns även rutter att skapa konto i webdatabasen, för att komma till personalregistret osv.
Personalregister/website/templates, denna mapp innehåller alla .html filer för att hantera de olika rutterna. Den som heter "base.html" är själva mallen på hemsidan som dem andra templatses sedan ärver deras struktur ifrån, som tillexempel navbar och footer.
Personalregister/website/static är det som inte ändras på, dessa är tillexempel style.css samt bilder som använts till hemsidan.
Personalregister/website/instance är där som själva databasen hamnar om man inte har någon och väljer att seeda data till den.
Personalregister/requirements.txt är en pipinstallationsfil som innehåller alla bibliotek som man behöver för att kunna köra projektet.
Databasen innehåller tre stycken tables. Det är ett för Personal, ett för de användare som registrerat sig för webaccess och ett table för att tillhandahålla unika bilder till de registrerade användarna.


Är det första gången man startar applicationen så kommer man endast att se en inloggningssida och en Sign up sida. Har man inget konto så får man skapat ett för att få tillgång till resten av hemsidan.
För enkelhetens skull så skapas ett konto som man kan logga in med direkt vid körning av programmet. (detta för att underlätta testningen av sidan.)
email: admin@admin.se
lösenord: admin123

När du registrerat dig så hamnar ditt nyskapade konto i databasen för webaccess konton (inte i personalregistret!).

När du sedan är inloggad så har du tillgång till personalregistret och att lägga till flera personer bland personalen. Du har även tillgång till själva hemsidans homepage.

På sidan personalregister kan du se alla personer i den databasen för personal. Sidan är paginerad och du ser endast 30st resultat åt gången. Klickar du på personalens bilder i tabellen så kommer du komma till en ny sidan där du kan läsa mer om den personen. Du kan även söka efter specifika personer på Personalregistersidan.
Du kan även lägga till flera personer via registreringsformuläret för personaldatabasen.

När du är klar så kan du även klicka på Logout.

Tack för att du använt min hemsida!