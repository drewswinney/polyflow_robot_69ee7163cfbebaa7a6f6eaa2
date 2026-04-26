import json
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package="motor_controller",
            executable="motor_controller_node",
            name="motor_controller_n69ee7285cfbebaa7a6f6f9c9",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69ee7285cfbebaa7a6f6f9c9",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"motor_id":"69ee7500f25c6f3e7bc9e6ce","mode":"speed","max_speed":1,"timeout_s":0}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":50,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3cd62b3f393789aad70a2:command","name":"command","direction":"input","msg_type":"std_msgs/Float64"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69ee79fadf065b5cb52a56b9","source_node_id":"69ee79f5df065b5cb52a5591","source_pin_id":"rear_left_motor","target_pin_id":"command"}]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
            }
        ),
        Node(
            package="motor_controller",
            executable="motor_controller_node",
            name="motor_controller_n69ee7287cfbebaa7a6f6fa37",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69ee7287cfbebaa7a6f6fa37",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"motor_id":"69ee758cf25c6f3e7bc9f1b6","mode":"speed","max_speed":1,"timeout_s":0}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":50,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3cd62b3f393789aad70a2:command","name":"command","direction":"input","msg_type":"std_msgs/Float64"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69ee79f8df065b5cb52a564d","source_node_id":"69ee79f5df065b5cb52a5591","source_pin_id":"front_left_motor","target_pin_id":"command"}]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
            }
        ),
        Node(
            package="motor_controller",
            executable="motor_controller_node",
            name="motor_controller_n69ee7289cfbebaa7a6f6faa5",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69ee7289cfbebaa7a6f6faa5",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"motor_id":"69ee74f9f25c6f3e7bc9e5c6","mode":"speed","max_speed":1,"timeout_s":0}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":50,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3cd62b3f393789aad70a2:command","name":"command","direction":"input","msg_type":"std_msgs/Float64"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69ee79fddf065b5cb52a5725","source_node_id":"69ee79f5df065b5cb52a5591","source_pin_id":"front_right_motor","target_pin_id":"command"}]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
            }
        ),
        Node(
            package="motor_controller",
            executable="motor_controller_node",
            name="motor_controller_n69ee728ccfbebaa7a6f6fb13",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69ee728ccfbebaa7a6f6fb13",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"motor_id":"69ee7913df065b5cb52a51d1","mode":"speed","max_speed":1,"timeout_s":0}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":50,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3cd62b3f393789aad70a2:command","name":"command","direction":"input","msg_type":"std_msgs/Float64"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69ee79ffdf065b5cb52a5791","source_node_id":"69ee79f5df065b5cb52a5591","source_pin_id":"rear_right_motor","target_pin_id":"command"}]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
            }
        ),
        Node(
            package="differential_drive",
            executable="differential_drive_node",
            name="differential_drive_n69ee79f5df065b5cb52a5591",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69ee79f5df065b5cb52a5591",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"wheel_radius":0.05,"wheel_separation":0.3,"max_wheel_speed":1}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":50,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3c8e4b3f393789aad6f84:cmd_vel","name":"cmd_vel","direction":"input","msg_type":"geometry_msgs/Twist"},{"pin_id":"69a3c8e4b3f393789aad6f84:mode","name":"mode","direction":"input","msg_type":"polyflow_msgs/ModeState"},{"pin_id":"69a3c8e4b3f393789aad6f84:front_left_motor","name":"front_left_motor","direction":"output","msg_type":"std_msgs/Float64"},{"pin_id":"69a3c8e4b3f393789aad6f84:rear_left_motor","name":"rear_left_motor","direction":"output","msg_type":"std_msgs/Float64"},{"pin_id":"69a3c8e4b3f393789aad6f84:front_right_motor","name":"front_right_motor","direction":"output","msg_type":"std_msgs/Float64"},{"pin_id":"69a3c8e4b3f393789aad6f84:rear_right_motor","name":"rear_right_motor","direction":"output","msg_type":"std_msgs/Float64"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69ee7a38df065b5cb52a5a4b","source_node_id":"69ee7a34df065b5cb52a598f","source_pin_id":"cmd_vel","target_pin_id":"cmd_vel"},{"connection_id":"69ee7a44df065b5cb52a5bc5","source_node_id":"69ee7a41df065b5cb52a5b09","source_pin_id":"mode","target_pin_id":"mode"}]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69ee79f8df065b5cb52a564d","target_node_id":"69ee7287cfbebaa7a6f6fa37","source_pin_id":"front_left_motor","target_pin_id":"command"},{"connection_id":"69ee79fadf065b5cb52a56b9","target_node_id":"69ee7285cfbebaa7a6f6f9c9","source_pin_id":"rear_left_motor","target_pin_id":"command"},{"connection_id":"69ee79fddf065b5cb52a5725","target_node_id":"69ee7289cfbebaa7a6f6faa5","source_pin_id":"front_right_motor","target_pin_id":"command"},{"connection_id":"69ee79ffdf065b5cb52a5791","target_node_id":"69ee728ccfbebaa7a6f6fb13","source_pin_id":"rear_right_motor","target_pin_id":"command"}]')),
            }
        ),
        Node(
            package="gamepad",
            executable="gamepad_node",
            name="gamepad_n69ee7a34df065b5cb52a598f",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69ee7a34df065b5cb52a598f",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"device_index":0,"poll_rate_hz":60,"deadzone":0.05,"max_linear_speed":1,"max_angular_speed":2}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":60,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3c77bb3f393789aad6f62:axes","name":"axes","direction":"output","msg_type":"polyflow_msgs/GamepadAxes"},{"pin_id":"69a3c77bb3f393789aad6f62:buttons","name":"buttons","direction":"output","msg_type":"polyflow_msgs/GamepadButtons"},{"pin_id":"69a3c77bb3f393789aad6f62:cmd_vel","name":"cmd_vel","direction":"output","msg_type":"geometry_msgs/Twist"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69ee7a38df065b5cb52a5a4b","target_node_id":"69ee79f5df065b5cb52a5591","source_pin_id":"cmd_vel","target_pin_id":"cmd_vel"}]')),
            }
        ),
        Node(
            package="mode_switcher",
            executable="mode_switcher_node",
            name="mode_switcher_n69ee7a41df065b5cb52a5b09",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69ee7a41df065b5cb52a5b09",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"default_mode":"teleop","allowed_modes":["teleop","automated","stopped"]}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3cd36b3f393789aad7079:set_mode","name":"set_mode","direction":"input","msg_type":"polyflow_msgs/ModeCommand"},{"pin_id":"69a3cd36b3f393789aad7079:mode","name":"mode","direction":"output","msg_type":"polyflow_msgs/ModeState"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69ee7a44df065b5cb52a5bc5","target_node_id":"69ee79f5df065b5cb52a5591","source_pin_id":"mode","target_pin_id":"mode"}]')),
            }
        ),
    ])