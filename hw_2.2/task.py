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


def query(collection: list, select: function, field_filter: function, *args) -> list:
    to_filter = {}

    for param in selected_params['field_filter']:
        if not to_filter[param]:
            to_filter[param] = selected_params['field_filter'][param]
        else:
            to_filter[param] += selected_params['field_filter'][param]

    to_expose = []
    for fr in friends:
        fields = [i for i in fr if i in to_filter.keys()]
        add = True
        for field in fields:
            if fr[field] not in to_filter[field]:
                add = False
        if add == True:
            to_expose.append(fr)

    print([{i: j for i, j in fri.items() if i in selected_params['select']} for fri in to_expose])

    return

