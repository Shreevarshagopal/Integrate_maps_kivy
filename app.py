from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.garden.mapview import MapView, MapMarker


class MapApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        mapview = MapView(zoom=11, lat=37.7749, lon=-122.4194)  # San Francisco coordinates

        marker = MapMarker(lat=37.7749, lon=-122.4194)
        mapview.add_marker(marker)

        layout.add_widget(mapview)

        return layout


if __name__ == '__main__':
    MapApp().run()
