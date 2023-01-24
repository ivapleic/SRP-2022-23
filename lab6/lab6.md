# Lab 6 izvještaj :

## **Online Password Guessing**

S obzirom da kod *online password guessing* napada **napadač** komunicira sa **serverom**, trebali smo se uvjeriti možemo li uspostaviti komunikaciju između nas i servera. To smo učinili **pinganjem** željenog servera.

Kako smo bili spojeni na lokalnu mrežu fakulteta, htjeli smo **ograničiti komunikaciju** na uređaje koji se isključivo nalaze u laboratoriju. Za to nam je pomogao alat **Nmap.**

> **Nmap**-alat za skeniranje mreže, tj. dohvaćanje svih IP adresa koje su povezane na našu mrežu
> 

Korištenjem **ssh klijenta** smo se probali spojiti na server:

```python
# ssh <username>@<your hostname>
ssh pleic_iva@pleiciva.local
```

Međutim, nismo imali pristup serveru jer nas je klijent tražio **lozinku**. Trebali smo je saznati. Za to smo koristili alat **Hydra**.

Imamo informaciju o lozinki:

- sadrži samo mala slova (26 malih slova)
- dužina lozinke je između 4 i 6 slova

Započeli smo sa naredbom:

```python
hydra -l pleic_iva -x 4:6:a pleiciva.local -V -t 4 ssh
```

> **4:6** predstavlja rang ******lozinke, a **:a** govori da se radi o malim slovima. **-t** parametar označava koliko zahtjeva šaljemo serveru. Taj parametar treba biti mali broj kako ne bismo opteretili server.
> 

### **Vrijeme izvršavanja:**

Već smo spomenuli kako se radi o lozinki koja se sastoji od **malih slova** te je dužine između **4 i 6 znakova**. Malih slova ima **26** u engleskoj abecedi.

Primjenom kombinatorike (Diskretna matematika :) možemo izračunati koliko bi bilo vremena potrebno za pronalazak lozinke.

![Untitled](Lab%206%20izvjes%CC%8Ctaj%203017cf74893a4f49b332d6fa763620af/Untitled.png)

Uz pomoć kombinatorike smo izračunali da postoji mogućih **2^30 kombinacija lozinke**. Pokretanjem zadatka smo dobili povratnu informaciju da je otprilike **64 zahtjeva po minuti**. Što znači da nam je potrebno **2^24 minuta** da bi prošli sve lozinke. Ako se to pretvori u godine, to je **2^5**, odnosno **32 godine**.

S obzirom da bi to trajalo predugo moramo koristit **dictionary** te izvesti **pre-computed dictionary attack.**

Profesor nam je priložio već kreirani *dictionary* kojeg je bilo potrebno preuzeti sa [http://challenges.local](http://challenges.local/). To smo napravili korištenjem alata **wget.**

Nakraju smo koristili ponovno hydru, ali sa dictionaryem:

```python
hydra -l pleic_iva -P dictionary/g3/dictionary_online.txt pleiciva.local -V -t 4 ssh
```

Kada smo dobili našu lozinku, pomoću **ssh klijenta** smo se prijavili **na *remote* server.

> KOMENTAR: Moja lozinka je bila: *ondres*
> 

## **Offline Password Guessing**

Kada smo se uspješno logirali u *remote* server započinjemo sa *offline password guessing* napadom.

Za ovaj zadatak koristit ćemo **hashcat** alat.

Ovu vrstu napada izvest ćemo korištenjem *hasheva* koji se nalaze pohranjeni u **Linux** OS-u:

```python
sudo cat /etc/shadow
```

Pokretanjem ove naredbe nam se ispisala lista korisnika navedena s njihovim ***hashevima***.

Izabrali smo proizvoljno nekog korisnika i njegov ***hash** (Alice Cooper)*.

Kopiranu ***hash*** vrijednost smo spremili na naš lokalni uređaj (u **pwd_hash.txt** datoteku).

Napad smo izvršili naredbom:

```python
hashcat --force -m 1800 -a 3 hash.txt ?l?l?l?l?l?l --status --status-timer 10
```

> ?l?l?l?l?l? predstavlja format naše lozinke
> 

Ukupan broj kombinacija je otprilike isti kao i kod prethodnog napada te unatoč činjenici što je *hash* funkcija brža nekih 100 puta, **razlika** u odnosu na prethodni napad je **zanemarivo mala**.

Stoga smo opet koristili ***dictionary***.

Sada ćemo uz pomoć *dictionary-a* **smanjiti broj mogućih kombinacija** te ponovn, izvršiti napad:

```python
hashcat --force -m 1800 -a 0 pwd_hash.txt dictionary/g3/dictionary_offline.txt --status --status-timer 10
```

Nakon što smo dobili lozinku, preko **ssh klijenta** smo se prijavili na server.

```python
ssh alice_cooper@10.0.15.5
```