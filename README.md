1. Napraviti stranicu s prikazom liste i forme za unos adrese RSS feeda. Svaki feed na sebi
mora imati oznaku aktivnosti koju je moguće mijenjati (ovu točku ne smatramo rješenjem ako se
to napravi uz pomoć Django admina).
2. Napraviti Django manage komandu koja dohvaća aktivne feedove i sprema njihove unose
(entries) u bazu.
a. iz sadržaja pojedinog unosa posebno izdvojiti sve riječi
b. svaku riječ spremiti u tablicu riječi tako da je svaka riječ navedena samo jednom
(jedinstveni ključ po riječi)
c. u dodatnu tablicu spremiti koliko puta se svaka pojedina riječ ponavlja u
pojedinom unosu te koliko se pojedina riječ ponavlja u pojedinom feedu, a uz
svaku riječ možete zapisati i ukupan broj pojavljivanja
3. Napraviti JSON API kojemu se kao parametar predaje riječ i kao odgovor dobije broj
ponavljanja te riječi. Kao parametar može se predati url feeda ili url unosa i u tom slučaju se
dobije broj ponavljanja te riječi u feedu ili u unosu.
4. Napraviti stranicu s top listom riječi prema broju pojavljivanja. Omogućiti filtriranje po
feedovima. Definirati optimalan broj riječi po stranici i u slučaju da ih ima previše napraviti
straničenje (paging).
