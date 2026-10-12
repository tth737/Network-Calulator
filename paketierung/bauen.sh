#!/bin/bash
# Netzwerk-Speed als Linux-Flatpak bauen.
#
# Ablauf:
#   1) Voraussetzungen (einmalig):
#        sudo dnf install clang lld gtk3-devel libsecret-devel gstreamer1-devel flatpak-builder
#        sudo flatpak install -y flathub org.freedesktop.Sdk//25.08
#        # (flet + Flutter-SDK werden beim ersten Build automatisch geholt)
#
#   2) Dieses Skript ausfuehren:
#        ./bauen.sh
#
# Ergebnis: <Buildordner>/dist/Netzwerk-Speed-0.1.0.flatpak
#
# Hinweis: Gebaut wird in einer lokalen Kopie, WEIL das NAS keine Symlinks
# erlaubt (flet build legt einen build/-Ordner mit Symlinks an). Der Quellcode
# bleibt dauerhaft auf dem NAS und wird hier nur kopiert.

set -euo pipefail

QUELLE="/home/theo/NAS-Lager/Workspace_Migration/Coding/Kleine Tools/Netzwerk-Speed"
BUILD="/home/theo/netzwerk-speed-build"
VENV="/home/theo/.venvs/netzwerk-speed/bin/flet"

echo "==> 1/5 Lokale Build-Kopie aktualisieren (NAS -> $BUILD)"
rm -rf "$BUILD"
mkdir -p "$BUILD"
cp -r "$QUELLE/app.py" "$QUELLE/pyproject.toml" "$QUELLE/requirements.txt" "$BUILD/"
cp -r "$QUELLE/daten" "$BUILD/daten"
cp -r "$QUELLE/assets" "$BUILD/assets"
cp -r "$QUELLE/LICENSE" "$BUILD/LICENSE"
find "$BUILD" -name __pycache__ -type d -prune -exec rm -rf {} + 2>/dev/null || true

echo "==> 2/5 Echtes App-Bundle bauen (flet build linux)"
(
  cd "$BUILD"
  "$VENV" build linux . --module-name app --yes
)

echo "==> 3/5 Flatpak in Sandbox verpacken (flatpak-builder)"
mkdir -p "$BUILD/flatpak"
cp "$QUELLE/paketierung/org.tth737.netzwerkspeed.json" "$BUILD/flatpak/"
cp "$QUELLE/paketierung/org.tth737.netzwerkspeed.metainfo.xml" "$BUILD/flatpak/"
flatpak-builder --force-clean \
  --repo="$BUILD/flatpak-repo" \
  --state-dir="$BUILD/flatpak-state" \
  "$BUILD/flatpak-app" \
  "$BUILD/flatpak/org.tth737.netzwerkspeed.json"

echo "==> 4/5 Einzeldatei erzeugen (.flatpak)"
mkdir -p "$BUILD/dist"
flatpak build-bundle \
  --runtime-repo=https://flathub.org/repo/flathub.flatpakrepo \
  "$BUILD/flatpak-repo" \
  "$BUILD/dist/Netzwerk-Speed-0.1.0.flatpak" \
  org.tth737.netzwerkspeed

echo "==> 5/5 Nach Kopie auf das NAS"
mkdir -p "$QUELLE/Pakete"
cp "$BUILD/dist/Netzwerk-Speed-0.1.0.flatpak" "$QUELLE/Pakete/"

echo "==> FERTIG:"
ls -la "$BUILD/dist/"
echo "Installieren mit:  flatpak install ./Pakete/Netzwerk-Speed-0.1.0.flatpak"
echo "Starten mit:       flatpak run org.tth737.netzwerkspeed"