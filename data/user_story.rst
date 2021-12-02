Firstly, thank you for your application for Data Engineer position at iDealogic. As a part of interview procedure, we would like to send you a Test for this position as detail below:
Data Engineering Assessment
By means of the case below, we want to see to what extent you have knowledge of Python, REST, data engineering best practices and self-reliance. We use this test for both inexperienced and experienced developers. It is important to show that you understand the core elements of Python for data engineering. Think of the correct use of patterns, generics, libraries and packages. Of course it is important that you work clearly and in a structured manner.

CASE:
Our fictional e-commerce company wants better insight into the sales of products, and the data team is therefore asked to develop an API on which to ask how often a certain product has been sold in the past days.

Every day the department will receive a file with the sales of the previous day. The file is a json dump, each line contains a transaction:
{"Id": customer id, "products": list of product_ids associated with the transactions}

Attached the transactions of 7th of February(reffer attacted file)

- create a publicly accessible git repository
- do in between commits so that the steps that have been taken can be derived from your commits
- keep an eye on scaling and performance.
- use Python 3
- make use of the best practices
- give comments in your code to explain why you make certain choices. For this test, too many comments do not exist as long as they clarify what your thinking is
- document the assumptions you make.
- (EXTRA) - add authorization

### Solution
Input
{"id": 0, "products": [1, 2, 3]}
{"id": 1, "products": [2, 3]}

Output of phase 1
date, cust_id, product_id
21  , cus_0      , pd_1
21  , cus_0      , pd_2
21  , cus_0      , pd_3
21  , cus_1      , pd_2
21  , cus_1      , pd_3

Output of phase 2

date, product_id, count
21  , pd_1  ,       1
21  , pd_2  ,       2
21  , pd_3  ,       2

