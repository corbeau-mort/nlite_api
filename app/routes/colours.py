from app.routes import bp_api
from flask import request, abort
import json
import re

maps_folder = "local_files/Maps/"

@bp_api.route('/colours/current', methods=['GET'])
def get_current():
    return bp_api.send_static_file("Maps/currentMap.json")

@bp_api.route('/colours/maps/<map_name>', methods=['POST', 'PUT'])
def save_new_map(map_name):
    map_dict = json.loads(request.form["map"])
    is_only_alphanum = (bool(re.match("^[A-Za-z0-9_-]*$", map_name)))
    if not is_only_alphanum:
        abort(400)
    if not isinstance(map_dict, list):
        abort(400)
    for element in map_dict:
        if not isinstance(element, list):
            abort(400)
        for val in element:
            if not isinstance(val, int):
                abort(400)
    with open(maps_folder+map_name+".json", "w+") as map_file:
        map_file.write(request.form["map"])
    return "map saved"


@bp_api.route('/colours/maps/<map_name>', methods=['DELETE'])
def delete_new_map(map_name):
    is_only_alphanum = (bool(re.match("^[A-Za-z0-9_-]*$", map_name)))
    if not is_only_alphanum:
        abort(400)
    return "map deleted"


