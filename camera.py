from matrix_functions import *

class Camera:
    def __init__(self, position = [0.0, 0.0, 0.0], rotation = [0.0, 0.0, 0.0], move_speed = 10, rotation_speed = 0.05):
        self.positions = vector_like(position)
        self.rotation = vector_like(rotation)
        self.move_speed = move_speed
        self.rotation_speed = rotation_speed
        
        self.rotation_identity()
        
    def control(self, dt):
        key = pygame.key.get_pressed()
        mouse_move = pygame.mouse.get_rel()
        if mouse_move != (0, 0):
            self.rotation[1] += mouse_move[0] * dt * self.rotation_speed
            self.rotation[0] += mouse_move[1] * dt * self.rotation_speed
            self.update_rotation()
        if key[pygame.K_a]:
            self.positions -= self.right * self.move_speed * dt
        if key[pygame.K_d]:
            self.positions += self.right * self.move_speed * dt
        if key[pygame.K_w]:
            self.positions += self.forward * self.move_speed * dt
        if key[pygame.K_s]:
            self.positions -= self.forward * self.move_speed * dt
        if key[pygame.K_SPACE]:
            self.positions += self.up * self.move_speed * dt
        if key[pygame.K_LSHIFT]:
            self.positions -= self.up * self.move_speed * dt
        if key[pygame.K_UP]:
            self.rotation[0] -= self.rotation_speed * dt
            self.update_rotation()
        if key[pygame.K_DOWN]:
            self.rotation[0] += self.rotation_speed * dt
            self.update_rotation()
        if key[pygame.K_RIGHT]:
            self.rotation[1] += self.rotation_speed * dt
            self.update_rotation()
        if key[pygame.K_LEFT]:
            self.rotation[1] -= self.rotation_speed * dt
            self.update_rotation()
            
    def rotation_identity(self):
        self.forward = np.array([0, 0, 1, 1])
        self.up = np.array([0, 1, 0, 1])
        self.right = np.array([1, 0, 0, 1])
        
    def update_rotation(self):
        rotation = rot_x(self.rotation[0]) @ rot_y(self.rotation[1])
        self.rotation_identity()
        self.forward = self.forward @ rotation
        self.up = self.up @ rotation
        self.right = self.right @ rotation
        
    def pitch_camera(self, angle):
        rotation = rot_w(self.right, angle)
        self.forward = self.forward @ rotation
        self.up = self.up @ rotation
        
    def yaw_camera(self, angle):
        rotation = rot_y(angle)
        self.forward = self.forward @ rotation
        self.right = self.right @ rotation
    
    def translation_matrix(self):
        x, y, z, w = self.positions
        return np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [-x, -y, -z, 1]
        ])
        
    def rotation_matrix(self):
        rx, ry, rz, w = self.right
        ux, uy, uz, w = self.up
        fx, fy, fz, w = self.forward
        return np.array([
            [rx, ux, fx, 0],
            [ry, uy, fy, 0],
            [rz, uz, fz, 0],
            [0, 0, 0, 1]
        ])
        
    def camera_matrix(self):
        return self.translation_matrix() @ self.rotation_matrix()