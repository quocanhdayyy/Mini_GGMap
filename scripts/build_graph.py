import json
import argparse
from math import radians, sin, cos, sqrt, atan2
from pathlib import Path
import pickle
import networkx as nx


def haversine_distance(lat1, lon1, lat2, lon2):
    R = 6371000
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    return 2 * R * atan2(sqrt(a), sqrt(1-a))


def build_graph_from_geojson(geojson_path: Path) -> nx.Graph:
    data = json.loads(geojson_path.read_text(encoding="utf-8"))
    G = nx.Graph()
    for i, feature in enumerate(data.get("features", [])):
        geom = feature.get("geometry", {})
        props = feature.get("properties", {}) or {}
        if geom.get("type") != "LineString":
            continue
        coords = geom.get("coordinates", [])
        road_name = props.get("name", f"road_{i}")
        highway = props.get("highway", "unknown")
        for j in range(len(coords) - 1):
            lon1, lat1 = coords[j]
            lon2, lat2 = coords[j + 1]
            node1 = (lat1, lon1)
            node2 = (lat2, lon2)
            G.add_node(node1)
            G.add_node(node2)
            dist = haversine_distance(lat1, lon1, lat2, lon2)
            G.add_edge(node1, node2,
                       weight=dist,
                       distance=dist,
                       road_name=road_name,
                       highway=highway,
                       segment_id=f"{i}_{j}")
    return G


def main():
    p = Path(__file__).resolve().parent.parent
    default_geo = p / "app" / "static" / "data" / "geojson" / "roads.geojson"
    parser = argparse.ArgumentParser(description="Build graph from GeoJSON (Mini_GGMap)")
    parser.add_argument("--geo", "-g", type=Path, default=default_geo, help="Path to input GeoJSON")
    parser.add_argument("--out", "-o", type=Path, default=p / "app" / "static" / "data" / "graph" / "roads.gpickle", help="Output gpickle path")
    args = parser.parse_args()

    if not args.geo.exists():
        print(f"GeoJSON not found: {args.geo}")
        return

    args.out.parent.mkdir(parents=True, exist_ok=True)
    print(f"Reading: {args.geo}")
    G = build_graph_from_geojson(args.geo)
    print(f"Nodes: {G.number_of_nodes()}, Edges: {G.number_of_edges()}")

    # Save graph (pickle)
    with open(args.out, 'wb') as fh:
        pickle.dump(G, fh)
    print(f"Saved graph to: {args.out}")


if __name__ == "__main__":
    main()
