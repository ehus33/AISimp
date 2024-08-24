# README

## AI Companion Chat Application

### Overview

This project is a simple AI-powered chat application using OpenAI's GPT-3.5-turbo model. The AI is designed to be a supportive, caring, and always-listening companion for the user. The application allows for continuous conversation, where the AI responds to user inputs while maintaining a memory of the conversation to provide more contextually relevant responses.

### Features

- **Continuous Conversation:** The AI keeps track of the conversation history, enhancing its ability to provide relevant and coherent responses.
- **Customizable Personality:** The AI is set to be supportive and caring, making it an ideal companion for someone looking for a friendly and empathetic chat.
- **Dynamic Memory:** The application uses a dynamic memory system that remembers the context of the conversation, leading to more personalized interactions.
- **Exit Commands:** The user can end the conversation at any time by typing "exit," "quit," or "bye."

### Requirements

- Python 3.5
- OpenAI Python Client Library
- An OpenAI API key

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ehus33/AISimp.git
   cd AISimp
   ```

2. **Install required packages:**
   Ensure you have `openai` installed. You can install it via pip:
   ```bash
   pip install openai
   ```

3. **Set up your OpenAI API Key:**
   Replace the placeholder in the `config.py` file with your actual OpenAI API key:
   ```python
   OPENAI_API_KEY = "your-openai-api-key"
   ```

### Usage

To run the AI Companion Chat application:

1. **Run the script:**
   ```bash
   python ai_companion.py
   ```

2. **Start the conversation:**
   The AI Companion will greet you and start the conversation. You can type your responses directly in the console.

3. **End the conversation:**
   To end the conversation, type "exit," "quit," or "bye."

### How It Works

The application uses OpenAI's `ChatCompletion.create()` method to generate AI responses. The conversation history (`memory`) is appended with each user input and AI response, allowing the AI to consider past interactions for generating new responses. The `max_tokens`, `temperature`, `top_p`, and penalty parameters are configured to fine-tune the behavior of the AI.

### Customization

- **Personality:** You can modify the AI's personality by changing the `system` message in the `generate_response` function.
- **Response Length and Creativity:** Adjust the `max_tokens`, `temperature`, `top_p`, `frequency_penalty`, and `presence_penalty` parameters to customize the AI's response length, creativity, and style.

### License

This project is licensed under the MIT License. See the LICENSE file for more details.

### Acknowledgments

This application leverages OpenAI's powerful language models to create an interactive and empathetic AI experience. Special thanks to OpenAI for providing the API and continuous improvements to AI models.
