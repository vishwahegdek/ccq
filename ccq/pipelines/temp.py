# myapp/utils/chatbot.py

from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate

class ChatBot:
    def __init__(self, api_key="gt8Qq1j3x1enSd7rFN3JHgRLE3COytKm", model="mistral-large-latest"):
        self.api_key = api_key
        self.model = model
        self.llm = ChatMistralAI(
            model=self.model,
            temperature=0.7,
            max_retries=2,
            api_key=self.api_key
        )
        self.prompt_template = ChatPromptTemplate.from_template("""
            Your name is Core-Bot. You help users based on the video transcript summary and here is the transcript:
            {summary}
            Here is the conversational history: {context}
            Question: {question}
            Answer:
        """)

    def get_response(self, summary, context, question):
        prompt = self.prompt_template
        chain = prompt | self.llm
        result = chain.invoke({
            "summary": summary,
            "context": context,
            "question": question
        })
        # print(result)
        return result.content if hasattr(result, 'content') else str(result)
