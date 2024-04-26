# Smart-ATS-Resume-Analyzer

Smart-ATS is a Streamlit web application that optimizes resumes for automated tracking systems using Google's Gemini Pro AI. The application analyzes resumes against job descriptions, providing insights into match percentages, identifying missing key skills, and suggesting areas for improvement. It's specifically designed for tech job seekers looking to enhance their resumes to stand out in competitive job markets.

## Features

- **Resume Match Percentage**: Calculates how well your resume matches the job description.
- **Missing Keywords**: Identifies key technologies and skills not mentioned in your resume.
- **Improvement Suggestions**: Offers actionable advice to improve your resume.

## Getting Started

### Prerequisites

- Python 3.10
- Conda (recommended for creating and managing environments)
- Pip

### Installation

1. **Clone the repository**
```
git clone https://github.com/kiran-001/Smart-ATS-Resume-Analyzer.git
cd Smart-ATS-Resume-Analyzer
```

2. **Set up a virtual environment**
```
conda create -p venv python==3.10 -y
conda activate ./venv
```

3. **Install dependencies**
```
pip install --upgrade pip
pip install -r requirements.txt
```

### API Key Configuration

Before running the application, you need to obtain an API key from Google's generative AI platform:

- Visit the [Google Cloud Platform](https://cloud.google.com/) and sign in or create a new account.
- Navigate to the APIs & Services dashboard and enable the API for Gemini Pro.
- Create credentials (API key) for accessing the API.
- Once obtained, store your API key in a `.env` file at the root of the project:
```
echo GOOGLE_API_KEY=your_api_key_here > .env
```

### Running the Application

After setting up your environment and API key, you can run the application using:
```
streamlit run app.py
```
Navigate to the provided localhost URL in your web browser to start using the Smart-ATS.
