import json

ALLOWED_EXTENSIONS = {'json'}

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def read_file(filename):
    trans = []
    with open(filename) as fp:
        for line in fp:
            trans.append(json.loads(line))

    return trans
