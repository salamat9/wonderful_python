from module_two import bye


def hello(name: str) -> str:
    """
    Say hello plus name!
    :param name: str
    :return: hello, 'name'
    """
    return f'hello {name}!'


name1 = 'Sam'
hello(name1)
bye(name1)