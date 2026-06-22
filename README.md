# GitHub Repo Video Card Skill

一个实验性的 Codex Skill，用来把 GitHub 开源项目整理成中文短视频包。

它把制作 GitHub 项目介绍视频时反复做的事情收拢起来：选题判断、README 提炼、截图计划、中文说明、分镜、封面提示词、标题和标签。

## What It Does

输入一个 GitHub 仓库地址，Skill 会引导 Codex 输出：

- 项目用途说明
- 项目适不适合做短视频的判断
- 需要截取哪些真实页面
- 中文屏幕文案
- 竖屏卡片视频分镜
- 3:4 封面提示词
- 视频标题和标签
- 可选 HyperFrames 制作方向

如果你的本地 Codex 环境有截图、图像生成和 HyperFrames 渲染能力，也可以继续把它做成视频。

## Demo

这个仓库主分支只放轻量预览图。完整 MP4 放在 GitHub Releases，避免仓库变成素材库。

封面预览：

![Demo cover](docs/assets/demo-cover.png)

多个封面样例：

![Cover samples](docs/assets/demo-cover-samples.jpg)

成片预览：

![Demo video preview](docs/assets/demo-preview.gif)

完整视频：

- [Watch / download demo video](https://github.com/rphui315/github-repo-video-card-skill/releases/tag/v0.1-demo)
- [Direct MP4 download](https://github.com/rphui315/github-repo-video-card-skill/releases/download/v0.1-demo/openwhispr_with_cover_1s.mp4)

## What It Does Not Include

这个开源版本不包含：

- 作者个人头像参考图
- 私有封面风格参考图
- 本地机器路径
- 主分支里的大体积视频资产
- 自动发布平台接口

不同机器上的 Codex、截图工具、图像生成工具和 HyperFrames 环境可能不一样，所以你需要按自己的环境调整。

## Folder Structure

```text
skills/github-repo-video-card/
  SKILL.md
  references/content-spec.md
  references/visual-spec.md
  templates/storyboard-template.md
  scripts/crop_image.py
examples/
docs/
```

## Install

把 `skills/github-repo-video-card` 复制到你的 Codex skills 目录：

```bash
mkdir -p ~/.codex/skills
cp -R skills/github-repo-video-card ~/.codex/skills/
```

重启 Codex 或开启新的对话后，使用类似请求：

```text
用 github-repo-video-card，把 https://github.com/owner/repo 做成一条中文卡片视频方案。
```

也可以让它先找选题：

```text
今天找 3 个适合做中文卡片视频的 GitHub 开源项目，先不要制作，等我确认。
```

## Dependencies

基础版本只需要 Codex 能读网页或你提供 README 内容。

如果要继续做成视频，通常还需要：

- GitHub 页面访问能力
- 浏览器截图能力
- 图像生成工具，用于封面
- HyperFrames 或其他 HTML/视频渲染工具
- FFmpeg，用于合成封面和视频

## Example Output

见 `examples/example-output.md`。

## Notes

这个 Skill 更适合做 AI 内容生产流程的起点。你可以直接改它的选题标准、文案风格、画面结构和封面规则。

如果你跑不通完整视频链路，可以先只使用文字部分：项目说明、分镜、标题、标签和封面提示词。

## License

MIT
