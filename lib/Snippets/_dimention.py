# IMPORT

from Autodesk.Revit.DB import *

# VARIABLES

uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document

# FUNCTIONS

def anno_dim(uidoc):
    """This function creates a dimention for the selected elements
    :param uidoc: uidoc where elements are selected
    :return: a dimension
    """
