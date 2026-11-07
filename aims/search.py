def search_by_title(items, keyword):
    return [dvd for dvd in items if keyword.lower() in dvd.title.lower()]


def search_by_category(items, category):
    return [d for d in items if d.category == category]
