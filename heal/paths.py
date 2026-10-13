def get_path(data, path):
    parts = path.split(".")
    current = data
    for part in parts:
        if not isinstance(current, dict) or part not in current:
            return None
        current = current[part]
    return current


def set_path(data, path, value):
    parts = path.split(".")
    current = data
    for part in parts[:-1]:
        current = current.setdefault(part, {})
    current[parts[-1]] = value
    return data


def flatten(data):
    if not isinstance(data, dict):
        return data

    flat = {}
    for key, value in data.items():
        if isinstance(value, dict):
            sub_flat = flatten(value)
            for sub_key, sub_value in sub_flat.items():
                flat[f"{key}.{sub_key}"] = sub_value
        else:
            flat[key] = value

    return flat