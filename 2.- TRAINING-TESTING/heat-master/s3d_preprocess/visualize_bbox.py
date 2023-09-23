import os
import json
import argparse

import cv2
import numpy as np
import matplotlib.pyplot as plt

from misc.utils import get_corners_of_bb3d_no_index, project_3d_points_to_2d, parse_camera_info


def visualize_bbox(args):
    with open(os.path.join(args.path, f"scene_{args.scene:05d}", "bbox_3d.json")) as file:
        annos = json.load(file)

    id2index = dict()
    for index, object in enumerate(annos):
        id2index[object.get('ID')] = index

    scene_path = os.path.join(args.path, f"scene_{args.scene:05d}", "2D_rendering")

    for room_id in np.sort(os.listdir(scene_path)):
        room_path = os.path.join(scene_path, room_id, "perspective", "full")

        if not os.path.exists(room_path):
            continue

        for position_id in np.sort(os.listdir(room_path)):
            position_path = os.path.join(room_path, position_id)

            image = cv2.imread(os.path.join(position_path, 'rgb_rawlight.png'))
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            height, width, _ = image.shape

            instance = cv2.imread(os.path.join(position_path, 'instance.png'), cv2.IMREAD_UNCHANGED)

            camera_info = np.loadtxt(os.path.join(position_path, 'camera_pose.txt'))

            rot, trans, K = parse_camera_info(camera_info, height, width)

            plt.figure()
            plt.imshow(image)

            for index in np.unique(instance)[:-1]:
                # for each instance in current image
                bbox = annos[id2index[index]]

                basis = np.array(bbox['basis'])
                coeffs = np.array(bbox['coeffs'])
                centroid = np.array(bbox['centroid'])

                corners = get_corners_of_bb3d_no_index(basis, coeffs, centroid)
                corners = corners - trans

                gt2dcorners = project_3d_points_to_2d(corners, rot, K)

                num_corner = gt2dcorners.shape[1] // 2
                plt.plot(np.hstack((gt2dcorners[0, :num_corner], gt2dcorners[0, 0])),
                         np.hstack((gt2dcorners[1, :num_corner], gt2dcorners[1, 0])), 'r')
                plt.plot(np.hstack((gt2dcorners[0, num_corner:], gt2dcorners[0, num_corner])),
                         np.hstack((gt2dcorners[1, num_corner:], gt2dcorners[1, num_corner])), 'b')
                for i in range(num_corner):
                    plt.plot(gt2dcorners[0, [i, i + num_corner]], gt2dcorners[1, [i, i + num_corner]], 'y')

            plt.axis('off')
            plt.axis([0, width, height, 0])
            plt.show()


def parse_args():
    parser = argparse.ArgumentParser(
        description="Structured3D 3D Bounding Box Visualization")
    parser.add_argument("--path", required=True,
                        help="dataset path", metavar="DIR")
    parser.add_argument("--scene", required=True,
                        help="scene id", type=int)
    return parser.parse_args()


def main():
    args = parse_args()

    visualize_bbox(args)


if __name__ == "__main__":
    main()
