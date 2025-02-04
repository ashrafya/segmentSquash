import cv2
import random


class matchVideo:
  def __init__(self, filepath: str):
      self.filepath = filepath



  def play_video(self) -> None:
    """plays video"""

    cap = cv2.VideoCapture(self.filepath)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.resize(frame, (1280, 720))  # Resize for efficiency
        cv2.imshow('Frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):   # break command
            break

    cap.release()
    cv2.destroyAllWindows()


  def count_frames(self) -> int:
    """returns number of frames in the file"""
    cap = cv2.VideoCapture(self.filepath)
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    return length


  def download_images(self, frame_num: int) -> None:
    """picks images and downloads them into data directory"""
    cap = cv2.VideoCapture(self.filepath)
    count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        if count == frame_num:
          cv2.imwrite("../data/frame-%d.jpg" % count, frame)
          break

        # frame = cv2.resize(frame, (1280, 720))  # Resize for efficiency
        # cv2.imshow('Frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):   # break command
            break
        count += 1

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
  filepath = "../data/Farag v Coll Tournament of Champions 2025  SF HIGHLIGHTS.mp4"
  match = matchVideo(filepath)
  # match.play_video()
  # print(match.count_frames())
  for i in range(9):
    random_int = random.randint(40, 9000)
    match.download_images(random_int)
    
