import os
from llama_index.core import Settings, Document, VectorStoreIndex
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.replicate import Replicate
from llama_index.llms.anthropic import Anthropic
from transformers import AutoTokenizer

# Set API key
# os.environ["REPLICATE_API_TOKEN"] = "r8_YL0Iibrqio0IIGi4foyzDflzDFA5sxH1h1INk"
os.environ["ANTHROPIC_API_KEY"] = ("sk-ant-api03-RCuXiep2mAqjK67"
                                   "-hI3bPS37QXMgHBkexKISG3NV1ZbeFsGYXCJsFEVMgbikhHLuiyzj7ck_Xt-g8MjKKV1MPA-_rEdrwAA")

# Load the knowledge base data
knowledge_base_data = """
Kayla is a Project Manager with 10 years of experience. She contracts to DemoCo.
Beneil is a Project Manager who has been working for 20 years. He is not a contractor.
Miesha is a Diversity and Inclusiveness Researcher with 10 years of work experience. She is a permanent employee at DemoCo.
Israel has 20 years of experience as a Diversity and Inclusiveness Researcher. He works at SubCo, a subcontractor to DemoCo.
"""

# # Create a Replicate object
# llama2_7b_chat = "meta/llama-2-7b-chat:8e6975e5ed6174911a6ff3d60540dfd4844201974602551e10e9e87ab143d81e"
# Settings.llm = Replicate(
#     model=llama2_7b_chat,
#     temperature=0.01,
#     additional_kwargs={"top_p": 1, "max_new_tokens": 300},
# )

# Set the LLM to Claude-3-Sonnet
Settings.llm = Anthropic(model="claude-3-sonnet-20240229")

# Set the tokenizer
tokenizer = Anthropic().tokenizer
Settings.tokenizer = tokenizer

# Set the embed model
os.environ["TOKENIZERS_PARALLELISM"] = "false"
Settings.embed_model = HuggingFaceEmbedding(
    model_name="BAAI/bge-small-en-v1.5"
)

# Create a Document object from the knowledge base data
document = Document(text=knowledge_base_data)

# Create an index from the Document using the specified embeddings
index = VectorStoreIndex.from_documents([document])


def generate_answer(query):
    prompt = f"""
    Based on the following knowledge base data:

    {knowledge_base_data}

    Please answer the query: "{query}"

    Provide the answer as a comma-separated list of names that match the requirements specified in the query. If no names match the requirements or the answer is unknown based on the given data, respond with "No result / Unknown".

    Answer:
    """

    query_engine = index.as_query_engine()
    response = query_engine.query(prompt)

    answer_string = response.response
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

    for query in queries:
        answer = generate_answer(query)
        print(f"Query: {query}")
        print(f"Answer: {answer}\n")
