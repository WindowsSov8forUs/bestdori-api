
API = {
    'user': {
        'info': '/api/user',
        'login': '/api/user/login',
        'me': '/api/user/me'
    },
    'post': {
        'basic': '/api/post/basic',
        'details': '/api/post/details',
        'list': '/api/post/list',
        'tag': '/api/post/tag',
        'post': '/api/post',
        'find': '/api/post/find',
        'like': '/api/post/like'
    },
    'charts': {
        'info': '/api/charts/{id}/{diff}.json'
    },
    'characters': {
        'info': '/api/characters/{id}.json',
        'all': '/api/characters/all.{index}.json'
    },
    'cards': {
        'info': '/api/cards/{id}.json',
        'all': '/api/cards/all.{index}.json'
    },
    'costumes': {
        'info': '/api/costumes/{id}.json',
        'all': '/api/costumes/all.{index}.json'
    },
    'events': {
        'info': '/api/events/{id}.json',
        'all': '/api/events/all.{index}.json',
        'top': '/api/eventtop/data'
    },
    'festival':{
        'stages': '/api/festival/stages/{id}.json',
        'rotation_musics': '/api/festival/rotationMusics/{id}.json',
    },
    'gacha': {
        'info': '/api/gacha/{id}.json',
        'all': '/api/gacha/all.{index}.json'
    },
    'songs': {
        'info': '/api/songs/{id}.json',
        'all': '/api/songs/all.{index}.json'
    },
    'loginCampaigns': {
        'info': '/api/loginCampaigns/{id}.json',
        'all': '/api/loginCampaigns/all.{index}.json'
    },
    'bands': {
        'all': '/api/bands/all.{index}.json',
        'main': '/api/bands/main.{index}.json'
    },
    'upload': {
        'file': '/api/upload/file/{hash}',
        'prepare': '/api/upload/prepare',
        'upload': '/api/upload',
        'status': '/api/upload/status/{hash}'
    },
    'misc': {
        'llsif': '/api/misc/llsif.{index}.json'
    },
    'player': {
        'info': '/api/player/{server}/{id}'
    },
    'tracker': {
        'eventtop': '/api/eventtop/data',
        'eventtracker': '/api/tracker/data'
    },
    'all': {
        'skills': '/api/skills/all.{index}.json',
        'stamps': '/api/stamps/all.{index}.json',
        'degrees': '/api/degrees/all.{index}.json',
        'meta': '/api/songs/meta/all.{index}.json',
        'archives': '/api/archives/all.{index}.json',
        'miracleTicketExchanges': '/api/miracleTicketExchanges/all.{index}.json',
        'comics': '/api/comics/all.{index}.json',
    }
}
'''Bestdori API 集合'''

ASSETS = {
    'characters': {
        'character_kv_image': '/assets/{server}/ui/character_kv_image/{id:>03d}_rip/image.png',
        'resourceset': '/assets/{server}/characters/resourceset/{resource_set_name}_rip/{name}_{type}.png',
        'livesd': '/assets/{server}/characters/livesd/{sd_resource_name}_rip/sdchara.png'
    },
    'event': {
        'banner': '/assets/{server}/event/{asset_bundle_name}/images_rip/banner.png',
        'logo': '/assets/{server}/event/{asset_bundle_name}/images_rip/logo.png',
        'topscreen': '/assets/{server}/event/{asset_bundle_name}/topscreen_rip/{type}_eventtop.png',
        'loginbouns': '/assets/{server}/event/loginbonus/{asset_bundle_name}_rip/background.png'
    },
    'songs': {
        'musicjacket': '/assets/{server}/musicjacket/musicjacket{index:>02d}_rip/assets-star-forassetbundle-startapp-musicjacket-musicjacket{index:>02d}-{jacket_image}-jacket.png',
        'sound': '/assets/{server}/sound/bgm{id:>03d}_rip/bgm{id:>03d}.mp3',
    },
    'thumb': {
        'chara': '/assets/{server}/thumb/chara/card{id:>05d}_rip/{resource_set_name}_{type}.png',
        'degree': '/assets/{server}/thumb/degree_rip/{degree_name}.png',
        'costume': '/assets/{server}/thumb/costume/group{id}_rip/{asset_bundle_name}.png',
    },
    'stamp': {
        'get': '/assets/{server}/stamp/01_rip/{image_name}.png',
    },
    'homebanner': {
        'get': '/assets/{server}/homebanner_rip/{banner_asset_bundle_name}.png',
    },
    'gacha': {
        'screen': '/assets/{server}/gacha/screen/gacha{id}_rip/{asset_name}.png',
    },
    'comic': {
        'comic': '/assets/{server}/comic/comic_{type}/{asset_bundle_name}_rip/{asset_bundle_name}.png',
        'thumbnail': '/assets/{server}/comic/comic_{type}_thumbnail/{asset_bundle_name}_rip/{asset_bundle_name}.png'
    },
    'missions': {
        'info': '/assets/{server}/missions/{id}.json',
        'all': '/assets/{server}/missions/all.{index}.json',
    },
    'band': {
        'logo': '/assets/{server}/band/logo/{id:>03d}_rip/{type}.png',
    },
    'live2d': {
        'buildData': '/assets/{server}/live2d/chara/{asset_bundle_name}_rip/buildData.asset',
    }
}
'''Bestdori 数据包集合'''

RES = {
    'icon': {
        'svg': '/res/icon/{name}.svg',
        'png': '/res/icon/{name}.png',
    },
    'image': {
        'png': '/res/image/{name}.png',
    },
    'emoji': {
        'png': '/res/emoji/{name}.png',
    }
}
'''Bestdori 资源集合'''

AYACHAN = {
    'version': 'https://api.ayachan.fun/v2/version',
    'chart_metrics': {
        'bandori': 'https://api.ayachan.fun/v2/chart/metrics/bandori/{chart_id}/{diff_str}',
        'bestdori': 'https://api.ayachan.fun/v2/chart/metrics/bestdori/{chart_id}',
        'custom': 'https://api.ayachan.fun/v2/chart/metrics/custom/{diff_str}'
    },
    'levels': {
        'post': 'https://sonolus.ayachan.fun/test/sonolus/levels',
        'info': 'https://sonolus.ayachan.fun/test/sonolus/levels/{uid}',
        'get': 'https://sonolus.ayachan.fun/test/sonolus/levels/{uid}/bdv2.json'
    }
}
'''ayachan API 集合'''
