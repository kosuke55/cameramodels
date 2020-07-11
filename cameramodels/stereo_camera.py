from cameramodels.pinhole_camera import PinholeCameraModel


class StereoCameraModel(object):

    """A Stereo Camera Model

    Parameters
    ----------
    left : cameramodels.PinholeCameraModel
        left camera model.
    right : cameramodels.PinholeCameraModel
        right camera model.
    """

    def __init__(self, left, right):
        self._left_camera = left
        self._right_camera = right

    @property
    def left_camera(self):
        """Getter of left camera.

        Returns
        -------
        self._left_camera : cameramodels.PinholeCameraModel
            left camera model
        """
        return self._left_camera

    @property
    def right_camera(self):
        """Getter of right camera.

        Returns
        -------
        self._right_camera : cameramodels.PinholeCameraModel
            right camera model
        """
        return self._right_camera

    @staticmethod
    def from_camera_info(left_camera_info_msg, right_camera_info_msg):
        """Return StereoCameraModel from camera info msgs.

        Parameters
        ----------
        left_camera_info_msg : sensor_msgs.msg.CameraInfo
            left message of camera info.
        right_camera_info_msg : sensor_msgs.msg.CameraInfo
            right message of camera info.

        Returns
        -------
        cameramodel : cameramodels.StereoCameraModel
            stereo camera model
        """
        left = PinholeCameraModel(left_camera_info_msg)
        right = PinholeCameraModel(right_camera_info_msg)
        return StereoCameraModel(left, right)
