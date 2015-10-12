"""User-facing tables defined here."""

import os

from terminaltables.base_table import BaseTable


class AsciiTable(BaseTable):
    """Draw a table using regular ASCII characters, such as `+`, `|`, and `-`."""

    CHAR_CORNER_LOWER_LEFT = '+'
    CHAR_CORNER_LOWER_RIGHT = '+'
    CHAR_CORNER_UPPER_LEFT = '+'
    CHAR_CORNER_UPPER_RIGHT = '+'
    CHAR_HORIZONTAL = '-'
    CHAR_INTERSECT_BOTTOM = '+'
    CHAR_INTERSECT_CENTER = '+'
    CHAR_INTERSECT_LEFT = '+'
    CHAR_INTERSECT_RIGHT = '+'
    CHAR_INTERSECT_TOP = '+'
    CHAR_VERTICAL = '|'


class UnixTable(BaseTable):
    """Draw a table using box-drawing characters on Unix platforms. Table borders won't have any gaps between lines.

    Similar to the tables shown on PC BIOS boot messages, but not double-lined.
    """

    CHAR_CORNER_LOWER_LEFT = '\033(0\x6d\033(B'
    CHAR_CORNER_LOWER_RIGHT = '\033(0\x6a\033(B'
    CHAR_CORNER_UPPER_LEFT = '\033(0\x6c\033(B'
    CHAR_CORNER_UPPER_RIGHT = '\033(0\x6b\033(B'
    CHAR_HORIZONTAL = '\033(0\x71\033(B'
    CHAR_INTERSECT_BOTTOM = '\033(0\x76\033(B'
    CHAR_INTERSECT_CENTER = '\033(0\x6e\033(B'
    CHAR_INTERSECT_LEFT = '\033(0\x74\033(B'
    CHAR_INTERSECT_RIGHT = '\033(0\x75\033(B'
    CHAR_INTERSECT_TOP = '\033(0\x77\033(B'
    CHAR_VERTICAL = '\033(0\x78\033(B'

    @property
    def table(self):
        """Return a large string of the entire table ready to be printed to the terminal."""
        ascii_table = super(UnixTable, self).table
        optimized = ascii_table.replace('\033(B\033(0', '')
        return optimized


class WindowsTable(BaseTable):
    """Draw a table using box-drawing characters on Windows platforms. This uses Code Page 437. Single-line borders.

    From: http://en.wikipedia.org/wiki/Code_page_437#Characters
    """

    CHAR_CORNER_LOWER_LEFT = b'\xc0'.decode('ibm437')
    CHAR_CORNER_LOWER_RIGHT = b'\xd9'.decode('ibm437')
    CHAR_CORNER_UPPER_LEFT = b'\xda'.decode('ibm437')
    CHAR_CORNER_UPPER_RIGHT = b'\xbf'.decode('ibm437')
    CHAR_HORIZONTAL = b'\xc4'.decode('ibm437')
    CHAR_INTERSECT_BOTTOM = b'\xc1'.decode('ibm437')
    CHAR_INTERSECT_CENTER = b'\xc5'.decode('ibm437')
    CHAR_INTERSECT_LEFT = b'\xc3'.decode('ibm437')
    CHAR_INTERSECT_RIGHT = b'\xb4'.decode('ibm437')
    CHAR_INTERSECT_TOP = b'\xc2'.decode('ibm437')
    CHAR_VERTICAL = b'\xb3'.decode('ibm437')


class WindowsTableDouble(BaseTable):
    """Draw a table using box-drawing characters on Windows platforms. This uses Code Page 437. Double-line borders."""

    CHAR_CORNER_LOWER_LEFT = b'\xc8'.decode('ibm437')
    CHAR_CORNER_LOWER_RIGHT = b'\xbc'.decode('ibm437')
    CHAR_CORNER_UPPER_LEFT = b'\xc9'.decode('ibm437')
    CHAR_CORNER_UPPER_RIGHT = b'\xbb'.decode('ibm437')
    CHAR_HORIZONTAL = b'\xcd'.decode('ibm437')
    CHAR_INTERSECT_BOTTOM = b'\xca'.decode('ibm437')
    CHAR_INTERSECT_CENTER = b'\xce'.decode('ibm437')
    CHAR_INTERSECT_LEFT = b'\xcc'.decode('ibm437')
    CHAR_INTERSECT_RIGHT = b'\xb9'.decode('ibm437')
    CHAR_INTERSECT_TOP = b'\xcb'.decode('ibm437')
    CHAR_VERTICAL = b'\xba'.decode('ibm437')


class SingleTable(WindowsTable if os.name == 'nt' else UnixTable):
    """Cross-platform table with single-line box-drawing characters."""

    pass


class DoubleTable(WindowsTableDouble):
    """Cross-platform table with box-drawing characters. On Windows it's double borders, on Linux/OSX it's unicode."""

    pass