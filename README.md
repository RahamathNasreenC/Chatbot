
### AI Chatbot using Streamlit & Gemini API

A simple AI-powered chatbot web application built using **Python**, **Streamlit**, and the **Google Gemini API**.
This project demonstrates how to integrate an AI model into a web interface while following secure API key handling practices.

---

### Technologies Used

* Python 3
* Streamlit
* Google Generative AI (Gemini API)
* HTML & CSS (for UI styling)



### Features

* Interactive AI chatbot interface
* Clean and modern UI with chat bubbles
* Session-based chat history
* Secure API key handling using environment variables
* Easy local setup and execution



### 📂 Project Structure


AI-Chatbot/
│
├── chatbot.py
├── requirements.txt
├── README.md


### API Key Setup (Important)

This project requires a **Google Gemini API key**.
For security reasons, the API key is **not hardcoded** in the source code.

Set your own API key as an environment variable named `GEMINI_API_KEY`.

### Windows (Command Prompt)

```cmd
set GEMINI_API_KEY=your_api_key_here
streamlit run chatbot.py
```

### Windows (PowerShell)

```powershell
$env:GEMINI_API_KEY="your_api_key_here"
streamlit run chatbot.py
```

### Linux / macOS

```bash
export GEMINI_API_KEY="your_api_key_here"
streamlit run chatbot.py
```


## How to Run the Project

1. Clone the repository

  git clone https://github.com/RahamathNasreenC/Chatbot.git
  cd Chatbot



3. Install the required dependencies:

   pip install -r requirements.txt

3. Set your Gemini API key as shown above.

4. Run the application:

   streamlit run chatbot.py

5. Open the URL displayed in the terminal (usually `http://localhost:8501`) to use the chatbot.

### 📌 Notes

* Users must provide their own Gemini API key to run this application.
* API keys are securely managed using environment variables.
* This project is created for learning and demonstration purposes.



### 📄 License

This project is open-source and free to use for educational purposes.


