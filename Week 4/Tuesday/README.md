# 🔎 Visibility Tools in LLM Ops

# 📚 Background

### Langsmith

LangChain makes it easy to prototype LLM applications and Agents. However, delivering LLM applications to production can be deceptively difficult. You will likely have to heavily customize and iterate on your prompts, chains, and other components to create a high-quality product. LangSmith is a unified platform for debugging, testing, and monitoring your LLM applications.

Langsmith can be useful when you want to:
- Quickly debug a new chain, agent, or set of tools
- Visualize how components (chains, llms, retrievers, etc.) relate and are used
- Evaluate different prompts and LLMs for a single component
- Run a given chain several times over a dataset to ensure it consistently meets a quality bar
- Capture usage traces and using LLMs or analytics pipelines to generate insights

### Weight and Biases Prompts
W&B Prompts is a suite of LLMOps tools built for the development of LLM-powered applications. Use W&B Prompts to visualize and inspect the execution flow of your LLMs, analyze the inputs and outputs of your LLMs, view the intermediate results and securely store and manage your prompts and LLM chain configurations.

**Trace Table** -  provides an overview of the inputs and outputs of a chain, the composition of a trace event in the chain, whether or not the chain ran successfully, and any error messages returned when running the chain.

**The Trace Timeline** - displays the execution flow of the chain and is color-coded according to component types. 

**Model Architecture** - provides details about the structure of the chain and the parameters used to initialize each component of the chain.



# Working session

## 🏗️ Build

Your assignment has one task:
- Extend any previous assignment (or new application) built with LangChain (or Llama Index) to include Weights and Biases tracing

## 🚢 Ship

Host your application on a Hugging Face Space!

## 🚀 Share

Share screenshots of your visibility tools outputs and explain (in your own words) what the use cases of visibility tooling are!


We'll be looking at two different visibility tools during this session:

1. [LangSmith](https://python.langchain.com/docs/guides/langsmith/walkthrough)
2. [Weights and Biases](https://docs.wandb.ai/guides/prompts)

Currently, LangSmith is in closed beta - you can request access [here](https://smith.langchain.com/) - we'll demo how to use it and what it can do, but we'll focus on Weights and Biases for the assignment.


### Environment Notices

We'll be using Python 3.11 as the base environment today.

You'll need to `pip install`:

- `wandb`
- `langchain`
- `langsmith` (if you have closed beta access)
- `openai`
- `jupyter`

### Weights and Biases API Key

You will need to have a Weights and Biases API key, which you can obtain following these instructions:

1. Create a Weights and Biases account.
2. Navigate to your `User Settings`

![image](https://i.imgur.com/oRRj40x.png)

3. Take the highway to (navigate to) the `Danger Zone`

![image](https://i.imgur.com/XBrOyfG.png)

4. Copy your new API key!








