################################################################################
#  THIS FILE IS 100% GENERATED BY ZPROJECT; DO NOT EDIT EXCEPT EXPERIMENTALLY  #
#  Read the zproject/README.md for information about making permanent changes. #
################################################################################
from . import utils
from . import destructors
libczmq_destructors = destructors.lib

class Ztrie(object):
    """
    simple trie for tokenizable strings
    """

    def __init__(self, delimiter):
        """
        Creates a new ztrie.
        """
        p = utils.lib.ztrie_new(delimiter._p)
        if p == utils.ffi.NULL:
            raise MemoryError("Could not allocate person")

        # ffi.gc returns a copy of the cdata object which will have the
        # destructor called when the Python object is GC'd:
        # https://cffi.readthedocs.org/en/latest/using.html#ffi-interface
        self._p = utils.ffi.gc(p, libczmq_destructors.ztrie_destroy_py)

    def insert_route(self, path, data, destroy_data_fn):
        """
        Inserts a new route into the tree and attaches the data. Returns -1
        if the route already exists, otherwise 0. This method takes ownership of
        the provided data if a destroy_data_fn is provided.
        """
        return utils.lib.ztrie_insert_route(self._p, utils.to_bytes(path), data._p, destroy_data_fn)

    def remove_route(self, path):
        """
        Removes a route from the trie and destroys its data. Returns -1 if the
        route does not exists, otherwise 0.
        the start of the list call zlist_first (). Advances the cursor.
        """
        return utils.lib.ztrie_remove_route(self._p, utils.to_bytes(path))

    def matches(self, path):
        """
        Returns true if the path matches a route in the tree, otherwise false.
        """
        return utils.lib.ztrie_matches(self._p, utils.to_bytes(path))

    def hit_data(self):
        """
        Returns the data of a matched route from last ztrie_matches. If the path
        did not match, returns NULL. Do not delete the data as it's owned by
        ztrie.
        """
        return utils.lib.ztrie_hit_data(self._p)

    def hit_parameter_count(self):
        """
        Returns the count of parameters that a matched route has.
        """
        return utils.lib.ztrie_hit_parameter_count(self._p)

    def hit_parameters(self):
        """
        Returns the parameters of a matched route with named regexes from last
        ztrie_matches. If the path did not match or the route did not contain any
        named regexes, returns NULL.
        """
        return utils.lib.ztrie_hit_parameters(self._p)

    def hit_asterisk_match(self):
        """
        Returns the asterisk matched part of a route, if there has been no match
        or no asterisk match, returns NULL.
        """
        return utils.lib.ztrie_hit_asterisk_match(self._p)

    def print_py(self):
        """
        Print the trie
        """
        utils.lib.ztrie_print(self._p)

    def test(verbose):
        """
        Self test of this class.
        """
        utils.lib.ztrie_test(verbose)

################################################################################
#  THIS FILE IS 100% GENERATED BY ZPROJECT; DO NOT EDIT EXCEPT EXPERIMENTALLY  #
#  Read the zproject/README.md for information about making permanent changes. #
################################################################################
