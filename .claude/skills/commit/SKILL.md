---
name: commit
description: |
  快速提交并推送。当用户说 "commit"、"/commit"、"提交"、"commit and push"、
  "自动提交" 或任何要求你提交代码、推送仓库的指令时，立即使用此 skill。
  即使只说了 "commit" 一个字也必须触发。
---

# Commit & Push

用户要求提交换时，执行以下步骤。**不要问确认，直接执行。**

## 工作流

### 1. 查看状态
```bash
git status --short
```
如果没有任何修改，报告 "Nothing to commit." 并停止。

### 2. 暂存所有修改
```bash
git add -A
```

### 3. 获取 diff 来生成提交信息
```bash
git diff --staged --stat
git diff --staged -- . ':!.gitignore' ':!*.lock' ':!package-lock.json' 2>/dev/null | head -200
```

### 4. 生成提交信息

基于 diff 内容生成符合 conventional commits 规范的英文提交信息：

格式: `type(scope): summary`

**类型（type）：**
- `feat` — 新功能
- `fix` — 修复 bug
- `docs` — 文档变更
- `refactor` — 重构（不改变功能）
- `chore` — 构建、依赖、配置等杂项
- `test` — 测试
- `style` — 格式调整

**规则：**
- 标题行不超过 72 字符，全部小写
- 用英文写
- summary 直接说明做了什么，不要泛泛的 "update" 或 "fix"
- 如果有多项独立修改，用换行列出要点（body）

**示例：**
- `feat(practice): add hello world script`
- `fix(01-run): correct syntax error in test.py`
- `refactor: extract common utils to shared module`
- `chore: add .gitignore for python project`

### 5. 提交
```bash
git commit -m "<生成的提交信息>"
```

### 6. 推送
```bash
git push
```
如果推送失败（无远程/网络问题），只提示一次，不要重复尝试。

## 熔断条件
- 没有 `.git` 目录 → 跳过
- 处于合并中或冲突状态 → 提示用户手动解决
- 没有任何修改 → 直接报告
