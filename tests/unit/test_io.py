import unittest

from api.models.io import IO
from api.models.db import DB


class TestDataIO(unittest.TestCase):

    def test_parse_jsonline(self):
        io = IO()
        json = {"id": 0, "products": [1, 2]}
        expect_out = [[0, 1], [0, 2]]
        ents = io.parse_jsonline(json)
        self.assertEqual(ents, expect_out)


    def test_parse_jsonlines(self):
        io = IO()
        json = [
            {"id": 0, "products": [1, 2, 3]},
            {"id": 1, "products": [2, 3]},
            {"id": 2, "products": [1, 3]}
        ]
        expect_out = [
            [0,1], [0,2], [0,3],
            [1,2], [1,3],
            [2,1], [2,3]
        ]
        ents = io.parse_jsonlines(json)
        self.assertEqual(ents, expect_out)

    # @pytest.mark.skip("WIP")
    def test_convert_arr_to_df(self):
        io = IO()

        import numpy as np
        import pandas as pd
        arr = [
            [0,1], [0,2], [0,3],
            [1,2], [1,3],
            [2,1], [2,3]
        ]
        np_arr = np.array(arr)
        gen_df = pd.DataFrame(data=np_arr, columns=['customer_id', 'product_id'])
        expect_df = gen_df.groupby('product_id')['customer_id'].count().reset_index(name="count")
        df = io.convert_arr_to_df(arr)
        self.assertEqual(df.size, expect_df.size)

    
    def test_add_date(self):
        io = IO()

        import numpy as np
        import pandas as pd
        arr = [
            [0,1], [0,2], [0,3],
            [1,2], [1,3],
            [2,1], [2,3]
        ]
        date = '20210102'
        np_arr = np.array(arr)
        gen_df = pd.DataFrame(data=np_arr, columns=['customer_id', 'product_id'])
        expect_df = gen_df.groupby('product_id')['customer_id'].count().reset_index(name="count")
        v_expect_df = expect_df
        expect_df['date'] = date
        df = io.add_date(date, v_expect_df)
        self.assertEqual(df.size, expect_df.size)


    def test_save_json(self):
        io = IO()

        url = 'sqlite://'
        db = DB(url)
        engine = db.connect()

        import numpy as np
        import pandas as pd
        arr = [
            [0,1], [0,2], [0,3],
            [1,2], [1,3],
            [2,1], [2,3]
        ]
        date = '20210102'
        np_arr = np.array(arr)
        gen_df = pd.DataFrame(data=np_arr, columns=['customer_id', 'product_id'])
        expect_df = gen_df.groupby('product_id')['customer_id'].count().reset_index(name="count")
        expect_df['date'] = date
        status = io.save_json(engine, expect_df)
        self.assertEqual(True, status)


    def test_get_json(self):
        io = IO()

        url = 'sqlite://'
        db = DB(url)
        engine = db.connect()

        import numpy as np
        import pandas as pd
        arr = [
            [0,1], [0,2], [0,3],
            [1,2], [1,3],
            [2,1], [2,3]
        ]
        date = '20210102'
        np_arr = np.array(arr)
        gen_df = pd.DataFrame(data=np_arr, columns=['customer_id', 'product_id'])
        expect_df = gen_df.groupby('product_id')['customer_id'].count().reset_index(name="count")
        expect_df['date'] = date
        status = io.save_json(engine, expect_df)
        query = """SELECT product_id, sum(count) AS total
                   FROM agg
                   WHERE product_id = 1
                   GROUP BY product_id;"""
        result = io.get_json(engine, query)
        expect_result = [{"product_id": 1, "total": 2}]
        self.assertEqual(expect_result, result)


    def test_get_json_with_many_dates(self):
        io = IO()

        url = 'sqlite://'
        db = DB(url)
        engine = db.connect()

        import numpy as np
        import pandas as pd
        arr = [
            [0,1], [0,2], [0,3],
            [1,2], [1,3],
            [2,1], [2,3]
        ]
        date_01 = '20210101'
        date_02 = '20210102'
        np_arr = np.array(arr)
        gen_df = pd.DataFrame(data=np_arr, columns=['customer_id', 'product_id'])
        expect_df = gen_df.groupby('product_id')['customer_id'].count().reset_index(name="count")
        v_expect_df = expect_df
        expect_df['date'] = date_01
        status1 = io.save_json(engine, expect_df)
        v_expect_df['date'] = date_02
        status2 = io.save_json(engine, v_expect_df)

        query = """SELECT product_id, sum(count) AS total
                   FROM agg
                   WHERE product_id = 1
                   GROUP BY product_id;"""
        result = io.get_json(engine, query)
        expect_result = [{"product_id": 1, "total": 4}]
        self.assertEqual(expect_result, result)
