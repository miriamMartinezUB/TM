def parse_filter(filter_string):
    if '[' in filter_string:
        parts = filter_string.split('[')
        filter_name = parts[0]
        argument = parts[1][:-1]
        return filter_name, argument
    return filter_string, None