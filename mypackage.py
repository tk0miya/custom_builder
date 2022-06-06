from sphinx.builders import Builder


class CustomBuilder(Builder):
    name = 'custom'

    def __init__(self, app):
        super().__init__(app)


def setup(app):
    app.add_builder(CustomBuilder)
