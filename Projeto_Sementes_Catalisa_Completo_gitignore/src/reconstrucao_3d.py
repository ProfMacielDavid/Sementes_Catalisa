
import open3d as o3d
import numpy as np

def reconstruir_3d(nuvem_pontos_path):
    print(f"Carregando nuvem de pontos: {nuvem_pontos_path}")
    pcd = o3d.io.read_point_cloud(nuvem_pontos_path)

    print("Filtrando e estimando normais...")
    pcd.estimate_normals()

    print("Reconstruindo malha com algoritmo Poisson...")
    mesh, _ = o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(pcd, depth=9)

    print("Salvando malha em formato OBJ...")
    o3d.io.write_triangle_mesh("saida_malha.obj", mesh)
    print("Reconstrução finalizada.")

# Exemplo de uso:
# reconstruir_3d("dados/nuvem_semente.ply")
