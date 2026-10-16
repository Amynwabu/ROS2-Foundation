from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'test2_py_pkg'
setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Workshop maintainer',
    maintainer_email='maintainer@example.com',
    description='ROS 2 foundation lecture examples',
    license='MIT',
    entry_points={'console_scripts': [
        'my_first_node = test2_py_pkg.mynode:main',
        'create_topic = test2_py_pkg.topic_creator:main',
        'waiter = test2_py_pkg.waiter:main',
        'chef = test2_py_pkg.chef:main',
        'restaurant_server = test2_py_pkg.restaurant_server:main',
        'order_client = test2_py_pkg.restaurant_client:main',
        'restaurant_client = test2_py_pkg.restaurant_client:main',
    ]},
)
