from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.list import OneLineAvatarListItem
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

KV = '''
#:import IconLeftWidget kivymd.uix.list.IconLeftWidget
#:import images_path kivymd.images_path
#:import hex kivy.utils.get_color_from_hex

<ElementosPanelLista>
    theme_text_color: 'Custom'
    divider: None

    IconLeftWidget:
        icon: root.icono
        #on_press: Manejador_De_Pantallas.current = 'Inicio'


<ContenidoPanel>

    BoxLayout:
        orientation: 'vertical'

        # PERFIL PANEL
        MDFloatLayout:
            size_hint_y: None
            height: "200dp"
            #adaptive_height: True
            md_bg_color: app.theme_cls.primary_color
            #md_bg_color: hex("#17212d")

            BoxLayout:
                id: top_box
                size_hint_y: None
                height: "200dp"
                #padding: "10dp"
                x: root.parent.x
                pos_hint: {"top": 1}

                FitImage:
                    source: f"{images_path}kivymd_alpha.png"

            MDIconButton:
                icon: "close"
                x: root.parent.x + dp(10)
                pos_hint: {"top": 1}
                on_release: root.parent.set_state()

            MDLabel:
                markup: True
                text: "[b]KivyMD[/b]\\nVersion: 0.102.1"
                #pos_hint: {'center_y': .5}
                x: root.parent.x + dp(10)
                y: root.height - top_box.height + dp(10)
                size_hint_y: None
                height: self.texture_size[1]

        # ELEMENTOS
        ScrollView:
            id: sc
            pos_hint: {"top": 1}

            MDGridLayout:
                id: box_item
                cols: 1
                size_hint_y: None
                height: self.minimum_height
                #adaptive_height: True
                #md_bg_color: hex("#1b2936")
                md_bg_color: app.theme_cls.primary_color


MDScreen:
    radius: [25, 0, 0, 0]
    #md_bg_color: app.theme_cls.theme_style
    #md_bg_color: app.theme_cls.primary_color
    #md_bg_color: hex("#1b2936")

    NavigationLayout:

        ScreenManager:
            id: Manejador_De_Pantallas

            # PANTALLA
            Screen:
                id: Inicio
                name: 'Inicio'

                BoxLayout:
                    orientation: 'vertical'

                    # TITULO
                    MDIconButton:
                        icon: "menu"
                        #x: root.parent.x + dp(10)
                        pos_hint: {"top": 1}
                        on_release: nav_drawer.set_state()

                    # CONTENIDO
                    MDLabel:
                        id: l2
                        text: "Inicio"
                        halign: 'center'

                    MDFlatButton:
                        text: 'BOTON PARA IR A AJUSTES'
                        pos_hint: {'center_x': .5, 'center_y': .75}
                        on_release: Manejador_De_Pantallas.current = 'Ajustes'

                    Widget:

            Screen:
                id: Ajustes
                name: 'Ajustes'

                MDBoxLayout:
                    orientation: 'vertical'
                    #adaptive_height: True
                    md_bg_color: hex("#1b2936")

                    MDIconButton:
                        icon: "menu"
                        #x: root.parent.x + dp(10)
                        pos_hint: {"top": 1}
                        on_release: nav_drawer.set_state()

                    MDLabel:
                        id: l2
                        text: "Ajustes"
                        halign: 'center'

                    MDRaisedButton:
                        text: "BOTON PARA IR A INICIO"
                        pos_hint: {'center_x': .5, 'center_y': .5}
                        #pos_hint: {'.5': '.5'}
                        on_press: Manejador_De_Pantallas.current = "Inicio"
                    Widget:

        # PANEL
        MDNavigationDrawer:
            id: nav_drawer

            ContenidoPanel:
                id: contenido_panel

'''


class ContenidoPanel(BoxLayout):
    pass


class ElementosPanelLista(OneLineAvatarListItem):
    icono = StringProperty()


class TestApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = "MDNavegacion"

    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        for items in {
            "home-circle-outline": "Inicio",
            "update": "Buscar Actualizacion",
            "settings-outline": "Ajustes",
            "exit-to-app": "Salir",
        }.items():
            self.root.ids.contenido_panel.ids.box_item.add_widget(
                ElementosPanelLista(
                    text=items[1],
                    icono=items[0],
                )
            )


if __name__ == '__main__':
    Window.size = (361, 641)
    TestApp().run()
