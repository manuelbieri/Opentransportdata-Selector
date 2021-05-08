import DataSelector.loader


class Selector:
    def __init__(self, file: DataSelector.loader.File) -> None:
        assert file is not None
        self.file = file
        self.filter_args = []

    def setFile(self, file: DataSelector.loader.File) -> None:
        assert file is not None
        self.file = file

    def filter(self, filter_args: list) -> list:
        assert len(filter_args) > 0
        assert self.file is not None
        self.filter_args = filter_args
        filtered_list = []

        for item in self.file.getDictList():
            if self.filterItem(item):
                filtered_list.append(item)

        assert len(filtered_list) <= len(self.file.getDictList())
        return filtered_list

    def filterItem(self, item) -> bool:
        assert len(item) != 0
        add = True
        for condition in self.filter_args:
            if item[condition['name']] != condition['value']:
                add = False
                break
        return add
