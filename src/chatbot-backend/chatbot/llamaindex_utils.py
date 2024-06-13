import os
from dotenv import load_dotenv
from llama_index.core import Settings, Document, VectorStoreIndex
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.anthropic import Anthropic

# Load environment variables from .env file
load_dotenv()

# Set API key from environment variable
os.environ["ANTHROPIC_API_KEY"] = os.getenv("ANTHROPIC_API_KEY")

# Load the knowledge base data
knowledge_base_data = """
Kayla is a Project Manager with 10 years of experience. She contracts to DemoCo.
Beneil is a Project Manager who has been working for 20 years. He is not a contractor.
Miesha is a Diversity and Inclusiveness Researcher with 10 years of work experience. She is a permanent employee at DemoCo.
Israel has 20 years of experience as a Diversity and Inclusiveness Researcher. He works at SubCo, a subcontractor to DemoCo.
"""


# Set the LLM to Claude-3-Sonnet
Settings.llm = Anthropic(model="claude-3-opus-20240229")

# Set the tokenizer
tokenizer = Anthropic().tokenizer
Settings.tokenizer = tokenizer

# Set the embed model and disable tokenizer parallelism
os.environ["TOKENIZERS_PARALLELISM"] = "false"
Settings.embed_model = HuggingFaceEmbedding(
    model_name="BAAI/bge-small-en-v1.5"
)

# Create a Document object from the knowledge base data
document = Document(text=knowledge_base_data)

# Create an index from the Document using the specified embeddings
index = VectorStoreIndex.from_documents([document])


def generate_answer(query):
    """
        Generates an answer based on the given query using the knowledge base data.

        Args:
            query (str): The query to answer.

        Returns:
            dict: A dictionary containing the generated answer.
    """
    # Define the prompt Template
    prompt = f"""
    Based on the following knowledge base data:

    {knowledge_base_data}

    Please answer the query: "{query}"

    Provide the answer as a comma-separated list of names that match the requirements specified in the query. If no 
    names match the requirements or the answer is unknown based on the given data, respond with "No result / Unknown".

    Answer:
    """

    # Query the index with the prompt
    query_engine = index.as_query_engine()

    # Generate a response based on the query
    response = query_engine.query(prompt)

    # Extract the answer string from the response
    answer_string = response.response

    # Create a dictionary with the answer
    answer_dict = {"answer": answer_string}

    return answer_dict


if __name__ == '__main__':
    # Example usage
    queries = [
        "Find people who fulfil the following requirements: any person",
        "Find people who fulfil the following requirements: they are a project manager",
        "Find people who fulfil the following requirements: they are a project manager, they have more than 15 years of"
        "experience",
        "Find people who fulfil the following requirements: they are a project manager, they are a contractor",
        "Find people who fulfil the following requirements: they are a project manager, they have more than 15 years of"
        "experience, they are a contractor",
        "Find people who fulfil the following requirements: they are a diversity and inclusiveness researcher",
        "Find people who fulfil the following requirements: they are a diversity and inclusiveness researcher, "
        "they have more than 15 years of experience",
        "Find people who fulfil the following requirements: they are a diversity and inclusiveness researcher, "
        "they are a contractor",
        "Find people who fulfil the following requirements: they are a diversity and inclusiveness researcher, "
        "they have less than 15 years of experience, they are a contractor"
    ]

    # Generate answers for the queries
    for query in queries:
        answer = generate_answer(query)
        print(f"Query: {query}")
        print(f"Answer: {answer}\n")
