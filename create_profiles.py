import pathlib
import argparse
import json
from uuid import uuid4
import shutil

PROJECT_DIR = pathlib.Path(__file__).parent
OUTPUT_DIR = PROJECT_DIR / "profiles"
ASSETS_DIR = PROJECT_DIR / "assets"


class CreateProfiles:
    def __init__(self, args: argparse.Namespace) -> None:
        self.__format = self.get_json_from_file(ASSETS_DIR / "strongswan_config.json")
        self.__servers = self.get_json_from_file(ASSETS_DIR / "server_list.json")
        if args.username:
            self.__format["local"] = {
                "eap_id" : args.username
            }
    
    @classmethod
    def get_json_from_file(cls, file_path: pathlib.Path):
        result = ""
        with open(file_path, "r") as fp:
            result = json.load(fp)
        
        return result
    
    def generate(self):
        if OUTPUT_DIR.exists():
            shutil.rmtree(OUTPUT_DIR)

        OUTPUT_DIR.mkdir()
        
        for index in self.__servers.keys():
            with open(OUTPUT_DIR / f"{index}.sswan", "w+") as fp:
                profile = self.__format.copy()
                profile['uuid'] = str(uuid4())
                profile['name'] = index
                profile['remote']['addr'] = self.__servers.get(index)
                fp.write(json.dumps(profile))
            print('created ', index, ' profile')

def main():
    parser = argparse.ArgumentParser(description="strongswan profile creator for windscribe vpn", allow_abbrev=False)
    parser.add_argument('-u', '--username', default=None, help="windscribe ikev2 username")
    profiles = CreateProfiles(parser.parse_args())
    profiles.generate()


if __name__ == "__main__":
    main()
