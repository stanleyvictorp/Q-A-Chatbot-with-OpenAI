# LinKer - LinkedIn Connection Request Message Creator

LinKer is a Streamlit-based web application that helps you create personalized LinkedIn connection request messages. By leveraging OpenAI's powerful language models, you can generate messages that are humble and professional, tailored to the person's name and bio.

## Features

- Simple and intuitive interface
- Customize OpenAI model, temperature, and max tokens
- Generates LinkedIn connection request messages with a focus on humility and professionalism

## Installation

1. **Clone the Repository**

   ```sh
   git clone https://github.com/your-username/linkedin-message-creator.git
   cd linkedin-message-creator
   ```

2. **Create and Activate a Virtual Environment**

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the Required Packages**

   ```sh
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**

   Create a `.env` file in the root directory of your project and add your OpenAI API key and Langchain API key:

   ```sh
   OPENAI_API_KEY=your_openai_api_key
   LANGCHAIN_API_KEY=your_langchain_api_key
   ```

## Usage

1. **Run the Streamlit App**

   ```sh
   streamlit run app.py
   ```

2. **Configure the Settings**

   - Enter your OpenAI API key in the sidebar.
   - Select the desired OpenAI model (`gpt-3.5-turbo`, `gpt-4`, `gpt-4-turbo`).
   - Adjust the temperature and max tokens as needed.

3. **Generate LinkedIn Messages**

   - Enter the name and bio of the person you want to connect with.
   - Click "Generate" to create a personalized LinkedIn connection request message.

## Project Structure

```
linkedin-message-creator/
│
├── .env                 # Environment variables
├── .gitignore           # Git ignore file
├── app.py               # Main Streamlit app
├── requirements.txt     # List of dependencies
└── README.md            # Project documentation
```

## Example

Here's how the app interface looks:

- **Sidebar**: Enter your OpenAI API key, select the model, adjust the temperature and max tokens.
- **Main Interface**: Enter the person's details (name and bio), and generate the message.


## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.


## Acknowledgments

- Thanks to [Streamlit](https://www.streamlit.io/) for the fantastic framework.
- Special thanks to [OpenAI](https://www.openai.com/) for providing powerful language models.

