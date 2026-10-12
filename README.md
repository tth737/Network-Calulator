# Netzwerk-Speed

Eine kleine App zum Umrechnen von Netzwerk- und Datengeschwindigkeiten, mit
einer kurzen Wissensdatenbank rund um Heimnetzwerke. Geschrieben mit Flet
(Python). Es gibt Pakete für Linux (Flatpak) und Android (APK).

## Funktionen

Rechner

- Zahl und Einheit eingeben (zum Beispiel 2,5 Gbit/s).
- Umrechnung in bit/s, kbit/s, Mbit/s, Gbit/s sowie B/s, kB/s, MB/s, GB/s.
- Karte "Was real ankommt": zeigt die effektive Dateigeschwindigkeit mit etwa
  6 Prozent Overhead.

Wissen

- Wissensdatenbank in vier Kategorien: Bit und Byte, Ethernet, WLAN,
  Netzwerkkabel.
- Suchfeld zum Filtern.
- Glühbirnen-Symbole im Rechner öffnen die passende Erklärung.

## Installation

Fertige Pakete liegen unter "Releases".

Flatpak (Linux):

    flatpak install ./Netzwerk-Speed-0.1.0.flatpak
    flatpak run org.tth737.netzwerkspeed

APK (Android, arm64):

    Die Datei Netzwerk-Speed-0.1.0-arm64.apk auf das Gerät kopieren, öffnen und
    installieren (dafür "Unbekannte Quellen" zulassen).

## Starten (Entwicklung)

    python3 -m venv .venv
    . .venv/bin/activate
    pip install -r requirements.txt
    flet run app.py

## Selbst bauen

Flatpak:

    ./paketierung/bauen.sh

APK:

    ./paketierung/bauen-apk.sh

Beide Skripte nutzen das Flutter-SDK und sind auf eine lokale Umgebung
ausgelegt. Einzelheiten stehen als Kommentar am Anfang der Skripte.

## Projektaufbau

    app.py                 Oberfläche und Navigation
    daten/umrechnung.py    Rechenlogik und Einheiten
    daten/texte.py         Oberflächentexte
    daten/wissen.py        Wissensdatenbank
    assets/icon.png        App-Icon
    paketierung/           Flatpak-Manifest, Metainfo und Build-Skripte

## Mitwirkende

- tth737

## Haftungsausschluss

Die Nutzung der App und aller enthaltenen Texte erfolgt auf eigene Gefahr. Es
wird keine Haftung für Schäden, Fehler oder daraus folgende Nachteile
übernommen.

## Lizenz

GNU General Public License v3.0. Der vollständige Text liegt in der Datei
LICENSE.
