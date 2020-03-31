import logging
import requests

logger = logging.getLogger(__name__)


DEFAULT_TIMEOUT = 10  # 10 seconds


def try_http(
    verb,
    url,
    json=None,
    headers={},
    success=(200, 201),
    squelch=(),
    response="json",
    timeout=DEFAULT_TIMEOUT,
):
    func = getattr(requests, verb.lower(), None)
    if func is None:
        raise NotImplementedError("%s is not a supported http action" % verb)
    try:
        r = func(url, json=json, headers=headers, timeout=timeout)
    except Exception as ex:
        logger.error("Error %sing %s: %s", verb.upper(), url, ex)
        return None
    if r.status_code not in success:
        if r.status_code in squelch:
            logger.debug(
                "Got status code %d %sing %s", r.status_code, verb.upper(), url
            )
        else:
            logger.error(
                "Got status code %d %sing %s", r.status_code, verb.upper(), url
            )
        if response == "status_code":
            return r.status_code
        else:
            return None

    # possible values here: json, text, status_code
    if response not in dir(r):
        raise NotImplementedError(
            "%s is neither a method nor an attribute of a requests response"
            % response
        )
    try:
        if response == "json":
            return r.json()
        return getattr(r, response)
    except Exception as ex:
        logger.error("Failure getting %s from %s: %s", response, url, ex)
        return None


def try_get(url, **kwargs):
    if "success" not in kwargs:
        kwargs["success"] = (200,)
    return try_http("get", url, **kwargs)


def try_put(url, **kwargs):
    return try_http("put", url, **kwargs)


def try_delete(url, **kwargs):
    return try_http("delete", url, **kwargs)


def try_patch(url, json, **kwargs):
    return try_http("patch", url, json=json, **kwargs)


def try_post(url, json, **kwargs):
    return try_http("post", url, json=json, **kwargs)
