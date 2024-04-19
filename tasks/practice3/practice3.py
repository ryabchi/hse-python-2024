from pathlib import Path
from typing import Dict, Any, List, Optional

import re

def count_words(text: str) -> Dict[str, int]:
    words = re.findall(r'\b[A-Za-z]+\b', text.lower())
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count



def exp_list(numbers: List[int], exp: int) -> List[int]:
    return [num ** exp for num in numbers]



def get_cashback(operations: List[Dict[str, Any]], special_category: List[str]) -> float:
    total_cashback = 0
    for operation in operations:
        if operation['category'] in special_category:
            total_cashback += operation['amount'] * 0.05
        else:
            total_cashback += operation['amount'] * 0.01
    return total_cashback



def get_path_to_file() -> Optional[Path]:
    if Path().resolve().name == 'tests':
        base_path = Path().resolve().parent
    else:
        base_path = Path().resolve()
    return base_path / 'tasks' / 'practice3' / 'tasks.csv'



import csv

def csv_reader(header: str) -> int:
    filepath = get_path_to_file()
    unique_elements = set()

    with open(filepath, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            unique_elements.add(row[header])

    return len(unique_elements)

