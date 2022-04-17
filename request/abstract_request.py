from abc import ABC, abstractmethod


class AbstractRequest(ABC):
    def get_result(self, area_name: int):
        df = self.__get_data_frame(area_name)
        layout = self.__get_layout()
        fig = self.__get_figure(layout, df)
        return self.__get_request(fig)

    @abstractmethod
    def __get_data_frame(self, area_name):
        pass

    @abstractmethod
    def __get_layout(self):
        pass

    @abstractmethod
    def __get_figure(self, layout, df):
        pass

    @abstractmethod
    def __get_request(self, fig):
        pass
