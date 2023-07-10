__title__ = "Selection"
__author__ = "Hung Le"
__doc__ = """
    This shows all of the elements that are currently selected in Revit UI
"""

# VARIABLES
uidoc = __revit__.ActiveUIDocument

# CUSTOM IMPORT
from Snippets._selection import get_selected_elements

if __name__ == "__main__":
    print(get_selected_elements(uidoc))
