from abc import abstractmethod


class LoaderManager:
    def __init__(self):
        pass

    @abstractmethod
    def load(self):
        pass
