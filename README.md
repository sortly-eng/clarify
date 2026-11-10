# clarify

Two skills that make the agent ask before it codes:

- **feature**: give it an idea, designs or a spec; it builds a feature brief.
- **bug**: give it what's broken plus any evidence; it builds a bug brief.

Each one reads your designs and code first, then asks 3–10 questions, one at a time, and shows a confidence meter before every question:

```
Confidence  █████░░░░░  57.5%   ·  Question 4 of max 10
Goal ✓  Scope ✓  UI ◐  Data ✗  States ◐  Edge ✗  Placement ✓  Done ◐
```

It stops at 80% (after at least 3 questions), writes a brief, and waits for your yes before touching code.

The percentage measures requirement completeness, not the probability of a correct implementation. Fractional scores are preserved, and each filled bar represents a completed 10%.

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
assets/icon.png                  shared listing and composer icon
PRIVACY.md                       plugin privacy policy
TERMS.md                         MIT-based terms of use
SUPPORT.md                       support instructions
scripts/package_openai.py        OpenAI submission ZIP builder
```

## OpenAI submission

Build the skills-only upload package with Python 3 (no additional dependencies):

```sh
python3 scripts/package_openai.py --output ../Clarify-0.2.1-OpenAI.zip
```

The ZIP contains the Codex manifest, both skills, the existing icon, and the public documentation. It excludes Git history, marketplace manifests, and packaging scripts. It contains no MCP server, app references, or lifecycle hooks.

The listing uses **Clarify by Sortly**, developer **Sortly**, and category **Developer Tools**. Select the matching verified publishing identity in Platform. Publish the source to `main` before uploading so the listing's [support](SUPPORT.md), [privacy](PRIVACY.md), and [terms](TERMS.md) URLs are accessible.

Upload the ZIP to the existing plugin draft using **Skills only**, then inspect the new metadata and skill-scan results. Local validation does not replace Platform checks or guarantee acceptance. See the [official submission guide](https://developers.openai.com/plugins/deploy/submission).

## Tuning

Everything lives in the two `SKILL.md` files:

- **Dimensions and weights**: edit the table. Weights should add up to 100.
- **Stop threshold**: change `80` in the rules.
- **Question limits**: change `3` and `10` in the rules.

Bump `version` in both `plugin.json` files on every release, or users won't receive the update.
