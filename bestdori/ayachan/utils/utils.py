'''`bestdori.ayachan.utils.utils`

ayachan 工具库模块'''


API = {
    'version': 'v2/version',
    'chart_metrics': {
        'bandori': 'v2/chart/metrics/bandori/{chart_id}/{diff_str}',
        'bestdori': 'v2/chart/metrics/bestdori/{chart_id}',
        'custom': 'v2/chart/metrics/custom/{diff_str}'
    },
    'levels': {
        'post': 'https://sonolus.ayachan.fun/test/sonolus/levels',
        'info': 'https://sonolus.ayachan.fun/test/sonolus/levels/{uid}',
        'get': 'https://sonolus.ayachan.fun/test/sonolus/levels/{uid}/bdv2.json'
    }
}
'''ayachan API 集合'''
