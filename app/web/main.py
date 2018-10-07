from . import web



@web.route('/')
def index():
    return 'This is a index page'


@web.route('/personal')
def personal_center():
    pass
