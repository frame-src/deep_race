def reward_function(params):
    
    all_wheels_on_track = params['all_wheels_on_track']
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    steering_angle = abs(params['steering_angle'])


    reward = 1e-3
    speed = params["speed"]
    if all_wheels_on_track and (0.5*track_width - distance_from_center) >= 0.05:
        reward = speed
    if steering_angle < 15 :
        reward = speed
    if steering_angle < 15 && speed == 1 :
        reward = speed * 2

    return float(reward)

