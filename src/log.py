logsettings = {
    'version' : 1,
    'loggers' : {
        '__main__' : {
            'level' : 'DEBUG',
            'handlers' : ['console'],
        },
        'reppar' : {
            'level' : 'DEBUG',
            'handlers' : ['console'],
        },
        'tabpar' : {
            'level' : 'DEBUG',
            'handlers' : ['console'],
        },
        'procrules' : {
            'level' : 'DEBUG',
            'handlers' : ['console'],
        }
    },
    'handlers' : {
        'console' : {
            'class' : 'logging.StreamHandler',
            'level' : 'DEBUG',
            'formatter' : 'tnlm',
        }
    },
    'formatters' : {
        'tnlm' : {
            'style' : '{',
            'format' : '{asctime} {name} line {lineno} - {message}',
        }
    },
}
