# Multilingual Sentiment Web Application

This project is a multilingual sentiment analysis web application built using Flask. It allows users to input text in various languages and receive sentiment analysis results.

## Project Structure

```
multilingual-sentiment-app
├── src
│   ├── app.py                # Main application file
│   ├── routes
│   │   └── __init__.py       # Route definitions
│   ├── templates
│   │   └── index.html        # Main HTML template
│   └── static
│       └── style.css         # CSS styles
├── requirements.txt          # Python dependencies
├── render.yaml               # Deployment configuration for Render
├── .env                      # Environment variables
└── README.md                 # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd multilingual-sentiment-app
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   Create a `.env` file in the root directory and add your API keys and secret keys as specified in the `.env` file.

5. **Run the application:**
   ```
   python src/app.py
   ```

## Usage

- Open your web browser and navigate to `http://localhost:5000` to access the application.
- Input text in the provided field and submit to receive sentiment analysis results.

## Deployment

This application can be deployed on Render using the provided `render.yaml` configuration file. Follow the instructions in the Render documentation to set up your deployment.

## License

This project is licensed under the MIT License.