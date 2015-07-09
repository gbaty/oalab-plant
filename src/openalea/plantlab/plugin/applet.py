
from openalea.core.plugin import PluginMeta


class Viewer3D(PluginMeta):
    name = 'Viewer3D'
    alias = 'Viewer'
    icon = 'icon_viewer.png'

    def __call__(self):
        # Load and instantiate graphical component that actually provide feature
        from openalea.plantlab.view3d import Viewer
        return Viewer
