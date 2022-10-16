# Ajánlórendszer funkcionális specifikáció

## 1. Áttekintés

Egy olyan rendszert fejlesztünk, ami segítségével az emberek értékelhessenek különböző filmeket, sorozatokat, zenéket, stb. A felhasználónak lehetősége lesz rengeteg különböző műfajból tartalmakat választani és értékelni, majd értékelései alapján kapni fog különböző ajánlásokat az adott műfajból. Az alkalmazás böngészőn keresztül érhető majd el, hogy letöltés nélkül lehessen élvezni az alkalmazás előnyeit. A rendszer teljesen ingyenes lesz, ezért bárki egy regisztráció után könnyedén hozzáférhet a szolgáltatáshoz. A folyton bővülő tartalmak miatt, a felhasználó folyamatosan kaphat újabb és újabb ajánlásokat, így sose fogy ki az újdonságokból.

## 2. Jelenlegi helyzet

A megrendelő szeretne egy olyan rendszert, ami segítségével a felhasználó nem csak értékeléseket tudna adni filmekre, zenékre, sorozatokra, stb., hanem az értékelések alapján az adott felhasználónak a legszemélyebbre szabott ajánlásokat tudja adni a program a különböző témákból és műfajokból. Ezzel a kibővített funkcióval is előnyhöz jutni a piacon a versenytársakkal szemben. Egy új rendszer előállítását rendelte meg, amely interneten keresztül modern megoldásokat használva működik. A rendszer egy kiváló lehetőséget ad azok számára akik új, például filmeket akarnak megismerni kedvenc témaköreikben. A mai világ már megköveteli, hogy mindez hálózaton is elérhető legyen, ennek megfelelően weboldalon a megrendelő rendelkezésére kell bocsátani. Eddig a megrendelő nem használt ehhez hasonló programokat, de számos kollégájától hallott róluk és észrevette a benne lévő piaci rést. Ezért elkezdett keresgélni és összeállítani egy olyan programtervet, amelyben kipótolja ezen rendszerek hiányosságait. Egy olyan programra lenne szükség, amely enged értékelni műfajokat, de ezzel együtt különböző ajánlásokat ad a felhasználónak értékelések alapján.

## 3. Vágyálom rendszer

A projekt célja egy olyan webalkalmazás fejlesztése, amely segítségével az emberek könnyedén értékelhetnek filmeket, zenéket, sorozatokat, könyveket, stb. A szoftver online, böngészőn keresztül érhető el. Regisztrációt követően a felhasználó kiválaszthatja kedvenc műfajait, amiben már el is kezdhet keresgélni és értékelni az adott tartalmat. A felhasználó értékelései alapján kaphat különböző ajánlásokat. A rendszernek van egy admin felülete is, ahol az admin egy bejelentkezés után fel tud tölteni az egyes műfajokba értékelhető tartalmakat.

## 4. Jelenlegi üzleti folyamatok

Ha valaki ajánlást szeretne valamiről (amilyen területen nem jártas), az egy hosszú és végeláthatatlan utánajárást von maga után. Például meg kell kérdeznie ismerőseit, vagy utánanézni az interneten, akár fórumokon, akár véleményező oldalakon. Mindezt pedig jó lenne szisztematikusan is csinálni, ami szinte biztos nem történik meg. Így végül nem a legjobb ajánlást kapja az adott személy.

Erre gondolotban megpróbálhatnánk egy szolgáltatást biztosítani. Az adatok gyűjtését sokféle módon lehetne kivitelezni. Például lehetne szerkeszteni online kérdőíveket. Ezeket nehéz összegyűjteni egy táblázatba, adatbázisba. Következő lépésként egy másik felületen elemezni, végül pedig visszaküldeni a válaszadóknak az eredményeket, például emailben.

Szóval a jelenlegi munkafolyamattal az a probléma, hogy kölünböző eszközöket, felületeket kell használni, amelyek nincsenek összehangolva. Továbbá sok benne a manuális, emberi feladat, annak ellenére, hogy könnyű lenne automatizálni a folyamatokat.

## 5. Igényelt üzleti folyamatok

A platformfügegtlen webalkalmazást egy Django alapú keretrendszerrel fogjuk kivitelezni, amely segítségével egyszerűbb lesz a fő oldalon való bejelentkezési adatok (felhasználónév, jelszó) kezelése, miután a felhasználó regisztrált a saját e-mail címével. Bejelentkezést követően a felhasználó lehetőséget kap különbőző funkciók használatához(különböző műfajokban keresgélés, ezek értekelése és ajánlások kapása a saját ízlésüknek megfelelően). Az oldalhoz tartoznak admin és user jogosultsággal rendelkező felhasználók, valamint több használható felület amiket HTML és CSS segítségével fogunk lértehozni, dizájnolni. Az admin felhasználók egy külön felülettel rendelkeznek, ahol különbőző értékelhető témakat képesek feltölteni, ezzel téve naprakésszé az alkalmazást. A user jogusultsággal rendelkező emberek, pedig értekelni tudnak különböző műfajokból kiválasztott tartalmakat (zene, film, sorozat, stb...), amik bármikor megváltoztathatóak és személyenként tárolva lesznek az adatok egy adatbázisban. Miután a felhasználó értékelt pár tartalmat, a webalkalmazás ajánlást tesz az értékelések alapján egy algoritmus segítségével a legérdekeltebb témákban, amik az újonnan feltöltött témák után frissülnek, így téve a felhasználók ízlésének eleget. Ezt követően, amennyiben a felhasználónak szüksége van rá, kijelentkezhet a saját felhasználójából. PL: (nem saját gép, más felhasználóba belépés) esetén.

## 6. Használati esetek

A rendszer használatához szükséges egy admin jogosultságokkal rendelkező felhasználó, aki fel tudja tölteni tartalommal az oldalt. Az adminok tudnak hozzáadni új témákat. A felületünk rengeteg témának teremti meg a lehetőséget. Ezek lehetnek filmek, ételek, műszaki cikkek stb. A témákon belül mintákat tudnak hozzáadni, szerkeszteni, törölni. A későbbiekben ezeket a mintákat fogják értékelni a felhasználók. Az admin összegző statisztikákat láthat a felhasználók által végzett értékelésekről.

Az átlagos felhasználók megtekinthetik a témákat. A témákon belül mintákat tudnak értékelni egy skálán. Viszont csak akkor értékelik, amennyiben ismerik is az adott mintát, különben kihagyják. Ők nem tudnak tartalmat feltölteni. Hozzáférnek a saját értékeléseikhez, illetve láthatják az ajánlásaikat.

## 7. Követelménylista

| Modul | ID  | Név | Verzió | Kifejtés |
|---|---|---|---|---|
| Felület | K01 | Admin  szerkesztés | 1.0| Adminfelületen felvihető mintacsoportok, minták |
| Jogosultság | K02 | Regisztráció | 1.0 | Felhasználók regisztrálása |
| Jogosultság | K03 | Belépés-kifelentkezés | 1.0 | Felhasználók és admin beléptetése-kijelentkeztetése |
| Felület | K04 | Értékelés | 1.0 | Minták értékelése |
| Felület | K05 | Ajánlás | 1.0 | Ajánlás készítés, felhasználói ízlésprofil alkotás |

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

Django:
>A Django egy nyílt forráskódú, magas szintű Python programozási nyelven írt keretrendszer, amely segítségével gyorsan tudunk weboldalakat készíteni és folyamatos fejlesztés alatt áll.

Algoritmus:
>Algoritmuson vagy eljáráson olyan megengedett lépésekből álló módszert, utasítás(sorozatot), részletes útmutatást, receptet értünk, amely valamely felmerült probléma megoldására alkalmas.
