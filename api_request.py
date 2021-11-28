def api_request(api_url, method, payload=None, base_domain=None, parameters=None, token=None,
                headers_t=None, paginate=True):
    """Make an API Request using the given method, domain, payload, and url endpoint.

    :param api_url: The api endpoint to call.
    :param method: The HTTP method to use.
    :param payload: The payload if any to use in a post or put method.
    :param base_domain: The base domain of the api.
    :param parameters: The url query parameters.
    :param token: The token to use to auth.
    :param paginate: Do we want to get all data via pagination or just whatever is returned on the first call.
    :return: The response of the request.
    """
    
    if base_domain in api_url:
        api_url = api_url.split(base_domain)[1]
    
    if base_domain.startswith("127.0.0.1"):
        conn = httplib.HTTPConnection(base_domain)
    else:
        conn = httplib.HTTPSConnection(base_domain)


    headers = {
        "accept": "*/*",
        "cache-control": "no-cache",
        "Authorization": "token " + token,
        "content-type": "application/json",
        "User-Agent": "preston-scibek"
    }

    if headers_t:
        for pair in headers_t:
            headers[pair[0]] = pair[1]

    if method == 'PUT':
        conn.request(method, api_url, json.dumps(payload), headers=headers)
    elif method == 'POST':
        conn.request(method, api_url, json.dumps(payload), headers=headers)
    elif method == 'GET':
        api_url = api_url + "?%s" % urllib.urlencode(parameters) if parameters is not None else api_url
        conn.request(method, api_url, headers=headers)
    elif method == 'DELETE':
        conn.request(method, api_url, headers=headers)
    else:
        conn.request(method, api_url, json.dumps(payload), headers=headers)

    res = conn.getresponse()
    data = res.read()
    try:
        jloaded = json.loads(data.decode('utf-8'))
        if paginate and isinstance(jloaded, dict):
            if jloaded.get('meta', {}).get('next', {}):
                items = jloaded.get('data', [])
                res = api_request(jloaded.get('meta', {}).get('next', "").split("base_domain")[-1], 'GET', parameters=parameters, base_domain=base_domain, token=token)
                if isinstance(res, dict):
                    items += res['data']
                else:
                    items += res
                return items
            elif jloaded.get("hasMore", False):
                items = jloaded.get('results', [])
                parameters = parameters if parameters else {}
                parameters["offset"] =  jloaded.get("offset")
                res = api_request(api_url.split("?")[0], 'GET', parameters=parameters, base_domain=base_domain, token=token)
            
                items += res
                return items
        else:
            if res.getheader("link"):
                x = res.getheader("link")
                x = x.replace("<", "").replace(">", "")
                x = x.split(",")
                x = [y.split(";") for y in x]
                x = [{y[1].split("\"")[1]: y[0].replace(" ", "")} for y in x]
                for v in x:
                    if v.get("next"):
                        jloaded = jloaded + api_request(v.get("next").split(base_domain)[1], "GET")
        return jloaded
    except ValueError:
        return data
