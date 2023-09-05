from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Import the os package.
import os

# Import the openai package.
import openai

# Set openai.api_key to the OPENAI_API_KEY environment variable.
openai.api_key = os.environ["OPENAI_API_KEY"]

# Import OpenAI.
from langchain.llms import OpenAI

# Import ChatOpenAI.
from langchain.chat_models import ChatOpenAI

# Open the text file and read its lines.
with open('financial_headlines.txt', 'r') as data:
    headlines = data.readlines()

# Print all headlines.
headlines

# Strip the new line character from all headlines.
headlines = [line.strip("\n") for line in headlines]

# Print all headlines.
headlines

# Import the PromptTemplate class.
from langchain.prompts import PromptTemplate

# Create a dynamic template to analyze a single headline.
prompt_template = PromptTemplate.from_template(
    template="Analyze the following financial headline for sentiment: {headline}",
)

# Format the prompt template on the first headline of the dataset.
formatted_prompt = prompt_template.format(headline=headlines[0])

# Print the formatted template.
formatted_prompt

# Import the ChatPromptTemplate class.
from langchain.prompts import ChatPromptTemplate

# Define the system message.
system_message = """You are performing sentiment analysis on news headlines regarding financial analysis.
    This sentiment is to be used to advice financial analysts.
    The format of the output has to be consistent.
    The output is strictly limited to any of the following options: [positive, negative, neutral]."""

# Initialize a new ChatPromptTemplate with a system message and human message.
chat_template = ChatPromptTemplate.from_messages([
    ("system", system_message),
    ("human", "Analyze the following financial headline for sentiment: {headline}"),
])

# Format the ChatPromptTemplate.
formatted_chat_template = chat_template.format_messages(
    headline=headlines[0]
)

# Print the formatted template.
formatted_chat_template

# # Import the LLMChain class.
# from langchain.chains import LLMChain

# # Create the LLMChain by combining a completion model and a prompt.
# completion_chain = LLMChain(llm=OpenAI(), prompt=prompt_template)

# # Run the LLMChain.
# completion_chain.run(headline=headlines[0])

# Import the LLMChain class.
from langchain.chains import LLMChain
from langchain_openai import OpenAI

# Create the LLMChain by combining a completion model and a prompt.
completion_chain = LLMChain(llm=OpenAI(), prompt=prompt_template)

# Run the LLMChain.
completion_chain.run(headline=headlines[0])

# Create the LLMChain by combining a chat completion model and a prompt.
chat_chain = LLMChain(llm=ChatOpenAI(), prompt=chat_template)

# Run the LLMChain.
chat_chain.run(headline=headlines[0], system_message=system_message)

# Import the CommaSeparatedListOutputParser class.
from langchain.output_parsers import CommaSeparatedListOutputParser

# Instantiate the output parser.
output_parser = CommaSeparatedListOutputParser()

# Get the format instructions from the output parser.
format_instructions = output_parser.get_format_instructions()

# Instantiate a new prompt template with the format instructions.
company_name_template = PromptTemplate(
    template="List all the company names from the following headlines, limited to one name per headline: {headlines}.\n{format_instructions}",
    input_variables=["headlines"],
    partial_variables={"format_instructions": format_instructions}
)

# Format the prompt using all headlines.
formatted_company_name_template = company_name_template.format(headlines=headlines)

# Instantiate a Langchain OpenAI Model object.
model = OpenAI(temperature=0)

# Run the model on the input.
_output = model(formatted_company_name_template)

# Parse the output.
company_names = output_parser.parse(_output)

# Print the data type the parsed output.
print(f"Data type: {type(company_names)}\n")

# Print the output.
print(company_names)

# # Import the necessary classes from langchain.
# from langchain.agents.agent_toolkits import create_python_agent
# from langchain.tools.python.tool import PythonREPLTool

# # Instantiate a Python agent, with the PythonREPLTool.
# agent_executor = create_python_agent(
#     llm=OpenAI(temperature=0, max_tokens=1000),
#     tool=PythonREPLTool(),
#     verbose=True
# )

# # Ask the agent for the solution of a mathematical equation.
# agent_executor.run("What is the square root of 250? Round the answer down to 4 decimals.")

# Import the necessary classes from langchain.
from langchain_experimental.agents.agent_toolkits import create_python_agent
from langchain_experimental.tools.python.tool import PythonREPLTool

# Instantiate a Python agent, with the PythonREPLTool.
agent_executor = create_python_agent(
    llm=OpenAI(temperature=0, max_tokens=1000),
    tool=PythonREPLTool(),
    verbose=True
)

# Ask the agent for the solution of a mathematical equation.
agent_executor.run("What is the square root of 250? Round the answer down to 4 decimals.")

# Run the agent
agent_executor.run(f"""For every of the following headlines, extract the company name and whether the financial sentiment is   positive, neutral or negative.
   Load this data into a pandas dataframe.
   The dataframe will have three columns: the name of the company, whether the financial sentiment is positive or negative and the headline itself.
   The dataframe can then be saved in the current working directory under the name financial_analysis.csv.
   If a csv file already exists with the same name, it should be overwritten.

   The headlines are the following:
   {headlines}
   """)

# Make the necessary import.
import pandas as pd

# Load the CSV file into a dataframe.
df = pd.read_csv("financial_analysis.csv")

# Print the dataframe.
df.head()

# Create a new prompt template with output parsing.
sentiment_template = PromptTemplate(
    template="Get the financial sentiment of each of the following headlines. The output is strictly limited to any of the following options: ['Positive', 'Negative', 'Neutral']: {headlines}.\n{format_instructions}",
    input_variables=["headlines"],
    partial_variables={"format_instructions": format_instructions}
)

# Format the prompt template.
formatted_sentiment_template = sentiment_template.format(headlines=headlines)

# Run the model on the formatted prompt template.
_output = model(formatted_sentiment_template)

# Parse the output.
sentiments = output_parser.parse(_output)

# Print the list of sentiments.
sentiments

# Define a new function with two inputs,
def visualize_sentiments(headlines, sentiments):
    # Assert that both inputs are of equal length
    assert len(headlines) == len(sentiments)

    # Visualize the sentiments and their respective headlines
    for i, _ in enumerate(headlines):
        print(f"{sentiments[i].upper()}: {headlines[i]}")

# Call the function
visualize_sentiments(headlines, sentiments)

# Store the few shot examples in a variable.
sentiment_examples = """
    If a company is doing financially better than before, the sentiment is positive. For example, when profits or revenue have increased since the last quarter or year, exceeding expectations, a contract is awarded or an acquisition is announced.
    If the company's profits are decreasing, losses are mounting up or overall performance is not meeting expectations, the sentiment is negative.
    If nothing positive or negative is mentioned from a financial perspective, the sentiment is neutral.
"""

# Instantiate a new prompt template with the format instructions.
sentiment_template = PromptTemplate(
    template="Get the financial sentiment of each of the following headlines. {few_shot_examples} The output is strictly limited to any of the following options: ['Positive', 'Negative', 'Neutral']: {headlines}.\n{format_instructions}",
    input_variables=["headlines", "few_shot_examples"],
    partial_variables={"format_instructions": format_instructions}
)

# Format the template.
formatted_sentiment_template = sentiment_template.format(headlines=headlines, few_shot_examples=sentiment_examples)

# Run the model on the formatted template.
_output = model(formatted_sentiment_template)

# Parse the model output.
sentiments = output_parser.parse(_output)

# Visualize the result.
visualize_sentiments(headlines, sentiments)

# Run the agent to create a file with the headlines, company names and sentiments.
agent_executor.run(f"""Create a dataframe with two columns: company_name, sentiment and headline.
To fill the dataframe, use the following lists respectively: {str(company_names)}, {str(sentiments)} and {str(headlines)}.
The dataframe can then be saved in the current working directory under the name financial_analysis_with_parsing.csv.
If a csv file already exists with the same name, it should be overwritten.
""")

# Load the CSV file into a dataframe.
df = pd.read_csv("financial_analysis_with_parsing.csv")

# Print the dataframe.
df

# Load the lines of the text file.
with open('reddit_comments.txt', 'r') as data:
    comments = data.readlines()

# Optionally print the comments.
comments

# Import the openai package.
from openai import OpenAI
client = OpenAI()

# Pick a comment.
comment = comments[0]

# Send the comment to the Moderation API.
moderation_output = client.moderations.create(input=comment)

# Optionally print the comment.
print(comment)

# Print the output.
moderation_output
