# DemoCo Chatbot Backend

This is the backend component of the DemoCo chatbot application. It provides the API endpoints and handles the processing of user queries to generate relevant answers.

## Technologies Used

- Django
- Python
- LlamaIndex

## Getting Started
### Prerequisites
- Python 3.X installed

### Installation
1. Clone the repository
```bash
git clone https://github.com/advaise-app/4df19892-bdb8-4144-a265-a72573278e2c.git
```

2. Navigate to the project directory
```bash
cd 4df19892-bdb8-4144-a265-a72573278e2c/src/chatbot-backend
```

3. Create a virtual environment
```bash
python -m venv venv
```

4. Activate the virtual environment
```bash
source env/bin/activate  # For Unix/Linux
env\Scripts\activate  # For Windows
```

5. Install the required packages
```bash
pip install -r requirements.txt
```
6. Set the Anthropic API key:
- Create a `.env` file in the project root.
- Add the following line to the `.env` file:
```bash
ANTHROPIC_API_KEY=your-api-key
```
- Replace `your-api-key` with your actual Anthropic API key.


### Running the server
```bash
python manage.py runserver
```

The server should now be running on `http://localhost:8000/`.

## API Endpoints

The backend provides an API endpoint for generating answers based on the knowledge base data. To use the API:

- Send a POST request to `http://localhost:8000/api/answer/` with the following JSON payload:
```json
{
 "query": "Your query here"
}
```
- The API will respond with the generated answer in the following format:
```json
{
 "answer": "The generated answer"
}
```




