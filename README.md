# DemoCo Chatbot
### Getting started

### Prerequisites
- Python 3.X
- Node.js 

### Installation
1. Clone the repository
```bash
git clone https://github.com/advaise-app/4df19892-bdb8-4144-a265-a72573278e2c.git
```

2. Set up the backend
* Navigate to the backend directory
    ```bash
    cd 4df19892-bdb8-4144-a265-a72573278e2c/src/chatbot-backend
    ```

* Create a virtual environment
    ```bash
    python -m venv venv
    ```

* Activate the virtual environment
  * For Unix/Linux:
    ```bash
    source venv/bin/activate
    ```
     * For Windows:
    ```bash
    venv\Scripts\activate
    ```
    
* Install the required packages
    ```bash
    pip install -r requirements.txt
    ```

* Set the Anthropic API key:
  * Create a `.env` file in the backend directory
  * Add the following line to the `.env` file:
    ```bash
    ANTHROPIC_API_KEY=your-api-key
    ```
  * Replace your-api-key with the API key you received from Anthropic


3. Set up the frontend

* Navigate to the frontend directory
    ```bash
    cd 4df19892-bdb8-4144-a265-a72573278e2c/src/chatbot-frontend
    ```
* Install the required packages
    ```bash
    npm install
    ```
  
### Usage
1. Start the backend
* Navigate to the backend directory:
    ```bash
    cd 4df19892-bdb8-4144-a265-a72573278e2c/src/chatbot-backend
    ```
  
* Run the backend
    ```bash
    python manage.py runserver
    ```
  
2. Start the frontend
* Navigate to the frontend directory:
    ```bash
    cd 4df19892-bdb8-4144-a265-a72573278e2c/src/chatbot-frontend
    ```
  
* Run the frontend
    ```bash
    npm start
    ```
  
3. Open your browser and go to `http://localhost:3000/` to use the chatbot

You should now have the DemoCo Chatbot up and running on your local machine.
  

