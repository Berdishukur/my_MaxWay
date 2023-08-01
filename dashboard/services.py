from django.db import connection
from contextlib import closing


def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row)) for row in cursor.fetchall()
    ]


def dictfetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))

def get_categories():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * from dashboard_category """)
        category = dictfetchall(cursor)
        return category

def get_product():
    with closing(connection.cursor()) as cursor:
        cursor.execute(""" SELECT dashboard_product.id, dashboard_product.title, dashboard_product.descriptions, 
        dashboard_product.price, 
        dashboard_product.created, 
        dashboard_category.name as category_name, dashboard_product.image as image  from dashboard_product
        left join dashboard_category on dashboard_product.category_id = dashboard_category.id""")
        product=dictfetchall(cursor)
        return product