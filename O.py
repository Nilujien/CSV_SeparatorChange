import win32con
import win32gui
import ctypes
import time
import atexit

# save system cursor, before changing it
cursor = win32gui.LoadImage(0, 32512, win32con.IMAGE_CURSOR,
                            0, 0, win32con.LR_SHARED)
save_system_cursor = ctypes.windll.user32.CopyImage(cursor, win32con.IMAGE_CURSOR,
                                                    0, 0, win32con.LR_COPYFROMRESOURCE)


def restore_cursor():
    # restore the old cursor
    print("restore_cursor")
    ctypes.windll.user32.SetSystemCursor(save_system_cursor, 32512)
    ctypes.windll.user32.DestroyCursor(save_system_cursor)


# Make sure cursor is restored at the end
atexit.register(restore_cursor)

# change system cursor
cursor = win32gui.LoadImage(0, "Marquee_Crosshair.cur", win32con.IMAGE_CURSOR,
                            0, 0, win32con.LR_LOADFROMFILE)
ctypes.windll.user32.SetSystemCursor(cursor, 32512)
ctypes.windll.user32.DestroyCursor(cursor)

time.sleep(20)
