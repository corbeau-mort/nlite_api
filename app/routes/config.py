from app.routes import bp_api


@bp_api.route('/config', methods=['GET'])
def get_config():
    return bp_api.send_static_file("Config/config.json")

