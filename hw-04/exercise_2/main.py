from typing import List, Dict


def read_file_save(path: str):
    try:
        with open(path, 'r', encoding='utf-8') as fh:
            return [el.strip() for el in fh.readlines() if el.strip()]
    except Exception as e:
        print(e)
        return []
    

def parse_cat_info(cat_str:str) -> Dict:
    try:
        id, name, age = cat_str.split(',')
        return {
            'id': id,
            'name': name,
            'age': int(age)
        }
    except Exception as e:
        print(e)
        return {}
    

def get_cats_info(path: str) -> List[Dict]:
    raw_data = read_file_save(path)
    return [cat for cat in [parse_cat_info(item) for item in raw_data] if cat]
    # cats = [{'id': id, 'name': name, 'age': int(age)} 
    #         for id, name, age in [item.split(',') for item in cats]]
    

cats_info = get_cats_info('hw-04/exercise_2/cats.txt')
print(cats_info)


