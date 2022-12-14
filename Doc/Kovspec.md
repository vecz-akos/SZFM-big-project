# Ajánlórendszer követelmény specifikáció

## 1. Áttekintés

Az alkalmazás célja, hogy bárki könnyedén értékelhessen filmeket, zenéket, és egyébb dolgokat, akár témákra osztva. Az alkalmazás segítségével nem csak értékelni lehet, de az értékelések által ajánlásokat is kap a felhasználó az adott témában. Web felülettel rendelkezik a szoftver, ami könnyedén bárki számára elérhető. 

## 2. Jelenlegi helyzet

A mai világban az emberek életében egyre nagyobb szerepet játszanak a sorozatok, filmek, zenék, ami miatt egyre több is készül belőlük. Ennek pedig az lett a következménye, hogy rengeteg időt pocsékolnak el az emberek azzal, hogy keresgélik a nekik megfelelő tartalmakat, mivel nincs egy olyan lehetőség, ami képes lenne nem csak egy fajta műfajban ajánlást tenni, hanem akár egyszerre többen is, mint például a filmekben és zenékben. Erre nyújtana megoldást az általunk készítendő szoftver, amely képes lesz egyszerre ajánlásokat tenni filmekben, zenékben, sorozatokban csupán az alapján, hogy hogyan értékelünk mondjuk egy adott zenét.

## 3. Vágyálom rendszer

A projekt célja egy olyan webalkalmazás fejlesztése, amely segítségével az emberek könnyedén értékelhetnek filmeket, zenéket, sorozatokat, könyveket, stb. A szoftver online, böngészőn keresztül érhető el. Regisztrációt követően a felhasználó kiválaszthatja kedvenc műfajait, amiben már el is kezdhet keresgélni és értékelni az adott tartalmat. A felhasználó értékelései alapján kaphat különböző ajánlásokat. A rendszernek van egy admin felülete is, ahol az admin egy bejelentkezés után fel tud tölteni az egyes műfajokba értékelhető tartalmakat.

## 4. Követelménylista

| Modul | ID  | Név | Verzió | Kifejtés |
|---|---|---|---|---|
| Felület | K01 | Admin  szerkesztés | 1.0| Adminfelületen felvihető mintacsoportok, minták |
| Jogosultság | K02 | Regisztráció | 1.0 | Felhasználók regisztrálása |
| Jogosultság | K03 | Belépés-kifelentkezés | 1.0 | Felhasználók és admin beléptetése-kijelentkeztetése |
| Felület | K04 | Értékelés | 1.0 | Minták értékelése |
| Felület | K05 | Ajánlás | 1.0 | Ajánlás készítés, felhasználói ízlésprofil alkotás |

## 5. Rendszerre vonatkozó törvények, szabványok, ajánlások

 1. A felhasználók által megadott személyes adatokat a GDPR által meghatározott szabályok szerint tároljuk, dolgozzuk fel.
 2. A webes felület HTML5 és CSS3 szabványoknak megfelelő lesz.
 3. A mintákhoz társítható rövid leírások, képek nem állhatnak szerzői jogi oltalom alatt.

## 6. Jelenlegi üzleti folyamatok

Ha valaki ajánlást szeretne valamiről (amilyen területen nem jártas), az egy hosszú és végeláthatatlan utánajárást von maga után. Például meg kell kérdeznie ismerőseit, vagy utánanézni az interneten, akár fórumokon, akár véleményező oldalakon. Mindezt pedig jó lenne szisztematikusan is csinálni, ami szinte biztos nem történik meg. Így végül nem a legjobb ajánlást kapja az adott személy.

Erre gondolotban megpróbálhatnánk egy szolgáltatást biztosítani. Az adatok gyűjtését sokféle módon lehetne kivitelezni. Például lehetne szerkeszteni online kérdőíveket. Ezeket nehéz összegyűjteni egy táblázatba, adatbázisba. Következő lépésként egy másik felületen elemezni, végül pedig visszaküldeni a válaszadóknak az eredményeket, például emailben.

Szóval a jelenlegi munkafolyamattal az a probléma, hogy kölünböző eszközöket, felületeket kell használni, amelyek nincsenek összehangolva. Továbbá sok benne a manuális, emberi feladat, annak ellenére, hogy könnyű lenne automatizálni a folyamatokat.

## 7. Igényelt üzleti folyamatok

A megrendelő egy olyan platformfügegtlen webalkalmazást szeretne, amelyen a fő oldalon lehet bejelentkezni (felhasználónév, jelszó), de ezt megelőzően regisztrálnia kell saját e-mail címével. Bejelentkezést követően a felhasználó lehetőséget kap különbőző funkciók használatához. Az oldalhoz tartoznak admin és user jogosultsággal rendelkező felhasználók. Az admin felhasználók egy külön felülettel rendelkeznek, ahol különbőző értékelhető témakat képesek feltölteni. A user jogusultsággal rendelkező emberek, pedig értekelni tudnak különböző műfajokból kiválasztott tartalmakat (zene, film, sorozat, stb...). Miután a felhasználó értékelt pár tartalmat, a webalkalmazás ajánlást tesz az értékelés alapján legérdekeltebb témákban, a felhasználóknak külön-külön személyre szabva.

## 8. Fogalomtár

GDPR:
>A GDPR a General Data Protection Regulation kezdőbetűiből képzett mozaikszó, magyarul általános adatvédelmi rendelet.

Platformfüggetlen:
>Egy alkalmazás nem korlátozódik le egy eszközre, hanem több különböző eszközről is használható.

HTML:
>A HTML (angolul: HyperText Markup Language, „hiperszöveges jelölőnyelv”) egy leíró nyelv, melyet weboldalak készítéséhez fejlesztettek ki, és mára már internetes szabvánnyá vált a W3C (World Wide Web Consortium) támogatásával.

CSS:
>A CSS (Cascading Style Sheets, magyarul: „lépcsőzetes stíluslapok”) a számítástechnikában egy stílusleíró nyelv, mely a HTML vagy XHTML típusú strukturált dokumentumok megjelenését írja le.

Admin:
>Egy adott rendszer felügyeletét ellátó, a felett általában teljes kontrollal rendelkező felhasználó.

User:
>A user(magyarul: felhasználó) az a személy (végfelhasználó) vagy szoftverágens, aki egy számítógépes vagy számítógép-hálózati szolgáltatás használója.
