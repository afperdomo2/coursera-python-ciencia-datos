from flask import Flask, make_response, jsonify, request

app = Flask(__name__)

data = [
    {
        "id": "3b58aade-8415-49dd-88db-8d7bce14932a",
        "first_name": "Tanya",
        "last_name": "Slad",
        "graduation_year": 1996,
        "address": "043 Heath Hill",
        "city": "Dayton",
        "zip": "45426",
        "country": "United States",
        "avatar": "http://dummyimage.com/139x100.png/cc0000/ffffff",
    },
    {
        "id": "d64efd92-ca8e-40da-b234-47e6403eb167",
        "first_name": "Ferdy",
        "last_name": "Garrow",
        "graduation_year": 1970,
        "address": "10 Wayridge Terrace",
        "city": "North Little Rock",
        "zip": "72199",
        "country": "United States",
        "avatar": "http://dummyimage.com/148x100.png/dddddd/000000",
    },
]


@app.route("/")
def index():
    return jsonify({"message": "Hello world"})


@app.route("/no_content")
def no_content():
    return make_response(jsonify({"message": "No content"}), 404)


@app.route("/data")
def get_data():
    try:
        if data and len(data) > 0:
            return {"message": f"Data of length {len(data)} found"}
        else:
            return {"message": "Data is empty"}, 500
    except NameError:
        return {"message": "Data not found"}, 404


@app.route("/name_search")
def get_first_name():
    """Find a person in the database.

    Returns:
        - JSON: person if found, with status code 200
        - Status code 404: if not found
        - Status code 422: if argument 'q' is missing
    """
    query = request.args.get("q")
    if not query:
        return {"message": "Missing 'q' argument"}, 422
    for person in data:
        if query.lower() in person["first_name"].lower():
            return person, 200
    return {"message": "Person not found"}, 404


@app.get("/count")
def count():
    try:
        data_count = len(data)
        return {"data count": data_count}, 200
    except NameError:
        return {"message": "data not defined"}, 500


@app.route("/person/<string:var_id>")
def find_by_uuid(var_id):
    for person in data:
        if person["id"] == var_id:
            return person, 200
    return {"message": "Person not found"}, 404


@app.route("/person/<string:var_id>", methods=["DELETE"])
def delete_person(var_id):
    if request.method == "DELETE":
        for person in data:
            if person["id"] == str(var_id):
                data.remove(person)
                return {"message": "ID of person deleted"}, 200
        return {"message": "Person not found"}, 404


@app.route("/person", methods=["POST"])
def insert_person():
    if request.method == "POST":
        new_person = request.json
        if not new_person:
            return {"message": "Invalid input parameter"}, 422

        data.append(new_person)
        return {"message": f"{new_person['id']} added successfully"}, 201


@app.errorhandler(404)
def error_handler(error):
    return {"message": "API Not found"}, 404
