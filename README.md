# YT Video to Notes

YT Video to Notes is a tool that generates detailed notes from YouTube videos.

## Setup

1. **Virtual Environment:**
   Set up a virtual environment for the project.

2. **Installation:**
   Install the required dependencies listed in `requirements.txt`.

3. **Get API Key:**
   Obtain an API key from [Google AI Studio](https://aistudio.google.com/app/apikey). For detailed instructions, refer to the [documentation](https://ai.google.dev/tutorials/python_quickstart).

4. **Clone Repository:**
   Clone this repository to your local machine.

5. **Environment Variables:**
   Add `GOOGLE_API_KEY` (use the exact name) environment varibale to the `.env` file .

6. **Run the Project:**
    Type `streamlit run app.py` in CLI

## Usage

1. **Provide YouTube Video Link:**
   Enter the YouTube video link into the application.

2. **Generate Detailed Notes:**
   Click on the "Get Detailed Notes" button to generate notes from the video.

## Requirements

- youtube_transcript_api
- streamlit
- google-generativeai
- python-dotenv
- pathlib

## Disclaimer

This project is for educational purposes only. The generated notes may not be entirely accurate or complete. Always cross-check information with reliable sources for critical content.

## Contact

Feel free to reach out for any inquiries or collaborations!
