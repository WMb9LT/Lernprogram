from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
import random

# KMU Kontenplan als Dictionary, angepasst für die vier Kategorien
kontenplan = {
    "1000": {"name": "Kasse", "typ": "Aktivkonto"},
    "1020": {"name": "Bankguthaben (inkl. PostFinance)", "typ": "Aktivkonto"},
    "1060": {"name": "Wertschriften (mit Börsenkurs)", "typ": "Aktivkonto"},
    "1100": {"name": "Forderungen aus Lieferungen und Leistungen", "typ": "Aktivkonto"},
    "1170": {"name": "Vorsteuer MWST", "typ": "Aktivkonto"},
    "1176": {"name": "Verrechnungssteuer (Guthaben)", "typ": "Aktivkonto"},
    "1190": {"name": "Sonstige kurzfristige Forderungen", "typ": "Aktivkonto"},
    "1200": {"name": "Handelswaren (Warenvorrat)", "typ": "Aktivkonto"},
    "1210": {"name": "Rohstoffe", "typ": "Aktivkonto"},
    "1260": {"name": "Fertige Erzeugnisse (Fertigfabrikate)", "typ": "Aktivkonto"},
    "1440": {"name": "Darlehen (Aktivdarlehen)", "typ": "Aktivkonto"},
    "1500": {"name": "Maschinen und Apparate", "typ": "Aktivkonto"},
    "1510": {"name": "Mobiliar und Einrichtungen", "typ": "Aktivkonto"},
    "1520": {"name": "Büromaschinen (inkl. Informatik, Kommunikation)", "typ": "Aktivkonto"},
    "1530": {"name": "Fahrzeuge", "typ": "Aktivkonto"},
    "1540": {"name": "Werkzeuge und Geräte", "typ": "Aktivkonto"},
    "1600": {"name": "Geschäftsliegenschaften", "typ": "Aktivkonto"},
    "2000": {"name": "Verbindlichkeiten aus Lieferungen und Leistungen", "typ": "Passivkonto"},
    "2100": {"name": "Bankverbindlichkeiten", "typ": "Passivkonto"},
    "2200": {"name": "Geschuldete MWST", "typ": "Passivkonto"},
    "2450": {"name": "Darlehen (Passivdarlehen)", "typ": "Passivkonto"},
    "2451": {"name": "Hypotheken", "typ": "Passivkonto"},
    "2800": {"name": "Eigenkapital", "typ": "Passivkonto"},
    "3000": {"name": "Produktionserlöse", "typ": "Ertragskonto"},
    "3200": {"name": "Handelserlöse (Warenertrag)", "typ": "Ertragskonto"},
    "3400": {"name": "Dienstleistungserlöse", "typ": "Ertragskonto"},
    "3600": {"name": "Übrige Erlöse", "typ": "Ertragskonto"},
    "6950": {"name": "Finanzertrag", "typ": "Ertragskonto"},
    "4000": {"name": "Materialaufwand Produktion", "typ": "Aufwandskonto"},
    "4200": {"name": "Handelswarenaufwand (Warenaufwand)", "typ": "Aufwandskonto"},
    "4400": {"name": "Aufwand für bezogene Dienstleistungen", "typ": "Aufwandskonto"},
    "5000": {"name": "Lohnaufwand", "typ": "Aufwandskonto"},
    "5700": {"name": "Sozialversicherungsaufwand", "typ": "Aufwandskonto"},
    "5800": {"name": "Übriger Personalaufwand", "typ": "Aufwandskonto"},
    "6000": {"name": "Raumaufwand", "typ": "Aufwandskonto"},
    "6100": {"name": "Unterhalt, Reparaturen, Ersatz (URE)", "typ": "Aufwandskonto"},
    "6200": {"name": "Fahrzeugaufwand", "typ": "Aufwandskonto"},
    "6300": {"name": "Versicherungsaufwand", "typ": "Aufwandskonto"},
    "6400": {"name": "Energie- und Entsorgungsaufwand", "typ": "Aufwandskonto"},
    "6500": {"name": "Verwaltungsaufwand", "typ": "Aufwandskonto"},
    "6600": {"name": "Werbeaufwand", "typ": "Aufwandskonto"},
    "6700": {"name": "Sonstiger Betriebsaufwand", "typ": "Aufwandskonto"},
    "6800": {"name": "Abschreibungen", "typ": "Aufwandskonto"},
    "6900": {"name": "Finanzaufwand", "typ": "Aufwandskonto"}
}

class LernprogrammApp(App):
    def build(self):
        self.correct_answers = self.wrong_answers = 0
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # Label für Kontoanzeige und Ergebnisanzeige
        self.konto_label = Label(font_size=24, size_hint_y=None, height=50)
        self.result_label = Label(text="Richtig: 0 | Falsch: 0", font_size=20, size_hint_y=None, height=40)
        layout.add_widget(self.konto_label)
        layout.add_widget(self.result_label)

        # Buttons für Auswahlmöglichkeiten
        buttons_layout = BoxLayout(size_hint_y=None, height=200)
        for konten_typ in ["Aktivkonto", "Passivkonto", "Aufwandskonto", "Ertragskonto"]:
            button = Button(text=konten_typ, on_press=lambda btn: self.check_answer(btn.text))
            buttons_layout.add_widget(button)
        layout.add_widget(buttons_layout)

        # Nächstes Konto laden
        self.next_konto()
        return layout

    def next_konto(self):
        self.current_konto = random.choice(list(kontenplan.keys()))
        konto_info = kontenplan[self.current_konto]["name"]
        self.konto_label.text = f"Konto: {self.current_konto} - {konto_info}"

    def show_solution_popup(self, correct_typ):
        # Popup anzeigen, wenn die Antwort falsch ist, mit Kontonummer und Typ
        konto_name = kontenplan[self.current_konto]["name"]
        popup_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        # Verwende markup=True, um das Konto fett zu formatieren
        solution_label = Label(text=f"Richtige Antwort: {konto_name} - [b]{correct_typ}[/b]", font_size=20, markup=True, size_hint_y=None, height=80)
        ok_button = Button(text="OK", size_hint_y=None, height=50)
        popup_layout.add_widget(solution_label)
        popup_layout.add_widget(ok_button)
        popup = Popup(title="Falsche Antwort", content=popup_layout, size_hint=(0.7, 0.4))
        ok_button.bind(on_press=lambda x: (popup.dismiss(), self.next_konto()))
        popup.open()

    def check_answer(self, selected_typ):
        correct_typ = kontenplan[self.current_konto]["typ"]
        if selected_typ == correct_typ:
            self.correct_answers += 1
        else:
            self.wrong_answers += 1
            self.show_solution_popup(correct_typ)

        self.result_label.text = f"Richtig: {self.correct_answers} | Falsch: {self.wrong_answers}"
        if selected_typ == correct_typ:
            self.next_konto()

# Hauptprogramm
if __name__ == "__main__":
    LernprogrammApp().run()
