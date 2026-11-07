def search_by_title(items, keyword):
    return [d for d in items if keyword in d.title]

def search_by_category(items, category):
    return [d for d in items if d.category == category]
