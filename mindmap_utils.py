from pydantic import BaseModel, Field
from typing import List
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import PromptTemplate
from query_data import query_rag
from langchain_together import Together
import textwrap

together_api_key = "fb5107bddcd0f7f144ca41251d77bbb59f9f5f64cb21435473f15a2801d28d73"
def wrap_text(text, width=20):
    return '\n'.join(textwrap.wrap(text, width=width))

class InfoNode(BaseModel):
    information: str = Field(description="Relevant information about the topic, that helps give an idea of what the topic is about")

class TopicNode(BaseModel):
    topic: str = Field(description="The topic of the node")
    children: List[InfoNode] = Field(description="A list of information nodes, about 3 or 4, that are children of this topic node")

class MindMap(BaseModel):
    topicNodes: List[TopicNode] = Field(description="A list of topics extracted from the given topic or content, to give an overview and walkthrough of the entire content")
def generate_mindmap(topic: str, chat_id : str) -> MindMap:
    # Use the existing RAG system to get information about the topic
    context, sources = query_rag(f"Provide detailed information about {topic}", chat_id)
    model = model = Together(
        model="meta-llama/Meta-Llama-3-8B-Instruct-Lite",
        temperature=0.7,
        max_tokens=1024,
        top_k=50,
        together_api_key=together_api_key
    )

    parser = PydanticOutputParser(pydantic_object=MindMap)
    format_instructions = parser.get_format_instructions()
    mindmap_prompt = PromptTemplate(
        template="""Based on the following information about {topic}, generate a mind map with 4 topic nodes, unless specified by user.
        Each topic may have about 4 to 5 information nodes. DO NOT USE JSON references like $ref, #defs, give only content required in each field.
        
        Information about {topic}:
        {context}
        
        {format_instructions}""",
        input_variables=["topic", "context"],
        partial_variables={"format_instructions": parser.get_format_instructions()}
    )
   
    try:
        mindmap_output = model.invoke(mindmap_prompt.format(topic=topic, context=context))
        mindmap = parser.parse(mindmap_output)
    except ValueError as e:
        if "$ref" or "#defs" in str(e):
            # Retry with a stricter prompt
            strict_prompt = PromptTemplate(
                template="""Based on the following information about {topic}, generate a mind map with 4 topic nodes, unless specified by user.
                Each topic may have about 4 to 5 information nodes. DO NOT USE ANY JSON SCHEMA REFERENCES like '#defs' or '$ref'. Provide only the actual content for each field.
                
                Information about {topic}:
                {context}
                
                {format_instructions}
                If mentioned by mistake, still don't use $defs or $ref""",
                input_variables=["topic", "context"],
                partial_variables={"format_instructions": parser.get_format_instructions()}
            )
            mindmap_output = model.invoke(strict_prompt.format(topic=topic, context=context))
            mindmap = parser.parse(mindmap_output)
        else:
            raise

    return convert_to_network_data(mindmap)


def convert_to_network_data(mindmap: MindMap) -> dict:
    nodes = []
    edges = []
    node_id = 1

    nodes.append({"id": node_id, "label": wrap_text(mindmap.topicNodes[0].topic), "group": "central"})
    central_id = node_id
    node_id += 1

    for topic_node in mindmap.topicNodes:
        topic_id = node_id
        nodes.append({"id": topic_id, "label": wrap_text(topic_node.topic), "group": "topic"})
        edges.append({"from": central_id, "to": topic_id})
        node_id += 1

        for info_node in topic_node.children:
            nodes.append({
                "id": node_id,
                "label": wrap_text(info_node.information),
                "group": "info",
                "shape": "box",
                "size": 30,
                "font": {"size": 14},
                "margin": 10
            })            
            edges.append({"from": topic_id, "to": node_id})
            node_id += 1

    return {"nodes": nodes, "edges": edges}