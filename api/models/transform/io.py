import json
import numpy as np
import pandas as pd

from api.models.sqla.product import Product


class IO:
    def __init__(self):
        pass

    
    def parse_jsonline(self, line):
        customer_id = line['id']
        products = line['products']
        flat_products = []
        for product_id in products:
            flat_product = []
            flat_product.append(customer_id)
            flat_product.append(product_id)
            flat_products.append(flat_product)
        return flat_products


    def parse_jsonlines(self, lines):
        convert_arr = []
        for line in lines:
            trans = self.parse_jsonline(line)
            convert_arr = convert_arr + trans
        
        return convert_arr


    def convert_arr_to_df(self, arr):
        "Groupby data by product_id"
        np_arr = np.array(arr)
        df = pd.DataFrame(data=np_arr, columns=['customer_id', 'product_id'])
        groupby_df = df.groupby('product_id')['customer_id'].count().reset_index(name="count")
        return groupby_df


    def add_date(self, date, df):
        df['date'] = date
        return df


    def save_object(self, db, objects):
        db.session.add_all(objects)
        db.session.flush()
        db.session.commit()
        return True


    def convert_legacy_to_json(self, raws):
        products = []
        product = {}
        product['product_id'] = raws.product_id
        product['units_sold'] = raws.units_sold
        products.append(product)

        return products


    def convert_legacy_to_jsons(self, raws):
        products = []
        for item in raws:
            product = {}
            product['product_id'] = item.product_id
            product['units_sold'] = item.units_sold
            products.append(product)

        return products


    def get_product(self, id):
        result = Product.query.filter_by(product_id=id).first()
        products = self.convert_legacy_to_json(result)
        return products


    def get_products(self):
        result = Product.query.all()
        products = self.convert_legacy_to_jsons(result)
        return products


    def convert_df_to_object(self, df):
        products_raw = df.values.tolist()
        products_object = [] 
        for item in products_raw:
            object = Product(date = item[2],
                             product_id = item[0],
                             units_sold = item[1])
            products_object.append(object)

        return products_object

    # TODO: should be to store raw data and agg data 
    def handle(self, db, date, lines):
        """Convert the jsonline to store database.
            _step 1: convert to dataframe(include agg before store db)
            _step 2: add date to campare each files
            _step 3: store to db
        """
        arr = self.parse_jsonlines(lines)
        groupby_df = self.convert_arr_to_df(arr)
        date_df = self.add_date(date, groupby_df)
        products = self.convert_df_to_object(date_df)
        self.save_object(db, products)
        return True
