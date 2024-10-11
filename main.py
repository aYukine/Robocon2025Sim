from settings import *
from robot import Robot
from trajectory import *
import time
pg.init()

class Simulation:
    def __init__(self):
        self.win = pg.display.set_mode(game_field_size)
        self.run = True
        self.game_field_img = pg.transform.scale(pg.image.load("assets/gameField.png"), (1504, 802)).convert_alpha()
        self.current_time = time.perf_counter()

        self.robots = [
            Robot(robot1_x, robot1_y, robot_d, RED, robot_speed),
            Robot(robot2_x, robot2_y, robot_d, RED, robot_speed),
            Robot(robot3_x, robot3_y, robot_d, BLUE, robot_speed),
            Robot(robot4_x, robot4_y, robot_d, BLUE, robot_speed)
        ]
        self.tasks = [robot1_tasks, robot2_tasks, robot3_tasks, robot4_tasks]
        self.clock = pg.time.Clock()

    def draw_robots(self):
        for robot in self.robots:
            robot.draw_robot(self.win)

    def doing_task(self, dt):
        for robot, tasks in zip(self.robots, self.tasks):
            if not tasks:
                continue
            current_task = tasks[0]
            task = current_task[0]
            param = current_task[1]
            completed = False
            if task == "Move": # iterate through task and its operation
                completed = robot.move(param[0], param[1], dt)
            elif task == "Dribble":
                completed = robot.dribble()
            elif task == "Shoot":
                completed = robot.shoot()

            if completed:
                tasks.pop(0)
                print("left over tasks", tasks)

    def mainloop(self):
        while self.run:
            self.clock.tick(FPS)
            runningfps = self.clock.get_fps()
            print(runningfps)
            dt = time.perf_counter() - self.current_time
            self.current_time = time.perf_counter()
            for events in pg.event.get():
                if events.type == pg.QUIT:
                    self.run = False

            self.doing_task(dt) # game process
            self.win.blit(self.game_field_img, (0, 0)) # this is the background
            self.draw_robots()

            pg.display.update()

def main():
    game = Simulation()
    game.mainloop()

if __name__ == "__main__":
    main()