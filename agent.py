from langchain_anthropic import ChatAnthropic
from langgraph.graph import END, StateGraph, MessagesState

model = ChatAnthropic(model="claude-3-5-sonnet-20240620")

graph_workflow = StateGraph(MessagesState)


def agent(state: MessagesState):
    response = model.invoke(state["messages"])
    return {"messages": [response]}


graph_workflow.add_node(agent)
graph_workflow.add_edge("agent", END)
graph_workflow.set_entry_point("agent")

graph = graph_workflow.compile()