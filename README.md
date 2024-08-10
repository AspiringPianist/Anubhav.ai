# Anubhav.ai Chatbot
======================

## Overview
-----------

Anubhav.ai is a chatbot with media viewer capabilities, built using HTML, CSS, JavaScript, and Flask. The chatbot allows users to interact with it, create mindmaps, take quizzes, and view media content such as YouTube videos and PDF documents. Usecases are not limited to asking questions about documents, but have additional features including things like Mindmap Generation, Auto-Graded Quiz Creations, etc based on the provided documents/youtube videos.

Here's a link for the quick demo : [Youtube](https://youtu.be/a4pJpp_DbgQ)

![Main Screenshot](https://github.com/AspiringPianist/Anubhav.ai/blob/main/main_ss?raw=True)

## Features
------------

* **Chatbot functionality**: Engage in conversations with the chatbot, ask questions, and receive responses.
* **Mindmap creation**: Create mindmaps on specific topics using the `/Mindmap` command.
* **Quiz creation**: Generate quizzes on specific topics using the `/QuizCreate` command.
* **Media viewer**: View YouTube videos and PDF documents in the media viewer, by just `pasting link directly in the input field`.
* **Chat history**: View previous conversations with the chatbot.
* **Media selector**: Select and view previous media content, like generated mindmaps or uploaded documents and videos.
* **Chat Folders**: Organize your chat sessions, by storing them in different folders, each with their own vector store for RAG. They are titled by your first message to chatbot.

  ![Screenshot 1](https://github.com/AspiringPianist/Anubhav.ai/blob/main/ss1.jpg?raw=True)
  ![Screenshot 2](https://github.com/AspiringPianist/Anubhav.ai/blob/main/ss2.jpg?raw=True)

## How to Use
--------------

### Running the Chatbot

1. After installing dependencies with `pip install -r requirements.txt `, Run the Flask application using `app.py` or run `flask --app app run` in the terminal.
2. Open a web browser and navigate to `http://127.0.0.1:5000` to access the chatbot interface.

### Interacting with the Chatbot

1. Type a message in the input field and press the send button or press Enter.
2. The chatbot will respond with a message.
3. You can ask the chatbot questions, provide input, or request actions.

### Creating Mindmaps

1. Type `/Mindmap <topic>` to create a mindmap on a specific topic.
2. The chatbot will generate a mindmap based on the topic.
3. You can view the mindmap in the media viewer.

### Taking Quizzes

1. Type `/QuizCreate <topic>` to create a quiz on a specific topic.
2. The chatbot will generate a quiz with questions and answers.
3. You can submit your answers and view the results.

### Viewing Media Content

1. Type a YouTube link to view a YouTube video.
2. Upload a PDF document to view it in the media viewer.

### Navigation

1. Use the chat history to view previous conversations.
2. Use the media selector to view previous media content.

## Technical Details
--------------------

* The chatbot uses Flask as the web framework.
* Langchain was used for handling LLM responses and developing endpoint backends.
* LLM APIs were used from Together.ai, the API keys for `Zense Submission` will be included in the `is there anything else we need to know section of the response`.
* The user interface is built using HTML, CSS, and JavaScript.
* Mindmaps are created using self developed APIs in python (flask), scalable to any LLM.
* Quizzes are generated based on user input and stored in a database, also an API that can be scaled to any LLM.
* Media content is displayed using embedded YouTube videos and PDF viewers.
* Chroma DB was used for vector stores.
* Ollama was used for embeddings using the `nomic-embed-text` model.

## Limitations
---------
* Since Llama 3 does not have a generous enough context size for 1 hour long videos, you might run into issues where the input tokens exceeds the maximum of about 10-12k.
* Some attempts were to use larger models for answering queries, and using lighter models like the 8B parameters version for quiz creation and mindmap generation.
* Only Instruct models were used, chat models provide unfavourable results.
* Local embedding models are used via ollama to convert the chunks to vector embeddings, due to API limitations.

## Contributing
---------------

If you'd like to contribute to Anubhav.ai, please fork the repository and submit a pull request with your changes. You can also report issues or suggest new features by creating an issue in the repository.

## License
---------

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Acknowledgments
----------------

* [Flask](https://flask.palletsprojects.com/en/2.0.x/) for the web framework.
* [HTML, CSS, and JavaScript](https://www.w3.org/) for the user interface.
* [YouTube](https://www.youtube.com/) for video content.
* [PDF.js](https://mozilla.github.io/pdf.js/) for PDF viewing.
* [Vis.js](https://visjs.org/) for mindmap visualization.
* [Together.ai](https://api.together.ai/) for LLM API (Llama 3 and Llama 3.1)
* [Langchain](https://www.langchain.com/)
* [Ollama](https://ollama.ai/)

## Contact
---------

If you have any questions or need help with the chatbot, please contact [Your Name](mailto:your@email.com).
