from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate


class ChatBot_LLama:
    def __init__(self, model="llama2"):
        self.model = model

    def run_bot(self, summary):
        template = """
        Your name is Core-Bot. You assist users based on the video transcript summary provided.
        Here is the transcript summary: {summary}
        Here is the conversational history: {context}
        Question: {question}
        Answer:
        """
        # Set up the Ollama LLM
        llm = Ollama(model=self.model)

        # Set up the prompt template
        prompt = ChatPromptTemplate.from_template(template)
        chain = prompt | llm

        def handle_conversation():
            context = ""
            print("Chatbot is ready! Type 'exit' to end the conversation.")

            while True:
                user_input = input("You: ")
                if user_input.lower() == 'exit':
                    print("Conversation ended.")
                    break

                # Invoke the chain with the provided context, question, and summary
                result = chain.invoke({"context": context, "question": user_input, "summary": summary})
                response = result.content if hasattr(result, 'content') else str(result)

                # Print the bot's response
                print("Core-Bot:", response)

                # Update the conversational history
                context += f"\nUser: {user_input}\nCore-Bot: {response}"

        handle_conversation()
