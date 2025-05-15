from dotenv import load_dotenv
import os
import streamlit as st
from crewai import Agent, LLM, Task, Crew
from crewai_tools import FirecrawlSearchTool

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
FIRECRAWL_API_KEY = os.getenv("FIRECRAWL_API_KEY")
search_tool = FirecrawlSearchTool(api_key=FIRECRAWL_API_KEY)

researcher = Agent(
    role="Current Affairs Researcher",
    goal="Fetch Top 10 current global including India news topics with the date of event happend",
    backstory="An expert news researcher with access to latest information",
    tools=[search_tool],
    llm=LLM(model="gemini/gemini-2.0-flash", api_key=GEMINI_API_KEY)
)

summarizer = Agent(
    role="Current Affairs Summarizer",
    goal="Summarize news topics",
    backstory="An expert in simplifying complex topics for understanding",
    llm=LLM(model="gemini/gemini-2.0-flash", api_key=GEMINI_API_KEY)
)

task1 = Task(
    description="Fetch Top 10 current global including India news topics with the date of event happend",
    agent=researcher,
    expected_output="Fetch Top 10 current global including India news topics with the date of event happend"
)

task2 = Task(
    description="Summarize news topics from previous new articles and give one line summary for each",
    agent=summarizer,
    expected_output="A one-line summary for each of the previously fetched news topics."
)

current_affairs_crew = Crew(
    agents=[researcher, summarizer],
    tasks=[task1, task2],
    process="sequential"
)

st.title("Current Affairs")
if st.button("Get Current News Summary"):
    with st.spinner("Fetching and summarizing news.."):
        output = current_affairs_crew.kickoff()
    st.subheader("Top News (One-liner Summary)")
    st.write(output.tasks_output[-1].raw)
