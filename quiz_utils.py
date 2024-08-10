from pydantic import BaseModel, Field
from typing import List
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import PromptTemplate
from query_data import query_rag
from langchain_together import Together

together_api_key = "fb5107bddcd0f7f144ca41251d77bbb59f9f5f64cb21435473f15a2801d28d73"

class MCQ(BaseModel):
    choice: str = Field(description="The text of the multiple-choice option")
    isAnswer: bool = Field(description="True if this choice is the correct answer, False otherwise")

class Question(BaseModel):
    question: str = Field(description="The text of the question")
    choices: List[MCQ] = Field(description="A list of multiple-choice options for this question")

class Quiz(BaseModel):
    topic: str = Field(description="The main topic of the quiz")
    multiple_choice_questions: List[Question] = Field(description="A list of multiple-choice questions for this quiz", min_items=1)

def generate_quiz(topic: str, chat_id : str) -> Quiz:
    context, sources = query_rag(f"Provide detailed information about {topic}", chat_id)
    model = Together(
        model="meta-llama/Meta-Llama-3-8B-Instruct-Lite",
        temperature=0.2,
        max_tokens=1024,
        top_k=50,
        together_api_key=together_api_key
    )

    parser = PydanticOutputParser(pydantic_object=Quiz)
    prompt = PromptTemplate(
        template="Generate a quiz on the topic of {topic} based on the following information:\n\n{context}\n\n{format_instructions}\n\nEnsure the quiz has 3 multiple-choice questions UNLESS SPECIFIED BY USER, each with 4 options. Do not include any Python code or explanations, only the JSON object.",
    input_variables=["topic", "context"],
        partial_variables={"format_instructions": parser.get_format_instructions()}
    )

    quiz_prompt = prompt.format(topic=topic, context=context)
    response = model.invoke(quiz_prompt)

    try:
        quiz = parser.parse(response)
        return quiz
    except Exception as e:
        print(f"Error parsing quiz: {e}")
        print(f"Raw response: {response}")
        raise
