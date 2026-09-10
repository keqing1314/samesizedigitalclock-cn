# 更新日志

本项目遵循 [语义化版本](https://semver.org/lang/zh-CN/) 规范。

## [1.0.0] - 2026-09-10

首个正式版本 🎉

基于 KDE 官方 DigitalClock 小部件改造的 Plasma 数字时钟插件，在保留原版「时间与日期等宽（Same size）」特性的基础上，完成中国本地化适配并新增事件显示开关。

### ✨ 新增功能

- **事件显示开关**：在 配置 → 日历 中可开启/关闭事件面板，开启后于日历左侧显示当天日程事件（KConfig 键 `showAgenda`）。
- **简体中文界面**：内置 `zh_CN` 翻译（`contents/locale/zh_CN/`），适配中文使用习惯。
- **滚动切换时区**：支持鼠标滚轮在已配置的多个时区之间切换。

### ⏰ 时钟特性

- 时间与日期使用相同字号尺寸，显示统一美观。
- 日期位置支持 自适应 / 时间旁 / 时间下。
- 秒数显示支持 从不 / 仅在提示框 / 始终。
- 支持 12/24 小时制与自定义日期格式（短日期 / 长日期 / ISO / 自定义）。
- 字体样式可自动或手动设置（字体、字号、粗细、斜体）。

### 🗓️ 日历特性

- 点击时钟展开完整日历视图。
- 支持显示周数、自定义一周第一天。
- 多时区世界时钟，时区可显示为代码 / 全称 / UTC 偏移。
- 事件数据来源可通过 `enabledCalendarPlugins` 选择已启用的日历插件。

### 📄 文档

- 完善 `README.md`：新增界面预览、系统要求、常见问题、贡献指南等章节。
- 新增 `screenshots/` 示例截图目录。

### 🔧 兼容性

- 要求 **KDE Plasma 6**（`X-Plasma-API-Minimum-Version`: 6.0）。
- 许可证：GPL-2.0+。

---

## 版本说明

- 本项目基于 [plasma-workspace](https://invent.kde.org/plasma/plasma-workspace) 中的 DigitalClock 改造，原始作者为 Martin Klapetek 及其他 KDE 贡献者。

[1.0.0]: https://github.com/keqing1314/samesizedigitalclock-cn/releases/tag/v1.0.0
