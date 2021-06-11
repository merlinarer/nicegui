from .custom_view import CustomView
from .element import Element

class ThreeView(CustomView):

    def __init__(self, on_click):

        super().__init__('three', __file__, [
            'https://cdn.jsdelivr.net/npm/three@0.129.0/build/three.min.js',
            'https://cdn.jsdelivr.net/npm/three@0.129.0/examples/js/controls/OrbitControls.js',
        ], camera_z=4)

        self.on_click = on_click
        self.allowed_events = ['onClick']
        self.initialize(temp=False, onClick=self.handle_click)

    def handle_click(self, msg):

        if self.on_click is not None:
            self.on_click(msg)

class Three(Element):

    def __init__(self, *, on_click=None):

        super().__init__(ThreeView(on_click))

    def move_camera(self, z):

        self.view.options.camera_z = z