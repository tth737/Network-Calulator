# AGENTS.md

Anleitung für KI-Agenten, die an diesem Projekt arbeiten. Menschliche
Übersicht: siehe README.md.

## Projekt

Netzwerk-Speed ist eine Flet-App (Python) zum Umrechnen von Netzwerk- und
Datengeschwindigkeiten, mit einer kleinen Wissensdatenbank. Es gibt Pakete für
Linux (Flatpak) und Android (APK).

## Umgebung einrichten

    python3 -m venv .venv
    . .venv/bin/activate
    pip install -r requirements.txt

## Starten

    flet run app.py

## Projektstruktur

- app.py: Oberfläche und Navigation.
- daten/umrechnung.py: Rechenlogik und Einheiten (1 Byte = 8 bit, Overhead 0.94).
- daten/texte.py: alle Oberflächentexte.
- daten/wissen.py: Wissensdatenbank.

## Konventionen

- Oberflächentexte nur in daten/texte.py oder daten/wissen.py ändern.
- Rechenlogik gehört in daten/umrechnung.py, nicht in die Oberfläche.
- Sprache ist Deutsch. Keine Emojis in Code, Doku oder Commit-Nachrichten.
- Commit-Nachrichten auf Deutsch, kurz und sachlich.

## Builds

- Flatpak: ./paketierung/bauen.sh
- APK: ./paketierung/bauen-apk.sh
  - baut nur arm64-v8a, aus einem sauberen Quellordner ohne flatpak-app/
  - benötigt JDK 17

## Vor dem Commit

- Es gibt keinen Testrunner. Änderungen durch Start mit flet run app.py prüfen.
