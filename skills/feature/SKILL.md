---
name: feature
description: Use when the user wants to build a new feature from an idea, designs or a spec. Asks 3–10 scored clarifying questions with a confidence meter, then writes a feature brief before any code.
---

# Feature intake

The feature to build is whatever the user described when invoking this skill, along with any designs, specs or links they attached. If they gave nothing, ask what they want to build first.

Do not write or change any code until the brief at the end is approved.

## 1. Gather context first

Before asking anything, read what is already available:

- Designs, screenshots, specs or links the user gave.
- The relevant parts of the codebase: similar components, routing, state management, API clients, styling conventions, tests.

Anything you can answer from this context, answer yourself. Do not ask the user for it.

## 2. Score your understanding

Rate each dimension `✗` unknown (0), `◐` partial (0.5) or `✓` clear (1).

| Dimension      | Weight | Clear means you know…                                        |
| -------------- | ------ | ------------------------------------------------------------ |
| Goal           | 15     | who it is for and what problem it solves                     |
| Scope          | 15     | what is in, and what is explicitly out                       |
| UI / design    | 15     | layout, components, responsive behaviour, design source      |
| Data / API     | 15     | where data comes from, its shape, and what gets saved        |
| States         | 10     | loading, empty, error and success states                     |
| Edge cases     | 10     | permissions, limits, bad input, slow network                 |
| Placement      | 10     | which files or modules it lives in, and what it reuses       |
| Done when      | 10     | acceptance criteria and how it will be tested                |

Confidence = sum of (score × weight). It is out of 100. Keep fractional values (for example, 57.5%) instead of rounding the numeric score. This measures how complete the available requirements are, not the probability that a plan or fix is correct.

## 3. Ask questions

Rules:

- Ask **one question at a time**, aimed at the dimension that adds the most confidence.
- Ask **at least 3** and **at most 10** questions.
- Stop once confidence is **80 or more**, but only after the 3rd question.
- When a question has likely answers, offer 2–4 options (use a multiple-choice question tool if you have one) and suggest a default.
- Re-score after every answer. Never raise a score without a reason from the answer or the code.

Start every question with the meter:

```
Confidence  █████░░░░░  57.5%   ·  Question 4 of max 10
Goal ✓  Scope ✓  UI ◐  Data ✗  States ◐  Edge ✗  Placement ✓  Done ◐
```

The bar has 10 blocks. Fill `floor(confidence / 10)` blocks and leave the rest empty; the numeric percentage shows the exact score.

## 4. Write the brief

When you stop, show the final meter, then:

- **Summary**: one or two sentences.
- **In scope / out of scope**
- **UI and states**
- **Data and API**
- **Files to create or change**
- **Acceptance criteria**: a checklist.
- **Open risks**: anything still `◐` or `✗`, with the assumption you will make.

Then ask: "Build this?" Only start coding after a yes.
