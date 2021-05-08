import csv
import json
import os


class Writer:
    def __init__(self, output_dir):
        assert output_dir is not None
        assert os.path.isdir(output_dir)
        self.output_dir = output_dir
        self.output_path = ''

    def write_csv(self, lines: list) -> str:
        assert len(lines) > 0
        self.checkAndCreatePath('csv')
        with open(self.output_path, 'w', newline='', encoding='utf-8') as f:
            header = lines[0].keys()
            csv_file = csv.DictWriter(f, header, delimiter=";")
            csv_file.writeheader()
            csv_file.writerows(lines)

        return self.output_path

    def write_json(self, lines: list) -> str:
        assert len(lines) > 0
        json_content = json.dumps(lines)
        self.checkAndCreatePath('json')
        with open(self.output_path, 'w') as f:
            f.write(json_content)

        return self.output_path

    def checkAndCreatePath(self, ending: str) -> None:
        assert len(ending) >= 3 and len(ending) >= 2
        counter = 0
        while True:
            self.output_path = self.output_dir + '/output' + str(counter) + "." + ending
            if not (os.path.isfile(self.output_path)):
                break
            counter += 1
