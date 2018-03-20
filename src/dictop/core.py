from functools import partial


def select(target, path, default=None, slient=True):
    """Select item with path from target. 

    If not find item and slient marked as True, return default value.
    If not find item and slient marked as False, raise KeyError.
    """
    def _(value, slient):
        if slient:
            return value
        else:
            raise KeyError("")
    default = partial(_, default, slient)
    names = path.split(".")
    node = target
    for name in names:
        if isinstance(node, dict):
            try:
                node = node[name]
            except:
                return default()
        elif isinstance(node, list) and name.isdigit():
            try:
                node = node[int(name)]
            except:
                return default()
        elif hasattr(node, name):
            node = getattr(node, name)
        else:
            return default()
    return node

def update(data, path, value):
    pass
