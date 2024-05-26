from pathlib import Path
from typing import Dict, Any, List, Optional

import re
from collections import Counter

def count_words(text: str) -> Dict[str, int]:
    words = re.findall(r'\b[a-zA-Z]{2,}\b', text)

    word_count = {}

    for word in words:
        word_lower = word.lower()
        if word_lower in word_count:
            word_count[word_lower] += 1
        else:
            word_count[word_lower] = 1

    return word_count



def exp_list(numbers: List[int], exp: int) -> List[int]:
    return [num ** exp for num in numbers]



def get_cashback(operations: List[Dict[str, Any]], special_category: List[str]) -> float:
    cashback = 0
    for operation in operations:
        if operation['category'] in special_category:
            cashback += operation['amount'] * 0.05
        else:
            cashback += operation['amount'] * 0.01
    return cashback



def get_path_to_file() -> Optional[Path]:

    if Path().resolve().name == 'tests':
        base_path = Path().resolve().parent
    else:
        base_path = Path().resolve()
    return base_path / 'tasks' / 'practice3' / 'tasks.csv'

import csv

def csv_reader(header: str) -> int:
    with open(get_path_to_file(), 'r') as f:
        reader = csv.DictReader(f)
        unique_elements = set()
        for row in reader:
            unique_elements.add(row[header])
        return len(unique_elements)

