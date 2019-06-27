import doctest
import file_validator
import class_grabber


def doc_test1(n):
    """

    >>> doc_test1("READ.txt")
    True
    >>> doc_test1("Rel.txt")
    True
    >>> doc_test1("test1.txt")
    File Does not Exist
    >>> doc_test1("View.py")
    False
    >>> doc_test1("READ.doc")
    File Does not Exist

    """

    i = file_validator.FileValidator(n)
    return i.check_plant()


def doc_test2(n):
    """

    >>> doc_test1("READ.txt")
    True
    >>> doc_test1("Rel.txt")
    True
    >>> doc_test1("test1.txt")
    File Does not Exist
    >>> doc_test1("READ.pdf")
    File Does not Exist
    >>> doc_test1("View.py")
    False

    """

    i = file_validator.FileValidator(n)
    return i.file_extension_check()


def doc_test3(n):
    """
    >>> doc_test3('getBlock()')
    'get_block()'
    >>> doc_test3('getInt()')
    'get_int()'
    >>> doc_test3('doThis()')
    'do_this()'
    >>> doc_test3('block()')
    'block()'
    >>> doc_test3('getAllFrom()')
    'get_all_from()'


    """

    i = class_grabber.ClassGrabber(new_class_name="name", new_data="")
    return i.formatter(n)

def doc_test4(n):
    """
    >>> doc_test3('getBlock()')
    'get_block()'
    >>> doc_test3('getInt()')
    'get_int()'
    >>> doc_test3('doThis()')
    'do_this()'
    >>> doc_test3('block()')
    'block()'
    >>> doc_test3('getAllFrom()')
    'get_all_from()'


    """

    i = class_grabber.ClassGrabber(new_class_name="name", new_data="")
    i.methods(n)
    return i.get_method



def doc_test5(n):
    """
    >>> doc_test3('getBlock')
    'get_block'
    >>> doc_test3('getInt')
    'get_int'
    >>> doc_test3('doThis')
    'do_this'
    >>> doc_test3('block')
    'block'
    >>> doc_test3('getAllFrom')
    'get_all_from'


    """

    i = class_grabber.ClassGrabber(new_class_name="name", new_data="")
    i.get_attrib(n)
    return i.get_attrib




if __name__ == "__main__":
    doctest.testmod()
