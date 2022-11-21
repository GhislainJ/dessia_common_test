from dessia_common.forms import MovingStandaloneObject

mso = MovingStandaloneObject(origin=0, name="Moving Test")

disp = mso._displays()

md_data = '# Object Moving Test of class MovingStandaloneObject\n\nThis is a markdown file' \
        ' https://www.markdownguide.org/cheat-sheet/\n\nThe good practice is to create a string python template and '\
        'move the template to another python module\n(like templates.py) to avoid mix python code and markdown, as '\
        'python syntax conflicts with markdown\n\nYou can substitute values with object attributes like the name of '\
        'the object: Moving Test\n\n# Attributes\n\nObject Moving Test of class MovingStandaloneObject has the '\
        'following attributes:\n\n| Attribute | Type | Value |\n| ------ | ------ | ------ |\n| origin | int | 0 |'\
        '\n| name | str | Moving Test |'

assert disp == [
    {
        'type_': 'markdown',
        'data': md_data,
        'traceback': '',
        'reference_path': '',
        'name': ''
    },
    {
        'type_': 'plot_data',
        'data': [],
        'traceback': '',
        'reference_path': '',
        'name': ''
    },
    {
        'type_': 'babylon_data',
        'data': {
            'meshes': [
                {
                    'positions': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 1.0, 1.0, 0.0, 0.0,
                                  0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0],
                    'indices': [0, 2, 1, 0, 3, 2, 4, 6, 5, 4, 7, 6, 0, 5, 1, 0, 4, 5,
                                1, 6, 2, 1, 5, 6, 2, 7, 3, 2, 6, 7, 3, 4, 0, 3, 7, 4],
                    'alpha': 1,
                    'name': '',
                    'color': [0.8, 0.8, 0.8]
                }
            ],
            'max_length': 1.0,
            'center': [0.5, 0.5, 0.5],
            'steps': [
                {
                    'time': 0,
                    0: {
                        'position': [0.0, 0.0, 0.0],
                        'orientations': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]
                    }
                },
                {
                    'time': 1,
                    0: {
                        'position': [0.0, 0.0, 0.0],
                        'orientations': [[0.764842, 0.0, -0.644218], [0.0, 1.0, 0.0], [0.644218, 0.0, 0.764842]]
                    }
                },
                {
                    'time': 2,
                    0: {
                        'position': [0.0, 1.0, 0.0],
                        'orientations': [[0.764842, 0.0, -0.644218], [0.0, 1.0, 0.0], [0.644218, 0.0, 0.764842]]
                    }
                },
                {
                    'time': 3,
                    0: {
                        'position': [0.0, 1.0, 0.0],
                        'orientations': [[0.169967, 0.0, -0.98545], [0.0, 1.0, 0.0], [0.98545, 0.0, 0.169967]]
                    }
                }
            ]
        },
        'traceback': '',
        'reference_path': '',
        'name': ''
    }
]
