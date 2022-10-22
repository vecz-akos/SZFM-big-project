# Ajánlórendszer rendszerterv

## 1. A rendszer célja


## 2. Projektterv

**Projekt szerepkörök és felelőségek**:

Backend: Bródi Máté Gábor

Frontend: Kerekes Konrád Péter

Adatbázis: Oravecz Ákos

**Ütemterv**:

 * Fejlesztés: 2022. 10. 24. - 11. 13. és 11. 28. - 12. 04.
 * Tesztelés: 2022. 10. 14. - 12. 04.
 * Határidő: 2022. 12. 05.


## 3. Üzleti folyamatok modellje


## 4. Követelmények


## 5. Funkcionális terv


## 6. Fizikai környezet

Az alkalmazás web platformra, hordozható eszközökre (okostelefonok, táblagépek) készül.
- Nincsenek megvásárolt komponensek.
- Kliens által biztosított eszközök:
    - Webszerver
    - Okostelefon
    - Számítógép
    - Táblagép
- Fejlesztői eszközök:
    - github
    - Visual Studio Code
    - Notepad++
- Tesztelési környezet:
    - Chrome
    - Firefox
    - Opera
    - Safari
    - Microsoft Edge

## 7. Architekturális terv


## 8. Adatbázis terv

Az adatbázis 4 táblából fog állni, ezek össze lesznek kapcsolva. Egy felhasználóhoz (`User`) több értékelés (`Rates`) tartozik. Egy-egy értékelés egy mintára (`Sample`) hivatkozik. Több minta tartozhat egy kategóriába (`Category`).

A minden felhasználó kap egy hozzáférési szintet, ami megadja, hogy rendelkezik-e az adott felhasználó például admin jogosultságokkal.

Egy mintába, illetve kategóriba opcionálisan megadhatunk leírást és kép elérési útját. Egy mintához megadhatunk tageket is sztringként, ami vesszővel elválasztott felsorolás. Ez a tervezési megközelítés gyorsabb elérhetőséget biztosít.

![Adatbázis terv](/Doc/imgs/adatbazis.png)

## 9. Implementációs terv

A backend `Python`-ban lesz megírva. Webes keretrendszerként `Django`-t fogunk használni. Ezzel könnyen és gyorsan tudjuk a fejlesztést végezni. Eredményként pedig egy gyors, biztonságos és könnyen skálázható rendszert fogunk kapni. Az adatok feldolgozását a `Pandas` adatelemző programkönyvtárral végezzük. Ez könnyű használhatóságának köszönhetően egy népszerű eszköz és így mi is ezt választottuk. Az adatbázisként `SQLite`-ot fogjuk használni, ami integrálva van a `Django`-ba. Az adatbázisból olvasás `REST API`-val történik, ez könnyű hozzáférhetőséget biztosít az adatokhoz, illetve haladó felhasználók könnyen tudnak lekéréseket végezni.

A frontend `HTML5`, `CSS3` és `JavaScript` technológiákat fogja használni. Természetesen a `HTML5` szabványú fájl fog felelni a tartalomért. A megjelenésért a `CSS3` szabványú stíluslapok lesznek felelősek. Figyelmet fordítunk a színvakok és látássérültek nehézségeire, így a felületi elemeken különböző árnyalatú, világosságú színeket fogunk használni, amelyek könnyen elkülöníthetőek lesznek egymástól. A kliensoldalon futó `JavaScript` kód le fogja venni a terhet a szerverről és csupán minimálisan fogja használni a kliens számítógép erőforrásait.

Az összes különbőző technológia külön fájlban lesz, amelyeket egymáshoz fogunk csatolni. Ez a megközelítés átláthatóbb és gyorsabban fejleszthető projektet eredményez, ami majd segíti a jövőbeli karbantartást is.

## 10. Tesztterv


## 11. Telepítési terv


## 12. Karbantartási terv

