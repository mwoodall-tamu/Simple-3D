from matrix_functions import *

class Object:
    def __init__(self, model_file : str, position = [0.0, 0.0, 0.0], rotation = [0.0, 0.0, 0.0], scale = [1.0, 1.0, 1.0], color = (255, 255, 255)):
        self.position = np.array([0.0, 0.0, 0.0, 1.0])
        self.rotation = np.array([0.0, 0.0, 0.0, 1.0])
        self.scale  = np.array([1.0, 1.0, 1.0, 1.0])
        self.color = np.array(color, dtype=np.float32)
        
        self.vertices : list[np.ndarray[np.float32]] = []
        self.faces : list[np.ndarray[np.int32]] = []
        self.normals : list[np.ndarray[np.float32]] = []
        self.colors : list[np.ndarray[np.float32]] = []
        
        self.load_model(model_file)
        
        # Bake lists to fixed size arrays
        self.vertices = np.array(self.vertices, dtype=np.float32)
        self.colors = np.array(self.colors, dtype=np.float32)
        self.faces = np.array(self.faces, dtype=np.int32)
        self.normals = np.array(self.normals, dtype=np.float32)
        
        self.set_scale(scale)
        self.set_rotation(rotation)
        self.set_translation(position)
        
    def load_model(self, model_file : str):
        model_type = model_file[-3:].lower()
        
        if model_type == "stl":
            raise NotImplementedError(f"Model type {model_type} is not yet supported")
            
        elif model_type == "obj":
            # Parse all vertices
            for line in open(model_file, "r"):
                if not line.strip : continue
                data = line.strip().split(" ")
                
                if data[0] == "v":
                    self.vertices.append(vector_like([float(value) for value in data[1:] if value != ""]))
            
            # Parse all faces
            for line in open(model_file, "r"):
                if not line.strip() : continue
                data = line.strip().split(" ")
                
                if data[0] == "f":
                    if len(data) == 4: # Triangle
                        self.faces.append([int(value) - 1 if "/" not in value else int(value.split("/")[0]) - 1 for value in data[1:]] + [0, len(self.vertices)])
                        self.vertices.append((self.vertices[self.faces[-1][0]] + self.vertices[self.faces[-1][1]] + self.vertices[self.faces[-1][2]])/3)
                    elif len(data) == 5: # Quad
                        self.faces.append([int(value) - 1 if "/" not in value else int(value.split("/")[0]) - 1 for value in data[1:]] + [len(self.vertices)])
                        self.vertices.append((self.vertices[self.faces[-1][0]] + self.vertices[self.faces[-1][1]] + self.vertices[self.faces[-1][2]] + self.vertices[self.faces[-1][3]])/4)
                    else : continue
                    v0 = self.vertices[self.faces[-1][0]][:3]
                    v1 = self.vertices[self.faces[-1][1]][:3]
                    v2 = self.vertices[self.faces[-1][2]][:3]
                    normal = np.cross(v1 - v0, v2 - v0)
                    normal /= np.linalg.norm(normal)
                    self.colors.append(self.color*(normal.mean()+1)/2)
        
        else:
            raise NotImplementedError(f"Model type {model_type} is not supported")
        
    def set_translation(self, new_position):
        new_position = vector_like(new_position)
        self.vertices = self.vertices @ translate(new_position - self.position)
        self.position = new_position
    
    def set_rotation(self, new_rotation):
        new_rotation = vector_like(new_rotation)
        
        dx = new_rotation[0] - self.rotation[0]
        dy = new_rotation[1] - self.rotation[1]
        dz = new_rotation[2] - self.rotation[2]
        
        if dx != 0 : self.vertices = self.vertices @ rot_x(dx)
        if dy != 0 : self.vertices = self.vertices @ rot_y(dy)
        if dz != 0 : self.vertices = self.vertices @ rot_z(dz)
        
        self.rotation = new_rotation
    
    def set_scale(self, new_scale):
        new_scale = vector_like(new_scale)
        self.vertices = self.vertices @ scale(new_scale / self.scale)
        self.scale = new_scale
        
    