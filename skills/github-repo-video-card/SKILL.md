---
name: github-repo-video-card
description: Turn a GitHub repository URL into a Chinese short-video package with repo analysis, real screenshots, screen copy, storyboard, optional cover prompt, and a HyperFrames-ready video plan. Use when the user asks to make a GitHub repo intro video, open-source project card video, Chinese repo explainer, GitHub tool sharing video, video cover, or gives a GitHub URL and wants a reusable short-video workflow.
---

# GitHub Repo Video Card

Use this skill to turn a public GitHub repository into a Chinese short-video package.

This open-source version focuses on a reusable workflow. It can produce the repo brief, screen copy, storyboard, screenshot plan, cover prompt, title, tags, and HyperFrames implementation direction. Final screenshot capture, image generation, and video rendering depend on the local tools available in the user's Codex environment.

## Core Principle

The viewer should quickly understand:

1. Which repository this is.
2. What the project does.
3. What problem it solves.
4. What the product or output looks like.
5. Why someone might save or try it.

Keep the video about the repository and the concrete result. Do not make the screen copy about internal agent steps.

## Inputs

At least one:

- GitHub repository URL.
- Repo slug such as `owner/repo`.
- A local analysis folder already created for a repository.

Optional:

- Target duration.
- Reference video or cover style.
- Existing screenshots.
- Music file.
- Whether to render a finished video or only prepare the package.

## Default Workflow

1. Check whether this repo has already been produced in `outputs/github_repo_cards/repo_index.md` if the file exists.
2. If the user asks you to find a repo, present 3-5 candidates first and wait for confirmation.
3. Read the README and visible project material.
4. Build a short repo brief:
   - repo path;
   - one-sentence identity;
   - main user;
   - concrete problem solved;
   - visible product/output;
   - main capabilities;
   - evidence source;
   - claims to avoid.
5. Capture or request real screenshots:
   - repo identity;
   - product/interface/result;
   - capability or demo evidence;
   - release/download/docs evidence if useful.
6. Write on-screen copy using `references/content-spec.md`.
7. Design the visual page using `references/visual-spec.md`.
8. Produce a storyboard using `templates/storyboard-template.md`.
9. If rendering is available, use HyperFrames or another local renderer to make a draft video.
10. Output one main Chinese title, optional backup titles, and compact tags.
11. Update `outputs/github_repo_cards/repo_index.md` when a publishable video is made.

## Candidate Selection

When Codex chooses the repo, do not start production immediately.

Give 3-5 options with:

- plain-language project explanation;
- why it may be worth filming;
- why it may be weak;
- visible material available;
- recommended pick.

If the user gives an exact URL or `owner/repo`, treat that as confirmation.

## Default Video Shape

For a vertical card video:

```text
Top: repo pill + short value title
Middle: real repo/product evidence panel
Bottom: designed Chinese explanation card with typewriter text
CTA: 找不到项目，评论区说一声
```

For a 16:9 explainer video:

```text
Presenter or screen recording remains the main visual.
Text and cards stay in side-safe zones.
Show the final result early if the video explains the workflow itself.
```

## Copy Rules

Use direct Chinese project explanation.

Good structure:

```text
<Project> 是一个 <类别/用途>，主要解决 <具体场景里的问题>。
你可以用它 <创建/管理/转换/自动化什么>。
它支持 <模型/文件/平台/工具/格式>。
最后产物可以 <调用/部署/导出/复用/接入业务>。
```

Avoid unsupported claims such as:

- 已实测
- 最强
- 必备
- 完整跑通
- 全自动

unless the current run truly verified them.

## Cover Guidance

If the user asks for a cover, generate a separate 3:4 cover prompt or image.

Default cover elements:

- owner / repo;
- large Chinese outcome headline;
- repo/product proof panel;
- star count, release, license, or category only if verified;
- compact CTA: `找不到项目，评论区说一声`.

For personal creator covers, the user should supply their own reference image. This open-source version does not include a person reference asset.

## Platform Safe Area

For 1080x1920 publish videos:

- top 110px: no critical repo/title text;
- bottom 300px: no critical CTA, tags, title, or explanation;
- footer text is optional and expendable.

## Deliverables

Planning package:

```text
drafts/YYYYMMDD-HHMMSS-owner-repo-video-card/
  00-repo-brief.md
  01-screen-copy.md
  02-storyboard.md
  03-screenshot-plan.md
  04-cover-prompt.md
  05-title-tags.md
```

Final package when rendering is available:

```text
outputs/github_repo_cards/
  cover/<repo-slug>-cover-3x4.png
  video/<repo-slug>_with_cover_1s.mp4
  <repo-slug>_repo_card.md
  repo_index.md
```

## Self-Review

Before reporting:

- repo name/path is visible;
- project purpose is understandable in one pass;
- screenshots show real evidence;
- screen text does not mention internal agent workflow;
- no important text is under platform overlay zones;
- cover facts are verified;
- final title and tags are included.

