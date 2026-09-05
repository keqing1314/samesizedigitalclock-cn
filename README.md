# Digital Clock - Same Size

基于 KDE 官方 [DigitalClock](https://invent.kde.org/plasma/plasma-workspace) 小部件改造的 Plasma 数字时钟插件。

本项目在保留原版「时间与日期等宽（Same size）」特性的基础上，进行了**中国本地化适配**，并新增了**事件显示开关**功能，更适合中文用户日常使用。

## 特性

- ⏰ **等宽数字时钟**：时间与日期使用相同的字号尺寸，显示更统一美观。
- 🗓️ **日历弹窗**：点击时钟可展开完整的日历视图，支持周数显示、多时区世界时钟。
- 📅 **事件显示开关（新增）**：可在设置中开启或关闭事件面板，从日历插件读取日程事件并当天展示。
- 🌍 **多时区支持**：配置多个时区，支持滚轮切换时区、时区代码/全称/UTC 偏移多种显示方式。
- 🕐 **灵活的日期与时间格式**：支持 12/24 小时制、秒数显示、自定义日期格式、日期在时间旁/下方/自适应位置。
- 🔤 **字体样式配置**：自动字体与字号，或手动指定字体、粗细、斜体、大小。
- 🇨🇳 **中国本地化**：内置简体中文（`zh_CN`）翻译，适配中文使用习惯。

## 安装

将整个插件目录复制到 Plasma 小部件目录，例如：

```bash
# 用户级安装（推荐）
cp -r com.github.alex47.samesizedigitalclock ~/.local/share/plasma/plasmoids/

# 或系统级安装
sudo cp -r com.github.alex47.samesizedigitalclock /usr/share/plasma/plasmoids/
```

安装后在桌面或面板上右键 →「添加小部件」，搜索 **Digital Clock - Same Size** 即可使用。

## 使用说明

- **左键点击时钟**：展开/收起日历弹窗。
- **滚轮**：在已配置的多个时区之间切换（需在设置中开启）。
- **右键菜单**：复制当前时间/日期、配置、锁定位置等。

## 配置项

在时钟的右键菜单 →「配置」中可调整：

### 外观（Appearance）

| 设置项 | 说明 |
| --- | --- |
| 显示日期 | 是否在时间旁显示日期 |
| 日期位置 | 自适应 / 时间旁 / 时间下 |
| 秒数显示 | 从不 / 仅在提示框 / 始终 |
| 时区显示 | 仅与本地时区不同时 / 始终显示 |
| 字体与字号 | 自动或手动设置字体、字号、粗细、斜体 |
| 时间格式 | 12/24 小时制 |
| 日期格式 | 短日期 / 长日期 / ISO / 自定义 |

### 日历（Calendar）

| 设置项 | 说明 |
| --- | --- |
| 显示周数 | 是否在日历中显示周数 |
| **显示事件** | **是否显示事件面板（新增事件开关）** |
| 一周第一天 | 使用区域默认 / 周日 / 周一 / 周五 / 周六 |
| 可用插件 | 选择事件数据来源的日历插件 |

### 时区（Time Zones）

- 添加 / 删除 / 排序多个时区。
- 设置时区显示格式（代码、全称、UTC 偏移）。

## 文件结构

```
├── metadata.json                  # 插件元数据（ID、名称、类别、许可证等）
└── contents/
    ├── config/
    │   ├── config.qml             # 配置分类模型
    │   └── main.xml               # 配置项定义（KConfig）
    ├── locale/
    │   └── zh_CN/                 # 简体中文翻译
    └── ui/
        ├── main.qml               # 小部件入口（紧凑表示 / 完整表示）
        ├── DigitalClock.qml       # 时钟紧凑表示
        ├── CalendarView.qml       # 日历弹窗（含事件面板）
        ├── Tooltip.qml            # 鼠标悬停提示框
        ├── NoTimezoneWarning.qml  # 无有效时区提示
        ├── configAppearance.qml   # 外观配置页
        ├── configCalendar.qml     # 日历配置页（含事件显示开关）
        └── configTimeZones.qml    # 时区配置页
```

## 事件显示开关

在 **配置 → 日历** 中勾选/取消「**显示事件**」即可控制事件面板的显隐。

- 开启后，会在日历左侧列出当天/所选日期的日程事件。
- 开关会读取 `enabledCalendarPlugins` 中已启用的日历插件数据。
- 若没有可用的事件插件，事件面板会自动隐藏。

## 许可证

本项目基于 [GPL-2.0+](https://www.gnu.org/licenses/old-licenses/gpl-2.0.html) 发布，遵循原版 KDE Plasma 小部件许可。

- 原始作者：Martin Klapetek 及其他 KDE 贡献者
- Bug 报告：[GitHub Issues](https://github.com/alex47/PlasmaDigitalClockSameSize/issues)
