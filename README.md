# 图片转PDF SKILLS

自行克隆或下载至项目根目录，目录结构如下
```sh
your_project_root
├── .agents
│   └── skills
│       └── img_to_pdf
│           ├── SKILL.md
│           ├── assets
│           │   └── test.jpg
│           ├── reference
│           └── scripts
│               └── img_to_pdf.py
├── .claude
│   ├── settings.local.json
│   └── skills
│       └── img_to_pdf
│           ├── SKILL.md
│           ├── assets
│           │   └── test.jpg
│           ├── reference
│           └── scripts
│               └── img_to_pdf.py
```

## TUI用法
终端启动`claude code`
```sh
claude --dangerously-skip-permissions
```
或终端启动`opencode`
```sh
opencode
```
提示词
```sh
/img_to_pdf 请你使用该skills，使用虚拟环境，演示图片如何转为pdf
```
小技巧：输入`/`可以用`tab`补全