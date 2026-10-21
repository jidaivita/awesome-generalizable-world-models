# 数据与生成说明

[← 首页](../README.md)

仓库使用 Python 标准库、JSON 和 Markdown。无需安装额外依赖。

## 内容从哪里修改

| 内容 | 维护位置 |
| :--- | :--- |
| 论文题名、链接、发表状态、简短注释 | `data/papers.json` |
| 七模块说明、论文联系、12 篇阅读顺序 | `data/map.json` |
| 页面布局 | `scripts/build.py` |
| 可公开笔记清单 | `publish-manifest.json` |
| 个人完整笔记 | 自己的笔记工具，仓库外 |

首页、七模块和阅读路线来自同一份数据。生成器只替换 `BEGIN GENERATED RESEARCH MAP` 与 `END GENERATED RESEARCH MAP` 标记之间的内容，保留区块外人工文字；拒绝覆盖未标记的现有文件。

## 基本操作

```bash
python3 scripts/validate.py
python3 scripts/build.py
python3 -m unittest discover -s tests
python3 scripts/build.py --check
```

验证覆盖唯一 ID、题名别名、arXiv 去重、模块归属、阅读路线和站内链接。生成结果不写入运行时间，同一输入重复构建保持一致。

## 添加论文

复制现有条目的结构，分配稳定 ID，填写已经确认的元数据。首次公开年份等未知信息保持 `null`。新条目先确定具体角色，再决定是否调整精选池；原有条目可以保留为扩展资料，避免静默删除。

初始精选池为 30 篇，模块数量为 4/6/4/4/4/4/4，推荐路线为 12 篇。这些是本版编辑约定，不是永久收录上限。

## 三种状态

`source_review` 记录来源核验范围与日期；`user_reading` 仅记录本人确认的阅读状态；`reproduction` 记录实际运行。三者互不推导。默认阅读状态为 `untracked`，运行状态为 `not_run`，页面不展示个人阅读进度。

只有实际重新核对过的来源才更新核验日期。构建页面或 HTTP 请求成功均不能替代内容核验。

## 公开笔记与导出

仅把决定公开的稿件放入 `public_notes/`，再将相对路径和标题加入 `publish-manifest.json` 的 `notes` 数组。清单初始为空，不扫描其他笔记目录。私人飞书链接和私人研究想法不进入公开数据。

`python3 scripts/export_public.py --output /absolute/path/to/export` 导出明确允许的导航、模板及清单内笔记；不会复制原始 JSON、测试、报告或其他本地文件。导出与 Git 推送是两件事：提交源仓库时仍需检查暂存文件。

## 外部链接检查

```bash
python3 scripts/check_links.py --output /absolute/path/to/link-report.json
```

该命令主动访问论文和代码入口，记录重定向与 HTTP 状态。403、429 和超时标为待核验，不自动删除条目。网络检查不会修改论文阅读状态或来源核验日期。
