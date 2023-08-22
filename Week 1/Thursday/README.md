# Questioning Barbie and Oppenheimer Through the Use of Agents

In the following notebook we will build an application that queries both the Barbie and Oppenheimer movies Wikipedia pages, as well as their reviews. 

The main focus of this notebook is to showcase a brief introduction to Agents.

## Build 🏗️

There are 3 main tasks in this notebook:

1. Construct a Barbie retriever
2. Construct an Oppenheimer retriever
3. Combine the two and allow users to query both resources from a single input through the use of Agents

## Ship 🚢

Based on Tuesday's session - construct a Chainlit (or Gradio) application that allows users to interface with the application.

## Share 🚀

Make a social media post about your final application.

## System Architecture Diagrams

### ReAct Agents

We'll condense the RAQA diagram into a single component.

![image](https://i.imgur.com/LqIln4g.png)

Now, let's look at the Agent diagram (in a slightly simplified diagram to avoid arrow-pocolypse)

![image](https://i.imgur.com/H55v09C.png)

### Ensemble Retrieval

[`EnsembleRetriever`](https://api.python.langchain.com/en/latest/retrievers/langchain.retrievers.ensemble.EnsembleRetriever.html#langchain.retrievers.ensemble.EnsembleRetriever)

Leverages the [RRF](https://plg.uwaterloo.ca/~gvcormac/cormacksigir09-rrf.pdf) reranking algorithm to combine sparse and dense search results for increased effectiveness for relevant document retrieval.

![image](https://i.imgur.com/mn4jXAz.png)

### Multi-query Retrieval

We can query multiple sources and then allow the LLM to parse the results from both in order to decide the final answer. 

![image](https://i.imgur.com/g3vGp4P.png)

