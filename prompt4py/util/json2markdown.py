def json_to_markdown(json_data: dict | list | None, indent: int = 0):
    md = []
    current_indent = '  ' * max(indent - 1, 0)
    next_indent = '  ' * max(indent, 0)
    if isinstance(json_data, dict):
        for key, value in json_data.items():
            if indent == 0:
                md.append(f"## {key}")
                md.append(json_to_markdown(value, indent + 1))
            else:
                next_line = f'{json_to_markdown(value, indent + 1).strip()} '
                if next_line.startswith('-') or next_line[0].isdigit():
                    md.append(f"{current_indent}- **{key}**:")
                    md.append(f'{next_indent}{next_line}')
                else:
                    md.append(f"{current_indent}- **{key}**: {next_line}")
    elif isinstance(json_data, list):
        for i, item in enumerate(json_data):
            item_str = json_to_markdown(item, indent + 1).strip()
            md.append(f"{current_indent}{i + 1}. {item_str}")
    else:
        if json_data is None:
            return "null"
        return str(json_data).lower() if isinstance(json_data, bool) else str(json_data)
    return '\n'.join(md)
