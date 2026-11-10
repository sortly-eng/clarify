# clarify

Two commands that make the agent ask before it codes:

- `/feature <idea + designs/spec>`: builds a feature brief.
- `/bug <what's broken + evidence>`: builds a bug brief.

Each one reads your designs and code first, then asks 3–10 questions, one at a time, and shows a confidence meter before every question:

```
Confidence  ██████░░░░  62%   ·  Question 4 of max 10
Goal ✓  Scope ✓  UI ◐  Data ✗  States ◐  Edge ✗  Placement ✓  Done ◐
```

It stops at 80% (after at least 3 questions), writes a brief, and waits for your yes before touching code.

## Install in Claude Code

```
/plugin marketplace add ./clarify
/plugin install clarify@clarify-marketplace
```

Push the folder to a GitHub repo to share it, then teammates run
`/plugin marketplace add <owner>/<repo>`.

Use it as `/feature …` or `/clarify:feature …`.

## Install in Codex

Codex reads custom prompts from `~/.codex/prompts/`. The same files work there:

```
mkdir -p ~/.codex/prompts
cp clarify/commands/*.md ~/.codex/prompts/
```

Use it as `/prompts:feature …` and `/prompts:bug …`.

## Tuning

Everything lives in the two Markdown files:

- **Dimensions and weights**: edit the table. Weights should add up to 100.
- **Stop threshold**: change `80` in the rules.
- **Question limits**: change `3` and `10` in the rules.
