# Netzwerk-Speed - App fuer Linux und Android
# Nur Dunkelmodus. Zwei Bereiche: "Rechner" und "Wissen".
#
# Start auf Linux:   flet run app.py
# (venv liegt in /home/theo/.venvs/netzwerk-speed)

import flet as ft

from daten import umrechnung as u
from daten import texte as t
from daten import wissen as w

# --- Farben (dunkles Design) ---
HINTERGRUND = "#101716"
KARTE = "#18211f"
AKZENT = "#3fd0b0"
DUMPF = "#9cada8"
LINIE = "#2b3936"
HERVO = "#1b2e29"
WARN = "#f0985a"

# Rahmen fuer Eingabefelder (neue Flet-1.0-API)
FELD_RAND = ft.OutlineInputBorder(border_radius=10, side=ft.BorderSide(1, LINIE))


def main(page: ft.Page):
    page.title = t.APP_TITEL
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = HINTERGRUND
    page.padding = 0
    page.dark_theme = ft.Theme(color_scheme_seed=AKZENT)

    def zeige_begriff(bid):
        """Gluehbirne: passenden Wissen-Eintrag als Dialog zeigen."""
        eintrag = w.finde(bid)
        if not eintrag:
            return
        dialog = ft.AlertDialog(
            modal=True,
            title=ft.Row([
                ft.Icon(ft.Icons.LIGHTBULB_OUTLINE, color=AKZENT, size=20),
                ft.Text(eintrag["titel"], size=17, weight=ft.FontWeight.BOLD),
            ]),
            content=ft.Container(ft.Text(eintrag["text"], size=15), width=320),
            actions=[ft.TextButton(content=ft.Text("Schliessen"),
                                   on_click=lambda ev: page.pop_dialog())],
        )
        page.show_dialog(dialog)

    def gluehbirne(bid, gross=18):
        return ft.IconButton(
            icon=ft.Icons.LIGHTBULB_OUTLINE,
            icon_color=AKZENT,
            icon_size=gross,
            tooltip=t.GLUEHBIRNE_TOOLTIP,
            on_click=lambda ev: zeige_begriff(bid),
        )

    # ----------------------------------------------------------
    # Rechner
    # ----------------------------------------------------------
    def ergebnis_zeile(key, wert, aktiv):
        e = u.finde(key)
        schreib = "  ·  ".join(e["schreibweisen"])
        return ft.Container(
            content=ft.Row([
                ft.Column([
                    ft.Text(e["kurz"], size=15,
                            weight=ft.FontWeight.BOLD if aktiv else ft.FontWeight.NORMAL,
                            color=AKZENT if aktiv else None),
                    ft.Text(schreib, size=11, color=DUMPF),
                ], spacing=0, expand=True),
                ft.Text(u.fmt(wert), size=16, color=AKZENT if aktiv else None,
                        weight=ft.FontWeight.BOLD if aktiv else ft.FontWeight.NORMAL),
                gluehbirne(e["hilfe"]),
            ], vertical_alignment=ft.CrossAxisAlignment.CENTER),
            padding=ft.Padding.symmetric(vertical=2, horizontal=8),
            bgcolor=HERVO if aktiv else None,
            border_radius=8,
        )

    def echt_inhalt(zahl, key):
        e = u.finde(key)
        bps = zahl * e["faktor"]
        bps_netto = bps * u.EFF
        if e["art"] == "byte":
            text = t.ECHT_ALS_BIT.format(bit=u.best_bit(bps))
            hilfe_id = "bitvsbyte"
        else:
            text = t.ECHT_ECHTE_DATEI.format(
                echt=u.best_byte(bps_netto / 8),
                theorie=u.best_byte(bps / 8),
                prozent=t.ECHT_PROZENT_OVERHEAD,
            )
            hilfe_id = "echt"
        return ft.Container(
            content=ft.Column([
                ft.Row([
                    ft.Text(t.RECHNER_ECHT_TITEL, size=13, color=DUMPF),
                    gluehbirne(hilfe_id, gross=16),
                ], alignment=ft.MainAxisAlignment.START, spacing=0),
                ft.Text(text, size=14),
            ], spacing=2),
            padding=14,
            border_radius=10,
            bgcolor=HERVO,
            margin=ft.Margin.only(top=10),
        )

    def baue_rechner():
        ergebnis = ft.Column(spacing=0)
        echt_box = ft.Container(visible=False)

        wert = ft.TextField(
            label=t.RECHNER_ZAHL_LABEL,
            hint_text=t.RECHNER_ZAHL_HINWEIS,
            value="2,5",
            border=FELD_RAND,
            filled=True,
            bgcolor=KARTE,
        )
        einheit = ft.Dropdown(
            label=t.RECHNER_EINHEIT_LABEL,
            value="gbit",
            border=FELD_RAND,
            filled=True,
            bgcolor=KARTE,
            options=[ft.dropdown.Option(key=e["key"], text=e["kurz"]) for e in u.EINHEITEN],
        )

        def berechne(ev=None):
            z = u.parse_zahl(wert.value)
            key = einheit.value or "gbit"
            ergebnis.controls.clear()
            if z is None or z < 0:
                ergebnis.controls.append(ft.Text(t.RECHNER_FEHLER, color=WARN))
                echt_box.visible = False
                page.update()
                return
            werte = u.umrechnen(z, key)
            for k in u.ANZEIGE_REIHENFOLGE:
                ergebnis.controls.append(ergebnis_zeile(k, werte[k], k == key))
            echt_box.content = echt_inhalt(z, key)
            echt_box.visible = True
            page.update()

        wert.on_change = berechne
        einheit.on_change = berechne

        kopf = ft.Column([
            ft.Row([
                ft.Text(t.RECHNER_TITEL, size=22, weight=ft.FontWeight.BOLD),
                gluehbirne("bitvsbyte"),
            ], alignment=ft.MainAxisAlignment.START, spacing=0),
            ft.Text(t.RECHNER_UNTERTITEL, size=13, color=DUMPF),
        ], spacing=2)

        eingabe = ft.ResponsiveRow([
            ft.Container(wert, col={"xs": 12, "sm": 7}),
            ft.Container(einheit, col={"xs": 12, "sm": 5}),
        ])

        karte = ft.Container(
            content=ft.Column([eingabe, ergebnis, echt_box], spacing=8),
            padding=16, border_radius=14, bgcolor=KARTE,
            border=ft.Border.all(1, LINIE), margin=ft.Margin.only(top=8),
        )

        fuss = ft.Text(t.FUSSNOTE, size=12, color=DUMPF)

        berechne()  # einmal vorrechnen
        return [kopf, karte, fuss]

    # ----------------------------------------------------------
    # Wissen
    # ----------------------------------------------------------
    def baue_wissen():
        suche = ft.TextField(
            hint_text=t.WISSEN_SUCHE,
            prefix_icon=ft.Icons.SEARCH,
            border=FELD_RAND,
            filled=True, bgcolor=KARTE,
        )
        liste = ft.Column(spacing=8)

        def filtern(ev=None):
            begriff = (suche.value or "").lower().strip()
            liste.controls.clear()
            erster = True
            for kat in w.WISSEN:
                treffer = [
                    e for e in kat["eintraege"]
                    if begriff in e["titel"].lower() or begriff in e["text"].lower()
                ]
                if not treffer:
                    continue
                kinder = [
                    ft.ExpansionTile(
                        title=ft.Text(e["titel"], size=14),
                        controls=[ft.Container(
                            content=ft.Text(e["text"], size=14),
                            padding=ft.Padding.only(left=16, right=8, bottom=12),
                        )],
                        dense=True,
                        tile_padding=ft.Padding.symmetric(horizontal=12),
                    )
                    for e in treffer
                ]
                liste.controls.append(ft.ExpansionTile(
                    title=ft.Text(kat["kategorie"], size=15, weight=ft.FontWeight.BOLD),
                    leading=ft.Icon(getattr(ft.Icons, kat["icon"], ft.Icons.INFO), color=AKZENT),
                    controls=kinder,
                    expanded=(begriff == "" and erster),
                    dense=True,
                    bgcolor=KARTE,
                    collapsed_bgcolor=KARTE,
                    shape=ft.RoundedRectangleBorder(radius=12),
                    margin=ft.Margin.only(bottom=4),
                ))
                erster = False
            if not liste.controls:
                liste.controls.append(ft.Text(t.WISSEN_NICHTS, color=DUMPF))
            page.update()

        suche.on_change = filtern

        kopf = ft.Column([
            ft.Text(t.WISSEN_TITEL, size=22, weight=ft.FontWeight.BOLD),
            ft.Text(t.WISSEN_UNTERTITEL, size=13, color=DUMPF),
        ], spacing=2)

        filtern()  # einmal aufbauen
        return [kopf, suche, ft.Container(liste, margin=ft.Margin.only(top=8))]

    # ----------------------------------------------------------
    # Navigation
    # ----------------------------------------------------------
    inhalt = ft.ListView(expand=True, spacing=12, padding=16)

    def wechsle(index):
        inhalt.controls.clear()
        if index == 1:
            inhalt.controls.extend(baue_wissen())
        else:
            inhalt.controls.extend(baue_rechner())
        nav.selected_index = index
        page.update()

    nav = ft.NavigationBar(
        selected_index=0,
        bgcolor=KARTE,
        indicator_color=HERVO,
        on_change=lambda e: wechsle(e.control.selected_index),
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.CALCULATE, label=t.NAV_RECHNER),
            ft.NavigationBarDestination(icon=ft.Icons.MENU_BOOK, label=t.NAV_WISSEN),
        ],
    )

    page.add(
        ft.Column(
            [inhalt, nav],
            expand=True,
            spacing=0,
        )
    )

    wechsle(0)


ft.run(main)
