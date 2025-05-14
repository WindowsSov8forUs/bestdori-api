---
# https://vitepress.dev/reference/default-theme-home-page
layout: home

hero:
  name: Bestdori API
  text: Python 驱动的 Bestdori API 调用库
  tagline: 整合 Bestdori 绝大多数资源
  image:
    light: /logo-light.png
    dark: /logo-dark.png
    alt: logo-shown
  actions:
    - theme: brand
      text: 了解 Bestdori API
      link: /brief
    - theme: alt
      text: 开始使用
      link: /fast-start
    - theme: alt
      text: GitHub
      link: https://github.com/WindowsSov8forUs/bestdori-api

features:
  - icon: 🎸
    title: （近乎）全面的资源覆盖
    details: 能够找到的 API 、能够获取到的资源，都可以通过本模块获取、使用。
  - icon: 🤓
    title: 同时支持同步与异步
    details: 由于作者某种来源不可知的执念，Bestdori API 同时支持了同步与异步（而不是提供某种转换方法），包括多种 HTTP 请求库适应，未来可能添加自定义请求库配置。
  - icon:
      src: /bestdori-logo.png
      height: 50
    title: 最佳资源库
    details: 虽然不是 Bestdori API 自身的优点，但作为最大的 BanG Dream! 社区与资源库，Bestdori 依然是你获取游戏资讯与资源的不二之选。
    link: https://bestdori.com/
    linkText: Bestdori.com
    rel: external
    target: _blank
---
