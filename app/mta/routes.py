from app.mta import mta


@mta.route('/mta')
def index():
    return 'Do you like trains?'
