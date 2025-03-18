# Talking Robot Web Application

This project is a web application that integrates a talking robot using Flask. The robot can recognize speech, respond with text-to-speech, and execute various commands.

## Project Structure

```
talking-robot-app
├── src
│   ├── app.py                # Main entry point of the web application
│   ├── static
│   │   ├── css
│   │   │   └── styles.css    # CSS styles for the web application
│   │   └── js
│   │       └── scripts.js     # JavaScript for user interactions
│   ├── templates
│   │   └── index.html        # HTML template for the web interface
│   └── robot
│       └── robot.py          # Python code for the talking robot functionality
├── requirements.txt           # List of dependencies
└── README.md                  # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd talking-robot-app
   ```

2. **Install dependencies:**
   Make sure you have Python installed. Then, create a virtual environment and install the required packages:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. **Run the application:**
   Start the Flask server:
   ```
   python src/app.py
   ```

4. **Access the application:**
   Open your web browser and go to `http://127.0.0.1:5000` to interact with the talking robot.

## Usage Guidelines

- Use the input field to send commands to the robot.
- The robot will respond with text-to-speech and display responses on the web page.
- Ensure your microphone is enabled for speech recognition functionality.

## Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements for the project.# AmighoProject0118
