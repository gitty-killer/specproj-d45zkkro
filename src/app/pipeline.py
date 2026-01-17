"""Processing pipeline."""

from . import parse, transform, validate


def process_lines(lines):
    parsed = [parse.parse_func_1(line) for line in lines]
    cleaned = [transform.transform_func_1(item) for item in parsed]
    valid = [item for item in cleaned if validate.validate_func_1(item)]
    return valid


def run_pipeline(text):
    lines = [line for line in text.splitlines() if line.strip()]
    return process_lines(lines)

