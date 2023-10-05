from launch_ros.actions import Node
from launch import LaunchDescription
# from launch.substitutions import FindPackageShare

def generate_launch_description():
    package_name = 'hb_task_1b'
    ld = LaunchDescription()

    service_node = Node(
        package=package_name,
        executable='service_node',
        output='screen'
    )

    ld.add_action(service_node)

    return ld