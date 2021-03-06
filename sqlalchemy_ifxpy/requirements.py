from sqlalchemy.testing.requirements import SuiteRequirements

from sqlalchemy.testing import exclusions


class Requirements(SuiteRequirements):

    @property  # TODO
    def order_by_col_from_union(self):
        return exclusions.closed()

    @property
    def group_by_complex_expression(self):
        return exclusions.closed()

    @property  # TODO
    def independent_connections(self):
        return exclusions.closed()

    @property
    def autocommit(self):
        return exclusions.open()

    @property  # TODO
    def unicode_data(self):
        return exclusions.closed()

    @property
    def date_coerces_from_datetime(self):
        return exclusions.closed()

    @property
    def datetime(self):
        """target dialect supports representation of Python
        datetime.datetime() objects."""

        return exclusions.open()

    @property
    def datetime_historic(self):
        """target dialect supports representation of Python
        datetime.datetime() objects with historic (pre 1900) values."""

        return exclusions.open()

    @property
    def datetime_microseconds(self):
        """target dialect supports representation of Python
        datetime.datetime() with microsecond objects."""

        return exclusions.closed()

    @property
    def date(self):
        """target dialect supports representation of Python
        datetime.date() objects."""

        return exclusions.open()

    @property
    def date_historic(self):
        """target dialect supports representation of Python
        datetime.datetime() objects with historic (pre 1900) values."""

        return exclusions.open()

    @property
    def time(self):
        """target dialect supports representation of Python
        datetime.time() objects."""

        return exclusions.open()

    @property
    def time_microseconds(self):
        return exclusions.closed()

    @property
    def unbounded_varchar(self):
        return exclusions.closed()

    @property
    def precision_generic_float_type(self):
        return exclusions.closed()

    @property
    def floats_to_four_decimals(self):
        return exclusions.closed()

    @property  # TODO
    def schemas(self):
        return exclusions.closed()

    @property  # TODO
    def schema_reflection(self):
        return exclusions.closed()

    @property
    def check_constraint_reflection(self):
        return exclusions.open()

    @property
    def cross_schema_fk_reflection(self):
        return exclusions.closed()

    @property
    def temp_table_reflection(self):
        return exclusions.closed()

    @property
    def parens_in_union_contained_select_w_limit_offset(self):
        return exclusions.closed()

    @property
    def parens_in_union_contained_select_wo_limit_offset(self):
        return exclusions.closed()

    @property
    def empty_inserts(self):
        return exclusions.closed()

    @property
    def insert_from_select(self):
        return exclusions.closed()

    @property
    def bound_limit_offset(self):
        return exclusions.closed()

    @property
    def implicitly_named_constraints(self):
        return exclusions.open()

    @property
    def foreign_key_constraint_option_reflection(self):
        return exclusions.open()

    @property
    def sequences(self):
        return exclusions.open()
