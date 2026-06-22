# Visual Spec

Use this when designing the HTML/HyperFrames/Remotion visual draft.

## Layout

Default 9:16 vertical layout:

```text
Top safe margin: first 110px should not carry critical text
Top 18-25%: title block
Middle 24-34%: real evidence panel / screenshot carousel
Bottom content 35-40%: written explanation card
Bottom safe margin: last 300px reserved for platform overlays
Footer: optional non-essential repo label only
```

The top title may start large and then move/scale to the upper area. This motion should create a video feel, not obscure the screenshot.

## Proven Card Layout

For the short "repo card" format, prefer:

```text
Top:
  repo pill
  1-2 line value title

Middle:
  browser-like panel with URL bar
  evidence scenes: address -> GUI -> demo/example -> release/download
  blue badge naming current evidence scene

Bottom:
  card header
  optional flow pill
  inner explanation box
  typewriter text
  compact tags
```

Good middle-scene examples:

- address card: `github.com/owner/repo` plus 4 meta tiles;
- GUI card: real app interface screenshot;
- demo card: one main example image plus two smaller evidence images;
- release card: package/download rows.

For process/workflow scenes, build a small semantic flow diagram over the real screenshot or repo evidence. Pick icons by meaning for this repo, such as video/play for video input, CC/caption lines for subtitles, microphone/sound waves for dubbing or audio API, file/page for document input, table/grid for data, and export/share for outputs. The icon choice should explain the step, not repeat a fixed template.

Process icons must look like finished explanatory UI, not placeholder marks. Avoid using only loose dots, a single bent line, or generic blocks for a step. Each icon should include at least:

- a clear object, such as file, chat bubble, table, graph node, browser window, terminal, database, report, audio wave, or image;
- a visible action/state, such as import, parse, connect, search, compare, generate, export, sync, or validate;
- a small result cue, such as rows extracted, linked nodes, highlighted answer, check mark, exported file, or returned card.

If a simple symbol is too vague at phone size, replace it with a compact mini-card illustration that combines icon + 1-2 detail marks. Treat workflow icons as explanation, not decoration.

Use star count, release version, license, output format, and core-result labels as small evidence chips. Keep them compact, left or bottom aligned, with lower visual weight than the screenshot and process labels. Avoid making these facts into three wide equal cards unless the whole scene is specifically a metrics card.

If a repo has a demo video, screenshots/GIFs, example outputs, Releases, or docs images, use those as middle evidence instead of leaving one static screenshot on screen.

Background direction:

- light document/workbench canvas works well for tool/document repos;
- use soft paper layers, mild shadows, and limited blue/green accents;
- keep screenshot/evidence panels high contrast enough to read.

## Platform Overlay Safe Area

For Xiaohongshu/Douyin-style publishing, design against the platform overlay, not only the raw exported frame.

In 1080x1920 videos:

- Keep critical content out of the top `0-110px` zone. Phone time/status icons can cover repo pills or title text.
- Keep critical content out of the bottom `1620-1920px` zone. Platform title, AI prompt/search chips, progress bar, and action buttons can cover it.
- Do not place CTA, tags, repo slug, or subtitle-like title text at the very bottom of the video.
- Put the weak CTA and compact tags as separate standalone chips in the empty band directly under the explanation card. Keep the whole CTA/tag row above `1620px`; around `1500-1605px` works well when the bottom card ends above it.
- If a small footer remains, it must be expendable. The viewer should lose no meaning if the platform UI covers it.
- QA should include at least one screenshot with a simulated bottom overlay or a real platform preview screenshot when available.

## Cover Layout

When producing a cover for the repo-card video, use a 3:4 cover image. When it is used as the one-second 9:16 video lead-in, center the full cover and fill the remaining vertical frame with a blurred/enlarged copy of the same cover.

Treat `3:4` as a measured output constraint, not a prompt wish. Before accepting a cover, run `sips -g pixelWidth -g pixelHeight cover.png`. The ratio must be within `0.748-0.752` width/height; common accepted outputs are `1086x1448`, `1024x1365`, and `1200x1600`. Regenerate any `1024x1536` / `2:3` result before video assembly.

Default composition:

```text
Small side/front: optional creator reference supplied by the user, used as account identity rather than the main poster subject
Main area: GitHub repo card + product/result motif
Headline: huge 2-line outcome
Badges: repo label, category/proof, output/file type, comment keyword
```

Keep the person modest on tool-card covers: around 18-24% of cover width and below roughly one quarter of visual weight. The tool/result should remain the first visual signal.

The person still needs to be part of the poster space. Use overlap and depth: title blocks, screenshot edges, repo cards, arrows, icons, glow, and the person can partially occlude one another. The good default is an integrated thumbnail where the creator is woven into the evidence scene and shares the same visual system as the project content.

If the user provides a cover-style reference, use it as the composition language. Otherwise use a generic integrated tech-thumbnail structure: large outcome headline, real repo/product proof, optional small creator identity, layered overlap, and compact CTA.

Treat the reference's person placement as one example of the broader composition language. Vary the creator's location and pose between covers so the person appears integrated into each project's specific content scene.

For document/tool repos, the background can show the transformation visually: input file -> core tool/module -> output file. Keep cover text much larger than in-video text.

Only put facts on the cover that are already verified from the repo or source. If star count, release number, license, or benchmark is not verified in this run, use a category badge such as `开源工具` instead.

## Screenshot Treatment

Use screenshot as evidence.

Repo scene:

- crop to top-left repo identity area;
- show `owner / repo`;
- keep Code tab and first file rows if useful;
- avoid right-side About/Releases unless star count or description is the point.

Product scene:

- show actual app UI;
- remove README section titles and surrounding webpage clutter;
- crop to the UI area and preserve key controls.

Capability scene:

- crop to the feature panel being discussed;
- use a focused crop rather than a full long screenshot.

## Motion Patterns

Good patterns:

- title enters large, then scales/moves to top;
- screenshot slides or zooms into frame;
- repo name region can briefly zoom in;
- bullets reveal one by one;
- bottom explanation types in character by character;
- evidence panel switches every 2.5-3.5 seconds in a 12-15 second card;
- a single purposeful callout frame points to a feature;
- screenshot transitions cleanly: old image out, new image in.

Avoid:

- overlapping screenshots during transitions;
- random boxes or arrows;
- fake mobile status bars;
- multiple decorative widgets on top of product screenshots;
- full-page screenshots too small to read.

## Annotation Rules

Only annotate when the viewer could miss the important feature.

Good labels:

```text
助手列表
对话区
模型设置
MCP 工具
仓库路径
```

Bad labels:

```text
核心价值
能力汇聚
边界说明
收尾判断
```

## Music

Music is optional.

- If user provides a track, add it as a separate audio layer.
- If no track is provided, reserve a placeholder and state it is pending.
- Do not use copyrighted platform audio without permission.

## QA Frames

Preview at least:

- title-only intro;
- repo scene with repo path visible;
- product scene with UI visible;
- capability scene;
- bottom explanation complete with highlighted keywords;
- cover first frame if a cover lead-in is included;
- first frame after the cover handoff;
- final scene.

Check no text or screenshots are cropped in a way that breaks meaning.
