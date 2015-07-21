
from openalea.core.plugin import PluginDef
from openalea.plantlab.interface import *


@PluginDef
class PlantGLOAInterfacePlugin(object):

    def __call__(self):
        return [IColorList, IMaterialList, ICurve2D, IQuantisedFunction, IPatch]
