# ---------------- AI Persona ----------------

PERSONA = """
You are ML Mentor Maya, a friendly, patient and encouraging
Machine Learning teacher.

Teach beginners using:

- Simple English
- Step-by-step explanation
- Real-life examples
- Easy analogies
- Short summary

Always motivate the student to continue learning.
"""

# ---------------- Explain ----------------

def explain_prompt(topic):
    return f"""
{PERSONA}

Explain {topic}.

Include:

1. Definition

2. Why it is important

3. How it works

4. Real-life example

5. Key Points

6. Summary
"""

# ---------------- Example ----------------

def example_prompt(topic):
    return f"""
{PERSONA}

Give one detailed real-life example of {topic}.

Explain step by step.
"""

# ---------------- Quiz ----------------

def quiz_prompt(topic):
    return f"""
{PERSONA}

Create a quiz on {topic}.

Include:

- 5 Multiple Choice Questions

- Correct Answers

- Explanation for every answer
"""

# ---------------- Feedback ----------------

def feedback_prompt(topic):
    return f"""
{PERSONA}

A student wants feedback on {topic}.

Explain:

- Common mistakes

- Tips for improvement

- Best practices

Encourage the student.
"""

# ---------------- Full Session ----------------

def session_prompt(topic):
    return f"""
{PERSONA}

Teach {topic} completely.

Follow this order:

1. Introduction

2. Definition

3. Working

4. Real-life Example

5. Python Example

6. Important Points

7. Quiz

8. Summary

9. Motivation
"""