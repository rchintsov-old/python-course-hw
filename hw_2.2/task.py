friends = [
{'name': 'Сэм', 'gender': 'Мужской', 'sport': 'Баскетбол', 'email': 'email@email.com'},
{'name': 'Эмили', 'gender': 'Женский', 'sport': 'Волейбол', 'email': 'email1@email1.com'}
]

selected_params = {'select': [],
                   'field_filter': []}


def select_wrapper(func):
    def inner(field_name: list):
        global selected_params
        selected_params['select'] += field_name
        return func(field_name)
    return inner


def field_filter_wrapper(func):
    def inner(field_name: str, collection: list):
        global selected_params
        selected_params['field_filter'].append({field_name: collection})
        return func(field_name, collection)
    return inner


@select_wrapper
def select(field_name: list):
    pass

@field_filter_wrapper
def field_filter(field_name: str, collection: list):
    pass


def query(select, field_filter, collection):
    pass


