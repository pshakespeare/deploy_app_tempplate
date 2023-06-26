import yaml
import json

def yaml_to_json(source_file: str,destination_file: str) -> None:
    with open(source_file, 'r') as yaml_in, open(destination_file,'w') as json_out:
        yaml_object = yaml.safe_load(yaml_in)
        json.dump(yaml_object,json_out)


if __name__ == '__main__':
    yaml_to_json('fire-bird.yaml','fire-bird.json')