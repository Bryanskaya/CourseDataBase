import logging

logging.basicConfig(filename="details.log", level=logging.INFO)

def do_log(f, request, **kwargs):
    login = None
    if 'user' in request.session.keys():
        login = request.session['user']['login']

    if 'HTTP_X_REAL_IP' in request.META.keys():
        logging.info("\n>>> GENERAL INFO server protocolUser: %s\tHTTP_HOST: %s\tUSER: %s\tHTTP: %s\topened %s",
                     request.META['SERVER_PROTOCOL'], request.META['HTTP_HOST'],
                     login,
                     request.META['HTTP_X_REAL_IP'], request.META['PATH_INFO'])
    else:
        logging.info("\n>>> GENERAL INFO server protocolUser: %s\tHTTP_HOST: %s\tUSER: %s\topened %s",
                     request.META['SERVER_PROTOCOL'], request.META['HTTP_HOST'],
                     login,
                     request.META['PATH_INFO'])

    # try:
    #     return f(request, **kwargs)
    # except BaseException as e:
    #     logging.exception(">>>ERROR: in %s (situated in) - %s", f.__name__, e.__class__, str(e))

    return f(request, **kwargs)