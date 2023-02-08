import csv
from pathlib import Path
from typing import Union

from .models import Exobiology, Riches


class Reader:
    rows = []

    def __init__(self, file: Union[Path, str]):
        self._current_index = 0
        if type(file) is str:
            self.path = Path(file)
        else:
            self.path = file
        if self.path.name.startswith('exobiology'):
            self.type = 'exobiology'
        elif self.path.name.startswith('riches'):
            self.type = 'riches'
        self.read()
        self._row_count = len(self.rows)

    def __iter__(self):
        return self

    def __next__(self):
        if self._current_index < self._row_count:
            member = self.rows[self._current_index]
            self._current_index += 1
            return member

        raise StopIteration

    def read(self) -> None:
        with open(self.path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    if self.type == 'exobiology':
                        read_row = Exobiology(
                            id=line_count,
                            completed=False,
                            system_name=row[0],
                            body_name=row[1],
                            body_subtype=row[2],
                            distance_to_arrival=row[3],
                            landmark_subtype=row[4],
                            value=row[5],
                            count=row[6],
                            jumps=row[7]
                        )
                    elif self.type == 'riches':
                        read_row = Riches(
                            id=line_count,
                            completed=False,
                            system_name=row[0],
                            body_name=row[1],
                            body_subtype=row[2],
                            is_terraformable=row[3],
                            distance_to_arrival=row[4],
                            estimated_scan_value=row[5],
                            estimated_mapping_value=row[6],
                            jumps=row[7]
                        )
                    self.rows.append(read_row)
                    line_count += 1
            print(f'Processed {line_count} lines.')

