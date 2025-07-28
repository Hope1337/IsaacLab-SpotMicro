import isaaclab.sim as sim_utils
from isaaclab.actuators import ActuatorNetLSTMCfg, DCMotorCfg
from isaaclab.assets.articulation import ArticulationCfg

from isaaclab.utils.assets import ISAACLAB_NUCLEUS_DIR
from isaaclab.actuators import ImplicitActuatorCfg, IdealPDActuatorCfg

joints = [
    'front_left_shoulder',
    'front_right_shoulder',
    'rear_left_shoulder',
    'rear_right_shoulder',
    'front_left_leg',
    'front_left_foot',
    'front_right_leg',
    'front_right_foot',
    'rear_left_leg',
    'rear_left_foot',
    'rear_right_leg',
    'rear_right_foot'
]

SPOT_MICRO_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path="/home/manh/Projects/Isaaclab-MicroSpot/source/isaaclab_assets/data/Robots/SpotMicro/spot_micro.usd",
        activate_contact_sensors=False,
        
        rigid_props=sim_utils.RigidBodyPropertiesCfg(
            rigid_body_enabled=True,
            disable_gravity=False,
            linear_damping=0.0,
            angular_damping=0.0,
            max_linear_velocity=1000.0,
            max_angular_velocity=1000.0,
            max_depenetration_velocity=1.0,
        ),
        articulation_props=sim_utils.ArticulationRootPropertiesCfg(
            enabled_self_collisions=True,  
            solver_position_iteration_count=32,  
            solver_velocity_iteration_count=16,   
        ),
    ),
    
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, .7),  
        joint_pos={
            ".*_left_shoulder": 0.0,    
            ".*_right_shoulder": 0.0,       
            ".*_leg":  0.0,             
            ".*_foot": 0.0,             
        },
        joint_vel={".*": 0.0}, 
    ),
    actuators={
        "servos": ImplicitActuatorCfg(
            joint_names_expr=joints,
            velocity_limit=8.0,
            effort_limit=3.4,
            stiffness=20.,  
            damping=0.5,    
            armature=0.0
        ),
    }
)