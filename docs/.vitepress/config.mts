import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "Bestdori API",
  description: "A Python powered API module for bestdori.com",
  head: [
    ['link', { rel: 'icon', href: 'favicon.ico' }],
  ],
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    logo: {
      src: '/logo.png',
    },
    nav: [
      { text: 'Bestdori API', link: '/' },
      { text: '开始', link: '/brief' }
    ],
    sidebar: [
      {
        text: '开始',
        items: [
          { text: '了解 Bestdori API', link: '/brief' },
          { text: '快速开始', link: '/fast-start' },
          { text: '配置', link: '/settings' },
          { text: '登录用户验证', link: '/me' }
        ]
      },
      {
        text: 'API 文档',
        items: [
          { text: 'bands.py 乐队模块', link: '/api/bands' },
          { text: 'cards.py 卡牌模块', link: '/api/cards' },
          { text: 'characters.py 角色模块', link: '/api/characters' },
          { text: 'charts.py 谱面模块', link: '/api/charts' },
          { text: 'comics.py 漫画模块', link: '/api/comics' },
          { text: 'costumes.py 服装模块', link: '/api/costumes' },
          { text: 'eventarchives.py 活动数据模块', link: '/api/eventarchives' },
          { text: 'events.py 活动模块', link: '/api/events' },
          { text: 'eventtop.py 活动 T10 排名模块', link: '/api/eventtop' },
          { text: 'eventtracker.py 活动 PT 与排名追踪模块', link: '/api/eventtracker' },
          { text: 'festival.py 团队佳节活动模块', link: '/api/festival' },
          { text: 'gacha.py 招募模块', link: '/api/gacha' },
          { text: 'icon.py 图标模块', link: '/api/icon' },
          { text: 'logincampaigns.py 登录奖励模块', link: '/api/logincampaigns' },
          { text: 'miracleticket.py 自选券模块', link: '/api/miracleticket' },
          { text: 'missions.py 任务模块', link: '/api/missions' },
          { text: 'player.py 玩家模块', link: '/api/player' },
          { text: 'post.py 帖子模块', link: '/api/post' },
          { text: 'skills.py 技能模块', link: '/api/skills' },
          { text: 'songmeta.py 歌曲 Meta 模块', link: '/api/songmeta' },
          { text: 'songs.py 歌曲模块', link: '/api/songs' },
          { text: 'stamps.py 贴纸模块', link: '/api/stamps' },
          { text: 'thumb.py 缩略图模块', link: '/api/thumb' },
          { text: 'upload.py 文件模块', link: '/api/upload' },
          { text: 'user.py 用户模块', link: '/api/user' },
          { text: 'ayachan Ayachan 模块', link: '/ayachan'},
          { text: '类型', link: '/typing'},
          { text: '杂项', link: '/utils'}
        ]
      }
    ],
    outline: {
      level: [2, 3],
      label: '页面导航'
    },
    socialLinks: [
      { icon: 'github', link: 'https://github.com/WindowsSov8forUs/bestdori-api' }
    ],
    search: {
      provider: 'local'
    },
    lastUpdated: {
      text: '最后一次更新于 ',
      formatOptions: {
        dateStyle: 'full',
        timeStyle: 'medium',
      }
    },
    footer: {
      message: '基于 <a href="https://github.com/WindowsSov8forUs/bestdori-api/blob/main/LICENSE">MIT 许可</a>发布',
      copyright: '版权 © 2023-2025 <a href="https://github.com/WindowsSov8forUs">WindowsSov8forUs</a>'
    }
  },
  lastUpdated: true
})
