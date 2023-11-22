Number-to-English Converter<br>
This Django project provides an API endpoint to convert numeric values into their English word representations.<br><br>

Installation<br>
Clone the repository:<br>
Copy code<br>
git clone https://github.com/your_username/number-to-english.git<br><br>

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
http://localhost:8000/num_to_english/?number=123.45<br>
curl -X GET "http://127.0.0.1:8000/num_to_english?number=100"<br><br>

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

Unit testing:<br>
To run the unit tests, execute the below command from the django project:<br>
python3 manage.py test number_to_english_app<br><br>

Cases tested:<br>
- Positive and negative whole numbers in range<br>
- Positive and negative decimal numbers in range<br>
- Positive and negative whole numbers out of range<br>
- Positive and negative decimal numbers out of range<br>
- Invalid number format<br><br>

Note:<br>
- The code doesn't handle numbers with special characters (including commas, but can be enhanced easilty depending on the requirement)<br>
- The server is insecure. It can easily be enhanced to include a certificate to make it secure.<br><br>
