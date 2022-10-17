# **Man-in-the-middle attacks** (ARP spoofing) 
---
## Opis vježbe

Za potrebe vježbe smo koristili **windows powershell** za upis naredbi te je potrebno na računalu imati instalirano **WSL** (Windows Subsystem for Linux)

Pomoću **Dockera** smo virtualizirali 3 uređaja te ih spojili u zajedničku mrežu.
 
**Uređaji:**
1. station-1 - uređaj koji će se ponašati kao klijent

2. station-2 - uređaj koji će se ponašati kao server

3. evil-station - uređaj kojim ćemo prisluškivati promet između klijenta i servera
---

Spojili smo se u terminal kao **station-1** uređaj i naredbom **ipconfig** saznali njegovu `IP` (172.29.0.2) i `MAC` (:02) adresu. Pa smo trebali saznati `IP` (172.29.0.4) i `MAC` (:04) adresu **station-2** uređaja. To smo učinili **pinganjem station-2** uređaja.

Korištenjem **netcat** alata uspostavili smo vezu između uređaja station-1 i station-2.

Sljedeće smo ubacili napadača **evil-station** u kanal kojim komuniciraju uređaji **station-1** i **station-2**.

Da bismo presreli promet između dvije žrtve, izvoru podataka (**station-1**) smo se, u ulozi napadača (**evil-station**), trebali predstaviti kao **station-2**. Da bismo postigli takvu situaciju, koristili smo alat **arpspoof**.S time je narušena vjerodostojnost podataka.

Kao napadač pronašli smo se između dvije žrtve te možemo čitati podatke koji se razmjenjuju između njih. U ovoj situaciji je narušena i povjerljivost podataka.
___
### **Kako funkcionira ARP Spoofing?**
Napadač (**evil-station**) se predstavi meti napada (**station-1**) kao domaćin (**station-2**). Tada **station-1** svoje podatke šalje **evil-stationu**, a **evil-station** ih prosljeđuje **stationu-2**.

Kada ih **evil-station** nebi prosljeđivao **stationu-2**, tada bi bila narušena i dostupnost podataka.

Nakon narušavanja dostupnosti podataka još uvijek je moguća razmjena podataka u smjeru od stationa-2 prema stationu-1.
___
![image](https://github.com/nduje/Sigurnost-ra-unala-i-podataka/raw/main/Images/ARP_spoofing.png)