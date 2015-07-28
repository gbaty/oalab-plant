
from openalea.core.plugin import PluginDef


@PluginDef
class Viewer3D(object):
    name = 'Viewer3D'
    label = 'Viewer'
    icon = 'icon_viewer.png'

    def __call__(self):
        # Load and instantiate graphical component that actually provide feature
        from openalea.plantlab.view3d import Viewer
        return Viewer
