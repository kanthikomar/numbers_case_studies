Number-to-English Converter<br>
This Django project provides an API endpoint to convert numeric values into their English word representations.<br><br>

Installation<br>
Clone the repository:<br>
Copy code<br>
git clone https://github.com/your_username/number-to-english.git<br><br>

Install dependencies:<br>
Copy code<br>
pip install -r requirements.txt<br><br>

Usage<br>
Configuration:<br>
Ensure that the config.json file is properly configured with the desired settings for number conversion.<br><br>

Run the Django server:<br>
Copy code<br>
python manage.py runserver<br><br>

API Endpoint:<br>
Endpoint URL: http://localhost:8000/num_to_english/<br>
Methods:<br>
GET: Pass the number as a query parameter number.<br>
POST: Send a JSON object with the key number via the request body.<br>

Example Usage:<br>
Copy code<br>
GET Request<br>
http://localhost:8000/num_to_english/?number=123.45<br><br>

POST Request (using cURL)<br>
curl -X POST -H "Content-Type: application/json" -d '{"number": "456.78"}' http://localhost:8000/num_to_english/<br><br>

Response:<br>
The API will respond with JSON containing the converted number in English or an error message, along with appropriate status information.<br><br>

Configuration File (config.json)<br>
Ensure the config.json file contains the necessary configuration for number conversion. Here's an example structure:<br><br>

json<br>
Copy code<br>
{<br>
  "units": ["Zero", "One", "Two", ... "Nineteen"],<br>
  "tens": ["", "Ten", "Twenty", ... "Ninety"],<br>
  "hundred": "Hundred",<br>
  "magnitudes": ["", "Thousand", "Million", "Billion"],
  "min_number": -1000000000,<br>
  "max_number": 1000000000<br>
}<br>
Modify the units, tens, hundred, magnitudes, min_number, and max_number fields as needed for your use case.<br><br>

