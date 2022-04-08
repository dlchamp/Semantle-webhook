from json import load, dump


def load_json():
    with open('./data/history.json') as f:
        return load(f)


def update_json(data):
    with open('./data/history.json','w') as f:
        dump(data, f, indent=4)

