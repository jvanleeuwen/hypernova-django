def prepare_request(req, _):
    for job in req.values():
        print "{color}{bold}Preparing job:{bold}{endcolor} {job}".format(
            bold='\033[1m',
            color='\033[92m',
            job=job,
            endcolor='\033[0m'
        )
    return req


def will_send_request(req, _):
    for job in req.values():
        print "{color}{bold}Requesting job:{bold}{endcolor} {job}".format(
            bold='\033[1m',
            color='\033[92m',
            job=job,
            endcolor='\033[0m'
        )
    return req


def on_error(err):
    print "{color}{bold}Error:{bold}{endcolor} {error}".format(
        bold='\033[1m',
        color='\033[91m',
        error=err,
        endcolor='\033[0m'
    )

dev_mode_plugin = {
    'prepareRequest': prepare_request,
    'willSendRequest': will_send_request,
    'onError': on_error,
}
