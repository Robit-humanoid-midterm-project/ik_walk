from launch import LaunchDescription
from launch.substitutions import PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    
    ik_walk = Node(
        package='ik_walk',
        executable='ik_walk',
        output='screen',
        emulate_tty=True,
    )

    return LaunchDescription([ik_walk])
