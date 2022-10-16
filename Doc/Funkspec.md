# Ajánlórendszer funkcionális specifikáció

## 1. Áttekintés

Egy olyan rendszert fejlesztünk, ami segítségével az emberek értékelhessenek különböző filmeket, sorozatokat, zenéket, stb. A felhasználónak lehetősége lesz rengeteg különböző műfajból tartalmakat választani és értékelni, majd értékelései alapján kapni fog különböző ajánlásokat az adott műfajból. Az alkalmazás böngészőn keresztül érhető majd el, hogy letöltés nélkül lehessen élvezni az alkalmazás előnyeit. A rendszer teljesen ingyenes lesz, ezért bárki egy regisztráció után könnyedén hozzáférhet a szolgáltatáshoz. A folyton bővülő tartalmak miatt, a felhasználó folyamatosan kaphat újabb és újabb ajánlásokat, így sose fogy ki az újdonságokból.

## 2. Jelenlegi helyzet

A megrendelő szeretne egy olyan rendszert, ami segítségével a felhasználó nem csak értékeléseket tudna adni filmekre, zenékre, sorozatokra, stb., hanem az értékelések alapján az adott felhasználónak a legszemélyebbre szabott ajánlásokat tudja adni a program a különböző témákból és műfajokból. Ezzel a kibővített funkcióval is előnyhöz jutni a piacon a versenytársakkal szemben. Egy új rendszer előállítását rendelte meg, amely interneten keresztül modern megoldásokat használva működik. A rendszer egy kiváló lehetőséget ad azok számára akik új, például filmeket akarnak megismerni kedvenc témaköreikben. A mai világ már megköveteli, hogy mindez hálózaton is elérhető legyen, ennek megfelelően weboldalon a megrendelő rendelkezésére kell bocsátani. Eddig a megrendelő nem használt ehhez hasonló programokat, de számos kollégájától hallott róluk és észrevette a benne lévő piaci rést. Ezért elkezdett keresgélni és összeállítani egy olyan programtervet, amelyben kipótolja ezen rendszerek hiányosságait. Egy olyan programra lenne szükség, amely enged értékelni műfajokat, de ezzel együtt különböző ajánlásokat ad a felhasználónak értékelések alapján.

## 3. Vágyálom rendszer

A projekt célja egy olyan webalkalmazás fejlesztése, amely segítségével az emberek könnyedén értékelhetnek filmeket, zenéket, sorozatokat, könyveket, stb. A szoftver online, böngészőn keresztül érhető el. Regisztrációt követően a felhasználó kiválaszthatja kedvenc műfajait, amiben már el is kezdhet keresgélni és értékelni az adott tartalmat. A felhasználó értékelései alapján kaphat különböző ajánlásokat. A rendszernek van egy admin felülete is, ahol az admin egy bejelentkezés után fel tud tölteni az egyes műfajokba értékelhető tartalmakat.

## 4. Jelenlegi üzleti folyamatok


## 5. Igényelt üzleti folyamatok


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

