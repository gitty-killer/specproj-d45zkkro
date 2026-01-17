"""Processing pipeline."""

from . import parse, transform, validate, filters, reducers


def process_lines(lines):
    parsed = [parse.parse_func_1(line) for line in lines]
    cleaned = [transform.transform_func_1(item) for item in parsed]
    valid = [item for item in cleaned if validate.validate_func_1(item)]
    return valid


def apply_filters(items):
    return [item for item in items if filters.filters_func_1(item)]


def reduce_items(items):
    return reducers.reducers_batch(items)


def run_pipeline(text):
    lines = [line for line in text.splitlines() if line.strip()]
    items = process_lines(lines)
    items = apply_filters(items)
    return reduce_items(items)

