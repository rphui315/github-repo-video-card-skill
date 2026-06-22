# Content Spec

Use this when writing on-screen text for a GitHub repo intro video.

## Content Order

For a 30-60 second intro, use 4 scenes:

1. **Repo identity**
   - `owner / repo`
   - what the project is
   - why it matters
2. **Product result**
   - what it becomes after use
   - what the main interface shows
3. **Capabilities**
   - what features/services/tools it brings together
   - how the user would use them
4. **Concrete outcome**
   - what work becomes easier
   - who should care
   - conservative next action

## Title Formula

Good:

```text
Cherry Studio：把 AI 工具做成桌面工作台
LiteDoc：本地 PDF 转 Markdown，不烧 token
CopilotKit：给 Agent 生成实时交互界面
```

For every final publishable video, output:

- one main title;
- 2-3 backup titles when useful;
- a compact tag set, usually 10-16 tags.

Tags should mix:

- platform/source: `#GitHub`;
- project name;
- category: `#AI工具`, `#开源项目`, `#效率工具`;
- concrete capability/use case: e.g. `#RAG`, `#Agent`, `#PDF转PPT`, `#自动化工作流`;
- audience or deployment angle when relevant: e.g. `#程序员工具`, `#一人公司`, `#自托管`.

Avoid:

```text
先解决入口分散
工具链可以接起来
值不值得看
边界说明
```

## Bottom Card Formula

Each scene uses one note line plus 3-4 bullets.

Example:

```text
GitHub：CherryHQ / cherry-studio

Cherry Studio 是开源 AI 桌面客户端。
它把常用 AI 能力放进一个桌面工作台。
仓库里能看到项目代码和功能说明。
适合想统一管理 AI 工具的人。
```

For the short repo-card format, one typed paragraph can replace bullets:

```text
MinerU2PPT是一个开源PDF/图片转PPT工具。它借助MinerU提取文档结构，再重建文字、图片和布局，输出可继续编辑的.pptx。适合报告、课件、论文资料和培训文档整理。
```

Preferred paragraph structure:

```text
<Project> 是一个 <类别/用途>，主要解决 <具体场景里 A/B/C 分散、重复、难落地、难维护的问题>。
你可以用它 <创建/管理/转换/自动化什么>。
它支持 <模型/文件/平台/工具/格式>。
最后产物可以 <调用/部署/导出/复用/接入业务>。
```

This keeps the pain point in the explanation without turning it into a spoken opener. For example:

```text
Dify是一个开源AI应用搭建平台，主要解决AI应用从原型到上线时，模型接入、知识库、Agent、工作流和部署分散的问题。你可以在里面创建聊天助手、知识库问答、Agent和工作流应用，接入OpenAI、Claude、Gemini或本地模型，把PDF、网页、文档做成RAG知识库。搭好的应用可以通过API调用，也可以自托管部署到自己的业务里。
```

Format this paragraph as a designed card:

- header: `项目说明`;
- optional compact flow pill: `输入 -> 中间结构 -> 输出`;
- inner text box with a left accent line;
- typewriter reveal over most of the video duration, character by character. Do not reveal whole paragraphs one by one in the default repo-card style;
- weak CTA line: `找不到项目，评论区说一声`;
- tags for input/output/interface/batch/integration.

Keyword color guidance:

- blue: project name, source/input category, dependency/tool names;
- green: output, result, reconstructed structure, editable file type;
- soft highlight: use cases or target work scenarios.

Product scene:

```text
产品界面：助手 + 对话 + 任务区

收进桌面后，就是一个工作区。
左侧固定助手和功能入口。
中间直接对话、写作、翻译、处理文档。
常用任务不用重新打开一堆网页。
```

## Language Rules

- Screen text should be written and concrete.
- Narration can be more conversational, but screen text should not sound like spoken filler.
- Prefer "X 是什么 / 能做什么 / 结果是什么".
- Prefer direct problem-solving definitions over setup phrases. Put the problem solved inside the first sentence.
- Avoid negative contrast formulas unless necessary.
- Avoid unsupported claims such as "已实测", "完整跑通", "最强", "必备".

## Replacement Checklist

Before accepting copy, ask:

- Can a stranger tell what this project is?
- Can they tell what changes after using it?
- Does each bullet name a concrete feature or outcome?
- Is any line only there because it sounds cool?
- Does it mention internal agent workflow? If yes, delete it.
