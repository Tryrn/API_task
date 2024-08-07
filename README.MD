This project is authored by Trym Ettestøl Osland, ans is part of the job interview process for the position of datascientist/portfolio manager at Volue

Parts

API consumption [back-end]              - pull data from API
Storage of data [back-end]                   - store data
Manipulate data [back-end]                - manipulate data
Present data [front-end]                        - display data
Optional: Versioning                                 - use git
Optional: Show work in GitHub         - create account if necessary

Run app.py and open the webpage by going to http://127.0.0.1:5000/
Insert parameters in the fields to fetch data from the api and store it as a json file.
Use the following parameters by default:
CustomerId: "TestCustomer"
Api-Key: "Api-Planner-996ba74c-cdaf-4f66-9448-ffff"
ForDate: "2024-02-03"
Market: "FCR-D-D1"
Country: "Sweden"

app.py uses API_requests.py to request and directly store the data as the data.json file

Once you have the json file, you cen run the entire jupyter notebook db_store.ipynb.
This notebook uses the stored data.json file to store data in an sqlite3 database.
The resulting database has three main tables; main --< series --< positions, and is stored as bids.db
The notebook also does some simple manipulation before storing the data, such as adding a dateTime value for each entry in positions. 

The resulting database is used for the Power BI visualization. 
To achieve this, ODBC Data source administration is used as an intermediate step to connect to Power BI, as Power BI does not directly accept sqlite3 databases.
The final visualization is found in the file Bid results.pbix
