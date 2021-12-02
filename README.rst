1. Setup

   cd path/lab_api
   
   virtualenv venv
   
   source venv/bin/activate
   
   pip install -r requirement.txt

2. Run app

   python -m flask run

3. Check api: Import file `NoCeling.postman_collection.json` to postman.

   UPLOAD: To upload file to system and store.

   PROCESS: To trigger a job to transform data.

   GET_DATA: To response data by using product_id

4. Test:

   python -m pytest --log-cli-level=DEBUG
