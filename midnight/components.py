class MetaSeo(object):

    __metatitle = ''

    __keywords = ''

    __description = ''

    __model = None

    def __init__(self, model = None):

        self.__model = model

        if self.__model is not None:

            self.__metatitle = self.__model.metatitle if self.__model.metatitle else self.__model.title

            self.__keywords = self.__model.keywords

            self.__description = self.__model.description

    def get_metatitle(self):
        return self.__metatitle

    def set_metatitle(self, value):
        self.__metatitle = value

    def get_keywords(self):
        return self.__keywords

    def set_keywords(self, value):
        self.__keywords = value

    def get_description(self):
        return self.__description

    def set_description(self, value):
        self.__description = value


    metatitle = property(get_metatitle, set_metatitle)

    keywords = property(get_keywords, set_keywords)

    description = property(get_description, set_description)
