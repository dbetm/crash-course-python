# Python >= 3.9

from typing import Dict, List, Tuple

positives: List[int] = [1, 2, 3, 4]

users: Dict[str, str] = {
    'Argentina': 1,
    'México': 34
}

countries: List[Dict[str, str]] = [
    {
        'name': 'Argentina',
        'people': '450000'
    },
    {
        'name': 'Colombia',
        'people': '9999'
    }
]

numbers: Tuple[int, float, int] = (1, 0.5, 1)

print(positives)
print(users)
print(countries)
print(numbers)

# In order to check the errors of defined types we can use mypy
