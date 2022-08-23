import os


def get_url():
    base_url = "/"
    try:
        base_url_env = os.environ.get("BASE_URL")
        if isinstance(base_url_env, str):
            base_url = base_url_env
    except:
        pass
    return base_url

def get_debug():
    debug = False
    try:
        debug_env = os.environ.get("DEBUG")
        if isinstance(debug_env, str):
            debug = bool(debug_env)
    except:
        pass
    return debug

def get_root():
    root = ""
    try:
        root_env = os.environ.get("ROOT_PATH")
        if isinstance(root_env, str):
            root = root_env
    except:
        pass
    return root
