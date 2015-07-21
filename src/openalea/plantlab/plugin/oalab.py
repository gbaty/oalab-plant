
from openalea.core.plugin import PluginDef
from openalea.oalab.plugin.oalab.control import ControlWidgetSelectorPlugin


@PluginDef
class PluginColorListWidget(ControlWidgetSelectorPlugin):
    controls = ['IColorList']
    name = 'ColorListWidget'
    edit_shape = ['large']
    paint = True

    def __call__(self):
        from openalea.plantlab.qtcontrol import ColorListWidget
        return ColorListWidget


@PluginDef
class PluginMaterialListWidget(ControlWidgetSelectorPlugin):
    controls = ['IMaterialList']
    name = 'MaterialListWidget'
    edit_shape = ['large']
    paint = True

    def __call__(self):
        from openalea.plantlab.qtcontrol import MaterialListWidget
        return MaterialListWidget


@PluginDef
class PluginCurve2DWidget(ControlWidgetSelectorPlugin):
    controls = ['ICurve2D']
    name = 'Curve2DWidget'
    edit_shape = ['large']
    paint = True

    def __call__(self):
        from openalea.plantlab.qtcontrol import Curve2DWidget
        return Curve2DWidget


@PluginDef
class PluginQuantisedFunctionWidget(ControlWidgetSelectorPlugin):
    controls = ['IQuantisedFunction']
    name = 'QuantisedFunctionWidget'
    edit_shape = ['large']
    paint = True

    def __call__(self):
        from openalea.plantlab.qtcontrol import QuantisedFunctionWidget
        return QuantisedFunctionWidget


@PluginDef
class PluginPatchWidget(ControlWidgetSelectorPlugin):
    controls = ['IPatch']
    name = 'NurbsPatchWidget'
    edit_shape = ['large']
    paint = True

    def __call__(self):
        from openalea.plantlab.qtcontrol import NurbsPatchWidget
        return NurbsPatchWidget


@PluginDef
class LPyModelGUI(object):
    name = 'LSystem'
    mimetype_data = "text/vnd-lpy"
    mimetype_model = "text/vnd-lpy"
    implements = ['IParadigmApplet']

    def __call__(self):
        from openalea.plantlab.paradigm import LPyModelController
        return LPyModelController
