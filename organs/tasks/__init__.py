from organs.tasks.tasks import Tasks

def greet(name: str) -> str:
    return f'Hi {name}!'

def web_search_summary(query: str) -> str:
    # Simulated web search summary — replace with real fetch later
    return f"""Top 3 results for '{query}':
1. Simulated summary: '{query}' is important because it relates to future tech.
2. Source: academic.example.com — Detailed exploration of '{query}' origins.
3. Community take: most users think '{query}' is game-changing."""

def summarize_research_goal(prompt: str) -> str:
    return f"""Goal: Understand and explore the topic: '{prompt}'
Summary: This research aims to gather insights, context, and potential use cases related to '{prompt}'.
Key Questions:
- What is '{prompt}' and why does it matter?
- Who is talking about it?
- What are the top 3 unknowns or controversies?
- How could it be applied in future systems?"""

def generate_followups(prompt: str) -> str:
    return f"""Follow-up queries for '{prompt}':
1. What are the latest advancements in {prompt}?
2. How are experts applying {prompt} in current projects?
3. What limitations or challenges exist in {prompt}-based systems?"""

def summarize_findings(result1: str, result2: str, result3: str) -> str:
    return f"""Synthesized Insight:
Based on the findings:
- {result1}
- {result2}
- {result3}

Combined, these suggest a broader understanding: '{result1.split(':')[-1].strip()}', built upon '{result2.split(':')[-1].strip()}', and shaped by the insight '{result3.split(':')[-1].strip()}'. This triangulates a clearer direction for deeper investigation."""

def deep_dive_research(prompt: str) -> str:
    tasks = setup_tasks()
    goal = tasks.run("summarize_research_goal", prompt)
    q = tasks.run("generate_followups", prompt).splitlines()[1:4]
    r1 = tasks.run("web_search_summary", q[0])
    r2 = tasks.run("web_search_summary", q[1])
    r3 = tasks.run("web_search_summary", q[2])
    summary = summarize_findings(r1, r2, r3)
    return f"{goal}\n\n{r1}\n\n{r2}\n\n{r3}\n\n{summary}"

def setup_tasks() -> Tasks:
    tasks = Tasks()
    tasks.register("greet", greet)
    tasks.register("web_search_summary", web_search_summary)
    tasks.register("summarize_research_goal", summarize_research_goal)
    tasks.register("generate_followups", generate_followups)
    tasks.register("summarize_findings", summarize_findings)
    tasks.register("deep_dive_research", deep_dive_research)
    return tasks
