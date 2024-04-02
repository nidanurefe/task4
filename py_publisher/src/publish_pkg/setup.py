from setuptools import find_packages, setup

package_name = 'publish_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='nida',
    maintainer_email='nida@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        "publisher_node=publish_pkg.publisher_node:main",
        "subscriber_node=publish_pkg.subscriber_node:main",

        ],
    },
)
