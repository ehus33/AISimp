import openai
from config import OPENAI_API_KEY

# Set your OpenAI API key
openai.api_key = OPENAI_API_KEY

def generate_response(user_input, memory):
    prompt = f"The following is a conversation with an AI companion who is supportive, caring, and always there to listen.\n\n{memory}\nUser: {user_input}\nAI:"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Updated model
        messages=[
            {"role": "system", "content": "You are a supportive, caring, and always listening AI companion."},
            {"role": "user", "content": user_input},
            {"role": "assistant", "content": prompt}
        ],
        max_tokens=150,
        temperature=0.9,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6
    )

    return response.choices[0].message['content'].strip()

def main():
    print("AI Companion: Hello! I'm here to chat with you. How are you feeling today?")
    
    memory = ""
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("AI Companion: Goodbye! I'm always here if you need to talk.")
            break
        
        # Append the user's input to the memory
        memory += f"User: {user_input}\n"

        # Generate the AI's response
        response = generate_response(user_input, memory)
        print(f"AI Companion: {response}")
        
        # Append the AI's response to the memory
        memory += f"AI: {response}\n"

if __name__ == "__main__":
    main()
