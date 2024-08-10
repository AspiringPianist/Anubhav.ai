# Anubhav.ai Chatbot
======================

## Overview
-----------

Anubhav.ai is a chatbot with media viewer capabilities, built using HTML, CSS, JavaScript, and Flask. The chatbot allows users to interact with it, create mindmaps, take quizzes, and view media content such as YouTube videos and PDF documents.

## Features
------------

* **Chatbot functionality**: Engage in conversations with the chatbot, ask questions, and receive responses.
* **Mindmap creation**: Create mindmaps on specific topics using the `/Mindmap` command.
* **Quiz creation**: Generate quizzes on specific topics using the `/QuizCreate` command.
* **Media viewer**: View YouTube videos and PDF documents in the media viewer, by just `pasting link directly in the input field`.
* **Chat history**: View previous conversations with the chatbot.
* **Media selector**: Select and view previous media content, like generated mindmaps or uploaded documents and videos.
* **Chat Folders**: Organize your chat sessions, by storing them in different folders, each with their own vector store for RAG. They are titled by your first message to chatbot.

## How to Use
--------------

### Running the Chatbot

1. Run the Flask application using `app.py`.
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
* The user interface is built using HTML, CSS, and JavaScript.
* Mindmaps are created using an external API.
* Quizzes are generated based on user input and stored in a database.
* Media content is displayed using embedded YouTube videos and PDF viewers.

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

## Contact
---------

If you have any questions or need help with the chatbot, please contact [Your Name](mailto:your@email.com).
