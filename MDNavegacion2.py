from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.list import OneLineAvatarListItem
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

KV = '''
#:import IconLeftWidget kivymd.uix.list.IconLeftWidget
#:import images_path kivymd.images_path

<ElementosPanelLista>
    theme_text_color: 'Custom'
    divider: None

    IconLeftWidget:
        icon: root.icono


<ContenidoPanel>

    BoxLayout:
        orientation: 'vertical'

        # PERFIL PANEL
        FloatLayout:
            size_hint_y: None
            height: "200dp"

            canvas:
                Color:
                    rgba: app.theme_cls.primary_color
                Rectangle:
                    pos: self.pos
                    size: self.size

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
                text: "[b]KivyMD[/b]\\nVersion: 0.104.0"
                #pos_hint: {'center_y': .5}
                x: root.parent.x + dp(10)
                y: root.height - top_box.height + dp(10)
                size_hint_y: None
                height: self.texture_size[1]

        # ELEMENTOS DEL PANEL
        ScrollView:
            pos_hint: {"top": 1}

            GridLayout:
                id: box_item
                cols: 1
                size_hint_y: None
                height: self.minimum_height


Screen:

    NavigationLayout:

        ScreenManager:
            id: screen_manager

            Screen:
                name: "inicio"

                BoxLayout:
                    orientation: 'vertical'

                    # TITULO
                    MDToolbar:
                        title: app.title
                        md_bg_color: app.theme_cls.primary_color
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.set_state()]]
                        right_action_items:
                            [['magnify', lambda x: app.Cambiar_Pantalla("Pantalla_De_Busqueda")],
                            ['dots-vertical', lambda x: print('lol') if app.func == 'Si' else print('No')]]

                    # CONTENIDO
                    MDFlatButton:
                        text: 'ESTAS EN INICIO BOTON PARA IR A AJUSTES'
                        pos_hint: {'center_x': .5, 'center_y': .75}
                        on_press: screen_manager.current = "ajustes"
                        #on_release: app.Cambiar_Pantalla("Pantalla_De_Ajustes")
                    Widget:

            Screen:
                name: "ajustes"

                BoxLayout:
                    orientation: 'vertical'

                    MDToolbar:
                        title: app.title
                        md_bg_color: app.theme_cls.primary_color
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.set_state()]]
                        right_action_items:
                            [['magnify', lambda x: app.Cambiar_Pantalla("Pantalla_De_Busqueda")],
                            ['dots-vertical', lambda x: print('lol') if app.func == 'Si' else print('No')]]

                    MDLabel:
                        id: l2
                        text: "Ajustes"
                        halign: 'center'
                    MDRaisedButton:
                        text: "BOTON PARA IR A INICIO"
                        pos_hint: {'center_x': .5, 'center_y': .5}
                        #pos_hint: {'.5': '.5'}
                        on_press: screen_manager.current = "inicio"
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


class TestNavigationDrawer(MDApp):
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
    TestNavigationDrawer().run()
