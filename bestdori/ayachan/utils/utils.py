'''`bestdori.ayachan.utils.utils`

ayachan 工具库模块'''


API = {
    'map-info': 'v2/map-info/',
    'bestdori': 'v2/map-info/bestdori/{id}',
    'version': 'v2/version',
    'chart_metrics': {
        'bandori': 'v2/chart/metrics/bandoru/{chart_id}/{diff_str}',
        'bestdori': 'v2/chart/metrics/bestdori/{chart_id}',
        'custom': 'v2/chart/metrics/custom/{diff_str}'
    },
    'levels': {
        'post': 'https://sonolus.ayachan.fun/test/sonolus/levels',
        'get': 'https://sonolus.ayachan.fun/test/sonolus/levels/{uid}/bdv2.json'
    }
}
'''ayachan API 集合'''
