
import collections

#Some utility functions for working with json data

def flattenDict(d):
    """Reduces the depth of a dictionary to 1, parent keys are ignored.

    >>> d = {'a': 1, 'c': {'e': 5, 'd': 4}, 'b': 2, 'f': {'g': {'h': 8}}}
    >>> flattenDict(d)
    {'a': 1, 'h': 8, 'b': 2, 'e': 5, 'd': 4}
    """
    result = {}
    for k, v in d.iteritems():
        if isinstance(v, dict):
            result.update(flattenDict(v))
        else:
            result.update({k:v})
    return result

def valueForNestedKey(d, key="", default=None):
    """Returns the value of the first occurrence of key on a pre-order
    traversal.

    >>> d = {'a': 1, 'c': {'e': 5, 'd': 4}, 'b': 2, 'f': {'g': {'h': 8}}}
    >>> valueForNestedKey(d, "h")
    8
    >>> valueForNestedKey(d, "q", "foo")
    'foo'
    """
    for k,v in d.iteritems():
        if k == key:
            return v
        elif isinstance(v, dict):
            result = valueForNestedKey(v, key, default)
            if result is not default:
                return result
    return default

def valueForKeyPath(d, key, separator=".", default=None):
    """Returns the value at the end of the string of keys split on the provided
    separator ("." by default.)

    >>> d = {'a': 1, 'c': {'e': 5, 'd': 4}, 'b': 2, 'f': {'g': {'h': 8}}}
    >>> valueForKeyPath(d, "a")
    1
    >>> valueForKeyPath(d, "f.g.h")
    8
    >>> valueForKeyPath(d, "q", default="foo")
    'foo'
    """
    return valueForKeyList(d, key.split(separator), default)

def valueForKeyList(d, keys, default=None):
    """Returns the value at the end of the list of keys.

    >>> d = {'a': 1, 'c': {'e': 5, 'd': 4}, 'b': 2, 'f': {'g': {'h': 8}}}
    >>> valueForKeyList(d, ('q',), "foo")
    'foo'
    >>> valueForKeyList(d, (), "foo")
    {'a': 1, 'c': {'e': 5, 'd': 4}, 'b': 2, 'f': {'g': {'h': 8}}}
    """
    for key in keys:
        if not key in d:
            return default
        d = d[key]
    return d

def setValueForKeyPath(d, key, value, separator="."):
    """Sets the value at the end of the string of keys split on the provided
    separator ("." by default.)

    >>> d = {'a': 1, 'c': {'e': 5, 'd': 4}, 'b': 2, 'f': {'g': {'h': 8}}}
    >>> setValueForKeyPath(d, "f.g.h", 80)
    >>> d
    {'a': 1, 'c': {'e': 5, 'd': 4}, 'b': 2, 'f': {'g': {'h': 80}}}
    """
    return setValueForKeyList(d, key.split(separator), value)

def setValueForKeyList(d, keys, value):
    """Sets the value at the end of the list of keys.

    >>> d = {'a': 1, 'c': {'e': 5, 'd': 4}, 'b': 2, 'f': {'g': {'h': 8}}}
    >>> setValueForKeyList(d, ('f', 'g', 'h'), 80)
    >>> d
    {'a': 1, 'c': {'e': 5, 'd': 4}, 'b': 2, 'f': {'g': {'h': 80}}}
    """
    d = valueForKeyList(d, keys[:-1])
    if (len(keys) == 1 and keys[0] not in d) or d is None:
        raise KeyError(key)
    d[keys[-1]] = value

def update(d, u):
    """Recursively update dictionary d with dictionary u.

    >>> d = {'a': 1, 'c': {'e': 5, 'd': 4}, 'b': 2, 'f': {'g': {'h': 8}}}
    >>> update(d, {'b': 20, 'f': {'g': {'h': 80}}})
    {'a': 1, 'c': {'e': 5, 'd': 4}, 'b': 20, 'f': {'g': {'h': 80}}}
    >>> update(d, {'c': 3})
    {'a': 1, 'c': 3, 'b': 20, 'f': {'g': {'h': 80}}}
    """
    for k, v in u.iteritems():
        if isinstance(v, collections.Mapping):
            r = update(d.get(k, {}), v)
            d[k] = r
        elif isinstance(d, collections.Mapping):
            d[k] = u[k]
        else:
            d = {k: u[k]}
    return d


def to_bool(value):
    """
       Converts 'something' to boolean. Raises exception for invalid formats
           Possible True  values: 1, True, "1", "TRue", "yes", "y", "t"
           Possible False values: 0, False, None, [], {}, "", "0", "faLse", "no", "n", "f", 0.0, ...
    """
    if str(value).lower() in ("yes", "y", "true",  "t", "1"): 
        return True
    if str(value).lower() in ("no",  "n", "false", "f", "0", "0.0", "", "none", "[]", "{}"): 
        return False
    

if __name__ == "__main__":
    import doctest
    doctest.testmod()
