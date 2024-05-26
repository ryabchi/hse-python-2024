from typing import Any, Optional

def search_phone(content: Any, name: str) -> Optional[str]:

    if isinstance(content, dict):

        if 'name' in content and 'phone' in content:
            if content['name'] == name:
                return content['phone']

        for key in content:
            result = search_phone(content[key], name)
            if result is not None:
                return result

    elif isinstance(content, list):

        for item in content:
            result = search_phone(item, name)
            if result is not None:
                return result


    return None
