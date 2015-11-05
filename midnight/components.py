class MetaSeo(object):

    metatitle = ''

    keywords = ''

    description = ''

    _model = None

    def __init__(self, model=None):

        self._model = model

        if self._model is not None:

            self.metatitle = self._model.metatitle if self._model.metatitle else self._model.title

            self.keywords = self._model.keywords

            self.description = self._model.description
