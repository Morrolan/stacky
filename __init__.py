"""

"""

import webbrowser


def stacky_error(error: Exception):
    """

    :param error: string containing the exception message
    """
    error_message = str(error)[10:]

    search_url = f"http://stackoverflow.com/search?q=[python] {error_message}"
    webbrowser.open(search_url)
