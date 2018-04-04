import importlib

def load_palette(reference):
    pkg = "swatchbook.%s" % reference
    mod = importlib.import_module(pkg)
    return mod.palette()
    
def closest(reference, hex):
    palette = load_palette(reference)
    return palette.closest(hex)

def closest_cmc(reference, hex):
    palette = load_palette(reference)
    return palette.closest_cmc(hex)