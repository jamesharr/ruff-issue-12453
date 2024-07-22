def test_bug1():
    # For the bug to occur:
    # - [repo-root]/mod1 must exist as a directory; contents of directory do not seem to matter
    # - There must be an empty line after the first import import
    # - It cannot be two blank lines
    # - It cannot be line with a comment
    # - It can be a line consisting of only tabs/whitespaces
    # - All 3 imports must exist and in this order
    # - All 3 imports must exist within the function
    #
    # When the above conditions are met, then tests/* are NOT checked for I001 (unsorted imports)
    # as requested in pyproject.toml.
    #
    # Files in src/* are checked for I001 as requested in pyproject.toml, regardless of the contents
    # of this file.

    from external_lib import qux

    from mod1 import foo
    from mod1.bar import baz

    # I think the code below is only important because it uses the above imports
    print(qux)
    print(foo)
    print(baz)
