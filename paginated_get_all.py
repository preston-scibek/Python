from api_calls import api_request

def paginated_get_all(endpoint, limit=25, parameters=None, base_domain=None, token=None, sort_func=None):
    """Get all objects from an endpoint, but do it nicely, using pagination
    
    :param endpoint: Endpoint to retrieve from.
    :param limit: Max objects per call.
    :param parameters: Parameter for the call.
    :param base_domain: Domain
    :param token: Auth Token
    :sort_func: Function to sort list by if wanted
    :return: List of objects retrieved from endpoint.
    """
    i = 0
    items = []

    parameters = parameters if parameters else {}

    parameters['limit'] = limit
    parameters['offset'] = limit * i

    res = api_request(endpoint, 'GET', parameters=parameters, base_domain=base_domain, token=token)

    items += res['data']

    while res['meta']["next"] is not None:
        i += 1
        parameters['offset'] = limit * i
        res = api_request(endpoint, 'GET', parameters=parameters, base_domain=base_domain, token=token)
        items += res['data']

    if sort_func:
        items.sort(cmp=sort_func)

    return items
