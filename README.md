# LangChain Learning Journey

My personal documentation and hands-on projects while learning LangChain - from basic concepts to building production-ready AI applications.

## 📚Project Structure

```
langchain-learning/
├── chains/                      # LangChain Chain Implementations
│   ├── simple_chain.py         # Basic chain with single LLM call
│   ├── sequential_chain.py     # Sequential execution of multiple chains
│   ├── parallel_chain.py       # Parallel chain execution
│   └── conditional_chain.py    # Conditional logic and branching
│
├── Langchain_prompts/          # Prompt Engineering & Templates
│   ├── chat_prompt_template.py # Chat-based prompt templates
│   ├── chatbot.py              # Interactive chatbot implementation
│   ├── messages.py             # Message handling and formatting
│   ├── message_placeholder.py  # Dynamic message placeholders
│   ├── prompt_generator.py     # Automated prompt generation
│   ├── prompt_ui.py            # UI for prompt experimentation
│   ├── chat_history.txt        # Sample chat histories
│   └── template.json           # Prompt template configurations
│
├── output_parsers/             # Output Parsing Techniques
│   ├── stroutputparser.py      # String output parsing
│   ├── stroutputparser1.py     # Alternative string parser
│   ├── jsonoutputparser.py     # JSON format parsing
│   ├── pydanticoutputparser.py # Type-safe Pydantic parsing
│   └── structuredoutputparser.py # Structured data extraction
│
├── structured_output/          # Structured Data Generation
│   ├── with_structured_output_json.py      # JSON schema output
│   ├── with_structured_output_pydantic.py  # Pydantic models
│   ├── with_structured_output_typeddict.py # TypedDict approach
│   ├── pypdantic_demo.py       # Pydantic demonstrations
│   ├── typeddict_demo.py       # TypedDict examples
│   └── json_schema.json        # JSON schema definitions
│
├── requirements.txt            # Python dependencies
├── .env.example               # Environment variables template
└── .gitignore                 # Git ignore rules
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- OpenAI API Key 
- Google API Key for Gemini 

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/octavian115/langchain_learning.git
cd langchain_learning
```

2. **Create and activate virtual environment**
```bash
python -m venv .venv
source .venv/bin/activate  # On Mac/Linux
# OR
.venv\Scripts\activate     # On Windows
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
```bash
cp .env.example .env
# Edit .env and add your API keys
```

## 📖 Learning Progress

### ✅ Completed Topics

#### Chains
- [x] **Simple Chains** - Basic LLM chain implementations
- [x] **Sequential Chains** - Chaining multiple operations in sequence
- [x] **Parallel Chains** - Concurrent chain execution for efficiency
- [x] **Conditional Chains** - Branching logic based on conditions

#### Prompts
- [x] **Prompt Templates** - Reusable prompt structures
- [x] **Chat Prompts** - Conversation-style prompting
- [x] **Message Handling** - Managing chat messages and history
- [x] **Prompt Engineering** - Optimizing prompts for better results

#### Output Parsing
- [x] **String Parsers** - Basic text output handling
- [x] **JSON Parsers** - Structured JSON extraction
- [x] **Pydantic Parsers** - Type-safe output validation
- [x] **Structured Output** - Complex data structure generation

### 🔄 Currently Learning

- [ ] **Agents** - Autonomous decision-making systems
- [ ] **Tools** - Integrating external tools and APIs
- [ ] **Memory Systems** - Conversation history and context retention

### 📋 Upcoming Topics

- [ ] **Vector Stores** - Embeddings and semantic search
- [ ] **RAG (Retrieval Augmented Generation)** - Document-based Q&A
- [ ] **LangGraph** - Complex workflow orchestration
- [ ] **LangSmith** - Debugging and monitoring
- [ ] **Production Deployment** - Scaling and optimization

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| **LangChain** | Framework for building LLM applications |
| **OpenAI GPT** | Primary language model (GPT-3.5/GPT-4) |
| **Google Gemini** | Alternative LLM provider |
| **Pydantic** | Data validation and parsing |
| **Python-dotenv** | Environment variable management |

## 💡 Key Learnings

### Chains
- Understanding when to use sequential vs parallel chains
- Implementing conditional logic for dynamic workflows
- Optimizing chain performance

### Prompts
- Crafting effective prompts for different use cases
- Managing conversation context and history
- Using templates for consistency

### Output Parsing
- Ensuring reliable structured output from LLMs
- Type safety with Pydantic models
- Handling parsing errors gracefully

## 📝 Usage Examples

### Running a Simple Chain
```bash
python chains/simple_chain.py
```

### Testing Output Parsers
```bash
python output_parsers/pydanticoutputparser.py
```

### Experimenting with Prompts
```bash
python Langchain_prompts/chatbot.py
```

## 🔐 Security Note

- **Never commit `.env` files** with actual API keys
- Use `.env.example` as a template only
- Keep your API keys secure and rotate them regularly
- Add `.env` to `.gitignore` (already configured)

## 📚 Resources

- [LangChain Documentation](https://python.langchain.com/docs/get_started/introduction)
- [LangChain Cookbook](https://github.com/langchain-ai/langchain/tree/master/cookbook)
- [OpenAI API Docs](https://platform.openai.com/docs)

## 🤝 Contributing

This is a personal learning repository, but feedback and suggestions are welcome! Feel free to:
- Open issues for questions or discussions
- Suggest improvements or corrections
- Share your own learning experiences

## 📄 License

MIT License - Feel free to use this for your own learning journey!

## 🌟 Acknowledgments

- LangChain team for the amazing framework
- OpenAI and Google for providing powerful LLM APIs
- The AI community for sharing knowledge and best practices

---

**⭐ If you find this helpful for your own LangChain learning journey, consider starring the repo!**

*Last Updated: February 2026*
