'''`bestdori.utils.utils`

工具库模块'''

API = {
    'user': {
        'info': 'user',
        'login': 'user/login',
        'me': 'user/me'
    },
    'post': {
        'basic': 'post/basic',
        'details': 'post/details',
        'list': 'post/list',
        'tag': 'post/tag',
        'post': 'post',
        'find': 'post/find',
        'like': 'post/like'
    },
    'charts': {
        'info': 'charts/{id}/{diff}.json'
    },
    'characters': {
        'info': 'characters/{id}.json',
        'all': 'characters/all.{index}.json'
    },
    'cards': {
        'info': 'cards/{id}.json',
        'all': 'cards/all.{index}.json'
    },
    'costumes': {
        'info': 'costumes/{id}.json',
        'all': 'costumes/all.{index}.json'
    },
    'events': {
        'info': 'events/{id}.json',
        'all': 'events/all.{index}.json',
        'top': 'eventtop/data'
    },
    'gacha': {
        'info': 'gacha/{id}.json',
        'all': 'gacha/all.{index}.json'
    },
    'songs': {
        'info': 'songs/{id}.json',
        'all': 'songs/all.{index}.json'
    },
    'loginCampaigns': {
        'info': 'loginCampaigns/{id}.json',
        'all': 'loginCampaigns/all.{index}.json'
    },
    'bands': {
        'all': 'bands/all.{index}.json',
        'main': 'bands/main.{index}.json'
    },
    'upload': {
        'file': 'upload/file/{hash}',
        'prepare': 'upload/prepare',
        'upload': 'upload',
        'status': 'upload/status/{hash}'
    },
    'misc': {
        'llsif': 'misc/llsif.{index}.json'
    },
    'player': {
        'get': 'player/{server}/{id}'
    },
    'all': {
        'skills': 'skills/all.{index}.json',
        'stamps': 'stamps/all.{index}.json',
        'degrees': 'degrees/all.{index}.json',
        'meta': 'songs/meta/all.{index}.json',
        'archives': 'archives/all.{index}.json',
        'miracleTicketExchanges': 'miracleTicketExchanges/all.{index}.json',
        'comics': 'comics/all.{index}.json',
    }
}
'''Bestdori API 集合'''

ASSETS = {
    'characters': {
        'character_kv_image': 'ui/character_kv_image/{id:>03d}_rip/image.png',
        'resourceset': 'characters/resourceset/{resource_set_name}_rip/{name}_{type}.png',
        'livesd': 'characters/livesd/{sd_resource_name}_rip/sdchara.png'
    },
    'event': {
        'banner': 'event/{asset_bundle_name}/images_rip/banner.png',
        'logo': 'event/{asset_bundle_name}/images_rip/logo.png',
        'topscreen': 'event/{asset_bundle_name}/topscreen_rip/{type}_eventtop.png',
        'loginbouns': 'event/loginbonus/{asset_bundle_name}_rip/background.png'
    },
    'songs': {
        'musicjacket': 'musicjacket/musicjacket{index:>02d}_rip/assets-star-forassetbundle-startapp-musicjacket-musicjacket{index:>02d}-{jacket_image}-jacket.png',
        'sound': 'sound/bgm{id:>03d}_rip/bgm{id:>03d}.mp3',
        'musicscore': ''
    },
    'thumb': {
        'chara': 'thumb/chara/card{id:>05d}_rip/{resource_set_name}_{type}.png',
        'degree': 'thumb/degree_rip/{degree_name}.png',
        'costume': 'thumb/costume/group{id}_rip/{asset_bundle_name}.png',
    },
    'stamp': {
        'get': 'stamp/01_rip/{image_name}.png'
    },
    'homebanner': {
        'get': 'homebanner_rip/{banner_asset_bundle_name}.png'
    },
    'gacha': {
        'screen': 'gacha/screen/gacha{id}_rip/{asset_name}.png'
    },
    'comic': {
        'comic': 'comic/comic_{type}/{asset_bundle_name}_rip/{asset_bundle_name}.png',
        'thumbnail': 'comic/comic_{type}_thumbnail/{asset_bundle_name}_rip/{asset_bundle_name}.png'
    },
    'missions': {
        'info': 'missions/{id}.json',
        'all': 'missions/all.{index}.json'
    },
    'band': {
        'logo': 'band/logo/{id:>03d}_rip/{type}.png'
    },
    'live2d': {
        'buildData': 'live2d/chara/{asset_bundle_name}_rip/buildData.asset'
    }
}
'''Bestdori 数据包集合'''

RES = {
    'icon': {
        'svg': 'icon/{name}.svg',
        'png': 'icon/{name}.png'
    },
    'image': {
        'png': 'image/{name}.png'
    },
    'emoji': {
        'png': 'emoji/{name}.png'
    }
}
'''Bestdori 资源集合'''