from matrix_functions import *
from numba import njit

@njit(fastmath=True)
def clip(shape, a, b):
    return np.any((shape == a) | (shape == b))

class Screen:
    def __init__(self, width, height, fov = 90, znear = 0.1, zfar = 100, bgcolor = (255, 255, 255)):
        self.canvas = pygame.display.set_mode((width, height), pygame.RESIZABLE)
        self.bgcolor = bgcolor
        
        self.fov = fov
        self.znear = znear
        self.zfar = zfar
        
        self.update_size(*pygame.display.get_window_size())
        
    def render(self, camera, objects):
        self.canvas.fill(self.bgcolor)
        
        for object in objects:
            # project to camera space
            vertices = object.vertices @ camera.camera_matrix()
            vertices = vertices @ self.projection_matrix
            
            # clip objects behind the camera and normalize the depth
            vertices[vertices[:, -1] < 0] = 0
            mask = vertices[:, -1] > 0
            vertices[mask] /= vertices[mask][:, -1].reshape(-1, 1)
            
            # sort face draw order by depth
            centers = vertices[object.faces[:, -1]].copy()
            sort_indices = np.argsort(centers[:, 2])[::-1]
            faces = object.faces[sort_indices]
            colors = object.colors[sort_indices]
            
            # clip the objects outside of the camera frustum and project to screen
            vertices[(vertices > 2) | (vertices < -2)] = 0
            vertices = vertices @ self.screen_matrix
            vertices = vertices[:, :2]
            
            for face, color in zip(faces, colors):
                if face[3] == 0 : shape = vertices[face[:3]]
                else : shape = vertices[face[:4]]
                if not clip(shape, self.width//2, self.height//2):
                    pygame.draw.polygon(self.canvas, color, shape)
                    
    def update_size(self, width, height):
        self.width = width
        self.height = height
        self.projection_matrix = self.get_projection_matrix()
        self.screen_matrix = self.get_screen_matrix()
        
    def get_projection_matrix(self):
        a = self.height / self.width
        s = 1/math.tan(math.radians(self.fov / 2))
        return np.array([
            [a * s, 0, 0, 0],
            [0, s, 0, 0],
            [0, 0, (self.zfar+self.znear)/(self.zfar-self.znear), 1],
            [0, 0, (-2*self.znear*self.zfar)/(self.zfar-self.znear), 0]
        ])
        
    def get_screen_matrix(self):
        return np.array([
            [self.width//2, 0, 0, 0],
            [0, -self.height//2, 0, 0],
            [0, 0, 1, 0],
            [self.width//2, self.height//2, 0, 1]
        ])