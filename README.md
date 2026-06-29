# RTA-DISCOVERY Skill

RTA-DISCOVERY 是整个 RTA 工作流的前置入口。

它不直接生成用户画像和用户生命旅程，它只负责：

1. 判断客户类型
2. 生成合适的访谈稿
3. 明确后续必须补哪些材料

## 适用场景

- 客户还没开始做内容
- 客户有成交，但表达和资料不完整
- 你准备给客户做用户画像 / 用户生命旅程 / 人设
- 你需要先判断客户该走哪种访谈路径

## 三种客户类型

- `zero_based`：零基础，没有真实成交验证
- `validated`：有真实成交和真实案例
- `mixed`：部分已验证，部分还在探索

## 输出内容

- Discovery 诊断
- 对应访谈路径
- 材料清单
- 人工确认后的 handoff 信息

## 目录结构

```text
.
├── SKILL.md
├── examples/
├── outputs/
├── references/
└── templates/
```

## 推荐工作流

```text
先判断客户类型
-> 出访谈稿
-> 拿调研语料
-> 人工确认
-> 再进入 RTA-USER
```

## 仓库内示例

- `examples/zero-based-example.md`
- `examples/validated-example.md`
- `examples/mixed-example.md`
- `outputs/test-oushijie-discovery.json`
- `outputs/test-oushijie-discovery.md`

## 本地自检

运行：

```bash
python3 scripts/smoke_test.py
```

它会检查：

- 核心文件是否齐全
- 示例输出 JSON 是否符合结构要求
- `client_type` 和 `recommended_next_mode` 是否合法
- handoff 是否保留人工确认闸门

## 最小安装说明

给你的客户时，只需要告诉他：

1. 下载这个仓库
2. 把整个文件夹放进自己的 Agent / Skill 目录
3. 保持目录结构不要改
4. 第一次使用时，先告诉 Agent 自己目前属于哪种状态：
   - 还没有真实成交
   - 已有真实成交
   - 部分验证、部分探索
5. 让 Agent 先完成 Discovery，不要直接跳到用户画像

建议客户第一次使用时这样说：

```text
请使用 RTA-DISCOVERY skill，先判断我现在属于哪一类客户，
再为我生成适合的访谈稿和资料清单。
如果信息不足，请先补问最少的问题，不要直接下结论。
```
