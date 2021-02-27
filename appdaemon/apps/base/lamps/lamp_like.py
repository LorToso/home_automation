from abc import abstractmethod


class LampLike:

    @abstractmethod
    def turn_on(self, **kwargs) -> None:
        pass

    @abstractmethod
    def turn_off(self, **kwargs) -> None:
        pass

    @abstractmethod
    def set_brightness(self, brightness: int) -> None:
        pass

    @abstractmethod
    def toggle(self, **kwargs) -> None:
        pass

    @abstractmethod
    def is_on(self) -> bool:
        pass

    @abstractmethod
    def is_off(self) -> bool:
        pass
