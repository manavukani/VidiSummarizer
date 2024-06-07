import streamlit as st
from extract_transcript import extract_transcript
from generate_summary import generate_summary

def main():
    st.title("VidiSummarizer: YouTube URL to Detailed Notes Generator")
    youtube_link = st.text_input("Enter YouTube Video Link:")
    user_prompt = st.text_area("Provide additional guidelines (optional):", height=100)

    # display image
    if youtube_link:
        video_id = youtube_link.split("=")[-1]
        st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)

    # Call function to extract transcript
    if st.button("Get Detailed Notes"):
        transcript_text = extract_transcript(youtube_link)

        if transcript_text:
            st.success("Transcript extracted successfully!")
            final_notes = generate_summary(transcript_text, user_prompt)
            st.markdown("## Detailed Notes:")
            st.write(final_notes)
        else:
            st.error("Failed to extract transcript.")

if __name__ == "__main__":
    main()
