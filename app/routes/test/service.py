
from . import test_bp
import json

# Path: app/routes/test/service.py


@test_bp.route('/extract')
def service():
    with open('/app/static/response.json', 'r') as json_file:
        data = json.load(json_file)
    return data
