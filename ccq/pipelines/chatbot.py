# from langchain_mistralai import ChatMistralAI
# from langchain_core.prompts import ChatPromptTemplate

# class ChatBot:
#     def __init__(self, api_key = "gt8Qq1j3x1enSd7rFN3JHgRLE3COytKm", model = "mistral-large-latest"):
#         self.api_key = api_key
#         self.model = model

#     def run_bot(self, summery):
#         template = """
#         Your name is Core-Bot you help the users base on the vidio transcript summery and here is the transcript
#         {summery}
#         Here is the conversational history: {context}
#         Question: {question}
#         Answer:
#         """
#         llm = ChatMistralAI(
#             model=self.model,
#             temperature=0.7,
#             max_retries=2,
#             api_key = self.api_key
#         )
#         prompt = ChatPromptTemplate.from_template(template)
#         chain = prompt | llm
#         def handle_conversation():
#             context = ""
#             print("Chatbot is ready! Type 'exit' to end the conversation.")

#             while True:
#                 user_input = input("You: ")
#                 if user_input.lower() == 'exit':
#                     print("Conversation ended.")
#                     break
#                 result = chain.invoke({"context": context, "question": user_input, "summery": summery})

#                 response = result.content if hasattr(result, 'content') else str(result)
#                 print("BOT: ", response)

#                 context += f"\nUser: {user_input}\nAI: {response}"
#         handle_conversation()

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
        print("\n\n\nIam here",summary,context,question)
        prompt = self.prompt_template
        chain = prompt | self.llm
        result = chain.invoke({
            "summary": summary,
            "context": context,
            "question": question
        })
        # print(result)
        return result.content if hasattr(result, 'content') else str(result)
