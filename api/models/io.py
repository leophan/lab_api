import json
import numpy as np
import pandas as pd


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
        np_arr = np.array(arr)
        df = pd.DataFrame(data=np_arr, columns=['customer_id', 'product_id'])
        groupby_df = df.groupby('product_id')['customer_id'].count().reset_index(name="count")
        return groupby_df


    def add_date(self, date, df):
        df['date'] = date
        return df


    def save_json(self, engine, df):
        df.to_sql('agg', con=engine, if_exists='append')
        return True


    def convert_legacy_to_json(self, raws):
        products = []
        for item in raws:
            product = {}
            product['product_id'] = item[0]
            product['total'] = item[1]
            products.append(product)

        return products


    def get_json(self, engine, query):
        try:
            result = engine.execute(query).fetchall()
            products = self.convert_legacy_to_json(result)
            return products
        except:
            return []


    # TODO: should be to store raw data and agg data 
    def handle(self, engine, date, lines):
        """Convert the jsonline to store database.
            _step 1: convert to dataframe(include agg before store db)
            _step 2: add date to campare each files
            _step 3: store to db
        """
        arr = self.parse_jsonlines(lines)
        groupby_df = self.convert_arr_to_df(arr)
        date_df = self.add_date(date, groupby_df)
        self.save_json(engine, date_df)
        return True
