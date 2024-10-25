scenario1 = [ 
            # robot 1
            [
                ("Move", (700, 200)),
                ("Dribble", ()),
                ("Move", (900, 300)),
                ("Shoot", ()) 
            ],
            # robot 2
            [
                ("Move", (700, 500)),
                ("Wait", 9),
                ("Move", (1100, 500)),
            ],
            # robot 3
            [],
            # robot 4
            []
]

scenario2 = [
            # robot1 tasks
            [
                ("Move", (200, 150)),  
                # ("Dribble", ()),       
                # ("Move", (600, 300)),
                ("Wait", 6), 
                ("Pass", 1),  
            ],
            # robot2 tasks
            [
                ("Wait", 3),
                ("Move", (1000, 700)),  # After receiving the ball, move to a new position
                ("Wait", 7),
                ("Shoot", ()),  
            ],
            # robot3 tasks
            [],
            # robot4 tasks
            []
]



current_trajectory = scenario2