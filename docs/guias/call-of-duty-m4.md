# Guia de compatibilitat de Call of Duty i Modern Warfare en Mac amb Apple Silicon (Mac Mini M4)

Si tens un **Mac Mini M4** i vols saber quins jocs de la saga **Call of Duty** i **Modern Warfare** pots jugar-hi, i com pots comprovar la seva compatibilitat, aquesta guia t'explicarà de manera detallada l'estat actual de la saga en els ordinadors Mac moderns.

---

## 1. El context tècnic de l'M4 i macOS modern

Abans d'analitzar joc per joc, és important entendre les regles del joc de macOS actual:
1. **Adéu als 32 bits:** macOS Catalina (10.15) i totes les versions posteriors (com macOS Sonoma i Sequoia) **no executen aplicacions de 32 bits**.
2. **Rosetta 2 i Apple Silicon (M1, M2, M3, M4):** Els xips de la sèrie M utilitzen una arquitectura diferent (ARM de 64 bits). Rosetta 2 és el traductor integrat de macOS que permet obrir jocs antics dissenyats per a processadors Intel, però **només si són de 64 bits**.
3. **Sistemes anti-trampes (Anti-Cheat):** Els llançaments moderns de Call of Duty utilitzen **Ricochet Anti-Cheat**, un programari que s'executa a nivell de nucli (kernel-level) a Windows. Això impedeix totalment executar aquests jocs utilitzant emuladors, màquines virtuals o capes de compatibilitat.

---

## 2. On pots comprovar la compatibilitat de qualsevol joc?

Quan vulguis saber si un joc concret funciona en el teu Mac Mini M4, et recomanem consultar les següents plataformes de referència creades per la comunitat de gaming en Mac:

1. **AppleGamingWiki** ([applegamingwiki.com](https://www.applegamingwiki.com)): La base de dades més gran de videojocs per a Mac. Indica si funcionen, si ho fan nativament o requereixen alguna eina (com Whisky o CrossOver), el rendiment (FPS) i possibles solucions a errors comuns.
2. **Apple Silicon Games** ([applesilicongames.com](https://applesilicongames.com)): Una excel·lent eina de cerca directa on pots escriure el títol de qualsevol joc per veure la seva compatibilitat i el tipus d'entorn necessari (Native, Rosetta, CrossOver, Parallels, etc.).
3. **MacGamerHQ** ([macgamerhq.com](https://www.macgamerhq.com)): Un lloc web de notícies i anàlisi sobre jocs per a Mac que ofereix llistats actualitzats de jocs d'acció i trets en primera persona (FPS) compatibles.
4. **Atenció amb Steam:** De vegades, Steam mostra que un joc és compatible amb Mac (amb una icona de l' poma), però cal vigilar: si és un títol de 32 bits (com els MW originals), no s'executarà nativament a menys que s'indiqui expressament que és compatible amb versions de macOS de 64 bits.

---

## 3. Classificació de la saga Call of Duty / Modern Warfare per al teu M4

Aquí tens l'estat de compatibilitat de la saga classificat segons la manera de jugar-hi:

### A. Jocs Natius / Compatibles localment (Rosetta 2)
Són jocs que es poden descarregar directament des de Steam o la Mac App Store i s'executen a l'M4 mitjançant Rosetta 2 de forma molt senzilla.

* **Call of Duty: Black Ops III (2015):**
  * **Estat:** **Perfectament playable (Compatible)**.
  * **Detalls:** Disposa d'una versió nativa per a Mac de 64 bits desenvolupada per Aspyr. Gràcies a la potència gràfica del xip M4, funciona amb un rendiment excel·lent i gràfics elevats.
  * **Nota de comunitat:** Per jugar al mode multijugador o zombies en línia amb usuaris de Windows, es recomana fer servir el pedaç comunitari conegut com **BO3MacFix** a Steam, ja que el servei de matchmaking original del port de Mac pot tenir dificultats de connexió.

### B. Jocs antics jugables mitjançant Capes de Compatibilitat o Màquines Virtuals
Són els títols de l'època clàssica que ja no funcionen de forma nativa a macOS per la restricció dels 32 bits, però que es poden jugar gràcies a programes externs a l'M4.

* **Call of Duty 4: Modern Warfare (2007 - Original):**
* **Call of Duty: Modern Warfare 2 (2009 - Original):**
* **Call of Duty: Modern Warfare 3 (2011 - Original):**
* **Call of Duty: Black Ops (2010):**
  * **Estat:** **No funcionen nativament** en macOS moderns, però **sí que funcionen mitjançant mètodes alternatius**.
  * **Com jugar-los a l'M4:**
    1. **Whisky o CrossOver (Capa de traducció de Windows gratuïta / de pagament):** Pots utilitzar aquestes utilitats per instal·lar la versió de Steam per a Windows d'aquests jocs clàssics. Funcionen molt bé i amb taxes de fotogrames estables.
    2. **Parallels Desktop o VMWare Fusion (Màquina virtual de Windows 11 ARM):** Windows 11 ARM inclou un emulador que tradueix aplicacions de 32 bits. Pots jugar-hi instal·lant Windows virtualitzat al teu Mac Mini M4, ideal si vols utilitzar comandaments (perifèrics) de manera senzilla.

### C. Jocs moderns jugables l'única via de Joc al Núvol (Cloud Gaming)
Són els títols més recents de la franquícia. Com que utilitzen sistemes anti-trampes molt estrictes (com Ricochet), és completament impossible executar-los localment en macOS, ni tan sols utilitzant Whisky, CrossOver o Parallels.

* **Call of Duty: Modern Warfare (2019):**
* **Call of Duty: Modern Warfare II (2022):**
* **Call of Duty: Modern Warfare III (2023):**
* **Call of Duty: Warzone (Gratuït):**
* **Call of Duty: Black Ops 6:**
  * **Estat:** **Incompatible localment**, però **jugables en streaming (Núvol)**.
  * **Com jugar-los a l'M4:**
    1. **GeForce NOW (NVIDIA):** Pots jugar a qualsevol d'aquests jocs connectant el teu compte de Steam, Battle.net o Xbox Game Pass. Funciona de meravella en el Mac Mini M4, ja que el processament gràfic es fa als servidors de NVIDIA, oferint resolució fins a 4K i 120 FPS si disposes d'una connexió estable a Internet (mínim de 40-50 Mbps recomanats).
    2. **Boosteroid:** Una plataforma de joc al núvol molt utilitzada a Europa que té un excel·lent suport per a tota la saga Call of Duty i una latència extremadament reduïda.
    3. **Xbox Cloud Gaming:** Si tens una subscripció a Xbox Game Pass Ultimate, pots jugar a les campanyes i multijugadors de Call of Duty inclosos directament des de Safari o qualsevol altre navegador de manera ràpida.

---

## 4. Consell addicional per a usuaris de Mac Mini M4

* **Adaptadors de Perifèrics:** Si tens joysticks, ratolins o auriculars de joc més antics amb connector USB-A (rectangular clàssic), recorda que el Mac Mini M4 compta exclusivament amb ports USB-C al darrere i al davant, per la qual cosa necessitaràs un petit adaptador o HUB USB-C per poder-los connectar.
* **Integració a l'escriptori de macOS:** Recorda que si utilitzes serveis de joc al núvol a través del navegador Safari, pots utilitzar la funció **"Afegeix a la dock"** (Add to Dock) per convertir la web de GeForce NOW o Xbox Cloud Gaming en una aplicació independent amb la seva pròpia icona per llançar els jocs ràpidament.
