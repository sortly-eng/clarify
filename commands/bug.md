---
description: Pin down a bug through scored questions before changing any code
argument-hint: <what is broken, plus screenshots, logs or a link to the ticket>
---

# Bug intake

The user reports:

$ARGUMENTS

Do not change any code until the brief at the end is approved.

## 1. Gather context first

Before asking anything, read what is already available:

- Screenshots, logs, stack traces, ticket text or links the user gave.
- The code paths involved: the component, its hooks and state, the API calls, recent changes (`git log` on the touched files).

Anything you can answer from this context, answer yourself. Do not ask the user for it.

## 2. Score your understanding

Rate each dimension `✗` unknown (0), `◐` partial (0.5) or `✓` clear (1).

| Dimension    | Weight | Clear means you know…                                         |
| ------------ | ------ | ------------------------------------------------------------- |
| Symptom      | 15     | exactly what the user sees                                    |
| Expected     | 15     | what should happen instead                                    |
| Repro steps  | 20     | the steps that reproduce it, every time or how often          |
| Environment  | 10     | browser, device, account or role, feature flags, build        |
| Evidence     | 15     | errors, logs or network responses that point to a cause       |
| Regression   | 10     | whether it used to work, and since when                       |
| Location     | 10     | the files or modules most likely at fault                     |
| Fix scope    | 5      | what must not change, and how the fix will be verified        |

Confidence = sum of (score × weight). It is out of 100.

## 3. Ask questions

Rules:

- Ask **one question at a time**, aimed at the dimension that adds the most confidence.
- Ask **at least 3** and **at most 10** questions.
- Stop once confidence is **80 or more**, but only after the 3rd question.
- When a question has likely answers, offer 2–4 options (use a multiple-choice question tool if you have one) and suggest a default.
- Re-score after every answer. Never raise a score without a reason from the answer or the code.

Start every question with the meter:

```
Confidence  █████░░░░░  50%   ·  Question 3 of max 10
Symptom ✓  Expected ✓  Repro ◐  Env ✗  Evidence ◐  Regression ✗  Location ◐  Scope ✗
```

The bar has 10 blocks, one per 10%.

## 4. Write the brief

When you stop, show the final meter, then:

- **Summary**: one sentence.
- **Repro steps**: numbered.
- **Expected vs actual**
- **Likely cause**: your best hypothesis, with the evidence for it.
- **Files to change**
- **Fix plan**: the smallest change that fixes the cause, not the symptom.
- **Verification**: a failing test to add first, plus manual checks.
- **Open risks**: anything still `◐` or `✗`, with the assumption you will make.

Then ask: "Fix this?" Only start changing code after a yes.
