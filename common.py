import pathlib


class BaseConfig:
    debug = True
    app_name = 'Social Network'
    SECRET_KEY = 'y@lmkt6*r5e$1si-9cnq5ie)(7$x6akmu*gr9kbqsoda^1y0t@'
    database_name = 'my_database'

    PROJECT_ROOT = pathlib.Path(__file__).parent.parent
    STATIC_DIR = str(PROJECT_ROOT / 'static')
