from setuptools import setup

setup(
        name                = 'droptype-composer',
        version             = 'dev',
        description         = '',
        long_description    = file('README.md').read(),
        url                 = 'https://github.com/marquee/composer',
        author              = 'Alec Perkins',
        author_email        = 'alec@droptype.com',
        license             = 'UNLICENSE',
        packages            = ['composer'],
        zip_safe            = False,
        keywords            = '',
        install_requires    = ['content'],
        dependency_links    = ['http://github.com/marquee/content/tarball/master#egg=content-dev'],
        package_data        = {
            'droptype-composer': ['../stylesheets/*'],
        },
        classifiers         = [
            'Development Status :: 2 - Pre-Alpha',
            'Intended Audience :: Developers',
            'License :: Public Domain',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: Implementation :: CPython',
            'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        ],
    )
