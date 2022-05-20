import csv
from books.models import Books

def csv_to_list(filename: str) -> list:
    with open(filename) as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',')
        csv_data = [line for line in reader]
    return csv_data

def save_data(data):
    aux = []
    for item in data:
        title = str(item.get('title'))
        author = str(item.get('author'))
        release_year = item.get('release_year')
        state = str(item.get('state'))
        pages = item.get('pages')
        publishing_company = str(item.get('publishing_company'))
        obj = Books(
            title = title,
            author = author,
            release_year = release_year,
            state = state,
            pages = pages,
            publishing_company = publishing_company,
        )
        aux.append(obj)
    Books.objects.bulk_create(aux)

data = csv_to_list('fix/books.csv')
save_data(data)