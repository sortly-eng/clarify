# clarify

Two skills that make the agent ask before it codes:

- **feature**: give it an idea, designs or a spec; it builds a feature brief.
- **bug**: give it what's broken plus any evidence; it builds a bug brief.

Each one reads your designs and code first, then asks 3–10 questions, one at a time, and shows a confidence meter before every question:

```
Confidence  ██████░░░░  62%   ·  Question 4 of max 10
Goal ✓  Scope ✓  UI ◐  Data ✗  States ◐  Edge ✗  Placement ✓  Done ◐
```

It stops at 80% (after at least 3 questions), writes a brief, and waits for your yes before touching code.

## Install in Claude Code

```
/plugin marketplace add sortly-eng/clarify
/plugin install clarify@clarify-marketplace
```

Use it as `/clarify:feature <idea>` or `/clarify:bug <what's broken>`.

## Install in Codex

```
codex plugin marketplace add sortly-eng/clarify
```

Then install **Clarify** from the Plugins directory and ask for the `feature` or `bug` skill by name.

## Layout

```
.claude-plugin/plugin.json        Claude Code manifest
.claude-plugin/marketplace.json   Claude Code marketplace
.codex-plugin/plugin.json         Codex manifest
.agents/plugins/marketplace.json  Codex marketplace
skills/feature/SKILL.md           feature intake
skills/bug/SKILL.md               bug intake
```

## Tuning

Everything lives in the two `SKILL.md` files:

- **Dimensions and weights**: edit the table. Weights should add up to 100.
- **Stop threshold**: change `80` in the rules.
- **Question limits**: change `3` and `10` in the rules.

Bump `version` in both `plugin.json` files on every release, or users won't receive the update.
