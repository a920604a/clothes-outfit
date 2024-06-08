from abc import ABC, abstractmethod


class TransformManager:
    def __init__(self):
        pass

    @abstractmethod
    def transform(self):
        pass
