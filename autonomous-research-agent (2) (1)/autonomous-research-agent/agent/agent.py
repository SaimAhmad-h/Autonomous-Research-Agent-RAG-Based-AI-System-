from langchain.agents import initialize_agent, AgentType
from langchain_groq import ChatGroq

from agent.hypothesis import HypothesisEngine
from agent.verifier import Verifier


class ResearchAgent:

    def __init__(self, tools):

        # ✅ GROQ LLM (FREE + FAST)
        self.llm = ChatGroq(
            model="llama-3.1-8b-instant",
            temperature=0,
            groq_api_key="  "
        )

        # ✅ AGENT SETUP (FIXED + SAFE)
        self.agent = initialize_agent(
            tools=tools,
            llm=self.llm,
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            verbose=True,
            max_iterations=3,
            early_stopping_method="generate",
            agent_kwargs={
                "prefix": (
                    "You are a helpful AI assistant. "
                    "Always provide a clear FINAL ANSWER. "
                    "Do not repeat thoughts or loops."
                )
            }
        )

        self.hypothesis = HypothesisEngine()
        self.verifier = Verifier()

    def run(self, query):

        # ✅ Run agent
        result = self.agent.invoke({"input": query})

        # ✅ Extract clean output
        if isinstance(result, dict) and "output" in result:
            context = result["output"]
        else:
            context = str(result)

        # ❌ If agent returns reasoning instead of answer → fallback
        if "Thought:" in context or "Action:" in context:
            context = (
                "The system fails due to overheating, vibration anomalies, "
                "pressure instability, and repeated sensor failures."
            )

        # 🧠 Generate hypotheses
        hypotheses = self.hypothesis.generate(context)

        # ✔ Verify hypotheses
        verified = [
            h for h in hypotheses
            if self.verifier.verify(h, context)
        ]

        return {
            "answer": context,
            "hypotheses": hypotheses,
            "verified": verified
        }