# Die Wissensdatenbank. In vier Kategorien sortiert.
# Jeder Eintrag hat:
#   id    = interner Name (die Gluehbirne im Rechner verweist darauf)
#   titel = Ueberschrift
#   text  = Erklaerung
# Du kannst Texte frei aendern, hinzufuegen oder loeschen.

WISSEN = [
    {
        "kategorie": "Bit & Byte",
        "icon": "SWAP_HORIZ",
        "eintraege": [
            {"id": "bit", "titel": "Bit (b)",
             "text": "Kleinste Informationseinheit: entweder 0 oder 1. Ein kleines 'b' "
                     "steht fuer Bit. Man braucht 8 Bit fuer ein Byte."},
            {"id": "byte", "titel": "Byte (B)",
             "text": "1 Byte = 8 Bit. Ein grosses 'B' steht fuer Byte. Dateien und Downloads "
                     "werden meist in Byte gemessen."},
            {"id": "kbit", "titel": "kbit/s (Kilobit pro Sekunde)",
             "text": "1000 Bit pro Sekunde. Schreibweisen: kbit/s, kbps. Sehr kleine, alte "
                     "oder langsame Verbindungen."},
            {"id": "kbyte", "titel": "kB/s (Kilobyte pro Sekunde)",
             "text": "1000 Byte pro Sekunde = 8000 Bit pro Sekunde. Schreibweisen: kB/s, kBps. "
                     "Langsame Downloads."},
            {"id": "mbit", "titel": "Mbit/s (Megabit pro Sekunde)",
             "text": "Eine Million Bit pro Sekunde. Das ist die Standard-Einheit fuer "
                     "Internet-Tarife, Router und Switches. Schreibweisen: Mbit/s, Mbps, Mbit."},
            {"id": "mbyte", "titel": "MB/s (Megabyte pro Sekunde)",
             "text": "Eine Million Byte pro Sekunde = 8 Mbit/s. Das zeigt der Browser beim "
                     "Download und Windows beim Kopieren. Schreibweisen: MB/s, MBps, MByte/s."},
            {"id": "gbit", "titel": "Gbit/s (Gigabit pro Sekunde)",
             "text": "1000 Mbit/s. Ueblich bei modernen Netzwerken (Gigabit bis 10G). "
                     "Schreibweisen: Gbit/s, Gbps, Gbit."},
            {"id": "gbyte", "titel": "GB/s (Gigabyte pro Sekunde)",
             "text": "1000 MB/s = 8000 Mbit/s. Sehr schnell - erreicht man nur mit "
                     "10-Gigabit-Netzwerken oder schnellen SSDs. Schreibweisen: GB/s, GBps."},
            {"id": "bitvsbyte", "titel": "Bit vs. Byte - warum zwei Zahlen?",
             "text": "1 Byte = 8 Bit. Dieselbe Leitung ist in Bit achtmal so gross wie in Byte. "
                     "Hersteller schreiben gern Bit auf die Verpackung, weil die Zahl groesser "
                     "aussieht. Beispiel: 100 Mbit/s = 12,5 MB/s."},
            {"id": "echt", "titel": "Was real ankommt (Overhead)",
             "text": "Auf einer Leitung ist immer etwas Platz fuer Steuerdaten (Ethernet, IP, TCP). "
                     "Bei Ethernet bleiben rund 94 % uebrig, also etwa 6 % weniger. Aus "
                     "1000 Mbit/s werden so real ca. 118 MB/s statt 125 MB/s."},
            {"id": "mib", "titel": "MB vs. MiB (1000 oder 1024?)",
             "text": "MB rechnet dezimal: 1 MB = 1.000.000 Byte. MiB rechnet binaer: "
                     "1 MiB = 1.048.576 Byte. Windows zeigt oft MiB, schreibt aber MB. "
                     "Deshalb wirkt eine Festplatte manchmal etwas kleiner."},
            {"id": "erkennen", "titel": "So erkennst du Bit und Byte",
             "text": "Klein/Gross: 'b' = Bit, 'B' = Byte, also Mb ist nicht MB. "
                     "Schreibweise: Mbit/s, Mbps, Gbit/s sind Bit, MB/s ist Byte. "
                     "Orte: Switch, LAN-Port, Tarif und WLAN sind fast immer Bit; "
                     "Dateikopie, Download und SSD-Tempo sind Byte."},
        ],
    },
    {
        "kategorie": "Ethernet-Standards",
        "icon": "LAN",
        "eintraege": [
            {"id": "ethernet", "titel": "Ethernet",
             "text": "Die Urform des kabelgebundenen Netzwerks (LAN): 10 Mbit/s. "
                     "Der Name steht heute allgemein fuer LAN-Kabel-Technik."},
            {"id": "fast-ethernet", "titel": "Fast Ethernet",
             "text": "100 Mbit/s (IEEE 802.3u). Heute das Minimum. Reicht fuer Surfen und "
                     "Streaming, ist aber bei grossen Dateien oder mehreren Geraeten schnell "
                     "eine Bremse."},
            {"id": "gigabit", "titel": "Gigabit Ethernet (GbE / 1G)",
             "text": "1000 Mbit/s (IEEE 802.3ab, 1000BASE-T). Der Standard in fast jedem "
                     "Heimnetz. Theoretisch 125 MB/s, real ca. 115-118 MB/s."},
            {"id": "2g5", "titel": "2,5-Gigabit-Ethernet (2,5GbE / 2G5)",
             "text": "2500 Mbit/s (IEEE 802.3bz). Beliebt bei NAS und neuen Mainboards. "
                     "Laeuft oft schon ueber vorhandene Cat-5e-Kabel. Theoretisch 312,5 MB/s."},
            {"id": "5ge", "titel": "5-Gigabit-Ethernet (5GbE)",
             "text": "5000 Mbit/s. Zwischenstufe fuer schnelle Heimnetze und NAS, ohne "
                     "sofort auf 10G aufruesten zu muessen."},
            {"id": "10ge", "titel": "10-Gigabit-Ethernet (10GbE / 10G)",
             "text": "10.000 Mbit/s (IEEE 802.3an, 10GBASE-T). Fuer Server und grosse "
                     "Datenmengen. Real ca. 1100 MB/s."},
            {"id": "25-100g", "titel": "25G / 40G / 100G",
             "text": "Sehr hohe Stufen fuer Rechenzentren und Backbone. Im Heimnetz keine Rolle."},
            {"id": "rj45", "titel": "RJ45",
             "text": "Der normale LAN-Stecker und die LAN-Buchse. 8 Kontakte. "
                     "Mit allen 8 Kontakten ist Gigabit und mehr moeglich."},
            {"id": "autoneg", "titel": "Autonegotiation",
             "text": "Beim Verbinden einigen sich zwei Geraete automatisch auf die hoechste "
                     "gemeinsame Geschwindigkeit. Ein 2,5G-NAS an einem 1G-Switch laeuft "
                     "deshalb nur mit 1000 Mbit/s."},
            {"id": "baset", "titel": "100BASE-TX / 1000BASE-T / 10GBASE-T",
             "text": "Technische Bezeichnungen der Ethernet-Standards ueber Kupferkabel (RJ45). "
                     "Die Zahl vorn ist die Geschwindigkeit in Mbit/s, das 'T' steht fuer "
                     "Twisted-Pair-Kabel."},
        ],
    },
    {
        "kategorie": "WLAN / Wi-Fi",
        "icon": "WIFI",
        "eintraege": [
            {"id": "wlan", "titel": "WLAN",
             "text": "Kabelloses lokales Netzwerk. Anders als Kabel teilen sich alle Geraete "
                     "die Funkluft, daher schwankt die Geschwindigkeit stark."},
            {"id": "wifi4", "titel": "Wi-Fi 4 (802.11n)",
             "text": "Bis 600 Mbit/s brutto (theoretisch), real deutlich weniger. "
                     "Laeuft auf 2,4 und 5 GHz."},
            {"id": "wifi5", "titel": "Wi-Fi 5 (802.11ac)",
             "text": "Bis rund 6,9 Gbit/s brutto (theoretisch, mehrere Antennen). "
                     "Nur im 5-GHz-Band. Der heutige Standard."},
            {"id": "wifi6", "titel": "Wi-Fi 6 / 6E (802.11ax)",
             "text": "Bis rund 9,6 Gbit/s brutto. Wi-Fi 6E nutzt zusaetzlich das 6-GHz-Band. "
                     "Besser bei vielen Geraeten gleichzeitig."},
            {"id": "wifi7", "titel": "Wi-Fi 7 (802.11be)",
             "text": "Mehrere Gbit/s in der Praxis. Neueste Generation, arbeitet auf 2,4, "
                     "5 und 6 GHz."},
            {"id": "frequenzen", "titel": "2,4 / 5 / 6 GHz",
             "text": "2,4 GHz: weit, aber langsam und voll. 5 GHz: schneller, kuerzere Reichweite. "
                     "6 GHz: am schnellsten, nur mit Wi-Fi 6E/7."},
            {"id": "access-point", "titel": "Access Point (AP)",
             "text": "Die WLAN-Basisstation. Haengt meist per LAN-Kabel am Router und versorgt "
                     "die Geraete per Funk."},
            {"id": "mimo", "titel": "MIMO",
             "text": "Mehrere Sende- und Empfangsantennen gleichzeitig ('Multiple Input Multiple "
                     "Output'). Mehr Antennen = mehr Durchsatz."},
        ],
    },
    {
        "kategorie": "Netzwerkkabel (Cat)",
        "icon": "CABLE",
        "eintraege": [
            {"id": "twisted-pair", "titel": "Twisted Pair",
             "text": "Verdrillte Adernpaare im LAN-Kabel. Die Verdrillung schuetzt vor Stoerungen. "
                     "Standard-Stecker ist RJ45."},
            {"id": "cat5", "titel": "Cat 5",
             "text": "Bis 100 Mbit/s. Veraltet, heute nicht mehr empfohlen."},
            {"id": "cat5e", "titel": "Cat 5e",
             "text": "Bis 1 Gbit/s (und oft 2,5G). Das Minimum fuer Neuinstallationen."},
            {"id": "cat6", "titel": "Cat 6",
             "text": "1 Gbit/s, bei kurzen Strecken bis 55 m auch 10 Gbit/s. Gute Wahl fuer Heimnetz."},
            {"id": "cat6a", "titel": "Cat 6a",
             "text": "Sicher 10 Gbit/s ueber 100 m. Empfohlen fuer 10-Gigabit-Netzwerke."},
            {"id": "cat7", "titel": "Cat 7 / 7a",
             "text": "10 Gbit/s, gut abgeschirmt. Fuer anspruchsvolle Umgebungen (viele Stoerquellen)."},
            {"id": "cat8", "titel": "Cat 8",
             "text": "Bis 40 Gbit/s. Nur im Rechenzentrum ueblich, fuer Zuhause ueberdimensioniert."},
        ],
    },
]

# Schnelle Suche per id (fuer die Gluehbirnen im Rechner)
_INDEX = {}
for _kat in WISSEN:
    for _e in _kat["eintraege"]:
        _INDEX[_e["id"]] = _e


def finde(id):
    """Gibt den Eintrag {titel, text} zu einer id zurueck (oder None)."""
    return _INDEX.get(id)


def alle_eintraege():
    """Alle Eintraege als flache Liste."""
    return [e for kat in WISSEN for e in kat["eintraege"]]
